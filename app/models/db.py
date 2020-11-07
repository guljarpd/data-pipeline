import os
import databases
import sqlalchemy

# SQLAlchemy specific code, as with any other app
DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://xisbiymuaiktao:402379fb2c1a4502848815ee4d0e63ab81e424973bebff46474e1b5dd91feb72@ec2-54-237-155-151.compute-1.amazonaws.com:5432/dfqf53rvj9248m")
database = databases.Database(DATABASE_URL, ssl="allow")

metadata = sqlalchemy.MetaData()

tickers = sqlalchemy.Table(
  "tickers",
  metadata,
  sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
  sqlalchemy.Column("symbol", sqlalchemy.Text),
  sqlalchemy.Column("info_highest_buy_bid", sqlalchemy.Numeric(14, 7)),
  sqlalchemy.Column("info_lowest_sell_bid", sqlalchemy.Numeric(14, 7)),
  sqlalchemy.Column("info_last_traded_price", sqlalchemy.Numeric(14, 7)),
  sqlalchemy.Column("info_yes_price", sqlalchemy.Numeric(13, 7)),
  sqlalchemy.Column("info_volume_max", sqlalchemy.String),
  sqlalchemy.Column("info_volume_min", sqlalchemy.String),
  sqlalchemy.Column("info_volume_volume", sqlalchemy.Numeric(15, 8)),
  sqlalchemy.Column("timestamp", sqlalchemy.Integer),
  sqlalchemy.Column("datetime", sqlalchemy.Integer),
  sqlalchemy.Column("high", sqlalchemy.String),
  sqlalchemy.Column("low", sqlalchemy.String),
  sqlalchemy.Column("bid", sqlalchemy.Numeric(14, 7)),
  sqlalchemy.Column("bid_volume", sqlalchemy.String),
  sqlalchemy.Column("ask", sqlalchemy.Numeric(14, 7)),
  sqlalchemy.Column("ask_volume", sqlalchemy.String),
  sqlalchemy.Column("vwap", sqlalchemy.String),
  sqlalchemy.Column("open", sqlalchemy.Numeric(13, 7)),
  sqlalchemy.Column("close", sqlalchemy.Numeric(14, 7)),
  sqlalchemy.Column("last", sqlalchemy.Numeric(14, 7)),
  sqlalchemy.Column("base_volume", sqlalchemy.Numeric(15, 8)),
  sqlalchemy.Column("quote_volume", sqlalchemy.String),
  sqlalchemy.Column("previous_close", sqlalchemy.String),
  sqlalchemy.Column("change", sqlalchemy.Numeric(11, 4)),
  sqlalchemy.Column("percentage", sqlalchemy.Numeric(15, 13)),
  sqlalchemy.Column("average", sqlalchemy.Numeric(14, 7))
)
# 
# 
engine = sqlalchemy.create_engine(DATABASE_URL)
# 
metadata.create_all(engine)

