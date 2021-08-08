FROM python:3.8-slim

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN apt-get update -y && apt-get install -y gcc g++
RUN python -m pip install --upgrade pip && python -m pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 5000

CMD ["gunicorn", "--timeout", "1000", "--bind", "0.0.0.0:5000", "app:app"]
