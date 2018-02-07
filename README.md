# Docker image for Synapse Matrix.org server

Docker image for https://github.com/matrix-org/synapse, including configuration changes used in EEA and adding HTTP JSON REST Authenticator module for synapse (https://github.com/kamax-io/matrix-synapse-rest-auth)

## Supported tags and respective `Dockerfile` links

- [`latest` (*Dockerfile*)](https://github.com/eea/eea.docker.matrix.synapse/blob/master/Dockerfile)
- [`v0.26.0` (*Dockerfile*)](https://github.com/eea/eea.docker.matrix.synapse/blob/v0.26.0/Dockerfile)

## Variables

1. SERVER_NAME - The public url of matrix, used in federation and under which every user is saved; Is used in Riot and Identity containers
2. REPORT_STATS - Send data to matrix.org: hostname, synapse version & uptime, total_users, total_nonbridged users, total_room_count, daily_active_users, daily_active_rooms, daily_messages and daily_sent_messages.
3. DATABASE - database type - postgresql or sqlite
4. POSTGRES_HOST - Postgres Host
4. DB_USER - Matrix postgres database user
4. DB_PASSWORD - Matrix postgres database password
5. DB_NAME - Matrix postgres database name
6. EMAIL_FROM - Email used to send notifications from Matrix
7. RIOT_BASE_URL: Will be included in emails
8. PUBLIC_BASE_URL: the same as SERVER_NAME
9. REGISTRATION_ENABLED: "yes"/"no"



## Usage

```
docker run -d -p 8008:8008 -p 8448:8448 -p 3478:3478  -v /tmp/data:/data eeacms/matrix-synapse
```

Docker compose example
```
  matrix:
    image: eeacms/matrix-synapse
    restart: always
    command: start
    ports:
      - "8208:8008"
      - "8248:8448"
      - "3578:3478"
    volumes:
      - ./data/synapse/:/data
    environment:
      SERVER_NAME: riot.devecs.eea.europa.eu
      REPORT_STATS: 'yes'
      DATABASE: postgresql
      POSTGRES_HOST: db
      DB_NAME: synapse
      DB_USER: matrix
      DB_PASSWORD: matrix
      EMAIL_FROM: 'Riot EEA <eea@eea.com>'
      RIOT_BASE_URL: https://riot_URL/
      PUBLIC_BASE_URL: matrix_base
      REGISTRATION_ENABLED: 'no'
```

