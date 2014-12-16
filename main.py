#coding=utf-8

import os, sys
import stockquote
import define_model

# init all
reload(sys)
sys.setdefaultencoding('utf-8')
del sys.setdefaultencoding

#h = stockquote.get_historical_quotes("600004.ss", "20141201", "20141231")
#for one in h:
#	print one
stock_list = stockquote.get_stockslist()
history = stockquote.get_historical_quotes(stock_list[0][0]+'.ss', '20140101', '20141231')

model = define_model.type_model(5)
model.train_model(history)
print model.data[0]









