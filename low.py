import matplotlib.finance as mpf
from matplotlib.dates import date2num
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt





idx=pd.date_range('2016/06/01','2016/07/31 23:59',freq='T')
dn=np.random.randint(2,size=len(idx))*2-1

#ランダムウォーク
rnd_walk=np.cumprod(np.exp(dn*0.0002))*100
df=pd.Series(rnd_walk,index=idx).resample('B').ohlc()

"""
fig=plt.figure()
ax=plt.subplot()

xdate=[x.date() for x in df.index]
ohlc=np.vstack((date2num(xdate),df.values.T)).T
mpf.candlestick_ohlc(ax,ohlc,width=0.7,colorup='g',colordown='r')

ax.grid()
ax.set_xlim(df.index[0].date(),df.index[-1].date())
fig.autofmt_xdate()
"""
fig=plt.figure()
ax=plt.subplot()

ohlc=np.vstack((range(len(df)),df.values.T)).T
mpf.candlestick_ohlc(ax,ohlc,width=0.7,colorup='g',colordown='r')

xtick0=(5-df.index[0].weekday())%5
plt.xticks(range(xtick0,len(df),5),[x.strftime('%Y-%m-%d') for x in df.index][xtick0::5])
ax.grid()
ax.set_xlim(-1,len(df))
fig.autofmt_xdate()
plt.show()



