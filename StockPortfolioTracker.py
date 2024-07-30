import requests
from datetime import datetime


API_KEY = 'your_alpha_vantage_api_key'

class Portfolio:
    def __init__(self):
      self.holdings = {}
      
