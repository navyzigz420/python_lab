# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 05:01:38 2019

@author: admin
"""
import numpy as np
np.random.seed(100)
np_hist = np.random.normal(loc=0, scale=1, size=1000)
np_hist[:10]
array([-1.74976547,  0.3426804 ,  1.1530358 , -0.25243604,  0.98132079,
        0.51421884,  0.22117967, -1.07004333, -0.18949583,  0.25500144])

np_hist.mean(),np_hist.std()
(-0.016772157343909157, 1.0458427194167)

hist,bin_edges = np.histogram(np_hist)
hist
array([  7,  37, 111, 207, 275, 213, 105,  31,  10,   4])
bin_edges
array([-3.20995538, -2.50316588, -1.79637637, -1.08958687, -0.38279736,
        0.32399215,  1.03078165,  1.73757116,  2.44436066,  3.15115017,
        3.85793967])
import matplotlib.pyplot as plt
%matplotlib inline

plt.figure(figsize=[10,8])

plt.bar(bin_edges[:-1], hist, width = 0.5, color='#0504aa',alpha=0.7)
plt.xlim(min(bin_edges), max(bin_edges))
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value',fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.title('Normal Distribution Histogram',fontsize=15)
plt.show()
bin_edges = np.round(bin_edges,0)
plt.figure(figsize=[10,8])

plt.bar(bin_edges[:-1], hist, width = 0.5, color='#0504aa',alpha=0.7)
plt.xlim(min(bin_edges), max(bin_edges))
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value',fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.title('Normal Distribution Histogram',fontsize=15)
plt.show()
hist, bin_edges = np.histogram([1, 1, 2, 2, 2, 2, 3],bins=range(5))
hist
array([0, 2, 4, 1])
bin_edges
array([0, 1, 2, 3, 4])
plt.figure(figsize=[10,8])
n, bins, patches = plt.hist(x=np_hist, bins=8, color='#0504aa',alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value',fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.title('Normal Distribution Histogram',fontsize=15)
plt.show()
plt.figure(figsize=[10,8])
x = 0.3*np.random.randn(1000)
y = 0.3*np.random.randn(1000)
n, bins, patches = plt.hist([x, y])
from sklearn.datasets import load_iris
import pandas as pd
data = load_iris().data
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width']
dataset = pd.DataFrame(data,columns=names)
dataset.head()
dataset.columns[0]
'sepal-length'
fig = plt.figure(figsize = (8,8))
ax = fig.gca()
dataset.hist(ax=ax)
plt.show()
plt.figure(figsize=[10,10])
f,a = plt.subplots(2,2)
a = a.ravel()
for idx,ax in enumerate(a):
    ax.hist(dataset.iloc[:,idx], bins='auto', color='#0504aa',alpha=0.7, rwidth=0.85)
    ax.set_title(dataset.columns[idx])
plt.tight_layout()
<Figure size 720x720 with 0 Axes>
import cv2
lena_rgb = cv2.imread('lena.png')
lena_gray = cv2.cvtColor(lena_rgb,cv2.COLOR_BGR2GRAY)
lena_gray.shape
(512, 512)
binary = cv2.imread('binary.png')
binary.shape
(1394, 2190, 3)
binary = cv2.resize(binary,(512,512),cv2.INTER_CUBIC)
binary.shape
(512, 512, 3)
binary_gray = cv2.cvtColor(binary,cv2.COLOR_BGR2GRAY)
binary_gray.shape
(512, 512)
plt.figure(figsize=[10,10])

plt.subplot(121)
plt.imshow(lena_rgb[:,:,::-1])
plt.title("Natural Image")

plt.subplot(122)
plt.imshow(binary[:,:,::-1])
plt.title("Document Image")
plt.show()
hist, edges = np.histogram(binary_gray,bins=range(255))
plt.figure(figsize=[10,8])

plt.bar(edges[:-1], hist, width = 0.8, color='#0504aa')
plt.xlim(min(edges), max(edges))
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value',fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.title('Document Image Histogram',fontsize=15)
plt.show()
hist, edges = np.histogram(lena_gray,bins=range(260))
plt.figure(figsize=[10,8])

plt.bar(edges[:-1], hist, width = 0.5, color='#0504aa')
plt.xlim(min(edges), max(edges))
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Pixels',fontsize=15)
plt.ylabel('Frequency of Pixels',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.title('Natural Image Histogram',fontsize=15)
plt.show()