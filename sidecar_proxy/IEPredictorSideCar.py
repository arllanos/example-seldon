from proto import prediction_pb2
from proto import prediction_pb2_grpc
import grpc
import requests
import json


def rest_request(deploymentName,request):
    print('within rest_request')
    print(request)
    print('----')
    response = requests.post(
                "http://localhost:8002/skmnist/prediction/predict",
                # "http://localhost:8000/api/v0.1/predictions",
                # json=request)
                data={'json': json.dumps(request)})
    return response.json()


# def grpc_request(deploymentName, data):
#     print('within grpc_request')
#     print(type(data))
#     print(data[0])
#     print('-----------')
#     datadef = prediction_pb2.DefaultData(
#         names=["a", "b"],
#         tensor=prediction_pb2.Tensor(
#             shape=[1, 784],
#             values=data[0]
#         )
#     )
#     request = prediction_pb2.SeldonMessage(data=datadef)
#     channel = grpc.insecure_channel(AMBASSADOR_API_IP)
#     stub = prediction_pb2_grpc.SeldonStub(channel)
#     metadata = [('seldon', deploymentName)]
#     response = stub.Predict(request=request, metadata=metadata)
#     return response

class IEPredictorSideCar(object):

    def __init__(self, ie_service_name):
        self.ie_service_name = ie_service_name

    def predict(self,X,feature_names):
        return rest_request(self.ie_service_name, X)