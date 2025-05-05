"""
Step 2 - normalize our results both in videos and music
"""

import pandas as pd
import os

# Load normalized CSV files
video_df = pd.read_csv("normalized_video_rhythm.csv")
music_df = pd.read_csv("normalized_music_tempo.csv")

# Prepare a list to collect matches
matches = []

# For each video, find the 3 music tracks with the closest tempo
for _, video_row in video_df.iterrows():
    video_file = video_row['video']
    video_rhythm = video_row['normalized_rhythm']

    # Compute absolute difference to all music tempos
    music_df['difference'] = music_df['normalized_tempo'].apply(lambda tempo: abs(tempo - video_rhythm))

    # Get top 3 closest matches
    top_matches = music_df.nsmallest(3, 'difference')

    for rank, (_, music_row) in enumerate(top_matches.iterrows(), 1):
        matches.append({
            'video_filename': video_file,
            'matched_music_filename': music_row['music'],
            'match_rank': rank,
            'video_score': video_rhythm,
            'music_score': music_row['normalized_tempo'],
            'score_difference': music_row['difference']
        })

# Save to CSV
output_df = pd.DataFrame(matches)
output_df.to_csv("video_music_matches.csv", index=False)

print("Top 3 music matches for each video saved to video_music_matches.csv")
