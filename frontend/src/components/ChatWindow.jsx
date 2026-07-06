import { useEffect, useRef } from "react";
import MessageBubble from "./MessageBubble";

function ChatWindow({ messages, loading }) {
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  return (
    <div
      style={{
        flex: 1,
        overflowY: "auto",
        padding: "35px",
        background: "#0f172a",
        display: "flex",
        flexDirection: "column",
      }}
    >
      <div
        style={{
          width: "100%",
          maxWidth: "900px",
          margin: "0 auto",
        }}
      >
        {/* Welcome Screen */}

        {messages.length === 0 && !loading && (
          <div
            style={{
              textAlign: "center",
              marginTop: "120px",
            }}
          >
            <h1
              style={{
                fontSize: "56px",
                marginBottom: "15px",
              }}
            >
              🤖 CodeMentor AI
            </h1>

            <p
              style={{
                color: "#94a3b8",
                fontSize: "22px",
              }}
            >
              Ask any programming question to get started.
            </p>
          </div>
        )}

        {/* Messages */}

        {messages.map((msg, index) => (
          <div key={index}>
            <MessageBubble
              sender="user"
              message={msg.question}
            />

            <MessageBubble
              sender="ai"
              message={msg.answer}
            />
          </div>
        ))}

        {/* Loading */}

        {loading && (
          <div
            style={{
              marginTop: "30px",
              padding: "18px",
              background: "#1e293b",
              borderRadius: "14px",
              color: "#60a5fa",
              fontWeight: "bold",
              width: "fit-content",
            }}
          >
            🤖 Thinking...
          </div>
        )}

        {/* Auto Scroll Target */}

        <div ref={bottomRef}></div>
      </div>
    </div>
  );
}

export default ChatWindow;