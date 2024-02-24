FROM python:3.10-alpine

RUN apk add --no-cache socat dash && ln -sf /usr/bin/dash /bin/sh

ENV PYTHONUNBUFFERED=1

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip

RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install flask

EXPOSE 1337

RUN addgroup -S ctf && adduser -S ctf -G ctf

COPY challenge/ /home/ctf/

WORKDIR /home/ctf

RUN mkdir -p /home/ctf/uploads
RUN chown -R ctf:ctf /home/ctf/uploads/

USER ctf

CMD ["python3", "./server.py"]