#!/usr/bin/env python

import httplib
import sys
import os


def GetStockPriceFromYahoo(stockid):
    yahoo = httplib.HTTPConnection('tw.stock.yahoo.com')

    req = "/q/q?s=" + str(stockid)
#    print req
    yahoo.request("GET", req)
    resp1 = yahoo.getresponse()

#print resp1.status, resp1.reason
    data1 = resp1.read()

    if str(resp1.status) == '200':
        idx = data1.find('13:')
        if idx < 0:
            idx = data1.find('14:')
        if idx < 0:
            return 0
        tempstr1 = data1[idx:]
        idx = tempstr1.find('<b>')
        idx2 = tempstr1.find('</b>')
        tempstr2 = tempstr1[(idx+3):idx2]
        return float(tempstr2)



print GetStockPriceFromYahoo(6189)
print GetStockPriceFromYahoo(3211)
print GetStockPriceFromYahoo(1717)
print GetStockPriceFromYahoo(9904)
print GetStockPriceFromYahoo(1718)
print GetStockPriceFromYahoo(2605)
print GetStockPriceFromYahoo(2345)
print GetStockPriceFromYahoo(3027)


