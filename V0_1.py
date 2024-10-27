# %%
""" 
THE FOLLOWING CODE WAS ORIGINALLY CREATED BY: 
HASEEB AHMED(https://github.com/H4seeb-Ahmd)
AND 
MADHAV KRISHNAN NATARAJAN(https://github.com/Madhav071)

ORIGINAL CODE: https://github.com/AppleBoys148/ML-MATRIX-AppleBoys

THIS IS AN UPDATED VERSION OF THE SAME CODE CREATED BY HASEEB AHMED 
"""

# %%
#imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Scaling imports
from imblearn.over_sampling import RandomOverSampler

#ML imports

    #KNN
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

    #NaiveBayes
from sklearn.naive_bayes import GaussianNB

    #Logistic Regression
from sklearn.linear_model import LogisticRegression

    #SVM
from sklearn.svm import SVC

    #Neural Networks
from sklearn.neural_network import MLPClassifier

# %%
dataset = pd.read_csv('dataset/dataset.csv')

# %%
dataset.head()

# %%
diseases = list(set(dataset["Disease"].values))
diseases = dict(zip(diseases, range(len(diseases))))
symptoms = list()
for sympt in dict.fromkeys(np.delete(np.array(dataset), 0, 1).reshape((1,-1))[0]):
    if not pd.isna(sympt):
        symptoms.append(sympt.strip())


# %%
rows = dataset.values
encodedrows = []
for row in rows:
    encoding = [row[0]]
    for sympt in symptoms:
        stripedRows = []
        for value in row:
            if not pd.isna(value):
                stripedRows.append(value.strip())
        if sympt in stripedRows[1:]:
            encoding.append(1)
        else:
            encoding.append(0)
    encodedrows.append(encoding)
    

encodedrows = np.array(encodedrows)

dataset = pd.DataFrame(encodedrows, columns = (["Disease"] + symptoms))

# %%
#TRAIN, VALID, TEST

# %%
def Scaler(DF : pd.DataFrame, oversample = False):
    
    X = DF[DF.columns[1:]].values
    Y = DF[DF.columns[0]].values

    if oversample:    
        ros = RandomOverSampler()
        X, Y = ros.fit_resample(X, Y)
    
    data = np.hstack((np.reshape(Y, (-1,1)), X))

    return data, X, Y

# %%
train, test = np.split(dataset.sample(frac = 1), [int(0.6 * len(dataset))])

# %%
train, Xtrain, Ytrain = Scaler(train, True)
test, Xtest, Ytest = Scaler(test, False)

# %%
#plot
def histogramplotter(data):
    plt.hist(data, bins = len(set(data)), rwidth = 0.5)
    plt.xlim(0, 41)
    plt.ylim(0, 100)
    plt.show()

# histogramplotter(Ytrain)
# histogramplotter(Ytest)

# %%
#KNN
knn_model = KNeighborsClassifier(n_neighbors = 10)
knn_model.fit(Xtrain, Ytrain)

y_pred = knn_model.predict(Xtest)

# print(classification_report(Ytest, y_pred))

# %%
#Naive Bayes

nb_model = GaussianNB()
nb_model = nb_model.fit(Xtrain, Ytrain)

Ypred = nb_model.predict(Xtest)

# print(classification_report(Ytest, Ypred))

# %%
#Logistic Regression

lg_model = LogisticRegression()
lg_model = lg_model.fit(Xtrain, Ytrain)

Ypred = lg_model.predict(Xtest)

# print(classification_report(Ytest, Ypred))

# %%
#SVM

svm_model = SVC()
svm_model = svm_model.fit(Xtrain, Ytrain)

Ypred = svm_model.predict(Xtest)

# print(classification_report(Ytest, Ypred))

# %%
#NEURAL NETWORKS

nn_model = MLPClassifier(hidden_layer_sizes = 10,
                         activation = "logistic",
                         solver = "adam")
nn_model = nn_model.fit(Xtrain, Ytrain)

Ypred = nn_model.predict(Xtest)

# print(classification_report(Ytest, Ypred))

# %%
def Diagnose(given_symptoms, model):
    encodedSympts = []
    for sympt in symptoms:
        if sympt in given_symptoms:
            encodedSympts.append(1)
        else:
            encodedSympts.append(0)
    diagnosis = model.predict(np.reshape(encodedSympts, (1, -1)))[0]
    print(diagnosis)
    return diagnosis

# %%
len(symptoms)

# %%
models = [knn_model, nb_model, lg_model, svm_model, nn_model]

# %%
# for model in models:
#     Diagnose([0]*131, model)

# %%



