from flask import Flask, request, jsonify, send_file, send_from_directory
import os
from music_recommendation import get_top3_music_for_video
from analyze_rhythm import estimate_rhythm
from flask_cors import CORS
import moviepy as mpe
from pydub import AudioSegment

#To be updated

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

CORS(app)

"""
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
    full_audio = full_audio.with_duration(video_clip.duration)
    video_with_audio = video_clip.with_audio(full_audio)
    video_with_audio.write_videofile(output_path, codec='libx264', audio_codec='aac')

    # Return merged file for download
    return send_file(output_path, as_attachment=True)
    
    """

@app.route('/merge_and_download', methods=['POST'])
def merge_and_download():
    video = request.files['video']
    music_title = request.form['music']

    # ✅ Get optional audio-tune preferences
    """
    add_fade = request.form.get('add_fade') == 'true'
    mood_intensity = int(request.form.get('mood_intensity', 50))
    instrumentation = int(request.form.get('instrumentation', 50))
    """

    # Save uploaded video
    upload_folder = 'uploads'
    os.makedirs(upload_folder, exist_ok=True)
    video_path = os.path.join(upload_folder, video.filename)
    video.save(video_path)

    # Full music path
    music_folder = 'music'
    music_path = os.path.join(music_folder, music_title)

    # Output path
    output_path = os.path.join(upload_folder, f"merged_{video.filename}")

    # Load media
    video_clip = mpe.VideoFileClip(video_path)
    audio_clip = mpe.AudioFileClip(music_path)

    # Loop and trim audio to video duration
    loops = int(video_clip.duration // audio_clip.duration) + 1
    full_audio = mpe.concatenate_audioclips([audio_clip] * loops)
    full_audio = full_audio.with_duration(video_clip.duration)

    # Merge
    final_video = video_clip.with_audio(full_audio)
    final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')

    return send_file(output_path, as_attachment=True)

# Apply fade in if requested
"""
@app.route('/apply_fade', methods=['POST'])
def apply_fade():

    merged_video_name = request.form['video_name']  # e.g., 'merged_video.mp4'
    fade_duration_ms = int(request.form.get('fade_duration', 2000))  # Optional control from slider

    input_path = os.path.join('uploads', merged_video_name)
    faded_path = os.path.join('uploads', f'faded_{merged_video_name}')

    # 1. Extract audio
    video_clip = mpe.VideoFileClip(input_path)
    audio_temp_path = os.path.splitext(input_path)[0] + "_temp_audio.mp3"
    video_clip.audio.write_audiofile(audio_temp_path)

    # 2. Apply fade using pydub
    audio = AudioSegment.from_mp3(audio_temp_path)
    faded_audio = audio.fade_in(fade_duration_ms).fade_out(fade_duration_ms)
    faded_mp3_path = os.path.splitext(audio_temp_path)[0] + "_faded.mp3"
    faded_audio.export(faded_mp3_path, format="mp3")

    # 3. Reattach faded audio
    faded_audio_clip = mpe.AudioFileClip(faded_mp3_path)
    final_clip = video_clip.with_audio(faded_audio_clip)
    final_clip.write_videofile(faded_path, codec='libx264', audio_codec='aac')

    # Cleanup temp files
    os.remove(audio_temp_path)
    os.remove(faded_mp3_path)

    return send_file(faded_path, as_attachment=True)
    """

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



