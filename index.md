---
layout: default
title: Emotion-Aware TTS
---

## Authors

**Suparna De**  
Email: [s.de@surrey.ac.uk](mailto:s.de@surrey.ac.uk)

**Ionut Bostan**  
Email: [ionut@nquiringminds.com](mailto:ionut@nquiringminds.com)

**Nishanth Sastry**  
Email: [n.sastry@surrey.ac.uk](mailto:n.sastry@surrey.ac.uk)

---

## Abstract

Recent studies have outlined the accessibility challenges that blind and visually impaired people face in interacting
with social networks, with monotone text-to-speech (TTS) screen
readers and audio narration of visual elements such as emojis.
Emotional speech generation traditionally relies on human input
of the expected emotion together with the text to synthesise,
with additional challenges around data simplification (causing
information loss) and duration inaccuracy, leading to lack of
expressive emotional rendering. In real-life communications, the
duration of phonemes can vary since the same sentence might
be spoken in a variety of ways depending on the speakers’
emotional states or accents (referred to as the one-to-many
problem of text to speech generation). As a result, an advanced
voice synthesis system is required to account for this unpredictability. We propose an end-to-end context-aware Text-toSpeech (TTS) synthesis system that derives the conveyed emotion
from text input and synthesises audio that focuses on emotions
and speaker features for natural and expressive speech, integrating advanced natural language processing (NLP) and speech
synthesis techniques for real-time applications. The proposed
system has two core components: an emotion classifier and a
speech synthesiser. The emotion classifier utilises a classification
model to extract sentiment information from the input text.
Leveraging a non-autoregressive neural TTS model, the speech
synthesiser generates Mel-spectrograms by incorporating speaker
and emotion embeddings derived from the classifier’s output. We
employ a Generative Adversarial Network (GAN)-based vocoder
to convert the Mel-spectrograms into audible waveforms. One of
the key contributions lies in effectively incorporating emotional
characteristics into TTS synthesis. Our system also showcases
competitive inference time performance when benchmarked
against the state-of-the-art TTS models, making it suitable for
real-time accessibility applications.

---

## Demo

Welcome to the demonstration page of our Emotion-Aware Text-to-Speech Models. Below, you can listen to audiohttps://raw.githubusercontent.com/ionut-cmd/Emotion-Aware-TTS/main/FastSpeech2_Text_Aware_Emotion_TTS samples from different TTS models.

<table>
  <tr>
    <th>Description</th>
    <th>FastSpeech 2[1]</th>
    <th>TEMOTTS[2]</th>
    <th>Our Model</th>
  </tr>
  <tr>
    <td>Bikes are fun to ride</td>
    <td>
      <audio controls>
        <source src="https://raw.githubusercontent.com/ionut-cmd/Emotion-Aware-TTS/main/FastSpeech2_Text_Aware_Emotion_TTS/samples/fastspeech/Bikes_are_fun_to_ride__gen.wav" type="audio/wav">
        Your browser does not support the audio tag.
      </audio>
    </td>
    <td>
      <audio controls>
        <source src="https://raw.githubusercontent.com/ionut-cmd/Emotion-Aware-TTS/main/FastSpeech2_Text_Aware_Emotion_TTS/samples/temotts/Bikes_are_fun_to_ride__gen.wav" type="audio/wav">
        Your browser does not support the audio tag.
      </audio>
    </td>
    <td>
      <audio controls>
        <source src="https://raw.githubusercontent.com/ionut-cmd/Emotion-Aware-TTS/main/FastSpeech2_Text_Aware_Emotion_TTS/samples/ours/Bikes are fun to ride..wav" type="audio/wav">
        Your browser does not support the audio tag.
      </audio>
    </td>
    </tr>
    <tr>
        <td>Dreams can come true</td>
        <td>
        <audio controls>
            <source src="https://raw.githubusercontent.com/ionut-cmd/Emotion-Aware-TTS/main/FastSpeech2_Text_Aware_Emotion_TTS/samples/fastspeech/Dreams_can_come_true__gen.wav" type="audio/wav">
            Your browser does not support the audio tag.
        </audio>
        </td>
        <td>
        <audio controls>
            <source src="https://raw.githubusercontent.com/ionut-cmd/Emotion-Aware-TTS/main/FastSpeech2_Text_Aware_Emotion_TTS/samples/temotts/Dreams_can_come_true__gen.wav" type="audio/wav">
            Your browser does not support the audio tag.
        </audio>
        </td>
        <td>
        <audio controls>
            <source src="https://raw.githubusercontent.com/ionut-cmd/Emotion-Aware-TTS/main/FastSpeech2_Text_Aware_Emotion_TTS/samples/ours/Dreams can come true.wav" type="audio/wav">
            Your browser does not support the audio tag.
        </audio>
        </td>
    </tr>
     <tr>
        <td>Friends make life more fun</td>
        <td>
        <audio controls>
            <source src="https://raw.githubusercontent.com/ionut-cmd/Emotion-Aware-TTS/main/FastSpeech2_Text_Aware_Emotion_TTS/samples/fastspeech/Friends_make_life_more_fun__gen.wav" type="audio/wav">
            Your browser does not support the audio tag.
        </audio>
        </td>
        <td>
        <audio controls>
            <source src="https://raw.githubusercontent.com/ionut-cmd/Emotion-Aware-TTS/main/FastSpeech2_Text_Aware_Emotion_TTS/samples/temotts/Friends_make_life_more_fun__gen.wav" type="audio/wav">
            Your browser does not support the audio tag.
        </audio>
        </td>
        <td>
        <audio controls>
            <source src="https://raw.githubusercontent.com/ionut-cmd/Emotion-Aware-TTS/main/FastSpeech2_Text_Aware_Emotion_TTS/samples/ours/Friends make life more fun.wav" type="audio/wav">
            Your browser does not support the audio tag.
        </audio>
        </td>
    </tr>
</table>

### Emotion Aware Samples

<table>
  <tr>
    <th>Description</th>
    <th>FastSpeech 2[1]</th>
    <th>TEMOTTS[2]</th>
    <th>Our Model</th>
  </tr>
  <tr>
    <td>Blowing out birthday candles makes me feel special!</td>
    <td>
      <audio controls>
        <source src="https://raw.githubusercontent.com/ionut-cmd/Emotion-Aware-TTS/main/FastSpeech2_Text_Aware_Emotion_TTS/samples/fastspeech/Blowing_out_birthday_candles_makes_me_feel_special__gen.wav" type="audio/wav">
        Your browser does not support the audio tag.
      </audio>
    </td>
    <td>
      <audio controls>
        <source src="https://raw.githubusercontent.com/ionut-cmd/Emotion-Aware-TTS/main/FastSpeech2_Text_Aware_Emotion_TTS/samples/temotts/Blowing_out_birthday_candles_makes_me_feel_special__gen.wav" type="audio/wav">
        Your browser does not support the audio tag.
      </audio>
    </td>
    <td>
      <audio controls>
        <source src="https://raw.githubusercontent.com/ionut-cmd/Emotion-Aware-TTS/main/FastSpeech2_Text_Aware_Emotion_TTS/samples/ours/Blowing out birthday candles makes me feel special!.wav" type="audio/wav">
        Your browser does not support the audio tag.
      </audio>
    </td>
    </tr>
    <tr>
        <td>Her heart felt heavy with sorrow</td>
        <td>
        <audio controls>
            <source src="https://raw.githubusercontent.com/ionut-cmd/Emotion-Aware-TTS/main/FastSpeech2_Text_Aware_Emotion_TTS/samples/fastspeech/Her_heart_felt_heavy_with_sorrow__gen.wav" type="audio/wav">
            Your browser does not support the audio tag.
        </audio>
        </td>
        <td>
        <audio controls>
            <source src="https://raw.githubusercontent.com/ionut-cmd/Emotion-Aware-TTS/main/FastSpeech2_Text_Aware_Emotion_TTS/samples/temotts/Her_heart_felt_heavy_with_sorrow__gen.wav" type="audio/wav">
            Your browser does not support the audio tag.
        </audio>
        </td>
        <td>
        <audio controls>
            <source src="https://raw.githubusercontent.com/ionut-cmd/Emotion-Aware-TTS/main/FastSpeech2_Text_Aware_Emotion_TTS/samples/ours/Her heart felt heavy with sorrow.wav" type="audio/wav">
            Your browser does not support the audio tag.
        </audio>
        </td>
    </tr>
     <tr>
        <td>I am feeling sad</td>
        <td>
        <audio controls>
            <source src="https://raw.githubusercontent.com/ionut-cmd/Emotion-Aware-TTS/main/FastSpeech2_Text_Aware_Emotion_TTS/samples/fastspeech/I_am_feeling_sad__gen.wav" type="audio/wav">
            Your browser does not support the audio tag.
        </audio>
        </td>
        <td>
        <audio controls>
            <source src="https://raw.githubusercontent.com/ionut-cmd/Emotion-Aware-TTS/main/FastSpeech2_Text_Aware_Emotion_TTS/samples/temotts/I_am_feeling_sad__gen.wav" type="audio/wav">
            Your browser does not support the audio tag.
        </audio>
        </td>
        <td>
        <audio controls>
            <source src="https://raw.githubusercontent.com/ionut-cmd/Emotion-Aware-TTS/main/FastSpeech2_Text_Aware_Emotion_TTS/samples/ours/I am feeling sad.wav" type="audio/wav">
            Your browser does not support the audio tag.
        </audio>
        </td>
    </tr>
</table>

# References

---

1. Yi Ren, Chenxu Hu, Xu Tan, Tao Qin, Sheng Zhao, Zhou Zhao, and Tie-Yan Liu, “Fastspeech 2: Fast and high-quality end-to-end text to speech,” in International Conference on Learning Representations, 2021.
2. Shreeram Suresh Chandra, Zongyang Du, Berrak Sisman, "TEMOTTS: Text-aware Emotional Text-to-Speech with no labels", Speech & Machine Learning Lab, The University of Texas at Dallas, TX, USA, 2024.
