#coding=utf-8

import os, sys
import csv
import dateutil.parser
import json
import optparse
import urllib, urllib2

# init all
reload(sys)
sys.setdefaultencoding('utf-8')
del sys.setdefaultencoding


def get_real_quotes(symbol):
    return 12

def get_historical_quotes(symbol, start_date, end_date):
    """
    Get historical quotes from Yahoo API for the given ticker symbol.

    Date format is 'YYYYMMDD', or anything understood by
    dateutil.parser.parse, or a datetime instance.

    Returns a nested list.
    """
    if isinstance(start_date, str):
        start_date = dateutil.parser.parse(start_date)
    if isinstance(end_date, str):
        end_date = dateutil.parser.parse(end_date)

    url = ('http://ichart.yahoo.com/table.csv?'
           's=%s&'
           'd=%s&e=%s&f=%s&'
           'a=%s&b=%s&c=%s&'
           'g=d&'
           'ignore=.csv'
           % (symbol,
              end_date.month - 1, end_date.day, end_date.year,
              start_date.month - 1, start_date.day, start_date.year))

    lines = urllib2.urlopen(url).readlines()
    csv_reader = csv.DictReader(lines[1:], fieldnames=lines[0].strip().split(','))

    prices = [dict(csv_line) for csv_line in csv_reader]

    for price_dict in prices:
        price_dict['symbol'] = symbol
        price_dict['source_url'] = url
        price_dict['source'] = 'Yahoo!'

    return prices

def get_stockslist_origin():
    file_origin = open('stockslist_origin.txt', 'r').read()
    file_split1 = file_origin.split(' \t')
    file_split2 = []
    for one in file_split1:
        file_split2 = file_split2 + one.split('\n')
    
    file_new = open('stockslist_new.txt', 'w')
    for one in file_split2:
        l = one.split(' (')
        if len(l[0]) > 3:
            l[1] = l[1][0:6]
            file_new.write(l[0] + '/' + l[1])
            file_new.write('\n')

def get_stockslist():
    """
    Get a list of Shanghai Stock Exchange from website:
    http://www.sse.com.cn/market/sseindex/indexlist/s/i000002/const_list.shtml

    Return a dict of stocks. 
    stocks_dict[0] := Index code
    stocks_dict[1] := Chinese name
    """

    if os.path.exists(r'/stockslist_new.txt') == False:
        get_stockslist_origin()
    
    stocks_dict = []
    file_origin = open('stockslist_new.txt').readlines()
    for one in file_origin:
        d = one.split('/')
        stocks_dict.append((d[1][0:6],d[0]))
    
    return stocks_dict