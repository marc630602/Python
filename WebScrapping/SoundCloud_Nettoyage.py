# -*- coding:utf-8 -*-
"""
@author:Marc
@file:hi.py
@time:2019/10/2022:36
"""

import pandas as pd

# get data
df = pd.read_csv('C:\\Users\\57621\\Desktop\\IMSD\\python\\projet\\data.csv',encoding='gbk')

# delete the firt coloumn
df = df.drop(columns=['Unnamed: 0'])

#drop those lignes which do not contain the name of song
df = df[df['Song']!='chanson']
a = df[df['play'].str.contains('follower')].index
df = df.drop(index=a)

# clean data for thoses colomn: play/like/repost
df = df.astype('str')
df['play'] = df['play'].str.strip('plays')
df['like'] = df['like'].str.strip('likes')
df['repost'] = df['repost'].str.strip('reposts')
for i in range(len(df)):
    df['play'][i] = df['play'][i].replace(',', '')

    df['like'][i] = df['like'][i].replace(',', '')

    df['repost'][i] = df['repost'][i].replace(',', '')

df.columns = ['Song','Arist','Gnere','Plays','Likes','Reposts']


df.iloc[:,3:] = df.iloc[:,3:].astype(int)

# save data
df.to_csv('C:\\Users\\57621\\Desktop\\IMSD\\python\\projet\\data_nettoyage.csv')