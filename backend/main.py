from fastapi import FastAPI
from dotenv import load_dotenv
from ai_agent.agent import ask_ai, get_eth_price
from ai_agent.interact_with_contract import deposit_eth

import os
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()
app = FastAPI()

@app.get("/")
def root():
    return {"status": "AI + Smart Contract API is running 🚀"}

@app.get("/eth_price")
def fetch_eth_price():
    try:
        price = get_eth_price()
        logger.info(f"ETH price: {price}")
        return {"price": price}
    except Exception as e:
        logger.error(f"Error fetching ETH price: {e}")
        return {"error": "Error fetching ETH price"}

@app.get("/insight")
def ai_insight():
    try:
        price = get_eth_price()
        prompt = f"Ethereum is currently trading at ${price}. Give me a short-term market insight."
        response = ask_ai(prompt)
        logger.info(f"AI response: {response}")
        return {"price": price, "ai_response": response}
    except Exception as e:
        logger.error(f"Error getting AI insight: {e}")
        return {"error": "Error getting AI insight"}

@app.post("/deposit")
def deposit():
    try:
        tx_hash = deposit_eth(1)
        logger.info(f"Deposited 1 ETH: {tx_hash}")
        return {"message": "Deposited 1 ETH", "transaction": tx_hash}
    except Exception as e:
        logger.error(f"Error depositing ETH: {e}")
