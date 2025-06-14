import pandas as pd

# Load inputs
video_rhythm_df = pd.read_csv('normalized_video_rhythm.csv')
video_emotion_df = pd.read_csv('video_emotions.csv')
music_df = pd.read_csv('normalized_music_features.csv')

# Merge video info
video_df = pd.merge(video_rhythm_df, video_emotion_df, on='video')
video_df.rename(columns={
    'normalized_rhythm': 'video_rhythm',
    'emotion': 'video_emotion'
}, inplace=True)

# Normalize column names in music
music_df.rename(columns={
    'tempo_norm': 'music_tempo',
    'volume_norm': 'music_volume'
}, inplace=True)

# Emotion to target volume map
emotion_to_volume = {
    'happy': 0.8,
    'sad': 0.2,
    'neutral': 0.5,
    'angry': 1.0,
    'fear': 0.3,
    'surprise': 0.6
}

matches = []

for _, video_row in video_df.iterrows():
    vid = video_row['video']
    rhythm = video_row['video_rhythm']
    emotion = video_row['video_emotion']

    # Get target volume based on emotion
    if emotion not in emotion_to_volume:
        print(f" Skipping {vid} - unknown emotion: {emotion}")
        continue
    target_volume = emotion_to_volume[emotion]

    # Calculate score for each music track
    music_df['score'] = 0.5 * abs(music_df['music_tempo'] - rhythm) + \
                        0.5 * abs(music_df['music_volume'] - target_volume)

    top_matches = music_df.nsmallest(3, 'score')

    for rank, (_, music_row) in enumerate(top_matches.iterrows(), 1):
        matches.append({
            'video_filename': vid,
            'matched_music_filename': music_row['music'],
            'match_rank': rank,
            'video_score_rhythm': rhythm,
            'target_volume_from_emotion': target_volume,
            'music_score_tempo': music_row['music_tempo'],
            'music_score_volume': music_row['music_volume'],
            'video_emotion': emotion,
            'score_difference': music_row['score']
        })

# Export results
matches_df = pd.DataFrame(matches)
matches_df.to_csv('final_video_music_matches.csv', index=False)
print("Matching complete. Saved to final_video_music_matches.csv")