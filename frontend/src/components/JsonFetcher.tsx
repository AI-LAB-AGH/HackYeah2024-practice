import React, { useEffect, useState } from "react";

const JsonDataViewer: React.FC = () => {
  const [jsonData, setJsonData] = useState<any[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("/api/get-json-data/");
        const data = await response.json();
        setJsonData(data);
      } catch (error) {
        console.error("Error fetching JSON data:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>JSON Data Viewer</h1>
      <pre>{JSON.stringify(jsonData, null, 2)}</pre>
    </div>
  );
};

export default JsonDataViewer;
