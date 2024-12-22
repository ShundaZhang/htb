FROM python:3.8-slim

ADD challenge /challenge

WORKDIR /challenge

RUN pip install -r requirements.txt

EXPOSE 1337

CMD ["python","./application/app.py"]