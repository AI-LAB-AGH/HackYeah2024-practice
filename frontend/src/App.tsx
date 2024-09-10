import { useState } from "react";
import Card from "./components/Card";
import DonutChart from "./components/DonutChart";
import ScatterChart from "./components/LineChart";
import ReactPlayer from "react-player";
import { transcript } from "./assets/cards";
import "./assets/sections.css";
import "./assets/accessories.css";

function App() {
  // const [count, setCount] = useState(0);
  const [view, setView] = useState(0);
  function handleViewSwitch() {
    view ? setView(0) : setView(1);
  }

  return (
    <>
      <div className="section-wrapper">
        <div className={"section mid" + (view ? " squeeze" : "")}>
          <div className="subsection-title">OTO TWÓJ FILM...</div>
          <div className="subsection-content">
            <div className="videoplayer">
              <ReactPlayer
                width={"45vw"}
                height={"60vh"}
                style={{ margin: "auto" }}
                url="https://www.youtube.com/watch?v=wJWksPWDKOc"
                controls={true}
                playing={false}
              ></ReactPlayer>
            </div>
          </div>
        </div>

        <div className="switch">
          <button className="switch-button" onClick={handleViewSwitch}>
            O
          </button>
        </div>

        <div className={"section side" + (view ? " stretch" : "")}>
          <div className="flex flex-col">
            <div className="subsection-title text-center">ANALIZA</div>
            <div className="flex flex-row my-auto">
              <div>
                <Card
                  className="s dir-tr filled dir-tl"
                  title="WIARYGODNOŚĆ"
                  isSmall={!view}
                  media={<ScatterChart />}
                ></Card>

                <Card
                  className="s dir-b"
                  title={transcript.title}
                  subtitle={transcript.subtitle}
                  isGradual={transcript.gradual}
                  isSmall={!view}
                >
                  {transcript.content}
                </Card>
              </div>

              <div
                className={
                  "subsection-content my-auto" + (view ? "" : " squeeze")
                }
              >
                <Card
                  className="l dir-br"
                  title="WYKRYTY TEKST JEST..."
                  media={
                    <DonutChart chartData={[0.8, 0.15, 0.05]}></DonutChart>
                  }
                ></Card>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
