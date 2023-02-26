# Modified from https://yu-ishikawa.medium.com/machine-learning-as-a-microservice-in-python-16ba4b9ea4ee

import logging
import typer

import grpc
import iris_pb2
import iris_pb2_grpc


app = typer.Typer()


@app.callback()
def callback():
    """
    Awesome Iris Predictor
    """


@app.command()
def run(
    sepal_length: float = 5.0,
    sepal_width: float = 3.6,
    petal_length: float = 1.3,
    petal_width: float = 0.25
) -> None:
    """
    Predict iris
    """
    logging.basicConfig()
    with grpc.insecure_channel('test2raywebapp.azurewebsites.net:50051') as channel:
        stub = iris_pb2_grpc.IrisPredictorStub(channel)
        request = iris_pb2.IrisPredictRequest(
            sepal_length=sepal_length,
            sepal_width=sepal_width,
            petal_length=petal_length,
            petal_width=petal_width
        )
        response = stub.PredictIris(request)
        print("Predicted species number: " + str(response.species))


if __name__ == "__main__":
    app()
