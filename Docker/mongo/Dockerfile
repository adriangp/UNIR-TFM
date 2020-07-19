FROM mongo:latest
LABEL MAINTAINER "Ejemplo basado en https://it-swarn.dev/mongodb"

RUN mkdir -p /data/db \
    && echo "dbpath = /data/db" >> /etc/mongodb.conf \
    && chown -R mongodb:mongodb /data/db

COPY . /data/db

RUN mongod --fork --logpath /var/log/mongodb.log --dbpath /data/db/ \
    && mongo 127.0.0.1:27017 /data/db/scripts/test-create.js \
    && mongod --dbpath /data/db --shutdown \
    && chown -R mongodb /data/db

CMD ["mongod","--config", "/etc/mongodb.conf"]


