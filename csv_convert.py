import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint
import linecache
import numpy as np
import re



html = urlopen("http://www.data.jma.go.jp/gmd/cpd/db/elnino/index/soi.html")

soup=BeautifulSoup(html,"html.parser")

day=[]

data=soup.find("pre")

str_data=str(data)
count=0
for i in str_data:
    if i == "\n":
        #print("ok")
        count+=1


word_str=np.core.defchararray.split(np.array(str_data))

P_day=re.compile('[A-Z]')
word_list=list(word_str)

for i in word_str:
    P_day_m = P_day.findall(i)
    if P_day_m:
      day.append(i)
      print(i)


print(P_day_m)
print(word_str)

print(count)
print(str_data)
print(str_data[1])

"""
with open('new_csv.csv','w')as f:
    writer=csv.writer(f,lineterminator='\n')
    writer.writerow(list)
"""



"""

#URLの指定
html = urlopen("http://www.data.jma.go.jp/gmd/cpd/db/elnino/index/soi.html")



bsObj=BeautifulSoup(html,"html.parser")

#テーブルを指定
table=bsObj.findAll("div",{"class":"contents"})[0]
rows=table.findAll("pre")
print(type(rows))

#ファル指定
with open("new_csv.csv",'wt',newline='',encoding='utf-8')as f:
    writer=csv.writer(f)
    for i in range(0,len(rows),2):
        print(i)
        writer.writerow([rows[i],rows[i+1]])






writer=csv.writer(csvFile,lineterminator='\n')

print(rows)
writer.writerows(rows)

"""