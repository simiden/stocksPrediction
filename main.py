#coding=utf-8

import os, sys
import stockquote
import stockslist

# init all
reload(sys)
sys.setdefaultencoding('utf-8')
del sys.setdefaultencoding

#h = stockquote.get_historical_quotes("600004.ss", "20141201", "20141231")
f = stockslist.get_stockslist()