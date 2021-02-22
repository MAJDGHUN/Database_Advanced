import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
import requests
import time
import pymongo as mongo


client = mongo.MongoClient("mongodb://127.0.0.1:27017")


  
def get_data():

    
    r = requests.get('https://www.blockchain.com/btc/unconfirmed-transactions')
    content = r.content
    soup = BeautifulSoup(content, "html.parser")
    #print(soup)

    alls = []
    for d in soup.findAll('div', attrs={'class':'sc-1g6z4xm-0 hXyplo'}):
        #print(d)
        Hash = d.find('a', attrs={'class':'sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK'})
        Time = d.findAll('span', attrs={'class':'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
        btc2 = d.findAll('span', attrs={'class':'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
        usd3= d.findAll('span', attrs={'class':'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
       

        all1=[]

        if Hash is not None:
            all1.append(Hash.text)
            
        
            
        else:
            all1.append("unknown-product")


        if Time is not None:
            all1.append(Time[0].text)
           
            
        else:
            all1.append("unknown-Time")

        if btc2 is not None:
            all1.append(btc2[1].text)
            
            
        else:
            all1.append("unknown-btc2")


        if usd3 is not None:
            all1.append(float(usd3[2].text.replace(',','').replace('$','')))
            
            
        else:
            all1.append("unknown-usd2")

        
        
        alls.append(all1) 
    return alls




  
db = client["My_DB"]
c_crypto = db["My_Col"]


while True:
  time.sleep(60)


  get_data()
  results = []
  results.append(get_data())
  flatten = lambda l: [item for sublist in l for item in sublist]
  df = pd.DataFrame(flatten(results),columns=['Hash', 'Time', 'Amount(BTC)', 'Amount(USD)'])
  df = df.sort_values('Amount(USD)', ascending=False)

  hasht =df['Hash'].iloc[0]
  timet =df['Time'].iloc[0]
  btct =df['Amount(BTC)'].iloc[0]
  usdt =df['Amount(USD)'].iloc[0]

  My_Crypto = {"Hash": hasht, "Time" : timet, "Amount(BTC)" : btct, "Amount(USD)" : usdt}
  c_crypto.insert_one(My_Crypto)




  print(hasht,timet,btct,usdt)
  df.head(0).to_csv("logfile.txt", header=None, index=None, sep='\t', mode='a')

  
  




