# Launching Linked Containers

You can launch linked ATSD and Axibase Collector containers on the same Docker host with `docker-compose`.

`docker-compose.yml`

```yaml
version: '2'

services:

  atsd:
    image: axibase/atsd:latest
    ports:
      - "8081:8081"
      - "8443:8443"
    container_name: atsd
    environment:
      - ADMIN_USER_NAME=${ADMUSR}
      - ADMIN_USER_PASSWORD=${ADMPWD}
      - COLLECTOR_USER_TYPE=api-rw
      - COLLECTOR_USER_NAME=${USR}
      - COLLECTOR_USER_PASSWORD=${PWD}

  collector:
    image: axibase/collector:latest
    ports:
      - "9443:9443"
    depends_on:
      - atsd
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      - COLLECTOR_USER_NAME=${USR}
      - COLLECTOR_USER_PASSWORD=${PWD}
      - ATSD_URL=https://atsd:8443
      - COLLECTOR_ARGS=-job-enable=docker-socket
```

Launch containers:

```sh
export ADMUSR=auser; export ADMPWD=apassword; \
      export USR=cuser; export PWD=cpassword; \
      docker-compose up -d
```

Log in to ATSD on `https://docker_host:8443` using administrator credentials.