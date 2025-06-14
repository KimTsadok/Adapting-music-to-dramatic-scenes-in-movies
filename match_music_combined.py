import pandas as pd

#New matching logic, BPM and Volume 50% each

# Load the normalized CSVs
video_df = pd.read_csv("normalized_video_rhythm.csv")
music_df = pd.read_csv("normalized_music_features.csv")

# Example mapping of emotion → preferred volume (as norm from 0 to 1)
emotion_volume_map = {
    "sad": 0.2,
    "neutral": 0.4,
    "happy": 0.6,
    "angry": 0.8
}

# You’ll need this CSV from the video emotion detector later:
video_emotion_map = {
    "scene1.mp4": "sad",
    "scene2.mp4": "angry",
    # Add more when you have them
}

# List to hold matches
matches = []

# For each video, compute score with every music track
for _, video_row in video_df.iterrows():
    video_file = video_row['video']
    video_rhythm = video_row['normalized_rhythm']
    emotion = video_emotion_map.get(video_file, "neutral")  # default if unknown
    target_volume = emotion_volume_map[emotion]

    # Calculate score = 50% tempo + 50% volume difference
    music_df['score'] = 0.5 * abs(music_df['tempo_norm'] - video_rhythm) + \
                        0.5 * abs(music_df['volume_norm'] - target_volume)

    top_matches = music_df.nsmallest(3, 'score')

    for rank, (_, music_row) in enumerate(top_matches.iterrows(), 1):
        matches.append({
            "video": video_file,
            "emotion": emotion,
            "matched_music": music_row['music'],
            "match_rank": rank,
            "video_rhythm": video_rhythm,
            "target_volume": target_volume,
            "music_tempo": music_row['tempo_norm'],
            "music_volume": music_row['volume_norm'],
            "score": music_row['score']
        })

# Save results
match_df = pd.DataFrame(matches)
match_df.to_csv("top_matches_combined.csv", index=False)
print(" Saved top_matches_combined.csv")
