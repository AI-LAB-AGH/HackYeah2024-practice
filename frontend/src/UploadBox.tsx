// import React, { useState } from 'react';

// interface UploadBoxProps {
//   onFileSelect: (file: File | null) => void; // Funkcja do przekazywania pliku do rodzica
// }

// const UploadBox: React.FC<UploadBoxProps> = ({ onFileSelect }) => {
//   const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
//     const selectedFile = event.target.files?.[0];
//     if (selectedFile) {
//       console.log("Selected file:", selectedFile);
//       onFileSelect(selectedFile); // Przekazanie pliku do rodzica
//     }
//   };

//   return (
//     <div className="box white">
//       <input 
//         type="file" 
//         accept="video/mp4" // Akceptacja tylko plików MP4
//         onChange={handleFileChange} 
//         style={{ marginBottom: '10px' }} 
//       />
//       <button onClick={() => alert('File upload functionality not implemented yet.')}>
//         Upload File
//       </button>
//     </div>
//   );
// };

// export default UploadBox;
