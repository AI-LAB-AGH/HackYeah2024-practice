import whisper_timestamped as whisper
import torch
import os
import moviepy.editor as mp
import json

class SpeechToText:
    def __init__(self) -> None:
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = whisper.load_model("small", device = self.device)
        self.path = "Machine_learning/wetransfer_hackyeah-2024-breakwordtraps_2024-09-28_0449"
        self.audio_folder = "Machine_learning/audio_folder"

    def __repr__(self) -> str:
        return "Class to load model from whisper_timestamped"
    
    def convert_audio(self) -> None:
        mp4_paths_list: list = []
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(".mp4"):
                    mp4_paths_list.append(file)
        print(f"MP4 files: {mp4_paths_list}")

        # Convert mp4 to wav, folder path = audio_folder
        for mp4_path in mp4_paths_list:
            prefix = mp4_path.split(".")[0]
            print(f"Converting {mp4_path} to wav")
            clip = mp.VideoFileClip(f"{self.path}/{mp4_path}")
            clip.audio.write_audiofile(f"{self.path}/{prefix}.wav")
            print(f"Converted {mp4_path} to wav")

    def transcribe_wav(self) -> str:
        for root, dirs, files in os.walk(self.audio_folder):
            for file in files:
                if file.endswith(".wav"):
                    prefix = file.split(".")[0]
                    print(f"Transcribing {file}")
                    audio = whisper.load_audio(f"{self.audio_folder}/{file}")
                    result = whisper.transcribe(self.model, audio = audio, language = "pl", vad = "auditok")

                    with open(f"{self.path}/{prefix}.json", "w") as f:
                        json.dump(result, f, ensure_ascii = False)

                    # get some text and save it to .txt file
                    text = result["text"]
                    with open(f"{self.path}/{prefix}.txt", "w") as f:
                        f.write(text)