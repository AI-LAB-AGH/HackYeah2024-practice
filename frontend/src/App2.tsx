import Card from "./components/Card";
import DonutChart from "./components/DonutChart";
import VideoPlayer from "./components/VideoPlayer";
import { VideoProvider } from "./components/VideoContext";
import "./assets/clean/content.css";

function App() {
  return (
    <>
      <div className="wrapper">
        <div className="content">
          <VideoProvider>
            <div className="content-element player">
              <VideoPlayer></VideoPlayer>
            </div>

            <div className="content-element info">
              <Card title="TRANSKRYPT" isGradual={true}></Card>

              <Card
                title="PODSUMOWANIE"
                media={<DonutChart chartData={[0.8, 0.15, 0.05]}></DonutChart>}
              ></Card>
            </div>
          </VideoProvider>
        </div>
      </div>
    </>
  );
}

export default App;
