from sklearn.externals import joblib
import os
import json

class SkMnist(object):
    def __init__(self, **kwargs):
        json_conf = os.environ['config_dict'].replace('||','"')
        config = json.loads(json_conf)
        self.clf = joblib.load('/data/{model_id}-{model_version}-{owner_id}-{data_version}/SVM.pkl'.format(**config)) 

    def predict(self,X,feature_names):
        # X is a numpy array containing dictionaries of the form
        # {'id':<ID>, 'values': <features>}
        # So each dictionary contain the sample to be use by one prediction plus
        # some identification identifying that sample.
        ids = [elem['id'] for elem in X]
        feature_matrix = np.array([elem['values'] for elem in X])
        predictions = self.clf.predict(feature_matrix).reshape(1, -1)
        predictions_with_ids = [{'id': elem[0], 'values': elem[1]} for elem in zip(ids, feature_matrix)]
        return predictions_with_ids

g