import React, { useEffect, useRef } from "react";
import "../assets/clean/player.css";

const CameraComponent: React.FC = () => {
  const videoRef = useRef<HTMLVideoElement | null>(null);
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  const captureFrame = () => {
    if (videoRef.current && canvasRef.current) {
      const canvas = canvasRef.current;
      const context = canvas.getContext("2d");

      if (context) {
        canvas.width = videoRef.current.videoWidth;
        canvas.height = videoRef.current.videoHeight;

        context.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);

        const imageData = canvas.toDataURL("image/jpeg");

        sendFrameToBackend(imageData);
      }
    }
  };

  const sendFrameToBackend = async (imageData: string) => {
    try {
      const response = await fetch("/process-frame/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCSRFToken(),
        },
        body: JSON.stringify({ imageData }),
      });

      const data = await response.json();

      if (canvasRef.current) {
        const img = new Image();
        img.src = `data:image/jpeg;base64,${data.processedFrame}`;
        img.onload = () => {
          const context = canvasRef.current!.getContext("2d");
          if (context) {
            context.clearRect(
              0,
              0,
              canvasRef.current!.width,
              canvasRef.current!.height
            );
            context.drawImage(img, 0, 0);
          }
        };
      }
    } catch (error) {
      console.error("Error sending frame to backend:", error);
    }
  };

  const getCSRFToken = () => {
    const cookieValue = document.cookie
      .split("; ")
      .find((row) => row.startsWith("csrftoken="))
      ?.split("=")[1];
    console.log(cookieValue);
    return cookieValue || "";
  };

  useEffect(() => {
    const getCameraStream = async () => {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({
          video: true,
        });
        if (videoRef.current) {
          videoRef.current.srcObject = stream;
        }
        setInterval(captureFrame, 50);
      } catch (error) {
        console.error("Error accessing camera:", error);
      }
    };

    getCameraStream();

    return () => {
      if (videoRef.current && videoRef.current.srcObject) {
        const stream = videoRef.current.srcObject as MediaStream;
        const tracks = stream.getTracks();
        tracks.forEach((track) => track.stop());
      }
    };
  }, []);

  return (
    <>
      <div className="player-wrapper">
        <img
          src="src/assets/videoplayer.png"
          style={{ width: "100%", height: "auto" }}
        ></img>
        <div>
          <video
            ref={videoRef}
            autoPlay
            playsInline
            style={{ display: "none" }}
          />
          <canvas ref={canvasRef} className="player-content" />
        </div>
      </div>
    </>
  );
};

export default CameraComponent;
