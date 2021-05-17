# Import useful libraries and classes.
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
#html upload
my_url=  "http://www.imdb.com/search/title?sort=num_votes,desc&start=1&title_type=feature&year=1950,2012"
uClient= uReq(my_url)
page_html= uClient.read()
uClient.close()
#html parser
page_soup= soup(page_html)
#read class from web page.
containers= page_soup.findAll("div", {"class": "lister-item mode-advanced"})
print(len(containers))
filename= "imdb_m.csv"
f= open(filename, "w")

headers= "Name, Year, Runtime \n"
f.write(headers)

for container in containers:
    name= container.img["alt"]
    year_mov= container.findAll("span", {"class": "lister-item-year"})
    year=year_mov[0].text
    runtime_mov= container.findAll("span", {"class": "runtime"})
    runtime=runtime_mov[0].text
    
    print(name + "," + year + "," + runtime +  "\n")
    f.write(name + "," + year + "," + runtime  + "\n")
    
f.close()
import pandas as pd
df = pd.read_csv("imdb_m.csv", encoding="latin1")
df.head()
