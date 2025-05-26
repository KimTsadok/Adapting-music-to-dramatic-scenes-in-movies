from flask import Flask, request, jsonify, send_file, send_from_directory
import os
from music_recommendation import get_top3_music_for_video
from analyze_rhythm import estimate_rhythm
from flask_cors import CORS
import moviepy.editor as mpe

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

CORS(app)

@app.route('/merge_and_download', methods=['POST'])
def merge_and_download():
    video = request.files['video']
    music_title = request.form['music']

    # Save uploaded video to disk
    upload_folder = 'uploads'
    os.makedirs(upload_folder, exist_ok=True)
    video_path = os.path.join(upload_folder, video.filename)
    video.save(video_path)

    # Full path to the music file
    music_folder = 'music'
    music_path = os.path.join(music_folder, music_title)

    # Output merged video path
    output_path = os.path.join(upload_folder, f"merged_{video.filename}")

    # Merge video + audio (audio looped to match video duration)
    video_clip = mpe.VideoFileClip(video_path)
    audio_clip = mpe.AudioFileClip(music_path)
    loops = int(video_clip.duration // audio_clip.duration) + 1
    full_audio = mpe.concatenate_audioclips([audio_clip] * loops)
    full_audio = full_audio.subclip(0, video_clip.duration)
    video_with_audio = video_clip.set_audio(full_audio)
    video_with_audio.write_videofile(output_path, codec='libx264', audio_codec='aac')

    # Return merged file for download
    return send_file(output_path, as_attachment=True)

@app.route('/music/<filename>')
def get_music(filename):
    return send_from_directory('music', filename)

@app.route('/upload', methods=['POST'])
def upload_video():
    file = request.files['video']
    video_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(video_path)

    # Suppose get_top3_music_for_video returns ["track1.mp3", "track2.mp3", "track3.mp3"]
    top3_music = get_top3_music_for_video(video_path, estimate_rhythm)
    # Create a list of dicts with URLs
    top3_music_with_urls = [
        {
            "title": music_file,
            "url": f"http://localhost:5001/music/{music_file}"
        }
        for music_file in top3_music
    ]

    return jsonify({'top_3_music': top3_music_with_urls})


if __name__ == '__main__':
    app.run(debug=True, port=5001)



