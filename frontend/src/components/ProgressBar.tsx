import React, { useState } from "react";
import "../assets/clean/player.css";

interface Segment {
  percentage: number;
  color: string;
  content: string; // The content to display on hover
}

interface ProgressBarProps {
  segments: Segment[];
}

const ProgressBar: React.FC<ProgressBarProps> = ({ segments }) => {
  const [hoveredContent, setHoveredContent] = useState<string | null>(null);

  const handleMouseEnter = (content: string) => {
    setHoveredContent(content);
  };

  const handleMouseLeave = () => {
    setHoveredContent(null);
  };

  return (
    <div className="progress-bar-container">
      <div className="progress-bar">
        {segments.map((segment, index) => (
          <div
            key={index}
            className="progress-segment"
            style={{
              width: `${segment.percentage}%`,
              backgroundColor: segment.color,
            }}
            onMouseEnter={() => handleMouseEnter(segment.content)} // Handle hover to show content
            onMouseLeave={handleMouseLeave}
          />
        ))}
      </div>

      {/* Display hovered content */}
      {hoveredContent && (
        <div className="hovered-content">{hoveredContent}</div>
      )}
    </div>
  );
};

export default ProgressBar;
