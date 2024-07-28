import os
import librosa
import numpy as np

def load_data(data_dir):
    genres = os.listdir(data_dir)
    features = []
    labels = []

    for genre in genres:
        genre_dir = os.path.join(data_dir, genre)
        for file_name in os.listdir(genre_dir):
            file_path = os.path.join(genre_dir, file_name)
            mfcc = extract_features(file_path)
            features.append(mfcc)
            labels.append(genre)

    return np.array(features), np.array(labels)

def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=22050, mono=True)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfcc.T, axis=0)
