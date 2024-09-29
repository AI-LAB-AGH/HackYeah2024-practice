import os
import json
import torch
import librosa
import soundfile as sf
import moviepy.editor as mp
import azure.cognitiveservices.speech as speechsdk


class SpeechToText:
    def __init__(self) -> None:
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.key = "9cf400b6a7a3492c90b1ad0f6bd640f6"
        self.region = "westeurope"

    def __repr__(self) -> str:
        return "Class to load model from whisper_timestamped"


    def convert_audio(self, video_path) -> None:
        audio_path = os.path.splitext(video_path)[0] + '.wav'
        with mp.VideoFileClip(video_path) as video:
            video.audio.write_audiofile(audio_path)
        return audio_path
    

    def trim_audio(self, audio_path) -> None:
        y, sr = librosa.load(audio_path)
        y_trimmed, _ = librosa.effects.trim(y)
        
        audio_path = audio_path.split(".")[0] + '_trim.wav'
        sf.write(audio_path, y_trimmed, sr)
        return audio_path


    def transcribe_wav(self, video_path) -> str:
        speech_config = speechsdk.SpeechConfig(subscription=self.key, region=self.region)
        speech_config.request_word_level_timestamps()
        speech_config.speech_recognition_language = "pl-PL"

        audio_path = os.path.splitext(video_path)[0] + '.wav'
        with mp.VideoFileClip(video_path) as video:
            video.audio.write_audiofile(audio_path)

        audio_path = self.trim_audio(audio_path)

        audio_input = speechsdk.AudioConfig(filename=audio_path)

        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
        speech_config.output_format = speechsdk.OutputFormat.Detailed

        result = speech_recognizer.recognize_once()

        prefix = audio_path.split(".")[0]
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            detailed_result = json.loads(result.json)
            with open(f"{prefix}.json", "w") as f:
                json.dump(detailed_result, f, ensure_ascii=False)

            nbest_result = detailed_result['NBest'][0]
            words = nbest_result['Words']

            # words - array of dicts with the attributes: Word, Offset, Duration
            for word_info in words:
                word = word_info['Word']
                start_time = word_info['Offset'] / 10_000_000  # Convert from 100-nanosecond units to seconds
                duration = word_info['Duration'] / 10_000_000  # Convert from 100-nanosecond units to seconds
                print(f"Word: '{word}', Start Time: {start_time}s, Duration: {duration}s")
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized.")
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print(f"Speech Recognition canceled: {cancellation_details.reason}")
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print(f"Error details: {cancellation_details.error_details}")

        return detailed_result
