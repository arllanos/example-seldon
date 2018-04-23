from sklearn.externals import joblib
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler


class SkIris(object):
    def __init__(self):
        self.class_names = ["class:{}".format(str(i)) for i in range(10)]
        self.clf = joblib.load('/data/sk_iris.pkl') 

    def predict(self,X,feature_names):
        file = open('messages.txt', 'w')
        file.write(str(type(X)))
        file.write(str(X))
        try:
            feature_matrix = X
            sc = StandardScaler()
            sc.fit(feature_matrix)
            X_test_std = sc.transform(feature_matrix)
            predictions =   self.clf.predict(X_test_std)
            file.write(str(predictions))
            file.close()
            return predictions

        except Exception as err:
            file.write('The error is: ' + str(err))
            file.close()    
        
