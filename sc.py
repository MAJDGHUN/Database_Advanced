import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
import requests
import time
import os



  
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
        btc2 = Time
        usd3= Time
       

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






while True:
  time.sleep(5)
  get_data()
  results = []
  results.append(get_data())
  flatten = lambda l: [item for sublist in l for item in sublist]
  df = pd.DataFrame(flatten(results),columns=['Hash', 'Time', 'Amount(BTC)', 'Amount(USD)'])
  df = df.sort_values('Amount(USD)', ascending=False)
  print(df.head(1))
  df.head(1).to_csv("logfile.txt", header=None, index=None, sep='\t', mode='a')




  
  




