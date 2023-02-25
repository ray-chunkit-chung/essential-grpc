# essential-grpc

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/ray-chunkit-chung/essential-grpc/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/ray-chunkit-chung/essential-grpc/tree/main)

## Reference

<https://grpc.io/docs/languages/python/basics/>

<https://grpc.io/docs/what-is-grpc/introduction/>

<https://protobuf.dev/overview/>

![image](https://user-images.githubusercontent.com/26511618/220845488-14a3640f-c7ab-46a3-9b05-ef33d15dbe64.png)

## Serving ML models with gRPC

<https://towardsdatascience.com/serving-ml-models-with-grpc-2116cf8374dd>

## Getting started of gRPC


### Install python venv and packages

```bash
python -m venv. venv
.venv\Scripts\activate  ## windows
python -m pip install --upgrade pip
pip install --upgrade -r requirements.txt
```

### Hello World

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

