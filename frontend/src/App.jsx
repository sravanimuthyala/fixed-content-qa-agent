import React, { useState } from "react";
import DocumentSelector from "./DocumentSelector";
import axios from "axios";

const API_BASE = "http://127.0.0.1:4000";

function App() {
  const [uploaded, setUploaded] = useState(false);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!uploaded) {
      alert("Please upload documents first");
      return;
    }

    // ✅ Prevent empty questions
    if (!question.trim()) return;

    setLoading(true);
    try {
      const res = await axios.post(`${API_BASE}/ask`, { question });
      setAnswer(res.data.answer);

      // ✅ Clear input after asking
      setQuestion("");
    } catch (err) {
      console.error(err);
      setAnswer("Error fetching answer.");
    }
    setLoading(false);
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "#f5f7fa",
        fontFamily: "sans-serif",
      }}
    >
      <div
        style={{
          width: "800px",
          padding: "40px",
          backgroundColor: "#ffffff",
          borderRadius: "12px",
          boxShadow: "0 10px 25px rgba(0,0,0,0.1)",
        }}
      >
        <h1 style={{ textAlign: "center" }}>Fixed Content Q&A Agent</h1>

        {/* Upload component */}
        <DocumentSelector setUploaded={setUploaded} />

        {/* Ask section */}
        <div style={{ marginTop: "40px", display: "flex", gap: "10px" }}>
          <input
            style={{
              flex: 1,
              padding: "12px",
              borderRadius: "6px",
              border: "1px solid #ccc",
            }}
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask a question from uploaded docs..."
          />
          <button
            onClick={handleAsk}
            disabled={loading}
            style={{
              padding: "12px 20px",
              borderRadius: "6px",
              border: "none",
              backgroundColor: "#4a90e2",
              color: "white",
              cursor: "pointer",
            }}
          >
            {loading ? "Thinking..." : "Ask"}
          </button>
        </div>

        {answer && (
          <div
            style={{
              marginTop: "30px",
              padding: "20px",
              backgroundColor: "#f4f6f8",
              borderRadius: "8px",
            }}
          >
            <strong>Answer:</strong>
            <p style={{ color: "black", marginTop: "10px" }}>{answer}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
