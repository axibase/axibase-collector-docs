# Installation on Docker

## Quick Start

For a quick installation of pre-integrated Axibase Collector and ATSD instances in a single Docker container, refer to the [ATSD Sandbox](https://github.com/axibase/dockers/tree/atsd-sandbox#overview) guide.

## Host Requirements

* [Docker Engine](https://docs.docker.com/engine/installation/) `1.7+`

## Image Information

* Image name: `axibase/collector:latest`
* [Dockerfile](https://github.com/axibase/docker-axibase-collector/blob/master/Dockerfile)
* [Docker Hub](https://hub.docker.com/r/axibase/collector/)

## Importing an Image in Restricted Environments

If the Docker host does not have connectivity to [Docker Hub](https://hub.docker.com), download and import the Collector image manually.

* Log in to a Docker host which is connected to Docker Hub.
* Pull the Collector image from Docker Hub and export into an archive file:

```sh
docker pull axibase/collector:latest
docker save -o docker-axibase-collector.tar axibase/collector:latest
gzip docker-axibase-collector.tar
```

* Copy the `docker-axibase-collector.tar.gz` archive to the target Docker host.
* Import the image from the archive:

```sh
docker load < docker-axibase-collector.tar.gz
```

Alternatively, download a pre-built image from the [`axibase.com`](https://axibase.com/public/docker-axibase-collector.tar.gz).

## Start Container

> Using Collector to monitor Docker? Launch the container in privileged mode as described in the [Docker Job Documentation](./jobs/docker.md#local-installation).

```sh
docker run \
 --detach \
 --publish-all \
 --restart=always \
 --name=axibase-collector \
 axibase/collector:latest
```

To automatically configure a connection to the Axibase Time Series Database add the `-atsd-url` parameter with the ATSD hostname and HTTPS port, by default `8443`, as well as [Collector account](https://axibase.com/docs/atsd/administration/collector-account.html) credentials.

```sh
docker run \
 --detach \
 --publish-all \
 --restart=always \
 --name=axibase-collector \
 axibase/collector:latest \
  -atsd-url=https://username:password@atsd_hostname:8443
```

If the username or password contains a `$`, `&`, `#`, or `!` character, escape the character with backslash `\`.

The password must contain at least **six** (`6`) characters and is subject to certain [requirements](https://axibase.com/docs/atsd/administration/user-authentication.html#password-requirements).

To send data to ATSD at `https://192.0.2.1:8443` as user `john.doe` with the password `password`, specify:

```sh
docker run \
 --detach \
 --publish-all \
 --restart=always \
 --name=axibase-collector \
 axibase/collector:latest \
  -atsd-url=https://john.doe:password@192.0.2.1:8443
```

## Start Container in Privileged Mode

The launch command is different if the Collector container is used to [monitor statistics](./jobs/docker.md#local-installation) from the local Docker Engine.

## Launch Parameters

**Name** | **Required** | **Description**
----- | ----- | -----
`--detach` | Yes | Run container in background and print container id.
`--publish-all` | No | Publish exposed HTTPS port (`9443`) to a random port.
`--restart` | No | Auto-restart policy. **Not supported in all Docker Engine versions.**
`--name` | No | Assign a host-unique name to the container.

To bind the Collector to a particular port instead of a random one, replace `--publish-all` with `--publish 10443:9443`, where the first number indicates an available port on the Docker host.

## Environment Variables

| **Name** | **Required** | **Description** |
|:---|:---|:---|
|`ATSD_SERVICE_HOST` | No | Host where Axibase Time Series Database is installed. |
|`ATSD_SERVICE_PORT_HTTPS` | No | HTTPS port. |
|`ATSD_SERVICE_PORT_TCP` | No | TCP port for [network commands](https://axibase.com/docs/atsd/api/network/). |
|`ATSD_URL` | No | URL (`protocol://host:port`) for the Axibase Time Series Database connection.|
|`COLLECTOR_USER_NAME` | No | Username for the [data collector](https://axibase.com/docs/atsd/administration/collector-rw-account.html) account. |
|`COLLECTOR_USER_PASSWORD` | No | [Password](https://axibase.com/docs/atsd/administration/user-authentication.html#password-requirements) for the data Collector account.|
|`DOCKER_HOSTNAME` | No | Hostname of the Docker host where Axibase Collector container is running.|
|`JAVA_OPTS` | No| Java VM options.<br>By default the Collector starts with option `-Xmx256m` |

To send data to ATSD at `https://192.0.2.1:8443` as user `mary.jones` with the password `password` sending data to ATSD at , specify:

```properties
docker run \
 --detach \
 --publish-all \
 --restart=always \
 --name=axibase-collector \
 --env COLLECTOR_USER_NAME=mary.jones \
 --env COLLECTOR_USER_PASSWORD=password \
 --env ATSD_URL=https://192.0.2.1:8443 \
 axibase/collector:latest
```

To set the maximum Java heap size, specify:

```properties
docker run \
 --detach \
 --publish-all \
 --restart=always \
 --name=axibase-collector \
 --env JAVA_OPTS=-Xmx512m \
 axibase/collector:latest
```

## Check Installation

Initializing the application can take up to five minutes.

```sh
docker exec -it axibase-collector tail -f /opt/axibase-collector/logs/axibase-collector.log
```

The following message indicates that the initial configuration is complete: `FrameworkServlet 'dispatcher': initialization completed.`

## Validation

```sh
docker ps | grep axibase-collector
```

```txt
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                     NAMES
ee15099d9f88        axibase/collector   "/bin/bash /opt/axiba"   33 seconds ago      Up 32 seconds       0.0.0.0:32769->9443/tcp   axibase-collector
```

Note the public HTTPS port assigned to `axibase-collector` container, `32769` in the example above.

## Login

Open `https://docker_hostname:32769` in your browser and create an [administrator account](./configure-administrator-account.md).

`docker_hostname` is the hostname or IP address of the Docker host and `32769` is the external port number assigned to the Collector container in the previous step.

## ATSD Connection Setup

Configure [ATSD Server connection](./atsd-server-connection.md) to send data into an ATSD instance.

## Troubleshooting

Review the log files for any errors:

```sh
docker exec -it axibase-collector tail -n 100 /opt/axibase-collector/logs/axibase-collector.log
```

```sh
docker exec -it axibase-collector tail -n 100 /opt/axibase-collector/logs/err-collector.log
```
