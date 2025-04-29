import librosa
import numpy as np
import pandas as pd
import os

# ---- CONFIG ----
whistle_folder = r"C:\Users\Yash Singh\Desktop\WhistleML\Whistle_Segments"       # Whistle split folder
nonwhistle_folder = r"C:\Users\Yash Singh\Desktop\WhistleML\NonWhistle_Segments" # Non-Whistle split folder
output_csv = r"C:\Users\Yash Singh\Desktop\WhistleML\Whistle_Features.csv"       # Final CSV output path

# ---- INIT STORAGE ----
data = []
labels = []

# ---- PROCESS WHISTLE FILES ----
print("\n🔵 Extracting Whistle Features...")
for filename in os.listdir(whistle_folder):
    if filename.endswith(".wav"):
        filepath = os.path.join(whistle_folder, filename)
        y, sr = librosa.load(filepath, sr=None)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mfcc_mean = np.mean(mfcc, axis=1)
        data.append(mfcc_mean)
        labels.append(1)  # Whistle = 1

# ---- PROCESS NON-WHISTLE FILES ----
print("\n🟢 Extracting Non-Whistle Features...")
for filename in os.listdir(nonwhistle_folder):
    if filename.endswith(".wav"):
        filepath = os.path.join(nonwhistle_folder, filename)
        y, sr = librosa.load(filepath, sr=None)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mfcc_mean = np.mean(mfcc, axis=1)
        data.append(mfcc_mean)
        labels.append(0)  # Non-Whistle = 0

# ---- CREATE FINAL DATAFRAME ----
print("\n📦 Saving Features to CSV...")
df = pd.DataFrame(data)
df['label'] = labels

df.to_csv(output_csv, index=False)
print(f"\n🎯 Feature extraction done successfully! Features saved at: {output_csv}")
