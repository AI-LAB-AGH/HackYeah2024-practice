import React, { useState } from "react";
import "../assets/clean/player.css";

const UploadBox = () => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    setSelectedFile(file || null);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please select a file first.");
      return;
    }

    const formData = new FormData();
    formData.append("video", selectedFile);

    await fetch("api/upload-video/", {
      method: "POST",
      body: formData,
      headers: {
        "X-CSRFToken": getCSRFToken(),
      },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.error("Error:", error);
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
      <div
        className="player-wrapper"
        style={selectedFile ? { display: "none" } : {}}
      >
        <img
          src="src/assets/videoplayer.png"
          style={{ width: "100%", height: "auto" }}
        ></img>
        <div className="player-content upload">
          <input type="file" accept="video/*" onChange={handleFileChange} />
          <button onClick={handleUpload}>Upload Video</button>
        </div>
      </div>
    </>
  );
};

export default UploadBox;
