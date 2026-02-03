import React, { useState } from "react";
import axios from "axios";

const API_BASE = "http://127.0.0.1:4000";


const DocumentSelector = ({ setUploaded }) => {
  const [files, setFiles] = useState([]);
  const [uploadStatus, setUploadStatus] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFiles(Array.from(e.target.files));
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setFiles(Array.from(e.dataTransfer.files));
  };

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  const uploadFiles = async () => {
    if (files.length === 0) {
      alert("Please select files first");
      return;
    }

    const formData = new FormData();
    files.forEach((file) => formData.append("files", file));

    try {
      setLoading(true);
      setUploadStatus("Uploading...");

      await axios.post(`${API_BASE}/upload`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      setUploadStatus("✅ Files uploaded!");
      setUploaded(true);
    } catch (err) {
      console.error(err);
      setUploadStatus("❌ Upload failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{margin:"19px", border: "1px solid #ddd", padding: "20px", borderRadius: "6px" }}>
      <h3 style={{margin:"9px"}}>Upload Documents</h3>

      {/* Drag & Drop Area */}
      <div
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        style={{
          border: "2px dashed #aaa",
          padding: "20px",
          marginBottom: "10px",
          textAlign: "center",
        }}
      >
        Drag & Drop files here
      </div>

      <input type="file" multiple onChange={handleFileChange} />

      {/* Show selected files */}
      {files.length > 0 && (
        <ul style={{ marginTop: "10px" }}>
          {files.map((file, idx) => (
            <li key={idx}>{file.name}</li>
          ))}
        </ul>
      )}

      <button
        onClick={uploadFiles}
        disabled={loading}
        style={{ marginTop: "10px", padding: "8px 15px" }}
      >
        {loading ? "Processing..." : "Upload & Process"}
      </button>

      <p style={{ marginTop: "10px" }}>{uploadStatus}</p>
    </div>
  );
};

export default DocumentSelector;
