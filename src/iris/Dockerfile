FROM python:3.11

WORKDIR /build
COPY requirements.txt requirements.txt
RUN pip install --upgrade -r requirements.txt

COPY . .

EXPOSE 50051
ENTRYPOINT ["python", "predict_iris_server.py"]