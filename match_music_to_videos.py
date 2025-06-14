"""
Step 1 - normalize our results both in videos and music
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load video rhythm scores
video_df = pd.read_csv('video_rhythm_results.csv')

# Load music tempo scores
music_df = pd.read_csv('music_tempo_scores.csv')

# Normalize rhythm scores
video_scaler = MinMaxScaler()
video_df['normalized_rhythm'] = video_scaler.fit_transform(video_df[['rhythm_score']])


# Convert string like '[80.74951172]' to float 80.74951172
music_df['tempo'] = music_df['tempo'].apply(lambda x: float(x.strip('[]')))

# Normalize tempo scores
music_scaler = MinMaxScaler()
music_df['normalized_tempo'] = music_scaler.fit_transform(music_df[['tempo']])

# Save normalized files (optional, for inspection)
video_df.to_csv('normalized_video_rhythm.csv', index=False)
music_df.to_csv('normalized_music_tempo.csv', index=False)

#normalized_music_tempo.csv is the old file, the new updated file is normalized_music_features.csv

print("Normalization complete. Data saved to CSV.")




