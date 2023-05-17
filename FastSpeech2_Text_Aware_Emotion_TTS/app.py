import gradio as gr
import subprocess

predefined_texts = [
    "A combination of Canadian capital quickly organized and petitioned for the same privileges.",
    "The date was nearly eighteen years old.",
    "Hardly were our plans made public before we were met by powerful opposition.",
]

emotion_mapping = {"amused": 0, "anger": 1,
                   "disgust": 2, "neutral": 3, "sleepiness": 4}


def synthesize_speech(input_type, text, own_text, speaker_id, embed_type, emotion_id):
    if input_type == "Choose from examples":
        selected_text = text
    else:
        selected_text = own_text

    if embed_type == "bert_embed":
        command = f"python3 synthesize.py --text '{selected_text}' --bert_embed 1 --speaker_id {speaker_id} --restore_step 900000 --mode single -p config/EmoV_DB/preprocess.yaml -m config/EmoV_DB/model.yaml -t config/EmoV_DB/train.yaml"
    else:
        command = f"python3 synthesize.py --text '{selected_text}' --emotion_id {emotion_mapping[emotion_id]} --speaker_id {speaker_id} --restore_step 900000 --mode single -p config/EmoV_DB/preprocess.yaml -m config/EmoV_DB/model.yaml -t config/EmoV_DB/train.yaml"

    output = subprocess.check_output(command, shell=True)
    audio_file = f'output/result/EmoV_DB/{selected_text}.wav'
    return audio_file


iface = gr.Interface(
    fn=synthesize_speech,
    inputs=[
        gr.inputs.Radio(
            ["Choose from examples", "Enter your own text"], label="Input Type"),
        gr.inputs.Dropdown(choices=predefined_texts, label="Select a text"),
        gr.inputs.Textbox(lines=2, label="Enter your own text"),
        gr.inputs.Slider(minimum=0, maximum=3, step=1,
                         default=0, label="Speaker ID"),
        gr.inputs.Radio(["bert_embed", "emotion_id"], label="Embedding Type"),
        gr.inputs.Dropdown(choices=emotion_mapping, label="Select Emotion"),
    ],
    outputs=gr.outputs.Audio(type="filepath"),
    title="Text-to-Speech Demo",
)
iface.launch()
