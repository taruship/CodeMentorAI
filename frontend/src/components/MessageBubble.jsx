import "./MessageBubble.css";

import { useState } from "react";
import ReactMarkdown from "react-markdown";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";
import { FaUser, FaRobot, FaCopy, FaCheck } from "react-icons/fa";

function MessageBubble({ sender, message }) {
  const isUser = sender === "user";
  const [copied, setCopied] = useState(false);

  const copyMessage = async () => {
    try {
      await navigator.clipboard.writeText(message);
      setCopied(true);

      setTimeout(() => {
        setCopied(false);
      }, 2000);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className={`message-row ${sender}`}>
      <div className="message-content">

        {!isUser && (
          <FaRobot
            className="message-avatar"
            size={24}
            color="#60a5fa"
          />
        )}

        <div className="message-box">

          {!isUser && (
            <button
              onClick={copyMessage}
              className="copy-btn"
            >
              {copied ? <FaCheck /> : <FaCopy />}
            </button>
          )}

          <ReactMarkdown
            components={{
              code({ inline, className, children }) {
                const match = /language-(\w+)/.exec(className || "");

                return !inline && match ? (
                  <SyntaxHighlighter
                    language={match[1]}
                    style={oneDark}
                    PreTag="div"
                    customStyle={{
                      borderRadius: "12px",
                      marginTop: "15px",
                    }}
                  >
                    {String(children).replace(/\n$/, "")}
                  </SyntaxHighlighter>
                ) : (
                  <code>{children}</code>
                );
              },
            }}
          >
            {message}
          </ReactMarkdown>
        </div>

        {isUser && (
          <FaUser
            className="message-avatar"
            size={24}
            color="#22c55e"
          />
        )}

      </div>
    </div>
  );
}

export default MessageBubble;