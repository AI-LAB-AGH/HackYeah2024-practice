import { createContext, ReactNode, useContext, useState } from "react";

interface VideoContextType {
  videoUrl: string | null;
  transcript: string | null;
  setVideoUrl: (url: string | null) => void;
  setTranscript: (transcript: string | null) => void;
}

const VideoContext = createContext<VideoContextType | undefined>(undefined);

interface Props {
  children: ReactNode;
}

export const VideoProvider = ({ children }: Props) => {
  const [videoUrl, setVideoUrl] = useState<string | null>(null);
  const [transcript, setTranscript] = useState<string | null>(null);

  return (
    <VideoContext.Provider
      value={{ videoUrl, setVideoUrl, transcript, setTranscript }}
    >
      {children}
    </VideoContext.Provider>
  );
};

export const useVideo = () => {
  const context = useContext(VideoContext);
  if (!context) {
    throw new Error("useVideo must be used within a VideoProvider");
  }
  return context;
};
