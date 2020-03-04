# -*- coding:utf-8 -*-
"""
@author:Marc
@file:SoundCloud.py
@time:2019/10/814:12
"""


from bs4 import BeautifulSoup
from requests import get
import re
from selenium import webdriver
import pandas as pd




url = "https://soundcloud.com/charts/top"
request = get(url)
html_soup = BeautifulSoup(request.text, 'lxml')
genres = html_soup.select('a[href*=genre]')[4:]

genre_link = []
genre_name = []
info_link = []
info_list = []

songs_list = []
name_list = []

stock_genre_list = []
songs_genre_list = []

play_list = []
like_list = []
repost_list = []

for index, genre in enumerate(genres):
    genre_link.append(genre.get("href"))
    stock_genre_list.append(genre.text)

for i in range(len(genre_link)):
#for i in [0]:
    url = "https://soundcloud.com" + genre_link[i]
    request = get(url)
    html_soup = BeautifulSoup(request.text, 'lxml')
    infos = html_soup.find_all('h2')[3:]

    for j in range(len(infos)):
        info_link.append(infos[j].a.get("href"))
        infos[j] = re.sub(u"\s", " ", infos[j].text)

    for k in range(15):
    #for k in [0]:
        url = "https://soundcloud.com" + info_link[k]
        options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        html_soup = BeautifulSoup(driver.page_source, 'lxml')
        detail_list = []
        stock_info_list = []

        songs_infos = html_soup.select('div[class*=soundTitle__titleContainer]')
        for index, info in enumerate(songs_infos):
            stock_info_list.append(info.text)

        details = html_soup.select('li[class*=sc-ministats-item ]')
        for index, detail in enumerate(details):
            detail_list.append(detail.get('title'))

        songs_list.append(stock_info_list[0].replace('Play', ' ').replace('Pause',' ').strip().split('\n')[4])
        name_list.append(stock_info_list[0].replace('Play', ' ').replace('Pause', ' ').strip().split('\n')[0])
        songs_genre_list.append(stock_genre_list[i])
        play_list.append(detail_list[0])
        like_list.append(detail_list[1])
        repost_list.append(detail_list[2])

        driver.close()
        print(k)
        data = {'song': songs_list, 'chanteur':name_list, 'genre': songs_genre_list, 'play': play_list, 'like': like_list, 'repost': repost_list}
        df = pd.DataFrame(data)
        df.to_csv('C:\\Users\\57621\\Desktop\\IMSD\\python\\projet\\data1.csv')









