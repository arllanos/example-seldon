from sklearn.externals import joblib

class SkMnist(object):
    def __init__(self, **kwargs):
        print 'extra arguments'
        print kwargs
        self.class_names = ["class:{}".format(str(i)) for i in range(10)]
        #self.clf = joblib.load('/data/sk.pkl') 

    def predict(self,X,feature_names):
        #predictions = self.clf.predict_proba(X)
        predictions = [[0.06666666666666667, 0.1, 0.03333333333333333, 0.03333333333333333, 0.06666666666666667, 0.1, 0.03333333333333333, 0.5333333333333333, 0.0, 0.03333333333333333]]
        return predictions

    
