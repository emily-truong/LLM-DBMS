import { useState } from "react";
import "./App.css";

function App() {
  const [activeTab, setActiveTab] = useState("world");
  const [dbType, setDbType] = useState("sql");
  const [inputs, setInputs] = useState({
    world: "",
    pokemon: "",
    sakila: "",
  });

  const [responses, setResponses] = useState({
    world: {
      sql: { query: "", output: "", result: [] },
      nosql: { query: "", output: "", result: [] },
    },
    pokemon: {
      sql: { query: "", output: "", result: [] },
      nosql: { query: "", output: "", result: [] },
    },
    sakila: {
      sql: { query: "", output: "", result: [] },
      nosql: { query: "", output: "", result: [] },
    },
  });

  const handleInputChange = (e) => {
    setInputs({ ...inputs, [activeTab]: e.target.value });
  };

  const handleSend = async (actionType) => {
    const endpoint = `${activeTab}/${actionType}`;
    const payload = {
      prompt: inputs[activeTab],
      dbType: dbType,
    };

    try {
      const res = await fetch(`http://127.0.0.1:5001/${endpoint}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const data = await res.json();
      const query = data.query ?? "-- query not returned --";
      const output = JSON.stringify(
        data.result ?? data.response ?? data.error ?? "No response",
        null,
        2
      );

      setResponses((prev) => ({
        ...prev,
        [activeTab]: {
          ...prev[activeTab],
          [dbType]: {
            query,
            output,
            result: Array.isArray(data.result)
              ? data.result
              : data.result || [],
          },
        },
      }));
    } catch (error) {
      console.error("Request failed:", error);
    }
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
        <div className="subtab-buttons">
          <button
            onClick={() => setDbType("sql")}
            className={dbType === "sql" ? "active-subtab" : ""}
          >
            SQL
          </button>
          <button
            onClick={() => setDbType("nosql")}
            className={dbType === "nosql" ? "active-subtab" : ""}
          >
            NoSQL
          </button>
        </div>

        <input
          type="text"
          value={inputs[activeTab]}
          onChange={handleInputChange}
          placeholder={`Ask something about ${activeTab} (${dbType})...`}
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

        {responses[activeTab][dbType].query && (
          <div className="response-section">
            <h4>Generated Query:</h4>
            <pre className="response code-box">
              {responses[activeTab][dbType].query}
            </pre>

            <h4>Output:</h4>
            <pre className="response code-box">
              {responses[activeTab][dbType].output}
            </pre>

            {typeof responses[activeTab][dbType].result === "string" && (
              <div className="response-summary">
                <h4>Summary:</h4>
                <p>{responses[activeTab][dbType].result}</p>
              </div>
            )}

            {Array.isArray(responses[activeTab][dbType].result) &&
              responses[activeTab][dbType].result.length > 0 && (
                <div className="table-container">
                  <h4>Table View:</h4>
                  <table>
                    <thead>
                      <tr>
                        {typeof responses[activeTab][dbType].result[0] ===
                          "object" &&
                        !Array.isArray(
                          responses[activeTab][dbType].result[0]
                        ) ? (
                          Object.keys(
                            responses[activeTab][dbType].result[0]
                          ).map((col) => <th key={col}>{col}</th>)
                        ) : (
                          <th>Value</th>
                        )}
                      </tr>
                    </thead>
                    <tbody>
                      {responses[activeTab][dbType].result.map((row, idx) => (
                        <tr key={idx}>
                          {typeof row === "object" && !Array.isArray(row) ? (
                            Object.values(row).map((val, i) => (
                              <td key={i}>{val === null ? "NULL" : val}</td>
                            ))
                          ) : (
                            <td>{row}</td>
                          )}
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
