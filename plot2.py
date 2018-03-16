import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("tweets_key1.csv")
df.head()


fig, ax = plt.subplots()
x=np.arange(df.size)
# ax.set_xticks(x)
# my_xticks = np.arange(68)
# plt.xticks(x, my_xticks)
# plt.plot(x, y)
ax.set_ylabel('Sentiment Value')
ax.set_xlabel('Time')
ax.set_title('Sentiment v/s Time')
plt.plot(df.iloc[:,0:1])
plt.show(block=True)
