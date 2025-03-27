from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from ai_agent.agent import ask_ai, get_eth_price
from ai_agent.interact_with_contract import deposit_eth
from backend.database import SessionLocal, init_db, Transaction, Prediction
from sqlalchemy.orm import Session

import os
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()
app = FastAPI()

# Set up CORS
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize global variables
tx_history = []
predictions = []


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
        prompt = (
            f"Simulate a short-term Ethereum market forecast for a demo. "
            f"Assume ETH is at ${price}. Write a fictional but realistic prediction using trading lingo. "
            f"This is a simulation. Avoid disclaimers."
            # f"Based on Ethereum's current price of ${price}, "
            # f"generate a bold and confident short-term market prediction. "
            # f"Include technical or sentiment-based reasoning, and assume this is a simulated analysis for a demo. "
            # f"Skip any disclaimers or safety warnings."
        )
        response = ask_ai(prompt)
        logger.info(f"AI response: {response}")
        return {"price": price, "ai_response": response}
    except Exception as e:
        logger.error(f"Error getting AI insight: {e}")
        return {"error": "Error getting AI insight"}

@app.post("/deposit")
def deposit():
    try:
        db: Session = SessionLocal()
        tx_hash = deposit_eth(1)
        tx_history.append(tx_hash)
        tx = Transaction(tx_hash=tx_hash)
        db.add(tx)
        db.commit()
        db.close() 
        logger.info(f"Deposited 1 ETH: {tx_hash}")
        return {"message": "Deposited 1 ETH", "transaction": tx_hash}
    except Exception as e:
        logger.error(f"Error depositing ETH: {e}")
        return {"error": "Error depositing ETH"}
    
@app.get("/transactions")
def get_transactions():
    db: Session = SessionLocal()
    transactions = db.query(Transaction).all()
    db.close()
    return {"transactions": tx_history}

@app.get("/predictions")
def get_predictions():
    db: Session = SessionLocal()
    price = get_eth_price()
    prompt = (
            f"You're a crypto strategist for a trading firm. "
            f"Ethereum is at ${price}. "
            f"Generate a 1-paragraph short-term market prediction with realistic price targets and key market factors. "
            f"Assume this is part of a financial report."
            )
    insight = ask_ai(prompt)

    prediction = Prediction(price=price, ai_response=insight)
    db.add(prediction)
    db.commit()
    db.close()

    return {"price": price, "ai_response": insight}

@app.on_event ("startup")
def on_startup():
    init_db()