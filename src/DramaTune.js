import React, { useState, useRef } from "react";
import { useEffect } from "react";

export default function DramaTune() {
  const [video, setVideo] = useState(null);
  const [loading, setLoading] = useState(false);
  const [musicTracks, setMusicTracks] = useState([]);
  const [isAnalyzed, setIsAnalyzed] = useState(false);
  const videoRef = useRef(null);
  const fileInputRef = useRef(null);

  // 👇 ADD THESE
  const moodRef = useRef(null);
  const instrRef = useRef(null);

  const [selectedTrack, setSelectedTrack] = useState(null);
  const [finalVideoUrl, setFinalVideoUrl] = useState(null);
  const [progressVisible, setProgressVisible] = useState(false);
  const [progress, setProgress] = useState(0);
  const [addFade, setAddFade] = useState(false);
  const [moodIntensity, setMoodIntensity] = useState(50);
  const [instrumentation, setInstrumentation] = useState(50);

  useEffect(() => {
  const brown = "#5C3A1E";
  const white = "white";

  if (moodRef.current) {
    moodRef.current.style.background = `linear-gradient(to right, ${brown} 0%, ${brown} ${moodIntensity}%, ${white} ${moodIntensity}%, ${white} 100%)`;
  }

  if (instrRef.current) {
    instrRef.current.style.background = `linear-gradient(to right, ${brown} 0%, ${brown} ${instrumentation}%, ${white} ${instrumentation}%, ${white} 100%)`;
  }
}, [moodIntensity, instrumentation]);

  const handleUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      if (video) {
        URL.revokeObjectURL(video);
      }
      const videoURL = URL.createObjectURL(file);
      setVideo(videoURL);
      setMusicTracks([]);
      setIsAnalyzed(false);
    }
  };

  const handleReupload = () => {
    if (video) {
      URL.revokeObjectURL(video);
    }

    setVideo(null);
    setMusicTracks([]);
    setIsAnalyzed(false);
    setLoading(false);
    fileInputRef.current.click();
  };

  const handleAnalyze = async () => {
  setLoading(true);
  setIsAnalyzed(false);
  setProgress(0); // Start from 0%

  // Animate progress over 6 seconds
  const interval = setInterval(() => {
    setProgress((prev) => {
      if (prev >= 100) {
        clearInterval(interval);
        return 100;
      }
      return prev + 1.7;
    });
  }, 100);

  const formData = new FormData();
  const videoFile = videoRef.current?.children[0]?.src;

  try {
    const blob = await fetch(videoFile).then((r) => r.blob());
    const file = new File([blob], "uploaded_video.mp4", { type: blob.type });
    formData.append("video", file);

    const response = await fetch("http://localhost:5001/upload", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    setMusicTracks(data.top_3_music);
    setIsAnalyzed(true);
  } catch (error) {
    console.error("Error analyzing video:", error);
  } finally {
    setProgress(100);
    setTimeout(() => setLoading(false), 1500); // let animation finish
  }
};

  const handleGenerateVideo = async () => {
    if (!selectedTrack || !videoRef.current) return;

    setProgress(0);
    setProgressVisible(true);

    const interval = setInterval(() => {
      setProgress((prev) => {
        if (prev >= 100) {
          clearInterval(interval);
          return 100;
        }
        return prev + 1.7;
      });
    }, 100);

    const formData = new FormData();
    const videoFileSrc = videoRef.current.children[0]?.src;
    const blob = await fetch(videoFileSrc).then((r) => r.blob());
    const file = new File([blob], "uploaded_video.mp4", { type: blob.type });

    formData.append("video", file);
    formData.append("music", selectedTrack.title);

    formData.append("add_fade", addFade);
    formData.append("mood_intensity", moodIntensity);
    formData.append("instrumentation", instrumentation);

    try {
      const response = await fetch("http://localhost:5001/merge_and_download", {
        method: "POST",
        body: formData,
      });

      const blob = await response.blob();
      const mergedUrl = URL.createObjectURL(blob);
      setFinalVideoUrl(mergedUrl);
    } catch (error) {
      console.error("Error generating merged video:", error);
    } finally {
      setProgress(100);
      setTimeout(() => setProgressVisible(false), 1500);
    }
  };

  return (
      <div className="p-6 max-w-lg mx-auto space-y-4">
        <h1 className="t-font">DramaTune</h1>
        <input type="file" ref={fileInputRef} accept="video/*" onChange={handleUpload} style={{display: 'none'}}/>

        {!video && (
            <button
                onClick={() => fileInputRef.current.click()}
                className="w-full px-4 py-2 bg-blue-500 text-black rounded-md hover:bg-blue-600 transition-colors"
            >
              Choose Video
            </button>
        )}

        {video && !finalVideoUrl && (
            <div className="video-container mb-4">
              <video
                  ref={videoRef}
                  controls
                  className="w-full rounded-lg shadow-md"
              >
                <source src={video} type="video/mp4"/>
                Your browser does not support the video tag.
              </video>

              <button
                  onClick={handleReupload}
                  className="mt-2 w-full px-4 py-2 bg-gray-200 text-gray-800 rounded-md hover:bg-gray-300 transition-colors"
              >
                Change Video
              </button>
            </div>
        )}

        {video && !isAnalyzed && (
            <button
                onClick={handleAnalyze}
                className="w-full px-4 py-2 bg-green-500 text-black rounded-md hover:bg-green-600 transition-colors"
            >
              Analyze Video
            </button>
        )}

        {/*first progress bar*/}
        {loading && (
            <div className="w-full bg-gray-200 rounded-full h-2.5 mt-4">
              <div
                  className="bg-blue-600 h-2.5 rounded-full transition-all duration-300"
                  style={{width: `${progress}%`}}
              ></div>
            </div>
        )}

        {isAnalyzed && musicTracks.length > 0 && (
            <div className="space-y-2">
              <h2 className="text-lg font-semibold">Suggested Tracks</h2>
              <div className="tracks-op space-y-4">
                {musicTracks.map((track, index) => (
                    <div key={track.url} className="track-item border rounded-lg shadow-sm">
                      <div className="p-4">
                        <span className="block mb-2">{`Dramatic Score ${index + 1}`}</span>
                        <div className="flex justify-center gap-4">
                          <button
                              className="px-4 py-2 bg-blue-500 text-white rounded-md"
                              onClick={() => window.open(track.url)}
                          >
                            Play
                          </button>

                          <button
                              className={`px-4 py-2 rounded-md border font-semibold ${
                                  selectedTrack?.url === track.url
                                      ? "bg-[#5C3A1E] text-black"
                                      : "bg-[#A97452] text-black hover:bg-[#8b5a2b]"
                              }`}
                              onClick={() => setSelectedTrack(track)}
                          >
                            {selectedTrack?.url === track.url ? "Selected" : "Select"}
                          </button>
                        </div>
                      </div>
                    </div>
                ))}

                {selectedTrack && (
                    <button
                        className="mt-2 w-full px-4 py-2 bg-gray-200 text-gray-800 rounded-md hover:bg-gray-300 transition-colors"
                        onClick={handleGenerateVideo}
                    >
                      Generate a new video
                    </button>
                )}
              </div>
            </div>
        )}

        {/*Fine tuning components*/}

  {finalVideoUrl && (
  <div className="space-y-4 mt-4">
    <h2 className="text-lg font-semibold">Audio Effects</h2>

    <div className="flex items-center justify-between">
      <label htmlFor="fade" className="mr-4">Add Fade In/Out</label>
      <input
        type="checkbox"
        id="fade"
        checked={addFade}
        onChange={() => setAddFade(!addFade)}
      />
    </div>

      <div>
          <label className="block mb-1">Mood Intensity</label>
          <input
              type="range"
              ref={moodRef}
              min="0"
              max="100"
              value={moodIntensity}
              onChange={(e) => setMoodIntensity(Number(e.target.value))}
              className="w-full custom-slider"
          />
      </div>

      <div>
          <label className="block mb-1">Instrumentation</label>
          <input
              type="range"
              ref={instrRef}
              min="0"
              max="100"
              value={instrumentation}
              onChange={(e) => setInstrumentation(Number(e.target.value))}
              className="w-full custom-slider"
          />
      </div>
  </div>
  )}


          {/*second progress bar*/}
          {progressVisible && (
              <div className="w-full bg-gray-200 rounded-full h-2.5 mt-4">
                  <div
                      className="bg-blue-600 h-2.5 rounded-full transition-all duration-300"
                  style={{width: `${progress}%`}}
              ></div>
            </div>
        )}

        {finalVideoUrl && (
            <div className="mt-4">
              <h3 className="text-md font-semibold mb-2">Preview of Merged Video</h3>
              <video controls src={finalVideoUrl} className="w-full rounded-lg shadow-md"/>
              <button
                  className="mt-2 px-4 py-2 bg-blue-500 text-black rounded-md"
                  onClick={() => {
                    const a = document.createElement("a");
                    a.href = finalVideoUrl;
                    a.download = "final_video.mp4";
                    a.click();
                  }}
              >
                Download Video
              </button>
            </div>
        )}
      </div>
  );
}
