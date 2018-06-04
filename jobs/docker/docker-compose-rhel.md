# Launching Linked Containers with `docker-compose`

You can launch linked ATSD and Axibase Collector containers on the same Docker host with `docker-compose`.

## Export Credentials as Environment Variables

`docker-compose.yml`

```yaml
version: '2'

services:

  atsd:
    image: registry.connect.redhat.com/axibase/atsd:latest
    ports:
      - "8088:8088"
      - "8443:8443"
      - "8081:8081"
      - "8082:8082/udp"
    container_name: atsd
    hostname: atsd
    restart: always
    environment:
      - COLLECTOR_USER_NAME=${C_USER}
      - COLLECTOR_USER_PASSWORD=${C_PASSWORD}
      - COLLECTOR_USER_TYPE=api-rw

  collector:
    image: registry.connect.redhat.com/axibase/collector:latest
    depends_on:
      - atsd
    ports:
      - "9443:9443"
    container_name: axibase-collector
    restart: always
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      - COLLECTOR_USER_NAME=${C_USER}
      - COLLECTOR_USER_PASSWORD=${C_PASSWORD}
      - ATSD_URL=https://atsd:8443
      - COLLECTOR_ARGS=-job-enable=docker-socket
```

Launch containers:

```sh
export C_USER=myuser; export C_PASSWORD=mypassword; docker-compose up -d
```