from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
import re




try:
    url= urlopen("http://bigdata.kepco.co.kr/cmsmain.do?scode=S01&pcode=000167")
except HTTPError as e :
    print(e)    
else : 
    bs = BeautifulSoup(url.read(), "html.parser")


    namelist = ["leg1","leg2","leg3","leg4","leg5","leg6","leg7","leg8","leg9","leg10","leg11","leg12","leg13","leg14",
    "leg15","leg16","leg17","leg18","leg19","leg20","leg21"]

    def delete_tag(name):
          name = re.sub('<span.+?<b','',name,0)
          name = re.sub('</b.+?</span>','',name,0)
          name = re.sub('< b="">','',name,0)
          name = re.sub(' <="" b="">','',name,0)
          name = re.sub(' b="" ','',name,0)
          name = re.sub('="" ','',name,0)
          name = re.sub('<="">','',name,0)
          name = re.sub(' <=""','',name,0)
          name = re.sub('="">', '',name,0)
          return name
          #name4 = str(bsobj.find('span', class_="leg4"))
    
data_list =[]
for i in range(0,21) : 
    data_list.insert(i,str(bs.find('span', class_=namelist[i])))

for i in range(0,21) : 
    print(delete_tag(data_list[i]))


