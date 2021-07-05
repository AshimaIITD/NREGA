import pandas as pd
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE
from adjustText import adjust_text
from csv import reader
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D


t = []
with open('support_trend.csv','r') as read_obj:
	csv_reader = reader(read_obj)
	for row in csv_reader:
		t.append(row)
# print(temp) 
t1 = []
with open('utilisation_trend.csv','r') as read_obj:
	csv_reader = reader(read_obj)
	for row in csv_reader:
		t1.append(row)
t2 = []
with open('management_trend.csv','r') as read_obj:
	csv_reader = reader(read_obj)
	for row in csv_reader:
		t2.append(row)
state_df = []

x = []
y = []
z = []
for i in range(len(t1[0])):
	# print(t2[1][i])
	x.append(float(t[1][i]))
	y.append(float(t1[1][i]))
	z.append(float(t2[1][i]))
	data_point = [t[1][i],t1[1][i],t2[1][i]]
	state_df.append(data_point)

state_df = state_df[0:len(state_df)]
print(len(state_df))
fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
ax = plt.axes(projection ='3d')
ax.scatter(x, y, z, c = 'r', marker = 'o')
ax.set_xlabel('support')
ax.set_ylabel('utilisation')
ax.set_zlabel('management')
plt.title('3D plot of overall scores')
plt.show()


# combine = []
# combine.append(t[0]); combine.append(x); combine.append(y); combine.append(z)
# with open('combine.csv', 'w', newline="") as myfile:
#     wr = csv.writer(myfile, delimiter=",")
#     for word in np.array(combine).T.tolist():
#         wr.writerows([word])



# tsne = TSNE(n_components = 2, learning_rate=50, init='pca', method='exact', n_iter=5000, perplexity = 5)
# tsne_df = tsne.fit_transform(state_df)
# print(tsne_df)
# sns.set()
# fig, ax = plt.subplots(figsize=(11.7, 8.27))
# sns.scatterplot(tsne_df[:, 0], tsne_df[:, 1], alpha=1)

# state_list = t[0]
# texts = []
# for title in range(len(state_list)):
#     texts.append(plt.text(tsne_df[title, 0], tsne_df[title, 1], state_list[title], fontsize=10))
# adjust_text(texts, force_points=0.4, force_text=0.4,
#             expand_points=(2, 1), expand_text=(1, 2),
#             arrowprops=dict(arrowstyle="-", color='black', lw=0.5))
# plt.show()
