#coding=utf-8

import os, sys
import stockquote

# init all
reload(sys)
sys.setdefaultencoding('utf-8')
del sys.setdefaultencoding

#h = stockquote.get_historical_quotes("600004.ss", "20141201", "20141231")
#f = stockquote.get_stockslist()
k = stockquote.from_yahoo('600004.ss')