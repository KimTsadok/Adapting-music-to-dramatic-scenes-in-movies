import cv2
from fer import FER

def detect_emotion_from_video(video_path):
    """
    Analyze a single video and return the dominant facial emotion.

    Args:
        video_path (str): Path to the video file.

    Returns:
        str: The most frequent emotion detected in the video.
    """
    detector = FER(mtcnn=True)
    cap = cv2.VideoCapture(video_path)

    frame_rate = int(cap.get(cv2.CAP_PROP_FPS)) or 24
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
                print(f" Error analyzing {video_path}: {e}")

        frame_count += 1

    cap.release()

    return max(set(emotions), key=emotions.count) if emotions else "neutral"
