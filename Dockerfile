FROM matrixdotorg/synapse:v0.34.1.1
LABEL maintainer="EEA: IDM2 A-Team <eea-edw-a-team-alerts@googlegroups.com>"


RUN find / -name python 

RUN apk add --no-cache --virtual .run-deps wget coturn \
    && wget -O /usr/local/lib/python2.7/site-packages/rest_auth_provider.py https://raw.githubusercontent.com/kamax-matrix/matrix-synapse-rest-auth/master/rest_auth_provider.py 



# add configs
COPY config/supervisord-matrix.conf config/supervisord-turnserver.conf  /conf/
COPY config/index.html config/logo.png /webclient/
COPY home_server_config.py start.sh config/supervisord.conf /

EXPOSE 8008 8448 3478

ENTRYPOINT ["/start.sh"]
CMD ["autostart"]
