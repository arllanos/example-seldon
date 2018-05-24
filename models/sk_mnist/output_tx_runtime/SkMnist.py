from sklearn.externals import joblib

class SkMnist(object):
    def __init__(self):
        self.class_names = ["class:{}".format(str(i)) for i in range(10)]

    def transform_output(self,X,feature_names):
        print "STARTING NEW TRANSFORMING!!!"
        print X
        with open('/data/output.txt', 'w') as f:
            f.write(str(type(X)))
            f.write(str(X))

        print "END TRANSFORMING"
        return X

    
