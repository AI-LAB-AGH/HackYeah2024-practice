import librosa
import os
import soundfile as sf
import numpy as np

class AnalyzeAudio:
    def __init__(self, audio_path='./audio_path') -> None:
        self.audio_path = audio_path
        self.audio_path_trimmed = audio_path + '_trimmed'

    def __repr__(self) -> str:
        return f'AnalyzeAudio({self.audio_path})'
    
    def rms_to_db(self, rms: float) -> float:
        return 20 * np.log10(rms + 1e-9)
    
    def get_tempo(self) -> dict:
        tempo_dict: dict = {}

        for audio in os.listdir(self.audio_path_trimmed):
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

    def too_long_pause(self, min_pause_duration: float = None) -> dict:
        pause_dict: dict = {}

        for audio in os.listdir(self.audio_path_trimmed):
            print(f'Analyzing {audio}...')
            y, sr = librosa.load(self.audio_path_trimmed + audio)
            non_silent_intervals = librosa.effects.split(y, top_db=30)
            pause_list: list = []

            for i in range(1, len(non_silent_intervals)):
                start_of_pause = non_silent_intervals[i-1][1]  # koniec poprzedniego segmentu
                end_of_pause = non_silent_intervals[i][0]      # początek kolejnego segmentu
                pause_duration = (end_of_pause - start_of_pause) / sr  # długość pauzy w sekundach

                if min_pause_duration is None or pause_duration >= min_pause_duration:
                    # Dodajemy pauzę jako tuplę (początek, koniec, długość pauzy)
                    pause_list.append(
                        (round(start_of_pause / sr, 3), round(end_of_pause / sr, 3), round(pause_duration, 3))
                    )

            pause_dict[audio] = pause_list

        return pause_dict
    
    def loudness_quietness(self) -> dict:
        loudness_dict: dict = {}
        quietness_dict: dict = {}

        # Progi w decybelach
        upper_threshold_db = -20  # np. segmenty głośniejsze niż -20 dB
        lower_threshold_db = -40  # np. segmenty cichsze niż -40 dB

        # Długość segmentu w sekundach
        segment_length = 0.5

        for audio in os.listdir(self.audio_path_trimmed):
            print(f'Analyzing {audio}...')
            y, sr = librosa.load(self.audio_path_trimmed + audio)

            # Zidentyfikuj segmenty niebędące ciszą (top_db określa próg ciszy)
            non_silent_intervals = librosa.effects.split(y, top_db=10)  # Próg ciszy to 30 dB

            # Przechowuj poziomy głośności i cichości dla każdego segmentu
            loud_segments = []
            quiet_segments = []

            for interval in non_silent_intervals:
                start_sample, end_sample = interval

                # Podziel segmenty niebędące ciszą na fragmenty co 0.5 sekundy
                for i in range(start_sample, end_sample, int(sr * segment_length)):
                    segment_end = min(i + int(sr * segment_length), end_sample)
                    segment = y[i:segment_end]

                    if len(segment) > 0:
                        # Oblicz RMS i przekształć na dB
                        rms = np.sqrt(np.mean(segment**2))
                        db = self.rms_to_db(rms)

                        # Konwersja próbek na czas
                        start_time = i / sr
                        end_time = segment_end / sr

                        # Sprawdzanie czy dB przekracza progi
                        if db > upper_threshold_db:
                            loud_segments.append((start_time, end_time, db))  # Głośne fragmenty
                        elif db < lower_threshold_db:
                            quiet_segments.append((start_time, end_time, db))  # Ciche fragmenty

            # Zapis wyników dla każdego pliku audio
            loudness_dict[audio] = loud_segments
            quietness_dict[audio] = quiet_segments

        return loudness_dict, quietness_dict
    
    def overall_loudness(self) -> dict:
        loudness_dict: dict = {}

        for audio in os.listdir(self.audio_path_trimmed):
            print(f'Analyzing {audio}...')
            y, sr = librosa.load(self.audio_path_trimmed + audio)

            # Oblicz RMS i przekształć na dB
            rms = np.sqrt(np.mean(y**2))
            db = self.rms_to_db(rms)

            loudness_dict[audio] = round(db, 1)

        return loudness_dict