# FastSpeech 2 - PyTorch Implementation

This is a PyTorch implementation of Microsoft's text-to-speech system [**FastSpeech 2: Fast and High-Quality End-to-End Text to Speech**](https://arxiv.org/abs/2006.04558v1).
This project is based on [xcmyz's implementation](https://github.com/xcmyz/FastSpeech) of FastSpeech. Feel free to use/modify the code.

There are several versions of FastSpeech 2.
This implementation is more similar to [version 1](https://arxiv.org/abs/2006.04558v1), which uses F0 values as the pitch features.
On the other hand, pitch spectrograms extracted by continuous wavelet transform are used as the pitch features in the [later versions](https://arxiv.org/abs/2006.04558).

![](./img/model.png)

## Samples

Please visit the [GitHub page](https://ionut-cmd.github.io/Emotion-Aware-TTS/) to view comparative samples.

Or generate new ones on HuggingFace

<a href="https://huggingface.co/spaces/Ionut-Bostan/Emotion_Aware_TTS">
    <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" alt="HuggingFace" width="50" height="auto"/>
</a>

## Dependencies

You can install the Python dependencies with

```
pip3 install -r requirements.txt
```

## Inference

You have to download the [pretrained FastSpeech2 model](https://drive.google.com/file/d/1_7L2Sxi7m47mfgL-u0l_qEWpqPbTLF1X/view?usp=sharing) and add it to `output/ckpt/EmoV_DB/`.

Also download the [pretrained RoBERTa model](https://drive.google.com/drive/folders/1yC8pQAcA4yb0vpXutx6XcpFn8nJm19k_?usp=sharing) and add it to `roberta_pretrained/`.

For English multi-speaker Emotional Aware TTS with RoBERTa embeddings,set multi_emotion to True in model.yaml and run

```
!python3 synthesize.py --text "Example text" --bert_embed 1 --speaker_id SPEAKER_ID  --restore_step 900000 --mode single -p config/EmoV_DB/preprocess.yaml -m config/EmoV_DB/model.yaml -t config/EmoV_DB/train.yaml
```

For English multi-speaker Emotional Aware TTS with multi-emotions, set multi_emotion to True in model.yaml and run

```
!python3 synthesize.py --text "Example text" --emotion_id EMOTION_ID --speaker_id SPEAKER_ID  --restore_step 900000 --mode single -p config/EmoV_DB/preprocess.yaml -m config/EmoV_DB/model.yaml -t config/EmoV_DB/train.yaml
```

The generated utterances will be put in `output/result/`.

## Controllability

The pitch/volume/speaking rate of the synthesized utterances can be controlled by specifying the desired pitch/energy/duration ratios.
For example, one can increase the speaking rate by 20 % and decrease the volume by 20 % by

```
!python3 synthesize.py --text "Example text" --emotion_id EMOTION_ID --speaker_id SPEAKER_ID  --restore_step 900000 --mode single -p config/EmoV_DB/preprocess.yaml -m config/EmoV_DB/model.yaml -t config/EmoV_DB/train.yaml --duration_control 0.8 --energy_control 0.8
```

# Training

For easy access you can [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/14ijl6OoW73ev9oV5YAiny-XIGIcwpMaV?usp=sharing) and follow the instructions in the jupiter notebook file

## Datasets

The supported datasets are

- [EmoV_DB](https://github.com/numediart/EmoV-DB): a multi-speaker Emotional Voices English dataset consists of four speakers, two females and two males. The emotions expressed in the recordings are amusement, anger, sleepiness,
  and disgust.

## Preprocessing and Training

Follow the steps in [Instructions](FS2_setup_EmoV.ipynb)

# Implementation Issues

- Following [xcmyz's implementation](https://github.com/xcmyz/FastSpeech), I use an additional Tacotron-2-styled Post-Net after the decoder, which is not used in the original FastSpeech 2.
- Gradient clipping is used in the training.
- In my experience, using phoneme-level pitch and energy prediction instead of frame-level prediction results in much better prosody, and normalizing the pitch and energy features also helps. Please refer to `config/README.md` for more details.

Please inform me if you find any mistakes in this repo, or any useful tips to train the FastSpeech 2 model.

# References

- [FastSpeech 2: Fast and High-Quality End-to-End Text to Speech](https://arxiv.org/abs/2006.04558), Y. Ren, _et al_.
- [Text aware Emotional Text-to-speech with BERT](https://www.isca-speech.org/archive/pdfs/interspeech_2022/mukherjee22_interspeech.pdf)
- [xcmyz's FastSpeech implementation](https://github.com/xcmyz/FastSpeech)
- [TensorSpeech's FastSpeech 2 implementation](https://github.com/TensorSpeech/TensorflowTTS)
- [rishikksh20's FastSpeech 2 implementation](https://github.com/rishikksh20/FastSpeech2)

# Citation

```
@INPROCEEDINGS{asonam2024,
 author={Suparna De and Ionut Bostan and Nishanth Sastry},
 booktitle={The 16th International Conference on Advances in Social Networks Analysis and Mining -ASONAM-2024},
 title={Making Social Platforms Accessible: Emotion-Aware Speech Generation with Integrated Text Analysis},
 year={2024}},
 address={Calabria, Italy},
 date={September 2-5, 2024}
```
