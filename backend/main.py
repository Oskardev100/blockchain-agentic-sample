from fastapi import FastAPI
from dotenv import load_dotenv
from ai_agent.agent import ask_ai, get_eth_price
from ai_agent.interact_with_contract import deposit_eth
import os

load_dotenv()
app = FastAPI()

@app.get("/")
def root():
    return {"status": "AI + Smart Contract API is running 🚀"}

@app.get("/eth_price")
def fetch_eth_price():
    price = get_eth_price()
    return {"price": price}

@app.get("/insight")
def ai_insight():
    price = get_eth_price()
    prompt = f"Ethereum is currently trading at ${price}. Give me a short-term market insight."
    response = ask_ai(prompt)
    return {"price": price, "ai_response": response}

@app.post("/deposit")
def deposit():
    tx_hash = deposit_eth(1)
    return {"message": "Deposited 1 ETH", "transaction": tx_hash}
