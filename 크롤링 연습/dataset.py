from bs4 import BeautifulSoup as bs
import urllib.request as req
import requests
import json
import re
from selenium import webdriver
data_json_url = "http://bigdata.kepco.co.kr/cmsajax.do"
json_string = requests.get(data_json_url).text
print(json_string)

baseurl = "http://bigdata.kepco.co.kr/cmsmain.do?scode=S01&pcode=000166"
driver = webdriver.PhantomJS()

soup = bs(driver.page_source, 'html5lib')

print(soup.findALL("div"))

#json_string = requests.get(data_json_url).text

#matched = re.search()


