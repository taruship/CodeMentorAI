import { useState } from "react";
import { FaPaperPlane } from "react-icons/fa";

function InputBox({ askAI }) {
  const [prompt, setPrompt] = useState("");

  const send = () => {
    if (!prompt.trim()) return;

    askAI(prompt);
    setPrompt("");
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      send();
    }
  };

  return (
    <div
      style={{
        maxWidth: "900px",
        margin: "0 auto",
        position: "relative",
      }}
    >
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder="Ask anything about programming..."
        style={{
          width: "100%",
          height: "80px",
          borderRadius: "18px",
          border: "1px solid #334155",
          background: "#1e293b",
          color: "white",
          padding: "18px 70px 18px 18px",
          resize: "none",
          fontSize: "16px",
          outline: "none",
        }}
      />

      <button
        onClick={send}
        style={{
          position: "absolute",
          right: "18px",
          bottom: "18px",
          width: "44px",
          height: "44px",
          borderRadius: "50%",
          border: "none",
          background: "#2563eb",
          color: "white",
          cursor: "pointer",
        }}
      >
        <FaPaperPlane />
      </button>
    </div>
  );
}

export default InputBox;