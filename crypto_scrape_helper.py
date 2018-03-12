# -*- coding: utf-8 -*-
"""
Poloniex
PUMP N DUMP HUNTING

"""

import pandas as pd

#Sample json URL
btc_url = 'https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=1439020800&end=1511202699&period=14400'

cryptos = ['ETH', 'VTC', 'STR', 'XRP','DASH','LTC','ETC','XMR','ZEC',
         'STRAT','XEM','VIA','SYS','LSK','FCT','CVC','BTS','DOGE',
         'DGB','DCR','SC','EXP','GNO','XCP','MAID',
           'NXC','GNT','STEEM','ZRX','GAME','FLO','NAV','CLAM',
           'LBC','HUC','OMNI','POT','BURST','BCY','NXT','FLDC',
           'ARDR','BLK','EMC2','NEOS','AMP','BCN','RADS','VRC', 'XVC',
           'REP','BTCD','XBC','RIC','PASC','NMC','PPC','PINK',
           'XPM','SBD','GRC','BELA','BTM']  



# 1511202699 = Nov 20th 2017, 631pm

#Look up coin of interest, make sure to input coin as string
def coin_lookup(coin):
    
    cc = 'BTC_'+str(coin)
    url = 'https://poloniex.com/public?command=returnChartData&currencyPair=XXX&start=1439020800&end=1511202699&period=14400'
    new_url = url.replace('XXX', str(cc))
    
    ico = pd.read_json(new_url)

    
    return ico



