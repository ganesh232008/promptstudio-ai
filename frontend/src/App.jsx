import { useState, useRef, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [idea, setIdea] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [sessionId, setSessionId] = useState(null);

  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

  const generatePrompt = async () => {
    if (!idea.trim()) return;

    const userMessage = {
      role: "user",
      text: idea,
    };

    setMessages((prev) => [...prev, userMessage]);

    const currentMessage = idea;
    setIdea("");

    setLoading(true);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          session_id: sessionId,
          message: currentMessage,
        }
      );

      if (!sessionId) {
        setSessionId(response.data.session_id);
      }

      const aiMessage = {
        role: "assistant",
        text: response.data.reply,
      };

      setMessages((prev) => [...prev, aiMessage]);

    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "❌ Unable to connect to backend.",
        },
      ]);
    }

    setLoading(false);
  };

  const newChat = () => {
    setMessages([]);
    setIdea("");
    setSessionId(null);
  };

  return (
    <div className="container">

      <div className="card">

        <h1>🚀 PromptForge AI</h1>

        <p className="subtitle">
          Multi-Agent Prompt Engineering Assistant
        </p>

        <textarea
          placeholder="Describe your idea..."
          value={idea}
          onChange={(e) => setIdea(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              e.preventDefault();
              generatePrompt();
            }
          }}
        />

        <button
          onClick={generatePrompt}
          disabled={loading}
        >
          {loading ? "Thinking..." : "Send"}
        </button>

        <button
          onClick={newChat}
          style={{
            marginTop: "10px",
            background: "#ef4444",
          }}
        >
          New Chat
        </button>

        <h2>Conversation</h2>

        <div className="output">

          {messages.length === 0 && (
            <p style={{ color: "#94a3b8" }}>
              Start chatting with PromptForge AI...
            </p>
          )}

          {messages.map((msg, index) => (

            <div
              key={index}
              className={
                msg.role === "user"
                  ? "userMessage"
                  : "aiMessage"
              }
            >

              <strong>
                {msg.role === "user"
                  ? "👤 You"
                  : "🤖 PromptForge AI"}
              </strong>

              <p>{msg.text}</p>

            </div>

          ))}

          {loading && (
            <div className="aiMessage">
              <strong>🤖 PromptForge AI</strong>
              <p>Thinking...</p>
            </div>
          )}

          <div ref={bottomRef}></div>

        </div>

      </div>

    </div>
  );
}

export default App;