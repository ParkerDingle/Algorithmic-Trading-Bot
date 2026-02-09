import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

# This will grab the secret keys
load_dotenv()
API_KEY = os.getenv('ALPACA_API_KEY')
SECRET_KEY = os.getenv('ALPACA_SECRET_KEY')
BASE_URL = 'https://paper-api.alpaca.markets' # paper url for testing

def get_connection():
    """Initializes the connection to Alpaca"""
    return tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

if __name__ == "__main__":
    # will only run if manually done for testing
    try:
        api = get_connection()
        account = api.get_account()
        print("--- Connection Status ---")
        print(f"Connected to Account: {account.id}")
        print(f"Buying Power: ${account.buying_power}")
        print("-------------------------")
    except Exception as e:
        print(f"Error: Could not connect. Check your .env file. Details: {e}")
