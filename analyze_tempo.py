import os
import librosa
import pandas as pd

# Folder where music is stored music
music_dir = 'music/'

results = []

for filename in os.listdir(music_dir):
    if filename.endswith('.mp3'):
        file_path = os.path.join(music_dir, filename)
        try:
            y, sr = librosa.load(file_path)
            tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
            results.append({'music': filename, 'tempo': tempo})
            print(f"✅ {filename}: {float(tempo):.2f} BPM")
        except Exception as e:
            print(f'Error processing {filename}: {e}')

# Save to CSV
df = pd.DataFrame(results)
df.to_csv('music_tempo_scores.csv', index=False)
print("Tempo scores saved to music_tempo_scores.csv")
