import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
import requests
import time
import pymongo as mongo
import redis


client = mongo.MongoClient("mongodb://127.0.0.1:27017")
Red = redis.Redis()


hasht =[]
timet =[]
btct =[]
usdt =[]

hasht_arr = []
timet_arr =[]
btct_arr =[]
usdt_arr =[]

db = client["My_DB"]
C_cryp = db["My_Col"]

def get_data(hasht,timet,btct,usdt,Red,C_cryp):
    

    
    r = requests.get('https://www.blockchain.com/btc/unconfirmed-transactions')
    content = r.content
    soup = BeautifulSoup(content, "html.parser")
    #print(soup)

    
    for d in soup.findAll('div', attrs={'class':'sc-1g6z4xm-0 hXyplo'}):
        #print(d)
        Hash = d.find('a', attrs={'class':'sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK'})
        Time = d.findAll('span', attrs={'class':'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
        btc = d.find('div', class_='sc-1au2w4e-0 fTyXWG')
        
        btc3 = float(btc.text[12:len(btc.text) - 3].strip())
        
        
        
        usd3= d.findAll('span', attrs={'class':'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
        usd4= float(usd3[2].text[1:].replace(',','').replace('$',''))
       

        all1=[]

        if Hash is not None:
            hasht_arr.append(Hash.text)
            Red.rpush("Hash", str(Hash.text))
            
        
            
        else:
            hasht_arr.append("unknown-product")


        if Time is not None:
            timet_arr.append(Time[0].text)
            Red.rpush("Time", str(Time[0].text))
           
            
        else:
            timet_arr.append("unknown-Time")

        if btc3 is not None:
            btct_arr.append(btc3)
            Red.rpush("Amount(BTC)", str(btc3))
            
            
        else:
            btct_arr.append("unknown-btc2")


        if usd3 is not None:
            usd4 = btc3 * usd4
            usdt_arr.append(usd4)


            #usdt_arr.append(float(usd4[2]))
            Red.rpush("Amount(USD)", str(usd4))
        
        else:
            usdt_arr.append("unknown-btc2")


    Red.expire("Hash", 60)
    Red.expire("Time", 60)
    Red.expire("Amount(BTC)", 60)
    Red.expire("Amount(USD)", 60)
    #My_Crypto = {"Hash": hasht_arr, "Time" : timet_arr, "Amount(BTC)" : btct_arr, "Amount(USD)" : usdt_arr}
    #print(My_Crypto)
    #C_cryp.insert_one(My_Crypto)

    #results = []
    #results.append(get_data())
    #flatten = lambda l: [item for sublist in l for item in sublist]
    #df = pd.DataFrame(flatten(results),columns=['Hash', 'Time', 'Amount(BTC)', 'Amount(USD)'])
    #df = df.sort_values('Amount(USD)', ascending=False)

    #hasht =df['Hash'].iloc[0]
    #timet =df['Time'].iloc[0]
    #btct =df['Amount(BTC)'].iloc[0]
    #usdt =df['Amount(USD)'].iloc[0]

    


  



while True:
  

  get_data(hasht,timet,btct,usdt,Red,C_cryp)
  time.sleep(60)

  #print(hasht,timet,btct,usdt)
  #df.head(0).to_csv("logfile.log", header=None, index=None, sep='\t', mode='w')

  
  






  



