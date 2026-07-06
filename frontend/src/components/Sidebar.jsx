function Sidebar({ messages, setMessages }) {
  return (
    <div
      style={{
        height: "100%",
        display: "flex",
        flexDirection: "column",
        padding: "20px",
      }}
    >
      <button
        style={{
          padding: "14px",
          borderRadius: "12px",
          border: "none",
          background: "#2563eb",
          color: "white",
          fontSize: "16px",
          cursor: "pointer",
          marginBottom: "25px",
        }}
        onClick={() => setMessages([])}
      >
        + New Chat
      </button>

      <h3
        style={{
          marginBottom: "15px",
          color: "#cbd5e1",
        }}
      >
        Previous Chats
      </h3>

      <div
        style={{
          overflowY: "auto",
          flex: 1,
        }}
      >
        {messages.map((msg, index) => (
          <div
            key={index}
            style={{
              padding: "12px",
              marginBottom: "10px",
              background: "#1e293b",
              borderRadius: "10px",
              cursor: "pointer",
              color: "#e2e8f0",
            }}
          >
            {msg.question.slice(0, 35)}...
          </div>
        ))}
      </div>
    </div>
  );
}

export default Sidebar;