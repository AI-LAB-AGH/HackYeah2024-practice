export const generateScatterData = () => {
  return Array.from({ length: 50 }, (_, i) => ({
    x: i * 0.1,
    y: Math.random(),
  }));
};
