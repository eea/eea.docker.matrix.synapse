FROM avhost/docker-matrix:v0.34.1.1
LABEL maintainer="EEA: IDM2 A-Team <eea-edw-a-team-alerts@googlegroups.com>"



RUN apt-get update -y -q --fix-missing \
    && apt-get install -y --no-install-recommends wget \
    && wget -O /usr/lib/python2.7/dist-packages/rest_auth_provider.py https://raw.githubusercontent.com/kamax-matrix/matrix-synapse-rest-auth/master/rest_auth_provider.py \
    && apt-get clean \
    && pip install bleach 



# add configs
COPY config/supervisord-matrix.conf config/supervisord-turnserver.conf  /conf/
COPY config/index.html config/logo.png /webclient/
COPY home_server_config.py start.sh config/supervisord.conf /

EXPOSE 8008 8448 3478

ENTRYPOINT ["/start.sh"]
CMD ["autostart"]
