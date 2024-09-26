import { Chart, ChartData } from "chart.js/auto";
import { useRef, useEffect } from "react";
import { generateScatterData } from "../assets/data";

const LineChart = () => {
  const chartRef = useRef<Chart | null>(null);
  const chartData = generateScatterData();
  const formatData = (data: { x: number; y: number }[]): ChartData => ({
    datasets: [{ data }],
  });

  const canvasCallback = (canvas: HTMLCanvasElement | null) => {
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (ctx) {
      if (chartRef.current) chartRef.current.destroy();
      chartRef.current = new Chart(ctx, {
        type: "line",
        data: formatData(chartData),
        options: {
          responsive: true,
          maintainAspectRatio: false,
          animation: false,
          borderColor: "#fff",

          scales: {
            x: {
              type: "linear",
              position: "bottom",
              title: {
                display: true,
                text: "Czas [s]",
                color: "#fff",
                font: {
                  family:
                    "'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif",
                  weight: "bold",
                },
              },
            },
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: "Wiarygodność",
                color: "#fff",
                font: {
                  family:
                    "'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif",
                  weight: "bold",
                },
              },
            },
          },

          plugins: {
            legend: { display: false },
          },
        },
      });
    }
  };

  useEffect(() => {
    if (chartRef.current) {
      chartRef.current.data = formatData(chartData);
      chartRef.current.update();
    }
  }, [chartData]);

  return (
    <div style={{ height: "30vh", margin: "5px" }}>
      <canvas ref={canvasCallback}></canvas>
    </div>
  );
};

export default LineChart;
