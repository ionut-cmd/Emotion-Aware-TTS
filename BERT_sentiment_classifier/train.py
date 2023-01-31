import numpy as np
import pandas as pd
import torch.nn as nn

from dataset import GoEmotionDataset
from model import DistilBertForMultilabelSequenceClassification

import transformers
from transformers import (AutoTokenizer, TrainingArguments, Trainer)
from torch.utils.tensorboard import SummaryWriter

import torch



def proces_data(data):
    print('Processing_data.......')

   
    df = data[['text', 'anger', 'disgust', 'fear',
                    'joy', 'surprise', 'sadness', 'neutral']].copy()


    label_cols = ['anger', 'disgust', 'fear',
                'happy', 'surprise', 'sadness', 'neutral']



    df = df.rename(columns={'joy': 'happy'})
    df = df.rename(columns={'text': 'sentence'})


    df["labels"] = df[label_cols].values.tolist()


    df = df[(df[['anger', 'disgust', 'fear', 'happy', 'surprise', 'sadness', 'neutral']] != 0).any(axis=1)]

    return df



def tokenize(tokenizer, df):

    print('tokenizing.....')
    train_encodings = tokenizer(df["sentence"].values.tolist(), truncation=True)
    test_encodings = tokenizer(df["sentence"].values.tolist(), truncation=True)


    # create train / test splits
    mask = np.random.rand(len(df)) < 0.8
    df_train = df[mask]
    df_test = df[~mask]

    train_labels = df_train["labels"].values.tolist()
    test_labels = df_test["labels"].values.tolist()


    train_dataset = GoEmotionDataset(train_encodings, train_labels)
    test_dataset = GoEmotionDataset(test_encodings, test_labels)

   

    return train_dataset, test_dataset



def config_model(model):


    model.config.id2label = {
        "0": "anger",
        "1": "disgust",
        "2": "fear",
        "3": "happy",
        "4": "surprise",
        "5": "sadness",
        "6": "neutral",
    }
    model.config.label2id ={
        "anger": 0,
        "disgust": 1,
        "fear": 2,
        "happy": 3,
        "surprise": 4,
        "sadness": 5,
        "neutral": 6,

    }
    model.config


def accuracy(y_pred, y_true, thresh=0.5, sigmoid=True):
    y_pred = torch.from_numpy(y_pred)
    y_true = torch.from_numpy(y_true)
    if sigmoid:
      y_pred = y_pred.sigmoid()
    return ((y_pred>thresh)==y_true.bool()).float().mean().item()

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    return {'accuracy': accuracy(predictions, labels)}




if __name__ == "__main__":
    

    df_1 = pd.read_csv('data/goemotions_1.csv')
    df_2 = pd.read_csv('data/goemotions_2.csv')
    df_3 = pd.read_csv('data/goemotions_3.csv')
    df_combined = pd.concat([df_1, df_2, df_3], axis=0)


    df = proces_data(df_combined)


   

    pre_trained =  "distilbert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(pre_trained)

    train_dataset, test_dataset = tokenize(tokenizer, df)

    print('declare model.....')
    num_labels=7
    device = "cuda" if torch.cuda.is_available else "cpu"
    print(f'device: {device}')
    model = DistilBertForMultilabelSequenceClassification 
    model = model.from_pretrained(pre_trained, num_labels=num_labels).to(device)

    config_model(model)

    batch_size = 32

    # configure logging so we see training loss
    logging_steps = len(train_dataset) // batch_size

    name = 'go_emotion'
    writer = SummaryWriter("logs".format(name))

    args = TrainingArguments(
        output_dir="emotion",
        evaluation_strategy = "epoch",
        save_strategy='epoch',
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=batch_size,
        num_train_epochs=3,
        weight_decay=0.01,
        logging_steps=logging_steps
    )


    trainer = Trainer(
        model,
        args,
        train_dataset=train_dataset,
        eval_dataset=test_dataset,
        compute_metrics=compute_metrics,
        tokenizer=tokenizer)


    trainer.train()

    writer.close()