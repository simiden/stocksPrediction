#coding=utf-8

import os, sys
import re
import stockquote

# init all
reload(sys)
sys.setdefaultencoding('utf-8')
del sys.setdefaultencoding

def get_stockslist():
	file = open('stockslist.txt', 'r').read()
	file_split = file.split(' \t')
	list = []
	for one in file_split:
		list = list + one.split('\n')
	
	return list