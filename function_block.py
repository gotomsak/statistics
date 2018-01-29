import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

import csv
import pandas as pd
from matplotlib import ticker
import math

from numpy.random import *
import sympy as sym


#ヒストグラムの表示
def plot_hist(n,d):
    hist=plt.hist(n,bins=d)
    plt.show(hist)

# 分数を割り算してdubleで返す
def Fraction(numerator,denominator):
    return numerator/denominator

# 二項分布を返す
def Binomial_distribution(count,probability):
    return np.random.binomial(n=count,p=probability)

# 偏差を返す
def deviation(average,list_multi):
    deviation_list=[]
    for i in range(len(list_multi)):
        deviation=list_multi[i]-average
        deviation_list.append(deviation)
    return deviation_list


# 分散を返す
def dispersion(deviation_list):
    total=0
    for i in range(len(deviation_list)):
        total+=pow(deviation_list[i],2)
    return total/len(deviation_list)

def zsocore(x,axis=None):
    mean=x.mean(axis=axis,keepdims=True)
    std=np.std(x,axis=axis,keepdims=True)
    zscore=(x-mean)/std
    return zscore

"""
def loading_csv(csv_file):
    with open(csv_file,'r')as f:
        reader=csv.reader(f)
        header=next(reader)
"""

"""
#toi1(1)
sainome=random(500)*360+0
print(sainome)
sainome_hist=plt.hist(sainome,bins=10,lw=3,rwidth=0.9)
plt.show(sainome_hist)
"""
"""
#toi1(2)
count=0
count_list=[]
for j in range(1000):
    saikoro = np.random.randint(1, 7, 10)
    print(saikoro)
    for i in range(len(saikoro)):
        if saikoro[i]==1:
            count+=1
    count_list.append(count)
    count=0

count_hist=plt.hist(count_list,bins=10)
plt.show(count_hist)
print(count_list)
"""
"""
#toi1(3)
count_list=[]
count=0
for j in range(500):
    count=0
    while True:
        count += 1
        saikoro = np.random.randint(1, 7)
        if saikoro==1:
            count_list.append(count)
            break


count_hist=plt.hist(count_list,bins=40)
print(count_list)
plt.show(count_hist)
"""

"""
#toi1(4)
x=np.random.exponential(5,500)
plt.hist(x)
plt.show()
"""
"""
#toi1(5)
x=np.random.poisson(2/5,1000)
plt.hist(x,bins=4,rwidth=0.8)

plt.show()
"""
"""
#toi2(2)
tosi_list=[]
df=pd.read_csv('new_csv.csv')
print(df.tosi)
count=0
for i in df.tosi:
    cast=int(i)
    tosi_list.append(cast)
    print(tosi_list[count])
    count+=1
print(type(tosi_list))


ax=df.plot(y=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'],
        rwidth=0.5,alpha=1,kind='hist',bins=30)

ax.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
plt.show(ax)
"""
"""
#toi3(1)
list_multi=[]
for i in range(1,11):
    multi=pow(i,2)
    list_multi.append(multi)

average=np.average(list_multi)

print(average)
deviation_list=deviation(average,list_multi)
print(deviation_list)
dispersion=dispersion(deviation_list)
print(dispersion)
"""
"""
#toi3(2-1)
cnt=1000
a=0
b=10

#一様乱数作成
x=np.random.uniform(a,b,cnt)
print(x)
plt.hist(x,50,normed=True)
#plt.show()
ave=np.average(x)
dev=deviation(ave,x)
dis=dispersion(dev)
m=a+b/2
y=pow((b-a),2)/12
print(ave,dis,m,y)
"""
"""
#toi3(2-2)
#正規乱数を作成
X=np.random.normal(40,5,1000)
#Y=norm.pdf(X,40,25)
ave=np.average(X)
dev=deviation(ave,X)
dis=dispersion(dev)
print(ave)
print(dis)
"""
"""
#toi3(2-3)
n=8
p=1/4
#二項分布を作成
bin=np.random.binomial(n,p,size=(1000))
ave=np.average(bin)
dev=deviation(ave,bin)
dis=dispersion(dev)
print(ave)
print(n*p)
print(dis)
print(n*p*(1-p))
"""
"""
#toi4(1,2)
nor=np.random.normal(55,12,6000)
x=np.arange(0,100,5)
plt.hist(nor,bins=20,range=(0,100),normed=True)
plt.plot(x,norm.pdf(x,55,12),lw=3,color="r")
plt.show()
"""

#toi(5)
nor=np.random.normal(160,50,10000)
cnt1=0
cnt2=0
cnt3=0
cnt4=0
for i in nor:
    if i>=210:
        cnt1+=1
    if 235>=i and i>=135:
        cnt2+=1
    if 223 >= i and i >= 151:
        cnt3 += 1
    if i>=290:
        cnt4+=1

kai1=cnt1/10000
kai2=cnt2/10000
kai3=cnt3/10000
kai4=cnt4/10000
print(kai1)
print(kai2)
print(kai3)
print(kai4*10000)






#bin=np.random.binomial(7200,1/3)
"""
n=7200
p=1/3
np0=n*p
np1=np0*(1-p)
dis=np.sqrt(np1)

sa1=2000-np0
z1=sa1/dis
print(z1)
"""
#ave=np.average(bin)
#print(bin)
#print(ave)


