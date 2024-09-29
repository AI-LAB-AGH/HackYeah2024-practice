import { useState } from "react";
import ReactPlayer from "react-player";
import { useVideo } from "./VideoContext";
import "../assets/clean/player.css";
import ProgressBar from "./ProgressBar";

const VideoPlayer = () => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const { videoUrl, setVideoUrl, setTranscript } = useVideo();

  const progressSegments = [
    { percentage: 15, color: "#00dd77", content: "Brak błędu" },
    { percentage: 5, color: "red", content: "Niezgodność" },
    { percentage: 50, color: "#00dd77", content: "Brak błędu" },
    { percentage: 15, color: "red", content: "Niezgodność" },
    { percentage: 15, color: "#00dd77", content: "Brak błędu" },
  ];

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    setSelectedFile(file || null);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please select a file first.");
      return;
    }

    setLoading(true);
    const formData = new FormData();
    formData.append("video", selectedFile);
    await fetch("api/process-video/", {
      method: "POST",
      body: formData,
      headers: {
        "X-CSRFToken": getCSRFToken(),
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data) {
          setTranscript(data.transcript);
          console.log(data.timestamps);
          fetch("api/get-video/").then(async (response) => {
            const videoBlob = await response.blob();
            const videoObjectUrl = URL.createObjectURL(videoBlob);
            setVideoUrl(videoObjectUrl);
          });
          fetch("api/delete-video/");
        }
      });
  };

  const getCSRFToken = () => {
    const cookieValue = document.cookie
      .split("; ")
      .find((row) => row.startsWith("csrftoken="))
      ?.split("=")[1];
    return cookieValue || "";
  };

  return (
    <>
      <div className="player-wrapper">
        <img
          src="/static/videoplayer.png"
          style={{ width: "100%", height: "auto" }}
        ></img>
        {videoUrl ? (
          <>
            <div className="player-content">
              <ReactPlayer
                url={videoUrl}
                controls={true}
                height={"100%"}
                width={"100%"}
              ></ReactPlayer>
            </div>
            <ProgressBar segments={progressSegments}></ProgressBar>
          </>
        ) : loading ? (
          <div className="player-content">
            <div className="loading"></div>
          </div>
        ) : (
          <div className="player-content upload">
            <div className="file-uploader">
              <label className="custom-file-upload">
                <input
                  type="file"
                  accept="video/*"
                  onChange={handleFileChange}
                />
                Wybierz plik
              </label>
              {selectedFile && <p className="file-name">{selectedFile.name}</p>}
              <button
                className="upload-button"
                onClick={handleUpload}
                disabled={!selectedFile}
              >
                Prześlij
              </button>
            </div>
          </div>
        )}
      </div>
    </>
  );
};

export default VideoPlayer;