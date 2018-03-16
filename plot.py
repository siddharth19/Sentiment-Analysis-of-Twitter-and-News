import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("tweets_key2.csv")
df.head()

y2=[]
x=len(df[df['Sentiment']==-1])
y=len(df[df['Sentiment']==0])
z=len(df[df['Sentiment']==1])
# print(x,y,z)
# print(len(df[df['Sentiment']==-1]))
y2.append(x)
y2.append(y)
y2.append(z)
x2=[1,2,3]
fig, ax = plt.subplots()
# ind = np.arange(1, 4)
#
# show the figure, but do not block
# plt.show(block=False)


pm, pc, pn = plt.bar(x2, y2)
pm.set_color('r')
pc.set_color('b')
pn.set_color('g')
ax.set_xticks(x2)
ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
mx=max(x,y,z)+5
ax.set_ylim([0, mx])
ax.set_ylabel('Count')
ax.set_title('Sentiment Analysis')

plt.show(block=True)
# plt.bar(x,y2)


