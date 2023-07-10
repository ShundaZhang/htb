FROM php@sha256:c5aa11a8d2dfe5c895d67bd602118362d017e724b7ec3e5b6e296dd5c92110c4
RUN useradd --user-group --no-log-init ctf
COPY challenge/php_logger.so /php_logger.so
COPY challenge /web
RUN mv /web/flag.txt /
WORKDIR /web
EXPOSE 1337
USER ctf
CMD ["/web/start.sh"]

