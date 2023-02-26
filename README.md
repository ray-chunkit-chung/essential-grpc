# essential grpc Quick start

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/ray-chunkit-chung/essential-grpc/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/ray-chunkit-chung/essential-grpc/tree/main)

## Reference

<https://grpc.io/docs/languages/python/basics/>

<https://grpc.io/docs/what-is-grpc/introduction/>

<https://protobuf.dev/overview/>

![image](https://user-images.githubusercontent.com/26511618/220845488-14a3640f-c7ab-46a3-9b05-ef33d15dbe64.png)

## gRPC Quick start

### Install python venv and packages

```bash
python -m venv. venv
.venv\Scripts\activate  ## windows
python -m pip install --upgrade pip
pip install --upgrade -r requirements.txt
```

### Example 1 Hello World

This example is from [This code's documentation lives on the grpc.io site.](https://grpc.io/docs/languages/python/quickstart)

Start server

```bash
source .venv/Scripts/activate
cd src/helloworld
python greeter_server.py
```

From another terminal, run the client:

```bash
source .venv/Scripts/activate
cd src/helloworld
python greeter_client.py
```

We can modifiy the service by the following steps:

1. Update rpc in service in src/protos/helloworld.proto

    ```proto
    service Greeter {
        // ...
        // Add new rpc here
        rpc SayHelloAgain (HelloRequest) returns (HelloReply) {}
        // ...
    }
    ```

2. Run at src\helloworld

    ```bash
    python -m grpc_tools.protoc -I../protos --python_out=. --pyi_out=. --grpc_python_out=. ../protos/helloworld.proto
    ```

3. Confirm three files should be modified:
    - helloworld_pb2_grpc.py (contains our generated request and response classes)
    - helloworld_pb2.py (contains our generated client and server classes)
    - helloworld_pb2.pyi

4. Update the server in src\helloworld\greeter_server.py
5. Update the client in src\helloworld\greeter_client.py

### Example 2 Generate server and client from proto

The code is by <https://grpc.io/docs/languages/python/basics/>

The following steps will create the server and client

1. Generate the gRPC client and server interfaces from src\protos\route_guide.proto

    ```bash
    cd src
    mkdir route_guide
    cd route_guide
    python -m grpc_tools.protoc -I../protos --python_out=. --pyi_out=. --grpc_python_out=. ../protos/route_guide.proto
    ```

2. Implement the server by creating files
    - src\route_guide\route_guide_server.py
    - src\route_guide\route_guide_resources.py
    - src\route_guide\route_guide_db.json

3. Implement the client by creating a new file src\route_guide\route_guide_client.py

### Example 3 Machine learning prediction service

Reference

- <https://blog.roboflow.com/deploy-machine-learning-models-pytorch-grpc-asyncio/>
- <https://yu-ishikawa.medium.com/machine-learning-as-a-microservice-in-python-16ba4b9ea4ee>
- <https://towardsdatascience.com/serving-deep-learning-model-in-production-using-fast-and-efficient-grpc-6dfe94bf9234>
- <https://towardsdatascience.com/serving-ml-models-with-grpc-2116cf8374dd>

1. Create server/client interface for the prediction engine

    ```bash
    cd src/iris
    python -m grpc_tools.protoc -I../protos --python_out=. --pyi_out=. --grpc_python_out=. ../protos/iris.proto
    ```

2. Implement
    - src\iris\train.py
    - src\iris\predict_iris_client.py
    - src\iris\predict_iris_server.py

3. Start prediction server

    ```bash
    cd src\iris
    python predict_iris_client.py
    ```

4. Test by making prediction

    ```bash
    python predict_iris_client.py run --sepal-length 1.0 --sepal-width 1.0 --petal-length 1.0 --petal-width 1.0
    ```

### Example 4 Serve with nginx/Azure

- <https://www.nginx.com/blog/nginx-1-13-10-grpc/>
- <https://www.thorsten-hans.com/exposing-grpc-services-in-azure-container-apps/>
- <https://github.com/Azure/app-service-linux-docs/blob/master/HowTo/gRPC/use_gRPC_with_dotnet.md>

Coming soon..
