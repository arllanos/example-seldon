from sklearn.externals import joblib

class SkMnist(object):
    def __init__(self):
        self.class_names = ["class:{}".format(str(i)) for i in range(10)]
        #self.clf = joblib.load('/data/sk.pkl') 

    def transform_output(self,X,feature_names):
        print(X)
        return X

    
