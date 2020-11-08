import json
from app.models.db import database, tickers

def make_json(params):

  # print(type(params))

  return {
    "symbol": params.get("symbol"),
    "info_highest_buy_bid": params.get("info").get("highest_buy_bid"),
    "info_lowest_sell_bid": params.get("info").get("lowest_sell_bid"),
    "info_last_traded_price": params.get("info").get("last_traded_price"),
    "info_yes_price": params.get("info").get("yes_price"),
    "info_volume_max": params.get("info").get("volume").get("max"),
    "info_volume_min": params.get("info").get("volume").get("min"),
    "info_volume_volume": params.get("info").get("volume").get("volume"),
    "timestamp": params.get("timestamp"),
    "datetime": params.get("datetime"),
    "high": params.get("high"),
    "low": params.get("low"),
    "bid": params.get("bid"),
    "bid_volume": params.get("bid_volume"),
    "ask": params.get("ask"),
    "ask_volume": params.get("ask_volume"),
    "vwap": params.get("vwap"),
    "open": params.get("open"),
    "close": params.get("close"),
    "last": params.get("last"),
    "base_volume": params.get("base_volume"),
    "quote_volume": params.get("quote_volume"),
    "previous_close": params.get("previous_close"),
    "change": params.get("change"),
    "percentage": params.get("percentage"),
    "average": params.get("average")
  }

async def read_and_save():
  try:
    # pass
    values = []
    # 
    with open("./app/data/tickers.json", "r", encoding="utf-8") as fp:
      json_data = json.load(fp)
      # print(json_data)
      for item in json_data:
        # print(json_data[item].get("symbol"))
        params = make_json(json_data[item])
        values.append(params)
        # print(params)
    # print(values)
    # 
    query = tickers.insert()
    print(query, values)
    await database.execute_many(query=query, values=values)
  except Exception as e:
    print(e)
    pass
  
    
    