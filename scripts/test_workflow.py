import sys
import os

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_full_workflow():
    # Step 1: Check ETH price
    price_response = client.get("/eth_price")
    assert price_response.status_code == 200

    # Step 2: Generate insight
    ai_response = client.get("/insight")
    assert ai_response.status_code == 200
    assert "ai_response" in ai_response.json()

    # Step 3: Deposit ETH
    deposit_response = client.post("/deposit")
    assert deposit_response.status_code == 200
    assert "transaction" in deposit_response.json()

# 👇 Add this
if __name__ == "__main__":
    test_full_workflow()
