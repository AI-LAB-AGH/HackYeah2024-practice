import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

# Ensure that you have the punkt tokenizer for NLTK
nltk.download('punkt')


# Function to compute text similarity between two Polish sentences
def compute_similarity(sentence1, sentence2):
    # Tokenize sentences
    tokens1 = word_tokenize(sentence1, language='polish')
    tokens2 = word_tokenize(sentence2, language='polish')

    # Rebuild tokenized sentences to avoid issues with TfidfVectorizer
    sentence1 = " ".join(tokens1)
    sentence2 = " ".join(tokens2)

    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform both sentences
    tfidf_matrix = vectorizer.fit_transform([sentence1, sentence2])

    # Compute cosine similarity between the two sentences
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return np.round(similarity[0][0], 4)

sound_transcripts = []
for root, dirs, files in os.walk("video-transcription-manually"):
    for file in files:
        with open(f"video-transcription-manually/{file}", "r", encoding="UTF-8") as f:
            sound_transcripts.append(f.read())

subtitles_transcripts = []

for root, dirs, files in os.walk("text-for-ocr"):
    for file in files:
        with open(f"text-for-ocr/{file}", "r", encoding="UTF-8") as f:
            subtitles_transcripts.append(f.read())

for i in range(len(sound_transcripts)):
    print(compute_similarity(sound_transcripts[i], subtitles_transcripts[i]))


print(subtitles_transcripts[2])
print(sound_transcripts[2])