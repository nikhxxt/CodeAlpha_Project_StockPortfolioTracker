import requests
from datetime import datetime


API_KEY = 'your_alpha_vantage_api_key'

class Portfolio:
    def __init__(self):
      self.holdings = {}
    
    def add_stock(self, symbol, shares, price_per_share):
        if symbol in self.holdings:
            self.holdings[symbol] ['shares'] += shares
            self.update_cost_basis(symbol, price_per_share)
        else;
             self.holdings[symbol] = {'shares ; shares, 'cost_basis' : price_per_share)
                                      
      def remove_stock(self, symbol, shares):
          if symbol in self.holdings:
              if shares >= self.holdings[symbol]['shares']:
                  del self.holdings[symbol]
              else:
                  self.holdings[symbol]['shares'] -=shares

      def update_cost_basis(self, symbol, price):
          if symbol in self.holdings:
              current_shares = self.holdings[symbol]['shares']
              current_cost = self.holdings[symbol]['cost_basis'] * current_shares
              new_cost = current_cost + (price * current_shares)
              self.holdings[symbol]['cost_basis'] = new_cost / current_shares

def portfolio_value(self):
    total_value = 0.0
    for symbol, data in self.holdings.items():
        price = self.get_stock_quotwe(symbol)
        total_value += price * data['shares']
    return total_value

def get_stock_quote(self, symbol):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    try:
       response = requests.get(url)
       data = response.json()
       return float(data['Global Quote']['0.5 price'])
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return 0.0

def print_portfolio(self):
    print
        
      
