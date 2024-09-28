import librosa
import os
import soundfile as sf

class AnalyzeAudio:
    def __init__(self) -> None:
        self.audio_path = './audio_folder/'
        self.audio_path_trimmed = './audio_folder_trimmed/'

    def __repr__(self) -> str:
        return f'AnalyzeAudio({self.audio_path})'
    
    def get_tempo(self) -> dict:
        tempo_dict: dict = {}

        for audio in os.listdir(self.audio_path):
            print(f'Analyzing {audio}...')
            y, sr = librosa.load(self.audio_path_trimmed + audio)
            onset_env = librosa.onset.onset_strength(y = y, sr = sr)
            tempo, _ = librosa.beat.beat_track(onset_envelope = onset_env, sr = sr)
            tempo_dict[audio] = round(tempo[0])

        return tempo_dict
    
    def trim_audio(self) -> None:
        for audio in os.listdir(self.audio_path):
            y, sr = librosa.load(self.audio_path + audio)
            y_trimmed, _ = librosa.effects.trim(y)
            
            # save to folder audio_folder_trimmed
            sf.write(f'./audio_folder_trimmed/{audio}', y_trimmed, sr)