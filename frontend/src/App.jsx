import "./App.css";
import { useState } from "react";
import axios from "axios";

import Sidebar from "./components/Sidebar";
import ChatWindow from "./components/ChatWindow";
import InputBox from "./components/InputBox";

function App() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const askAI = async (question) => {
    setLoading(true);

    try {
      const res = await axios.get("http://127.0.0.1:8000/ask", {
        params: {
          prompt: question,
        },
      });

      setMessages((prev) => [
        ...prev,
        {
          question,
          answer: res.data.response,
        },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          question,
          answer: "❌ Unable to connect to backend.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const clearChat = () => {
    setMessages([]);
  };

  return (
  <div className="app">
    <header className="header">
      🤖 CodeMentor AI
    </header>

    <div className="main">

      <aside className="sidebar">
        <Sidebar
          messages={messages}
          setMessages={setMessages}
        />
      </aside>

      <div className="chat">

        <ChatWindow
          messages={messages}
          loading={loading}
        />

        <div className="input-area">
          <InputBox askAI={askAI} />
        </div>

      </div>

    </div>
  </div>
);
}

export default App;