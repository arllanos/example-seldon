import numpy as np
from sklearn import svm, metrics
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from sklearn.externals import joblib

if __name__ == '__main__':
    data_dir = 'tmp/tensorflow/mnist/input_data'
    mnist = input_data.read_data_sets(data_dir, one_hot=True)
    train_data=mnist.train.images
    train_labels=np.array(np.where(mnist.train.labels==1))[1]
    classifier = svm.SVC(gamma=0.001)
    classifier.fit(train_data, train_labels)
    joblib.dump(classifier, 'data/models/mnist_svm_0_0/SVM.pkl')


