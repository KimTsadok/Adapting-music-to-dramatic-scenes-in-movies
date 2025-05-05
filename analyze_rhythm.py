import cv2
import mediapipe as mp
import os
import pandas as pd

# Initialize MediaPipe pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Folder where videos are stored
video_folder = "videos"
output_data = []

def estimate_rhythm(video_path):
    cap = cv2.VideoCapture(video_path)
    movement_count = 0
    prev_landmarks = None

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Convert image to RGB
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)

        if results.pose_landmarks:
            landmarks = [(lm.x, lm.y, lm.z) for lm in results.pose_landmarks.landmark]

            if prev_landmarks:
                diff = sum([
                    ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5
                    for a, b in zip(landmarks, prev_landmarks)
                ])
                if diff > 0.05:  # Adjust threshold as needed
                    movement_count += 1

            prev_landmarks = landmarks

    cap.release()
    return movement_count

# Loop through all videos
for filename in os.listdir(video_folder):
    if filename.endswith(".mp4"):
        print(f"Processing video: {filename}")
        path = os.path.join(video_folder, filename)
        rhythm = estimate_rhythm(path)
        output_data.append({"video": filename, "rhythm_score": rhythm})

# Save to CSV
df = pd.DataFrame(output_data)
print("Saving to CSV...")
df.to_csv("video_rhythm_results.csv", index=False)
print("Saved successfully.")
