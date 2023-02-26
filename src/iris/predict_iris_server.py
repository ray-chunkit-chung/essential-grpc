# Modified from https://yu-ishikawa.medium.com/machine-learning-as-a-microservice-in-python-16ba4b9ea4ee

from concurrent import futures
import logging
import joblib
import os

import grpc
import iris_pb2
import iris_pb2_grpc

PWD = os.path.dirname(os.path.abspath(__file__))


class IrisPredictorServicer(iris_pb2_grpc.IrisPredictorServicer):

    def __init__(self):
        # Put model pickle and server in the same folder
        model_path = os.path.join(PWD, 'iris_model.pkl')
        self.clf = joblib.load(model_path)

    def PredictIris(self, request, context):
        sepal_length = request.sepal_length
        sepal_width = request.sepal_width
        petal_length = request.petal_length
        petal_width = request.petal_width
        result = self.clf.predict(
            [[sepal_length, sepal_width, petal_length, petal_width]])
        return iris_pb2.IrisPredictReply(species=result[0])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    iris_pb2_grpc.add_IrisPredictorServicer_to_server(
        IrisPredictorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
