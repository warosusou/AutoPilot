from binance.client import Client

class AutoPilot:
    def __init__(self, key, secret):
        self.client = Client(api_key=key, api_secret=secret)

    def get_all_tickers(self) -> list:
        try:
            return self.client.get_all_tickers()
        except Exception as e:
            print(e)
            return None

    def get_symbol_tikcer(self, symbol: str) -> dict:
        try:
            if(symbol):
                return self.client.get_symbol_ticker(symbol=symbol)
            else:
                raise ValueError('designate symbol')
        except Exception as e:
            print(e)
            return None

    def get_symbol_info(self,symbol:str) -> dict:
        try:
            if(symbol):
                return self.client.get_symbol_info(symbol=symbol)
            else:
                raise ValueError('designate symbol')
        except Exception as e:
            print(e)
            return None