import { Chart, ChartData } from "chart.js/auto";
import { useRef, useEffect } from "react";

interface Props {
  chartData: number[];
}

const DonutChart = ({ chartData }: Props) => {
  const chartRef = useRef<Chart | null>(null);
  const formatData = (data: number[]): ChartData => ({
    labels: [
      data[0] * 100 + "% PRAWIDŁOWY",
      data[1] * 100 + "% NIEPEWNY",
      data[2] * 100 + "% NIEREGULARNY",
    ],
    datasets: [{ data }],
  });

  const canvasCallback = (canvas: HTMLCanvasElement | null) => {
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (ctx) {
      if (chartRef.current) chartRef.current.destroy();
      chartRef.current = new Chart(ctx, {
        type: "doughnut",
        data: formatData(chartData),
        options: {
          responsive: true,
          maintainAspectRatio: false,
          // backgroundColor: "#00dd67",

          plugins: {
            legend: {
              position: "right",
              labels: {
                color: "#fff",
                boxWidth: 20,
                padding: 15,
                font: {
                  size: 12,
                  style: "italic",
                  weight: "lighter",
                  family:
                    "'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif",
                },
                usePointStyle: true,
                pointStyle: "rectRounded",
              },
            },
          },
          elements: {
            arc: {
              borderWidth: 1,
              hoverBorderWidth: 3,
            },
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

  return <canvas ref={canvasCallback}></canvas>;
};

export default DonutChart;
