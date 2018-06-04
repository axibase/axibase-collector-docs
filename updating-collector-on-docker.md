# Updating Axibase Collector on Docker

## Download the Latest Axibase Collector Release

The latest release is available at the following [link](https://axibase.com/public/axibase-collector_latest.htm):

```bash
wget -O axibase-collector.tar.gz http://axibase.com/public/axibase-collector-v{revision}.tar.gz
```

If `wget` is not installed, use `curl`:

```bash
curl -o axibase-collector.tar.gz http://axibase.com/public/axibase-collector-v{revision}.tar.gz
```

## Copy Archive to Docker Host

Copy the `axibase-collector.tar.gz` file to the Docker host on which Axibase Collector container is running.

Alternatively, if the Docker host is connected to external networks, you can download the `axibase-collector.tar.gz` directly to the Docker host.

## Unpack Archive

```bash
tar xvf axibase-collector.tar.gz
```

## Stop the Collector Process

Assuming `axibase-collector` is the name of the Collector container to be updated, execute the following command.

```bash
docker exec axibase-collector /opt/axibase-collector/bin/stop-collector.sh
```

> Make sure the container is running when you run the command.

## Replace war File

Copy `axibase-collector.war` into the container to replace the old version:

```bash
docker cp ./axibase-collector/lib/axibase-collector.war axibase-collector:/opt/axibase-collector/lib/
```

## Start the Collector Process

```bash
docker exec axibase-collector /opt/axibase-collector/bin/start-collector.sh
```