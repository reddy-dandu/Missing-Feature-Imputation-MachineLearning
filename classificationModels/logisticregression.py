# -*- coding: utf-8 -*-
"""LogisticRegression-ML_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mvLF6ixIaVk33gb0a1BR5VFBJeUv8aSU
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
from tqdm import tqdm

"""## Read Data and get features X, targets y"""

train=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/ML_FinalProject/LogisticRegression/Train_data.csv')

# train=train.head(30)

features=train.drop(['class_sitting', 'class_sittingdown','class_standing','class_standingup','class_walking'], axis = 1)

features.head(5)

targets=train[['class_sitting', 'class_sittingdown','class_standing','class_standingup','class_walking']]

targets.head(5)

features.head(1)

"""## Mean Centering Method!"""

features=features-features.mean()

features.head(5)

targets = targets.apply(pd.to_numeric)

targets.head(1)

"""## Define functions to predict target, define cost, etc"""

def hypothesis(theta, X):
    return 1 / (1 + np.exp(-(np.dot(theta, X.T)))) - 0.0000001 #1/(1+e^-z) where z is theta.X

def cost(X, y, theta):
    y1 = hypothesis(theta, X)
    return -(1/len(X)) * np.sum(y*np.log(y1) + (1-y)*np.log(1-y1))

def gradient_descent(X, y, theta, alpha, epochs):
    m = len(X)
    for i in tqdm(range(0, epochs)):
        for j in range(0, 5):
            theta = pd.DataFrame(theta)
            h = hypothesis(theta.iloc[:,j], X)
            for k in range(0, theta.shape[0]):
                theta.iloc[k, j] -= (alpha/m) * np.sum((h-y.iloc[:, j])*X.iloc[:, k])
            theta = pd.DataFrame(theta)
    return theta, cost

"""## Adding bias column to X"""

print(len(features))
print(len(targets))
X = pd.concat([pd.Series(1, index=features.index, name='00'), features], axis=1) #bias column

X.head(5)

y = targets

y.head(5)

"""## Training"""

#create theta from theta 0 to theta num_features for each column of y; size of the theta array is num_features X num_targets
theta = np.zeros([features.shape[1]+1, y.shape[1]])
theta.shape

# learning_rates = [0.001, 0.003, 0.005, 0.01]
# thetaGlobal=[]
# for rate in learning_rates:
theta,cost = gradient_descent(X, y, theta, 0.002, 2500)
  # thetaGlobal.append(theta)

theta

# theta = np.zeros([df.shape[1]+1, y1.shape[1]])
# theta2 = pd.DataFrame(theta)
# theta2

type(theta)

theta3=theta

"""## Testing"""

test=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/ML_FinalProject/LogisticRegression/Test_data.csv')

featuresTest=test.drop(['class_sitting', 'class_sittingdown','class_standing','class_standingup','class_walking'], axis = 1)

"""### Mean centering method!"""

featuresTest=featuresTest-featuresTest.mean()

targetsTest=test[['class_sitting', 'class_sittingdown','class_standing','class_standingup','class_walking']]

print(len(featuresTest))
print(len(targetsTest))
Xtest = pd.concat([pd.Series(1, index=featuresTest.index, name='00'), featuresTest], axis=1) #bias column

ytest=targetsTest

output = []
for i in range(0, 5):
    h = hypothesis(theta3.iloc[:,i], Xtest)
    # theta4 = pd.DataFrame(theta)
    # h = hypothesis(theta4.iloc[:,i], X)
    output.append(h)
output=pd.DataFrame(output)

output.head(5)

"""## Argmax of y0,y1,y2,y3,y4 is marked as the class"""

for m in range(33127):
  max=np.argmax(list(output.iloc[:, m]))
  output.iloc[max, m]=1

"""## Accuracy calculations"""

accuracy = 0
for col in range(0, 5):
    for row in range(len(ytest)):
        if ytest.iloc[row, col] == 1 and output.iloc[col, row] == 1:
            accuracy += 1
accuracy = accuracy/len(Xtest)

accuracy


