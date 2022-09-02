import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import seaborn as sns
from sklearn.model_selection import train_test_split
from math import exp
from sklearn.metrics import confusion_matrix



# Generate blobs dataset
features, label = make_blobs(n_samples=800, centers=2,\
                             n_features=2, random_state=12)
data = pd.DataFrame()
data['x1'] = features[:,0]
data['x2'] = features[:,1]
data['y']  = label

sns.pairplot(data,hue='y')

# print(data)

train, test = train_test_split(data.values,test_size=0.2)

def predict(row, beta):
    x = row[0:2]
    yhat = beta[0] + beta[1]*x[0] + beta[2]*x[1]
    return 1.0 / (1.0 + exp(-yhat))


l_rate = 0.3
n_epoch = 100

loss = np.zeros(n_epoch)
beta = [0.0,0.0,0.0]
for epoch in range(n_epoch):
    sum_error = 0
    for row in train:
        x = row[0:-1] # input features
        y = row[-1]   # output label
        yhat = predict(row, beta)
        error = y - yhat
        sum_error += error**2
        beta[0] += l_rate * error * yhat * (1.0 - yhat)
        beta[1] += l_rate * error * yhat * (1.0 - yhat) * x[0]
        beta[2] += l_rate * error * yhat * (1.0 - yhat) * x[1]
    loss[epoch] = sum_error

print('Coefficients:',beta)
plt.plot(loss)
plt.xlabel('Epoch')
plt.ylabel('Loss')



yhat = []
for row in test:
    yhat.append(round(predict(row, beta)))

cmat = confusion_matrix(test[:,-1],yhat)
sns.heatmap(cmat,annot=True)
