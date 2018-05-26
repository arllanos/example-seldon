from sklearn.externals import joblib
import time

class SkMnist(object):
    def __init__(self):
        self.class_names = ["class:{}".format(str(i)) for i in range(10)]


    def transform_input(self, X, feature_names):
        time.sleep(2)
        print "STARTING NEW TRANSFORMING input!!!"
        print X
        with open('/data/output.txt', 'w') as f:
            f.write(str(type(X)))
            f.write(str(X))
        print "END TRANSFORMING"
        predictions = [[0.99, 0.1, 0.03333333333333333, 0.03333333333333333, 0.06666666666666667, 0.1, 0.03333333333333333, 0.5333333333333333, 0.0, 0.03333333333333333]]
        return predictions

    def transform_output(self,X,feature_names):
        print "STARTING NEW TRANSFORMING!!!"
        print X
        with open('/data/output.txt', 'w') as f:
            f.write(str(type(X)))
            f.write(str(X))

        print "END TRANSFORMING"

        predictions = [[0.99, 0.1, 0.03333333333333333, 0.03333333333333333, 0.06666666666666667, 0.1, 0.03333333333333333, 0.5333333333333333, 0.0, 0.03333333333333333]]
        return predictions

        

    
