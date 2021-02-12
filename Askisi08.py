#Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα λεξικό από αρχείο το οποίο περιέχει τα κρυπτονομίσματα (όνομα) που έχει ένας χρήστης και πόσα από αυτά. Χρησιμοποιείστε το API https://min-api.cryptocompare.com για να βρείτε σε τι ποσό σε ευρώ αντιστοιχούν.
#{"BTC":1.345,"ETH":8.2,"LTC":1.234}

import urllib.request
import json
from time import sleep

def get_coin_data(coin):
    url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC&tsyms=EUR&e=CCCAGG"
    r = urllib.request.urlopen(url)
    html = r.read()
    html = html.decode()
    d = json.loads(html)
    return d[coin]["EUR"]

cryptoportfolioineuros= {
  "BTC": 0,
  "ETH": 0,
  "LTC": 0
}

with open('portfolio.txt') as document: 
  d = document.read() 
cryptoportfolio= json.loads(d) 
print(cryptoportfolio) 

while True:
    bitprice=get_coin_data("BTC")
    print(get_coin_data("BTC"))
    ethprice=get_coin_data("ETH")
    print(get_coin_data("ETH"))
    ltcprice=get_coin_data("LTC")
    print(get_coin_data("LTC"))

    bit=float(cryptoportfolio['BTC'])
    eth=float(cryptoportfolio['ETH'])
    ltc=float(cryptoportfolio['LTC'])

    cryptoportfolioineuros["BTC"] = bitprice*bit
    cryptoportfolioineuros["ETH"] = ethprice*eth
    cryptoportfolioineuros["LTC"] = ltcprice*ltc
    
    
    print(cryptoportfolioineuros)
    sleep(10)
