import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
import requests
import time
import pymongo as mongo
import redis

import multiprocessing
import time


Red = redis.Redis()

client = mongo.MongoClient("mongodb://127.0.0.1:27017")
db = client["My_DB"]
C_cryp = db["My_Col"]

Hash = []
Times = []
Btc = []
Usd = []


def MY_MAX_FUN(Red, C_cryp):
    Hash = list(map(str, Red.lrange("Hash", 0, -1)))
    Times = list(map(str, Red.lrange("Time", 0, -1)))
    Btc = list(map(float, Red.lrange("Amount(BTC)", 0, -1)))
    Usd = list(map(float, Red.lrange("Amount(USD)", 0, -1)))
    M_USD = max(Usd)
    index = Usd.index(M_USD)
    M_HASH = Hash[index]
    M_TIME = Times[index]
    M_BTC = Btc[index]
    My_V = {"Hash": M_HASH, "Time": M_TIME, "Amount(BTC)": M_BTC, "Amount(USD)": M_USD}
    C_cryp.insert_one(My_V)
    
    
   



# continue with your code then terminate the child

while True:
    MY_MAX_FUN(Red, C_cryp)
    time.sleep(60)


    
    
    
    
    


    
    
    



    