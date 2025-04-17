import { useState } from "react";
import "./App.css";

function App() {
  const [activeTab, setActiveTab] = useState("world");
  const [inputs, setInputs] = useState({ world: "", pokemon: "", sakila: "" });
  const [responses, setResponses] = useState({
    world: { code: "", output: "" },
    pokemon: { code: "", output: "" },
    sakila: { code: "", output: "" },
  });

  const handleInputChange = (e) => {
    setInputs({ ...inputs, [activeTab]: e.target.value });
  };

  const handleSend = async (actionType) => {
    const mockCode = `-- [${actionType.toUpperCase()}]\nSELECT * FROM ${activeTab}_table WHERE column = 'value';`;

    const res = await fetch("http://127.0.0.1:5001/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        description: inputs[activeTab],
        category: activeTab,
        action: actionType, // will be "explore", "query", or "modify"
      }),
    });

    const data = await res.json();
    setResponses({
      ...responses,
      [activeTab]: {
        code: mockCode,
        output: data.response,
      },
    });
  };

  const tabNames = ["world", "pokemon", "sakila"];

  return (
    <div className="app-container">
      <h1>ChatDB 58</h1>
      <h2>Team Members: Evan Hu, Emily Truong, & Aditya Venkataramani</h2>

      <div className="tab-buttons">
        {tabNames.map((tab) => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab)}
            className={activeTab === tab ? "active" : ""}
          >
            {tab.toUpperCase()}
          </button>
        ))}
      </div>

      <div className="chat-area">
        <h2>{activeTab.toUpperCase()} Chat</h2>
        <input
          type="text"
          value={inputs[activeTab]}
          onChange={handleInputChange}
          placeholder={`Ask something about ${activeTab}...`}
        />

        <div className="action-buttons">
          <button onClick={() => handleSend("explore")}>
            Schema Exploration
          </button>
          <button onClick={() => handleSend("query")}>Query Execution</button>
          <button onClick={() => handleSend("modify")}>
            Data Modification
          </button>
        </div>

        {responses[activeTab].code && (
          <div className="response-section">
            <h4>Generated Code:</h4>
            <p className="response code-box">{responses[activeTab].code}</p>
            <h4>Output:</h4>
            <p className="response code-box">{responses[activeTab].output}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
