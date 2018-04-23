import sys
import time
from concurrent import futures
from sklearn.linear_model import Perceptron
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
import time


if __name__ == '__main__':
    classifier = Perceptron(n_iter=40, eta0=0.1, random_state=1)
    iris = datasets.load_iris()
    sc = StandardScaler()
    X = iris.data[:, [2, 3]]
    sc.fit(X)
    X = sc.transform(X)
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1, stratify=y)
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    classifier.fit(X_train_std, y_train)
    print(classifier.score(X_test, y_test))
    joblib.dump(classifier, '/data/sk_iris.pkl') 

    #introducing a delay for debugging purposes
    time.sleep(600)