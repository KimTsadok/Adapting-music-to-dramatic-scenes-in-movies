import os
import cv2
from fer import FER
import pandas as pd

# Adjust path if your videos are elsewhere
video_folder = 'videos/'
results = []

# FER uses MTCNN for better face detection
detector = FER(mtcnn=True)

for filename in os.listdir(video_folder):
    if filename.endswith(".mp4"):
        video_path = os.path.join(video_folder, filename)
        cap = cv2.VideoCapture(video_path)

        frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
        frame_count = 0
        emotions = []

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Sample 1 frame per second
            if frame_count % frame_rate == 0:
                try:
                    analysis = detector.detect_emotions(frame)
                    if analysis:
                        dominant = max(analysis[0]["emotions"], key=analysis[0]["emotions"].get)
                        emotions.append(dominant)
                except Exception as e:
                    print(f"Error analyzing {filename}: {e}")

            frame_count += 1

        cap.release()

        # Get the most common emotion in the video
        dominant_emotion = max(set(emotions), key=emotions.count) if emotions else "neutral"
        print(f"✅ {filename}: {dominant_emotion}")
        results.append({"video": filename, "emotion": dominant_emotion})

# Save to CSV
df = pd.DataFrame(results)
df.to_csv("video_emotions.csv", index=False)
print("🎉 Saved to video_emotions.csv")
