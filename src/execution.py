import os
from alpaca_client import get_connection
from database_manager import log_trade

# start the alpaca connection
api = get_connection()

def is_already_holding(symbol):
    """
    WEEK 2 STATE MANAGEMENT: 
    Checks if we already own the stock to prevent 'double-buying'.
    """
    positions = api.list_positions()
    for position in positions:
        if position.symbol == symbol:
            return True
    return False

def place_buy_order(symbol, qty):
    """
    WEEK 3 EXECUTION:
    Sends a buy order to Alpaca and logs it to our SQLite database.
    """
    if is_already_holding(symbol):
        print(f"⚠️ Already holding {symbol}. Skipping purchase to prevent duplicate trades.")
        return None

    try:
        # send order to alpaca
        order = api.submit_order(
            symbol=symbol,
            qty=qty,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
        
        # Log to Database
        # placeholder price since the market orders will fill at the current price
        log_trade(symbol, 'BUY', 0.0, qty) 
        
        print(f"✅ Success! Bought {qty} shares of {symbol}.")
        return order
        
    except Exception as e:
        print(f"❌ Trade failed: {e}")
        return None

if __name__ == "__main__":
    # test to see if we are holding Apple
    ticker = "AAPL"
    if is_already_holding(ticker):
        print(f"Status: Currently holding {ticker}")
    else:
        print(f"Status: Not holding {ticker}")
