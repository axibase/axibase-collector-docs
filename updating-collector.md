# Updating Axibase Collector

## Download the Latest Axibase Collector Release

The latest release is available from the [Axibase Downloads](https://axibase.com/public/axibase-collector_latest.htm) page:

```bash
wget -O axibase-collector.tar.gz http://axibase.com/public/axibase-collector-v{revision}.tar.gz
```

## Copy Archive

Copy the `axibase-collector.tar.gz` file to the server where Axibase Collector is running.

## Switch User

Switch to the user under which Collector java processes execute.

To look up the Axibase Collector installation directory, run:

```bash
axibase@36e26a5fd70a:~$ ps aux | grep "axibase-collector.war"
axibase  25647 27.0  0.9 8037420 625988 ?      Sl   07:23   6:53 java -XX:PermSize=128m ...
```

```bash
su axibase
```

## Unpack Archive

```bash
tar xvf axibase-collector.tar.gz
```

## Stop the Collector Process

To look up Axibase Collector installation directory, run:

```sh
axibase@36e26a5fd70a:~$ ps aux | grep "axibase-collector.war"
axibase  25647 27.0  0.9 8037420 625988 ?      Sl   07:23   6:53 java -XX:PermSize=128m ...
-Dlogback.configurationFile=/opt/axibase-collector/conf/logback.xml ...
```

The installation directory is `/opt/axibase-collector` in the above example.

```bash
/opt/axibase-collector/bin/stop-collector.sh
```

## Replace axibase-collector.war File

Replace `/opt/axibase-collector/lib/axibase-collector.war` with the version contained in the archive:

```bash
cp ./axibase-collector/lib/axibase-collector.war /opt/axibase-collector/lib/
```

## Start the Collector Process

```sh
/opt/axibase-collector/bin/start-collector.sh
```

## Updating Collector on Docker

Follow the steps outlined in the following brief [Update Guide](updating-collector-on-docker.md).
