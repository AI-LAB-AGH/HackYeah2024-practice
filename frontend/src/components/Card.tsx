import { ReactNode, useEffect, useState } from "react";
import { useVideo } from "./VideoContext";
import ".././assets/clean/card.css";

interface Props {
  title: string;

  media?: ReactNode;
  subtitle?: string;
  isGradual?: boolean;
  isSmall?: boolean;
  className?: string;
}

const Card = ({ title, media, subtitle, isGradual, className }: Props) => {
  const [index, setIndex] = useState(0);
  const { videoUrl, transcript } = useVideo();
  const contentAsArray = transcript ? transcript.split(" ") : [];

  useEffect(() => {
    const timer = setTimeout(() => {
      if (index <= contentAsArray.length)
        setIndex((curr) => (isGradual ? curr + 1 : contentAsArray.length));
    }, 200);

    return () => clearTimeout(timer);
  });

  return (
    <div className={"card-wrapper " + className + (videoUrl ? "" : " hide")}>
      <div className="card-title">{title}</div>
      <div className="card-subtitle">{subtitle}</div>
      <div className="card-content">
        {media
          ? media
          : contentAsArray.map((token, key) => (
              <div className={"token" + (key < index ? " visible" : "")}>
                {token}&nbsp;
              </div>
            ))}
      </div>
    </div>
  );
};

export default Card;
