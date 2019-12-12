FROM python:3.7.3
RUN pip install -U pip
WORKDIR /app
COPY gameChallenge /app/
COPY run_local /app/
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000

