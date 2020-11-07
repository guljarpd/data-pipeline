from os import pathsep
from typing import List, Optional
from fastapi import APIRouter
from fastapi import params
from fastapi.params import Query
from app.models.db import database, tickers
from app.models.tickers import TickersIn, TickersOut

# 
router = APIRouter()



"""
## Payload for create new record

{
  "symbol":"BTC/INR",
  "info_highest_buy_bid":858558.95,
  "info_lowest_sell_bid":859172.24,
  "info_last_traded_price":858586.59,
  "info_yes_price":860330.8,
  "info_volume_max":"874081.00",
  "info_volume_min":"853002.96",
  "info_volume_volume":5.99453366,
  "timestamp":1602485335788,
  "datetime":1602485335788,
  "high":"874081.00",
  "low":"853002.96",
  "bid":858558.95,
  "bid_volume":"",
  "ask":859172.24,
  "ask_volume":"",
  "vwap":"",
  "open":860330.8,
  "close":858586.59,
  "last":858586.59,
  "base_volume":5.99453366,
  "quote_volume":"",
  "previous_close":"",
  "change":-1744.2100000000792,
  "percentage":-0.20273713320505077,
  "average":859458.6950000001
}
"""
# create a new record
@router.post('/ticker/create', response_model=TickersOut)
async def create_record(params: TickersIn):

  query = tickers.insert().values(**params.dict())
  # 
  last_record_id = await database.execute(query)
  return {**params.dict(), "id": last_record_id}


# get record
@router.get('/ticker/get', response_model=List[TickersOut])
async def get_record(limit: Optional[int] = 20, page: Optional[int] = 1, q: Optional[str] = None):

  offset = 0 if page <= 1 else (page-1)*limit

  query = tickers.select().limit(limit).offset(offset)

  return await database.fetch_all(query)

# update record
@router.put('/ticker/update/{id}', response_model=TickersOut)
async def update_record(id: int, params: TickersIn):

  query = tickers.update().where(tickers.c.id == id).values(**params.dict())
  await database.execute(query)
  return {**params.dict(), "id": id}

# delete
@router.delete('/ticker/delete/{id}')
async def delete_record(id: int):
  # 
  query = tickers.delete().where(tickers.c.id == id)

  await database.execute(query)

  return {"message": "Data deleted"}
