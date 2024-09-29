import React, { useState } from 'react';
import './App.css'; // Importuj swój plik CSS

const App: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [rightText, setRightText] = useState<string>("Hello World"); // Stan dla tekstu w prawym prostokącie

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = event.target.files?.[0];
    if (selectedFile) {
      setFile(selectedFile);
      console.log("Selected file:", selectedFile);
      setRightText("nic"); // Zmiana tekstu na "nic" po wybraniu pliku
    }
  };

  const handleUpload = () => {
    if (file) {
      // Tutaj możesz dodać logikę do przesyłania pliku
      console.log("Uploading file:", file);
    } else {
      alert("Please select a file first!");
    }
  };

  return (
    <div className="container">
      <div className="box white">
        <input 
          type="file" 
          onChange={handleFileChange} 
          style={{ marginBottom: '10px' }} 
        />
        <button onClick={handleUpload}>Upload File</button>
      </div>
      <div className="box gray">
        <h1>{rightText}</h1> {/* Wyświetlanie tekstu z stanu rightText */}
      </div>
    </div>
  );
};

export default App;
