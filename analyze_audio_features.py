import os
import librosa
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

#Analyzing audio features to maximize video to soundtrack matching (by BPM and Volume)

# Folder where music is stored
music_dir = 'music/'  # Adjust if needed

results = []

for filename in os.listdir(music_dir):
    if filename.endswith('.mp3'):
        file_path = os.path.join(music_dir, filename)
        try:
            y, sr = librosa.load(file_path)

            # Extract tempo
            tempo, _ = librosa.beat.beat_track(y=y, sr=sr) #calculates bpm, e.g. 120 BPM means 2 beats per sec

            # Extract volume (RMS energy)
            rms = librosa.feature.rms(y=y)[0]
            avg_volume = float(np.mean(rms))  # average volume

            results.append({
                'music': filename,
                'tempo': float(tempo),  # ✅ convert to plain float
                'volume': float(avg_volume)  # already safe, but double-safe now
            })

            print(f" {filename}: {float(tempo):.2f} BPM, Volume: {avg_volume:.5f}")

        except Exception as e:
            print(f' Error processing {filename}: {e}')

# Save to CSV
df = pd.DataFrame(results)
df.to_csv('music_audio_features.csv', index=False) #previously music_tempo_scores.csv
print(" Audio features saved to music_audio_features.csv")

#Normilizing audio features in order to create better matching (0 to 1 values)

# Step 1 – Load your audio features
df = pd.read_csv("music_audio_features.csv")

# Step 2 – Create a MinMaxScaler object
scaler = MinMaxScaler()

# Step 3 – Apply it to the tempo and volume columns
df[['tempo_norm', 'volume_norm']] = scaler.fit_transform(df[['tempo', 'volume']])

# Step 4 – Save the result
df.to_csv("normalized_music_features.csv", index=False)
print(" Saved to normalized_music_features.csv")