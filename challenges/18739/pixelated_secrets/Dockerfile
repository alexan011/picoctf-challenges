FROM python:3.11-slim

WORKDIR /challenge

COPY artifacts /challenge/artifacts
COPY setup-challenge.py /challenge/setup-challenge.py

RUN python3 /challenge/setup-challenge.py

CMD ["python3", "-m", "http.server", "8000"]

