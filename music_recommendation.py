import joblib
import pandas as pd
import numpy as np
from analyze_rhythm import estimate_rhythm

# Load model and music data once
model = joblib.load('random_forest_model.pkl')
music_data = pd.read_csv('normalized_music_tempo.csv')

def get_top3_music_for_video(video_path, estimate_rhythm):
    """
    video_path: path to uploaded video file
    estimate_rhythm: your function for getting rhythm from video
    Returns: List of top 3 music IDs (or names)
    """
    rhythm_score = estimate_rhythm(video_path)  # A number, e.g., 223

    # Replace these with your real min/max!
    min_rhythm = 0
    max_rhythm = 300

    normalized_rhythm = (rhythm_score - min_rhythm) / (max_rhythm - min_rhythm)

    # If you want to use the model (not recommended for now):
    input_pairs = [[normalized_rhythm, tempo] for tempo in music_data['normalized_tempo']]
    predictions = model.predict(input_pairs)
    top3_indices = np.argsort(predictions)[-3:][::-1]
    top3_music_ids = music_data.iloc[top3_indices]['music'].tolist()

    print("Video:", video_path, "Rhythm Normal Score:", normalized_rhythm)
    print("First 5 music tempos:", music_data['normalized_tempo'].head())
    print("First 5 prediction inputs:", input_pairs[:5])
    print("First 5 predictions:", predictions[:5])
    print("Top 3 music indices:", top3_indices)
    print("Top 3 music IDs:", top3_music_ids)
    return top3_music_ids

