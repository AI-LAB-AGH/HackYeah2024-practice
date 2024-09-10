import { ReactNode, useEffect, useRef, useState } from "react";
import ".././assets/cards.css";

interface Props {
  title: string;

  children?: string;
  media?: ReactNode;
  subtitle?: string;
  isFading?: boolean;
  isGradual?: boolean;
  isSmall?: boolean;
  className?: string;
}

const Card = ({
  title,
  children,
  media,
  subtitle,
  isFading,
  isGradual,
  isSmall,
  className,
}: Props) => {
  const contentAsArray = children ? children.split(" ") : [];
  const [index, setIndex] = useState(0);
  const [isHidden, setIsHidden] = useState(false);
  const divRef = useRef<HTMLDivElement>(null);

  const checkPosition = () => {
    if (divRef.current) {
      const rect = divRef.current.getBoundingClientRect();
      const halfHeight = (rect.bottom - rect.top) / 2;

      if (
        rect.top < window.innerHeight - halfHeight &&
        rect.bottom > halfHeight
      ) {
        setIsHidden(false);
      } else {
        setIsHidden(true);
      }
    }
  };

  useEffect(() => {
    const timer = setTimeout(() => {
      if (index <= contentAsArray.length)
        setIndex((curr) => (isGradual ? curr + 1 : contentAsArray.length));
    }, 200);

    return () => clearTimeout(timer);
  });

  useEffect(() => {
    window.addEventListener("scroll", checkPosition);
    window.addEventListener("resize", checkPosition);

    checkPosition();

    return () => {
      window.removeEventListener("scroll", checkPosition);
      window.removeEventListener("resize", checkPosition);
    };
  });

  return (
    <div
      ref={divRef}
      className={
        "card-wrapper " + className + (isHidden && isFading ? " fade" : "")
      }
    >
      <div className={"card-title" + (isSmall ? " small" : "")}>{title}</div>
      <div className="card-subtitle">{subtitle}</div>
      <div className={"card-content" + (isSmall ? " small" : "")}>
        {contentAsArray.map((token, key) => (
          <div className={"token" + (key < index ? " visible" : "")}>
            {token}&nbsp;
          </div>
        ))}
        {media}
      </div>
    </div>
  );
};

export default Card;
