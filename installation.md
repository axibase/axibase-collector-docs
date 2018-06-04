# Axibase Collector Installation

## Quick Start

For a quick installation of pre-integrated Axibase Collector and ATSD instances in a single Docker container, refer to the [ATSD Sandbox](https://github.com/axibase/dockers/tree/atsd-sandbox#overview) guide.

## Install Java 8 JDK

### OpenJDK on Ubuntu or Debian

```sh
sudo apt-get update
sudo apt-get install openjdk-8-jdk
```

### OpenJDK on RHEL, SLES, CentOS

```sh
sudo yum install java-1.8.0-openjdk-devel
```

### Oracle JDK

Download Java 8 JDK from the [Oracle web site](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html).

```sh
sudo rpm -i jdk-8u131-linux-x64.rpm
```

## Verify Java Installation

Verify that the `java` command displays version 1.8.x.

```sh
java -version
```

## Install

Download Axibase Collector [archive](https://axibase.com/public/axibase-collector_latest.htm).

Replace `${VERSION}` placeholder in the command below with the specific version number, for example `19111`. Extract the archive.

```sh
tar xvf axibase-collector-v${VERSION}.tar.gz
```

## Check Ports

Check that port `9443` is available. If the port is available, output of this command should be blank.

```sh
sudo netstat -tulnp | grep "9443"
```

If port `9443` is taken by another processes, open the `start-collector.sh` script and set a custom port:

```sh
nano ./axibase-collector/bin/start-collector.sh
COLLECTOR_OPTS="-httpsPort=10443"
```

## Start Collector

```sh
./axibase-collector/bin/start-collector.sh
```

It may take up to 5 minutes for collector to initialize.

## Check Installation

Check the collector log file for the message FrameworkServlet 'dispatcher': initialization completed.

```sh
tail -f ./axibase-collector/logs/axibase-collector.log
```

## Login

Open `https://hostname:9443` in your browser and [configure](configure-administrator-account.md) an administrator account.

## Setup ATSD connection

Configure Axibase Collector to send data into an Axibase Time Series Database instance.

* [ATSD Server connection](atsd-server-connection.md)

## Stopping Axibase Collector

In order to stop Axibase Collector, execute the following command:

```sh
./axibase-collector/bin/stop-collector.sh
```