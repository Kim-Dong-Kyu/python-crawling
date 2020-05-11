import requests as req
from bs4 import BeautifulSoup as bs
import pymysql
#import pandas as pd
import re
from sqlalchemy import create_engine
from urllib.request import urlopen
from urllib.request import HTTPError
from datetime import datetime, timedelta


try : 
 baseurl =urlopen("http://www.kpx.or.kr/")
except HTTPError as e : 
    print(e)

else : 
    bsObj = bs(baseurl.read(), 'html.parser')
    now = datetime.now()
    #peek = bsObj.find('dl',class_='graph_list')
    peek = bsObj.find('dl',class_='graph_list')
    peek2 = bsObj.select('dl > dd')
    print(peek.text)
    print(peek2)
    #(str)date = (str)now.year + (str)now.month + (str)now.day 
    










