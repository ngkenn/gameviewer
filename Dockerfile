FROM python:3.7.3
RUN pip install -U pip
RUN mkdir /app
WORKDIR /app
# COPY gameChallenge /app/
COPY run_local /app/
COPY requirements.txt .
COPY ./ /app/
RUN pip install -r requirements.txt
EXPOSE 8000

