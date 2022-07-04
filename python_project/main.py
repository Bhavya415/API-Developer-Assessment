from fastapi import FastAPI
from typing import List
from models import Trade,TradeDetails
from datetime import datetime as dt
from uuid import UUID,uuid4
from typing import Optional

# datetime_object = datetime.datetime.now()
app= FastAPI()

ans=[]
test=[]
min_time=dt.strptime("01/01/00", "%m/%d/%y")
max_time=dt.strptime("08/19/20", "%m/%d/%y")
db:List[Trade]=[
   
    Trade(
        # id=UUID("ac171ec2-c8c4-44fd-838e-76682de65233"),
        assetClass="stocks",
        counterparty="Aditya",
        instrumentId="AAPL ",
        instrumentName="CFDs",
        tradeDetails_1={
            'bsi':"buy",
            'price':35,
            'quantity':100
        },
        tradeDateTime=dt.strptime("10/14/13", "%m/%d/%y"),
        tradeId=1,
        trader="bhavya1"
    ),

     Trade(
        # id=UUID("f2c68c8d-a5a0-4fe6-b6c7-3ae164b89bd6"),
        assetClass="bonds",
        counterparty="sagar",
        instrumentId="AAPL",
        instrumentName="instrumentName_2",
        tradeDetails_1={
            'bsi':"buy",
            'price':40,
            'quantity':120
        },
        tradeDateTime=dt.strptime("10/12/13", "%m/%d/%y"),
        tradeId=2,
        trader="bhavya2"
    ),Trade(
        # id=UUID("ac171ec2-c8c4-44fd-838e-76682de65233"),
        assetClass="assetClass_3",
        counterparty="counterparty_3",
        instrumentId="AAPL",
        instrumentName="instrumentName_3",
        tradeDetails_1={
            'bsi':"sell",
            'price':25,
            'quantity':100
        },
        tradeDateTime=dt.strptime("10/11/13", "%m/%d/%y"),
        tradeId=3,
        trader="bhavya3"
    ),

     Trade(
        # id=UUID("f2c68c8d-a5a0-4fe6-b6c7-3ae164b89bd6"),
        assetClass="assetClass4",
        counterparty="counterparty4",
        instrumentId="TSLA",
        instrumentName="instrumentName4",
        tradeDetails_1={
            'bsi':"buy",
            'price':35.5,
            'quantity':100
        },
        tradeDateTime=dt.strptime("10/15/13", "%m/%d/%y"),
        tradeId=4,
        trader="bhavya4"
    )
]
#Listing trades
@app.post("/api/v1/users")
async def detch_users():
    return db


#Single trade
@app.get("/api/v1/users/{user_id}")
async def fetch_users(user_id:int):
    for trades in db:
        if trades.trade_id == user_id:
            return trades
        else:
           continue
            # return db    


#searching trade
@app.get("/api/v1/user_info/{search}")
async def search_trades(search:str):
        # ans.clear()
        for trades in db:
            if ((trades.counterparty == search) or (trades.instrument_id == search) or (trades.instrument_name == search) or (trades.trader == search)):
                # ans=[]
                ans.append(trades)
                # return trades
            else:
               continue
        return ans
        # ans.clear()
            # return db  



  
# Advanced filtering

@app.get("/api/vi/filtering/")
async def read_item(assetClass_1: Optional[str]= None, end: Optional[str]= 1 ,minprice: Optional[float] = None,maxPrice: Optional[float] = None,start: Optional[int] = None,tradeType_1: Optional[str]=None):
    if assetClass_1:
        for trades in db:
            if(trades.asset_class == assetClass_1):
                ans.append(trades)
            else:
                continue
            
    if tradeType_1:
        for trades in db:
            if(dict(trades.trade_details).get("buySellIndicator") == tradeType_1):
                ans.append(trades)
            else:
                continue


    if minprice and maxPrice:
        for trades in db:
            if(dict(trades.trade_details).get("price") > minprice and dict(trades.trade_details).get("price")< maxPrice):
                ans.append(trades)
            else:
                continue

    # if start:
    #     for trades in db:
    #         if trades.trade_date_time < :#passing today date
    #             if test:
    #                 test.pop()
    #                 max_time=trades.trade_date_time
    #                 test.append(trades)
    #             else:
    #                 max_time=trades.trade_date_time
    #                 test.append(trades)
    #         else:
    #             continue
    

    #     for trades in test:
    #         ans.append(trades)
    # test.clear()
       
    # return ans



    # if end:
    #     for trades in db:
    #         if trades.trade_date_time > dt.strptime("01/01/00", "%m/%d/%y"):
    #             if test:
    #                 test.pop()
    #                 min_time=trades.trade_date_time
    #                 test.append(trades)
    #             else:
    #                 max_time=trades.trade_date_time
    #                 test.append(trades)
    #         else:
    #             continue
    

    #     for trades in test:
    #         ans.append(trades)
       
    # return ans
    

    