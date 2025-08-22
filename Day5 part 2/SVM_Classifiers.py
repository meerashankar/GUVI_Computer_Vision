import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split


digits = datasets.load_digits()


X = digits.images
y = digits.target


n_samples = len(X)
X = X.reshape((n_samples, -1))


X_train, X_test, y__train, y_test = train_test_split(X, y, test_size=0.5,shuffle=False)


clf = svm.SVC(gamma=0.001)
clf.fit(X_train, y__train)