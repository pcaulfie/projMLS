FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=powerapp.py

CMD python -m flask run