import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Function to fetch ETH price
def get_eth_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
    response = requests.get(url).json()
    return float(response["price"])

# AI agent logic
def ask_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Example: AI agent monitors ETH price and decides
if __name__ == "__main__":
    eth_price = get_eth_price()
    print(f"Current ETH Price: ${eth_price}")

    # ai_response = ask_ai(f"Ethereum is currently trading at ${eth_price}. What is your financial insight?")
    ai_response = ask_ai(f"Ethereum is currently trading at ${eth_price}. "
                     f"Analyze recent market trends and give a potential short-term forecast based on historical patterns.")
    print("\nAI Response:", ai_response)