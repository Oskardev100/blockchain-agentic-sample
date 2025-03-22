import json
import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GANACHE_URL = os.getenv("GANACHE_URL")
PRIVATE_KEY = os.getenv("GANACHE_PRIVATE_KEY")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider(GANACHE_URL))

# Load contract ABI
with open("ai_agent/escrow_abi.json", "r") as file:
    contract_abi = json.load(file)["abi"]

# Get contract instance
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

# Get wallet account
account = w3.eth.account.from_key(PRIVATE_KEY)
wallet_address = account.address

# Function to deposit ETH into escrow
def deposit_eth(amount_eth):
    amount_wei = w3.to_wei(amount_eth, "ether")
    nonce = w3.eth.get_transaction_count(wallet_address)

    txn = contract.functions.deposit().build_transaction({
        "from": wallet_address,
        "value": amount_wei,
        "gas": 200000,
        "gasPrice": w3.eth.gas_price,
        "nonce": nonce
    })

    signed_txn = w3.eth.account.sign_transaction(txn, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
    return w3.to_hex(tx_hash)

# Function to release funds
def release_funds():
    nonce = w3.eth.get_transaction_count(wallet_address)

    txn = contract.functions.releaseFunds().build_transaction({
        "from": wallet_address,
        "gas": 200000,
        "gasPrice": w3.eth.gas_price,
        "nonce": nonce
    })

    signed_txn = w3.eth.account.sign_transaction(txn, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
    return w3.to_hex(tx_hash)

# Example usage
if __name__ == "__main__":
    print("Depositing 1 ETH into Escrow...")
    tx_hash = deposit_eth(1)
    print(f"✅ Transaction Hash: {tx_hash}")

    input("\nPress Enter to release funds...")

    print("Releasing funds...")
    tx_hash = release_funds()
    print(f"✅ Transaction Hash: {tx_hash}")
