# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17VNVEM5d-Neh6fW6aIpn2XCKGRNkJEo7
"""

import pandas as pd
!wget http://iali.in/datasets/IEEEAPSIT/unsupervised-ml/Wholesale%20customers%20data.csv
data = pd.read_csv ('http://iali.in/datasets/IEEEAPSIT/unsupervised-ml/Wholesale%20customers%20data.csv')
data=data.drop(["Channel","Region"],axis=1).values
from sklearn.datasets import load_iris
from itertools import cycle
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from numpy.random import RandomState
import pylab as pl

class clustering:
	def __init__(self):
		self.plot(load_iris().data)

	def plot(self, X):
		pca = PCA(n_components=3, whiten=True).fit(X)
		X_pca = pca.transform(X)
		kmeans = KMeans(n_clusters=8, random_state=RandomState(42)).fit(X_pca)
		plot_2D(X_pca, kmeans.labels_, ["c0", "c1", "c2", "c3", "c4", "c5", "c6","c7","c8"])

def plot_2D(data, target, target_names):
	colors = cycle('rgbcmyk')
	target_ids = range(len(target_names))
	pl.figure()
	for i, c, label in zip(target_ids, colors, target_names):
		pl.scatter(data[target == i, 0], data[target == i, 1],
					c=c, label=label)
	pl.legend()
	pl.show()

if __name__ == '__main__':
	c = clustering()

