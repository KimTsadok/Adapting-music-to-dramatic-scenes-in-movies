import pandas as pd
import numpy as np
import joblib
from analyze_rhythm import estimate_rhythm
from emotion_utils import detect_emotion_from_video

# Load model and features
model = joblib.load("random_forest_model.pkl")
music_df = pd.read_csv("normalized_music_features.csv")  # expects: music, tempo_norm, volume_norm

# Define emotion encoding
emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
emotion_to_index = {e: i for i, e in enumerate(emotion_labels)}

def get_top3_music_for_video(video_path):
    # 1. Rhythm detection
    rhythm_score = estimate_rhythm(video_path)
    normalized_rhythm = (rhythm_score - 0) / (300 - 0)

    # 2. Emotion detection
    video_emotion = detect_emotion_from_video(video_path)
    emotion_index = emotion_to_index.get(video_emotion, -1)

    # 3. Predict match score per music track
    def predict_score(row):
        input_vec = [
            normalized_rhythm,
            emotion_index,
            row['tempo_norm'],
            row['volume_norm']
        ]
        return model.predict([input_vec])[0]

    music_df['score'] = music_df.apply(predict_score, axis=1)
    top3 = music_df.nsmallest(3, 'score')

    # 4. Output
    print("Video:", video_path)
    print("Detected emotion:", video_emotion, f"(index {emotion_index})")
    print("Rhythm:", normalized_rhythm)
    print("Top 3 music matches:")
    print(top3[['music', 'score']])

    return top3['music'].tolist(), video_emotion
