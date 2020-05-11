from bs4 import BeautifulSoup as bs
import urllib.request as req
#import request 
baseUrl = "http://bigdata.kepco.co.kr/cmsmain.do?scode=S01&pcode=000167"

res = req.urlopen(baseUrl)
soup = bs(res,"html.parser")
#result = soup.select('.a_c')
result = soup.find_all('td',class_='leg1')

result_list = ['leg1','leg2','leg3','leg4','leg5','leg6','leg7','leg8','leg9','leg10','leg11','leg12','leg13','leg14']


print(result)
#for idx in result_list :
 #print(soup.find(class_='result_list[idx]'))


#result = soup.select(".leg12")

