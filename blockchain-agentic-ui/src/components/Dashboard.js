import React, { useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Tooltip } from 'chart.js';
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Tooltip);


const API_BASE = "http://localhost:8000"; // FastAPI backend

function Dashboard() {
  const [price, setPrice] = useState(null);
  const [insight, setInsight] = useState("");
  const [txHash, setTxHash] = useState("");
  const [transactions, setTransactions] = useState([]);
  const [predictions, setPredictions] = useState([]);

  const getPrice = async () => {
    const res = await axios.get(`${API_BASE}/eth_price`);
    setPrice(res.data.price);
  };

  const getInsight = async () => {
    const res = await axios.get(`${API_BASE}/insight`);
    setInsight(res.data.ai_response);
  };

  const deposit = async () => {
    const res = await axios.post(`${API_BASE}/deposit`);
    setTxHash(res.data.transaction);
  };

  const fetchTransactions = async () => {
    const res = await axios.get(`${API_BASE}/transactions`);
    setTransactions(res.data.transactions);
  };
  
  const fetchPrediction = async () => {
    const res = await axios.get(`${API_BASE}/predictions`);
    setPredictions((prev) => [...prev, res.data]);
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <h2>🧠 AI + Smart Contract Dashboard</h2>

      <div>
        <button onClick={getPrice}>🔍 Get ETH Price</button>
        {price && <p>ETH Price: ${price}</p>}
      </div>

      <div>
        <button onClick={getInsight}>🤖 Get AI Insight</button>
        {insight && <p><strong>AI Insight:</strong> {insight}</p>}
      </div>

      <div>
        <button onClick={deposit}>💸 Deposit 1 ETH</button>
        {txHash && <p>Transaction Hash: {txHash}</p>}
      </div>

      <div>
        <button onClick={fetchTransactions}>📜 Get Transaction History</button>
        <ul>
            {transactions.map((tx, index) => (
                <li key={index}>{tx}</li>
            ))}
        </ul>
      </div>

      <div>
        <button onClick={fetchPrediction}>📈 Get Prediction & Update Chart</button>
        {predictions.length > 0 && (
            <Line
            data={{
                labels: predictions.map((p, i) => `#${i + 1}`),
                datasets: [
                {
                    label: 'ETH Price',
                    data: predictions.map(p => p.price),
                    borderColor: 'blue',
                    tension: 0.2
                }
                ]
            }}
            />
        )}
      </div>

    </div>
  );
}

export default Dashboard;
