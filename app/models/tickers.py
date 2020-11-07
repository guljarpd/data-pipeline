from pydantic import BaseModel
from typing import Optional


# class Volume(BaseModel):
#     max: str
#     min: str
#     volume: float


# class Info(BaseModel):
#     highest_buy_bid: float
#     lowest_sell_bid: float
#     last_traded_price: float
#     yes_price: float
#     volume: Volume




class TickersIn(BaseModel):
    symbol: str
    info_highest_buy_bid: float
    info_lowest_sell_bid: float
    info_last_traded_price: float
    info_yes_price: float
    info_volume_max: str
    info_volume_min: str
    info_volume_volume: float
    timestamp: int
    datetime: int
    high: str
    low: str
    bid: float
    bid_volume: Optional[str] = None
    ask: float
    ask_volume: Optional[str] = None
    vwap: str
    open: float
    close: float
    last: float
    base_volume: Optional[float] = None
    quote_volume: Optional[str] = None
    previous_close: Optional[str] =  None
    change: float
    percentage: float
    average: float

class TickersOut(BaseModel):
    id: int
    symbol: str
    info_highest_buy_bid: Optional[float] = None
    info_lowest_sell_bid: Optional[float] = None
    info_last_traded_price: Optional[float] = None
    info_yes_price: Optional[float] = None
    info_volume_max: Optional[str] = None
    info_volume_min: Optional[str] = None
    info_volume_volume: Optional[float] = None
    timestamp: int
    datetime: int
    high: str
    low: str
    bid: float
    bid_volume: Optional[str] = None
    ask: float
    ask_volume: Optional[str] = None
    vwap: str
    open: float
    close: float
    last: float
    base_volume: Optional[float] = None
    quote_volume: Optional[str] = None  
    previous_close: Optional[str] = None
    change: float
    percentage: float
    average: float
