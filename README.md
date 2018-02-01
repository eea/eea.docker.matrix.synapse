# docker-synapse

## Run

```
docker run -d -p 8008:8008 -p 8448:8448 -p 3478:3478 -v /tmp/data:/data donbeave/matrix-synapse
```
Docker compose example
```
  matrix:
    image: eeacms/synapse
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

