#coding=utf-8

import os, sys
import stockquote

# init all
reload(sys)
sys.setdefaultencoding('utf-8')
del sys.setdefaultencoding

#h = stockquote.get_historical_quotes("600004.ss", "20141201", "20141231")
#for one in h:
#	print one
stock_list = stockquote.get_stockslist()
history = stockquote.get_historical_quotes(stock_list[0][0]+'.ss', '20100101', '20141231')
for i in range(history.length()-2, 0):
	train_model(history, i)

def train_model(history, index):
	"""
	Training the data of ten days. 
	To predict the trendency of the next day and the next week.
	"""
