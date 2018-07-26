class MnistConsumer(object):
    def predict(self,X,feature_names):
        print("Receiving " + str(X))
        return X