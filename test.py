import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
GANACHE_URL = os.getenv("GANACHE_URL")  # Now pointing to Ganache

w3 = Web3(Web3.HTTPProvider(GANACHE_URL))

if w3.is_connected():
    print("✅ Connected to Local Ganache Blockchain")
    print(f"Current Block: {w3.eth.block_number}")
else:
    print("❌ Connection Failed")


# Get list of accounts
accounts = w3.eth.accounts
print("\nAvailable Accounts:")
for account in accounts:
    balance = w3.eth.get_balance(account)
    print(f"{account} → {w3.from_wei(balance, 'ether')} ETH")    