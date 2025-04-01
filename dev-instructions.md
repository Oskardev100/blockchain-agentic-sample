## Project Setup – Step-by-Step Instructions

### 1. Clone the Repository
git clone https://github.com/Oskardev100/blockchain-agentic-sample.git
cd blockchain-agentic-sample


### 2. Setup Python Virtual Environment 
python -m venv venv
venv\Scripts\activate   # For Windows
# OR
source venv/bin/activate  # For macOS/Linux


### 3. Install Python Dependencies
pip install -r requirements.txt


### 4. Setup Frontend ReactJs
cd frontend
npm install
cd ..

### 5. Configure Environment Variables
## Create a .env file in the root directory and add the following:
OPENAI_API_KEY=your_openai_api_key
GANACHE_PRIVATE_KEY=your_ganache_account_private_key
CONTRACT_ADDRESS=0xYourDeployedContract
GANACHE_URL=http://127.0.0.1:7545


### 6. Start Ganache (Local Ethereum Testnet)
- Open Ganache UI
- Click Quickstart
- Make sure the RPC is running at: http://127.0.0.1:7545


### 7. Compile & Deploy the Smart Contract
npx hardhat compile
npx hardhat run scripts/deploy.js --network ganache
## Note: After deployment, copy the generated contract address and update CONTRACT_ADDRESS in your .env file.


### 8. Start the FastAPI Backend
## Ensure your Python virtual environment is activated, then run:
uvicorn backend.main:app --reload
## The backend will be available at: http://localhost:8000


### 9. Start react front end
cd frontend
npm start

## The frontend will be available at: http://localhost:3000

