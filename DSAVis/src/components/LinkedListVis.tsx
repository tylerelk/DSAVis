import React, { ReactHTMLElement, useState } from "react";

const LinkedListVis: React.FC = () => {
  const [inputValue, setInputValue] = useState("");
  const [values, setValues] = useState<number[]>([]);
  const [linkedList, setLinkedList] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string>("");

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(e.target.value);
  };

  const handleAddNode = () => {
    const num = parseInt(inputValue, 10);
    if (!isNaN(num)) {
      setValues([...values, num]);
      setInputValue("");
    } else {
      setError("Please enter a valid number");
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    if (values.length < 1) {
      setError("Add a node to the list");
      setLoading(false);
      return;
    }

    try {
      const response = await fetch(
        import.meta.env.VITE_FLASK_LOCALHOST + "/linkedlist",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ values }),
        }
      );
      if (!response.ok) {
        throw new Error("Failed to create linked list");
      }
      const linkedListResponse = await response.json();
      setLinkedList(linkedListResponse);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const renderLinkedList = () => {
    if (linkedList.length < 1) {
      return <h3>No nodes to display</h3>;
    }
    return (
      <ul>
        {linkedList.map((node, index) => (
          <li key={index}>
            {node.value}
            {node.next ? "  -->  " : ""}
          </li>
        ))}
      </ul>
    );
  };

  return (
    <div>
      <h1>Linked List Visualizer</h1>

      <div>
        <input
          type='text'
          value={inputValue}
          onChange={handleInputChange}
          placeholder='Enter a number'
        />
        <button onClick={handleAddNode}>Add Node</button>
      </div>

      <div>
        <h3>Current List of Values</h3>
        <p>{values.join(", ")}</p>
      </div>

      <div>
        <button onClick={handleSubmit} disabled={loading}>
          {loading ? "Creating Linked List..." : "Create Linked List"}
        </button>
      </div>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <div>
        <h2>Linked List Visualization</h2>
        {renderLinkedList()}
      </div>
    </div>
  );
};

export default LinkedListVis;
