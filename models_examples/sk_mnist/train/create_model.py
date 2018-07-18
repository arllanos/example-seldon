import numpy as np
from sklearn import svm, metrics
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from sklearn.externals import joblib
import os

if __name__ == '__main__':
    PERSISTENT_VOLUME = '/data'

    data_dir = '%s/tmp/tensorflow/mnist/input_data' % PERSISTENT_VOLUME
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    mnist = input_data.read_data_sets(data_dir, one_hot=True)
    train_data=mnist.train.images
    train_labels=np.array(np.where(mnist.train.labels==1))[1]

    classifier = svm.SVC(gamma=0.001)
    classifier.fit(train_data, train_labels)

    model_id = 'mnist'
    model_version = 'svm'
    owner_id = '1'
    data_version = '0'
    dump_dir = '%s/%s-%s-%s-%s' % (PERSISTENT_VOLUME, model_id, model_version, owner_id, data_version)
    if not os.path.exists(dump_dir):
        os.makedirs(dump_dir)
    fullfilename = '%s/%s' % (dump_dir, '%s.pkl' % model_version)
    try:
        joblib.dump(classifier, fullfilename)
    except Exception as e:
        print('Dump model error: %s' % str(e))
        pass

