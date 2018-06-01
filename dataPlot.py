from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import torch.nn as nn
import torch.nn.functional as F
import torch
from torch.autograd import Variable 
from sklearn.metrics import accuracy_score
from sklearn.utils import shuffle
from sklearn import svm
from collections import defaultdict


dataset=pd.read_csv("dataUpdated.csv")
dataset.dropna(how='all', inplace = True)
	
sales = {}
for month in range(1, 13):
	for year in  range(2010, 2019):
		sales[str(year) + str(month)] = 0;
	
	
	
plt.clf()
plt.title("")
for index, set in dataset.iterrows():
	#print (str(set["year"]))
	if (set["year"] >= 2010 and set["sale"] == 1):
		sales[str(set["year"]) + str(set["month"])] += 1

for month in range(1, 13):
	for year in  range(2010, 2019):
		plt.scatter(year, month, sales[str(year) + str(month)] / 4)
plt.xlim(2009, 2019)
plt.ylim(0, 13)
plt.show()
