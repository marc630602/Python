import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('C:\\Users\\57621\\Desktop\\IMSD\\python\\projet\\data_nettoyage.csv',encoding='gbk')

df_groups_sum = df.iloc[:,2:].groupby('Genre').sum()
df_groups_mean = df.iloc[:,2:].groupby('Genre').mean()

# Analyse of Plays
data_count_plays = df_groups_sum['Plays'].sort_values(ascending=False).to_frame().reset_index()
data_mean_plays = df_groups_mean['Plays'].sort_values(ascending=False).to_frame().reset_index()

f1, [ax1, ax2, ax3] = plt.subplots(3, 1, figsize=(20, 20))
sns.barplot(x='Genre', y='Plays', palette="Blues_d", data=data_count_plays.head(15), ax=ax1)
ax1.set_title('Plays_times by genre', fontsize=15)
ax1.set_xlabel('Genre')
ax1.set_ylabel('Play_times')

sns.barplot(x='Genre', y='Plays', palette="Blues_d", data=data_mean_plays.head(15), ax=ax2)
ax2.set_title('Plays_times by genre', fontsize=15)
ax2.set_xlabel('Genre')
ax2.set_ylabel('Play_times')

plt.pie(data_count_plays['Plays'])
ax3.set_title('Plays_times by genre', fontsize=15)
ax3.set_xlabel('Genre')
ax3.set_ylabel('Play_times')

plt.show()

# Analyse of Likes
data_count_likes = df_groups_sum['Likes'].sort_values(ascending=False).to_frame().reset_index()
data_mean_likes = df_groups_mean['Likes'].sort_values(ascending=False).to_frame().reset_index()

f2, [ax1, ax2, ax3] = plt.subplots(3, 1, figsize=(20, 20))
sns.barplot(x='Genre', y='Likes', data=data_count_likes.head(15), ax=ax1)
ax1.set_title('Likes_times by genre', fontsize=15)
ax1.set_xlabel('Genre')
ax1.set_ylabel('Likes_times')


sns.barplot(x='Genre', y='Likes',  data=data_mean_likes.head(15), ax=ax2)
ax2.set_title('Likes_times by genre', fontsize=15)
ax2.set_xlabel('Genre')
ax2.set_ylabel('Likes_times')

plt.pie(data_count_likes['Likes'])
ax3.set_title('Likes_times by genre', fontsize=15)
ax3.set_xlabel('Genre')
ax3.set_ylabel('Likes_times')

plt.show()

# Analyse of Reposts
data_count_reposts = df_groups_sum['Reposts'].sort_values(ascending=False).to_frame().reset_index()
data_mean_reposts = df_groups_mean['Reposts'].sort_values(ascending=False).to_frame().reset_index()

f3, [ax1, ax2, ax3] = plt.subplots(3, 1, figsize=(20, 20))
sns.barplot(x='Genre', y='Reposts', data=data_count_reposts.head(15), ax=ax1)
ax1.set_title('Reposts_times by genre', fontsize=15)
ax1.set_xlabel('Genre')
ax1.set_ylabel('Reposts_times')


sns.barplot(x='Genre', y='Reposts',  data=data_mean_reposts.head(15), ax=ax2)
ax2.set_title('Reposts_times by genre', fontsize=15)
ax2.set_xlabel('Genre')
ax2.set_ylabel('Reposts_times')

plt.pie(data_count_reposts['Reposts'])
ax3.set_title('Reposts_times by genre', fontsize=15)
ax3.set_xlabel('Genre')
ax3.set_ylabel('Reposts_times')

plt.show()

#



