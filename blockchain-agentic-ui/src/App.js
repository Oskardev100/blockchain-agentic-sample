// filepath: blockchain-agentic-ui/src/App.js
import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [ethPrice, setEthPrice] = useState(null);
  const [insight, setInsight] = useState(null);
  const [depositMessage, setDepositMessage] = useState(null);
  const [error, setError] = useState(null);

  const fetchEthPrice = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/eth_price');
      setEthPrice(response.data.price);
      setError(null);
    } catch (error) {
      console.error('Error fetching ETH price:', error);
      setError('Error fetching ETH price');
    }
  };

  const fetchInsight = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/insight');
      setInsight(response.data.ai_response);
      setError(null);
    } catch (error) {
      console.error('Error fetching AI insight:', error);
      setError('Error fetching AI insight');
    }
  };

  const depositEth = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/deposit');
      setDepositMessage(response.data.message);
      setError(null);
    } catch (error) {
      console.error('Error depositing ETH:', error);
      setError('Error depositing ETH');
    }
  };

  return (
    <div className="App">
      <h1>Blockchain Agentic UI</h1>
      <button onClick={fetchEthPrice}>Get ETH Price</button>
      {ethPrice && <p>ETH Price: ${ethPrice}</p>}
      
      <button onClick={fetchInsight}>Get AI Insight</button>
      {insight && <p>AI Insight: {insight}</p>}
      
      <button onClick={depositEth}>Deposit 1 ETH</button>
      {depositMessage && <p>{depositMessage}</p>}
      
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}

export default App;