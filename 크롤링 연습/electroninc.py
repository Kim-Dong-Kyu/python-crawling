from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
import re



try :
    url = urlopen("http://bigdata.kepco.co.kr/cmsmain.do?scode=S01&pcode=000166")
except HTTPError as e :
    print(e)
else: 
    bsobj = BeautifulSoup(url.read(), "html.parser")

    namelist = ["leg1","leg2","leg3","leg4","leg5","leg6","leg7","leg8","leg9","leg10","leg11","leg12","leg13","leg14",
    "leg15","leg16","leg17","leg18","leg19","leg20","leg21"]
    

    name = str(bsobj.find('span', class_="leg1"))
    name = re.sub('<span.+?<b','',name,0)
    name = re.sub('</b.+?</span>','',name,0)
    name = re.sub('< b="">','',name,0)
    
    print(name)

    name = str(bsobj.find('span', class_="leg2"))
    name = re.sub('<span.+?<b','',name,0)
    name = re.sub('</b.+?</span>','',name,0)
    name = re.sub('< b="">','',name,0)
    name = re.sub(' <="" b="">','',name,0)
    
    print(name)

    name = str(bsobj.find('span', class_="leg3"))
    name = re.sub('<span.+?<b','',name,0)
    name = re.sub('</b.+?</span>','',name,0)
    name = re.sub('< b="">','',name,0)
    name = re.sub(' <="" b="">','',name,0)
    name = re.sub(' b="" ','',name,0)
    name = re.sub('="" ','',name,0)
    name = re.sub('<="">','',name,0)

    print(name)
 
 
    name = str(bsobj.find('span', class_="leg4"))
    name = re.sub('<span.+?<b','',name,0)
    name = re.sub('</b.+?</span>','',name,0)
    name = re.sub('< b="">','',name,0)
    name = re.sub(' <="" b="">','',name,0)
    name = re.sub(' b="" ','',name,0)
    name = re.sub('="" ','',name,0)
    name = re.sub('<="">','',name,0)
    print(name)

    name4 = str(bsobj.find('span', class_="leg4"))
    def delete_tag(name):
          name = re.sub('<span.+?<b','',name,0)
          name = re.sub('</b.+?</span>','',name,0)
          name = re.sub('< b="">','',name,0)
          name = re.sub(' <="" b="">','',name,0)
          name = re.sub(' b="" ','',name,0)
          name = re.sub('="" ','',name,0)
          name = re.sub('<="">','',name,0)

          return name

    print(delete_tag(name4))