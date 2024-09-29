import numpy as np

from audio_analyze import AnalyzeAudio
from speech_to_text import SpeechToText

analyze = AnalyzeAudio()
speech = SpeechToText()

# speech.transcribe_wav()

# trim from silence
# analyze.trim_audio()

# get tempo of audio files
# print(analyze.get_tempo())

# print(analyze.too_long_pause(min_pause_duration = 0.75))

# ld, qd = analyze.loudness_quietness()
# print(f"Loudness: ")
# print(ld)
# print(f"Quietness: ")
# print(qd)

# printing overall loudness
# loudness_dict = analyze.overall_loudness()

# sort by loudness
# loudness_dict = dict(sorted(loudness_dict.items(), key = lambda item: item[1], reverse = True))

# for key, value in loudness_dict.items():
#     print(f"{key}: {value}")  

for key, value in analyze.white_noise().items():
    print(f"{key}: {value}")