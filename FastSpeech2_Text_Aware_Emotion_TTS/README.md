# FastSpeech 2 - PyTorch Implementation

This is a PyTorch implementation of Microsoft's text-to-speech system [**FastSpeech 2: Fast and High-Quality End-to-End Text to Speech**](https://arxiv.org/abs/2006.04558v1).
This project is based on [xcmyz's implementation](https://github.com/xcmyz/FastSpeech) of FastSpeech. Feel free to use/modify the code.

There are several versions of FastSpeech 2.
This implementation is more similar to [version 1](https://arxiv.org/abs/2006.04558v1), which uses F0 values as the pitch features.
On the other hand, pitch spectrograms extracted by continuous wavelet transform are used as the pitch features in the [later versions](https://arxiv.org/abs/2006.04558).

![](./img/model.png)

## Dependencies

You can install the Python dependencies with

```
pip3 install -r requirements.txt
```

## Inference

You have to download the [pretrained model](https://drive.google.com/file/d/1_7L2Sxi7m47mfgL-u0l_qEWpqPbTLF1X/view?usp=sharing) and put it in `output/ckpt/EmoV_DB/`.

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
@INPROCEEDINGS{chien2021investigating,
  author={Chien, Chung-Ming and Lin, Jheng-Hao and Huang, Chien-yu and Hsu, Po-chun and Lee, Hung-yi},
  booktitle={ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  title={Investigating on Incorporating Pretrained and Learnable Speaker Representations for Multi-Speaker Multi-Style Text-to-Speech},
  year={2021},
  volume={},
  number={},
  pages={8588-8592},
  doi={10.1109/ICASSP39728.2021.9413880}}
```
