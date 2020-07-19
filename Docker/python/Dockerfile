FROM python:3.7
LABEL MAINTAINER "Adrian Ganan"

RUN mkdir /App
WORKDIR /App
COPY src/requirements.txt /App
RUN pip install -r requirements.txt
COPY src /App

EXPOSE 8080

ENTRYPOINT ["python","/App/app.py"]
