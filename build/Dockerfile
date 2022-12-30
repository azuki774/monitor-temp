FROM python:3.11.1-slim-bullseye
LABEL description="monitoring-temp"
RUN apt-get update && \
    apt-get install -y jq curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install influxdb-client
COPY src/client/ /app
WORKDIR /app
ENTRYPOINT ["python3", "main.py"]
