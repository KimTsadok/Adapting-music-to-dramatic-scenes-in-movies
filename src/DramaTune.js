import React, { useState, useRef } from "react";

export default function DramaTune() {
  const [video, setVideo] = useState(null);
  const [loading, setLoading] = useState(false);
  const [musicTracks, setMusicTracks] = useState([]);
  const [isAnalyzed, setIsAnalyzed] = useState(false);
  const videoRef = useRef(null);
  const fileInputRef = useRef(null);

  const handleUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      if (video) {
        URL.revokeObjectURL(video);
      }
      // Create a URL for the uploaded video
      const videoURL = URL.createObjectURL(file);
      setVideo(videoURL);
      setMusicTracks([]);
      setIsAnalyzed(false);
    }
  };

  const handleReupload = () => {
    // Trigger file input click
    if (video) {
      URL.revokeObjectURL(video);
    }
    
    setVideo(null);
    setMusicTracks([]);
    setIsAnalyzed(false);
    setLoading(false);

    // Trigger file input
    fileInputRef.current.click();
  };

  const handleAnalyze = () => {
    setLoading(true);
    setIsAnalyzed(false);
    
    setTimeout(() => {
      setMusicTracks([
        { id: 1, title: "Dramatic Score 1", url: "#" },
        { id: 2, title: "Dramatic Score 2", url: "#" },
        { id: 3, title: "Dramatic Score 3", url: "#" },
      ]);
      setLoading(false);
      setIsAnalyzed(true);
    }, 3000); // Simulating analysis process
  };


  return (
    <div className="p-6 max-w-lg mx-auto space-y-4">
      <h1 className="t-font">DramaTune</h1>
      <input type="file" ref={fileInputRef} accept="video/*" onChange={handleUpload} style={{ display: 'none' }} />
      
      {/* If no video is selected, show upload button */}
      {!video && (
        <button 
          onClick={() => fileInputRef.current.click()}
          className="w-full px-4 py-2 bg-blue-500 text-black rounded-md hover:bg-blue-600 transition-colors"
        >
          Choose Video
        </button>
      )}

      {/* Video Display Section */}
      {video && (
        <div className="video-container mb-4">
          <video 
            ref={videoRef}
            controls 
            className="w-full rounded-lg shadow-md"
          >
            <source src={video} type="video/mp4" />
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
          >Analyze Video</button>
      )}


      {loading && (
        <div className="w-full bg-gray-200 rounded-full h-2.5">
          <div className="bg-blue-600 h-2.5 rounded-full w-1/2"></div>
        </div>
      )}

      {isAnalyzed && musicTracks.length > 0 && (
        <div className="space-y-2">
          <h2 className="text-lg font-semibold">Suggested Tracks</h2>
          <div className="tracks-op">
            {musicTracks.map((track) => (
              <div key={track.id} className="track-item border rounded-lg shadow-sm">
                <div className="flex justify-between items-center p-4">
                  <span>{track.title}</span>
                  <button
                    className="px-4 py-2 bg-blue-500 text-white rounded-md"
                    onClick={() => window.open(track.url)}
                  >
                    Play
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}