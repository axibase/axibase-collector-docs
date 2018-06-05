# Axibase Collector

## Overview

Axibase Collector is a Java-based ETL application that queries external data sources on a defined schedule and uploads the data as series, properties, messages, and files into the [Axibase Time Series Database](https://axibase.com/docs/atsd/) (ATSD).

The Collector supports data markers to minimize the load on the source systems as well as [list](collections.md)-based automation to efficiently copy data from multiple sources with re-usable configurations.

## Use Cases

* Download a CSV/TSV file from a URL or an FTP server and upload it into ATSD.
* Offload data from a relational database for long-term storage in ATSD.
* Query a web service, convert its JSON output into tabular format, and upload it into ATSD.
* Historize metrics by querying current values and retaining their history in ATSD.
* Collect key performance metrics from Java applications (JMX), network devices (SNMP), etc.

## Supported Databases

* Oracle
* IBM DB2
* Microsoft SQL Server
* MySQL
* PostgreSQL
* Sybase
* Apache Derby
* Vertica
* ATSD
* SAP HANA
* OSISoft PI Data Archive
* OSISoft PIOleDBEnt
* Custom

## Supported Data/Network Protocols

* JDBC
* SNMP
* JMX
* ICMP
* TCP
* HTTP

## Supported File Formats

* CSV
* TSV
* Text
* JSON

## Supported Schemas

* [Open Data/SOCRATA](https://project-open-data.cio.gov/v1.1/schema/)

## Supported APIs

* Kafka
* Amazon Web Services CloudWatch
* Docker Engine
* HP OVPM (Performance Manager)

## Installation

* [Requirements](requirements.md)
* Installation:
  * Installation on [host](installation.md)
  * Installation in [Docker container](installation-on-docker.md)
  * Installation on [Kubernetes](installation-on-kubernetes.md)
* [Administrator Account](configure-administrator-account.md)
* [Collector account](https://axibase.com/docs/atsd/administration/collector-account.html) in ATSD
* [ATSD Server Connection](atsd-server-connection.md)

## Jobs

* [Overview](job-generic.md)
* [Scheduling](scheduling.md)
* [Monitoring](monitoring.md)

## Automation

* [Item Lists](collections.md)

## Job Types

**Type** | **Description**
----- | -----
[AWS](jobs/aws.md) | Collects AWS statistics using CloudWatch API.
[Docker](jobs/docker.md) | Collects container, image, and volume statistics using Docker Engine API.
[File](jobs/file.md) | Downloads CSV/TSV files from remote servers or local file system and uploads them into ATSD for parsing.<br>Supports HTTP/s, FTP, SFTP, SCP, and FILE protocols.
[HTTP](jobs/http.md) | Executes HTTP requests or Web Driver scripts and stores response status and response times as metrics.
[ICMP](jobs/icmp.md) | Pings hostnames/IP addresses and stores response status.
[JDBC](jobs/jdbc.md) | Executes SQL queries against relational databases.<br>Converts rows into series,  property, or message commands.
[JMX](jobs/jmx.md) | Collects MBean attribute values from Java applications.
[JSON](jobs/json.md) | Downloads JSON files, parses the documents and converts JSON fields into series, property, and message commands using JSONPath.
[Kafka](jobs/kafka.md) | Reads JSON messages from Kafka brokers, parses the messages and converts them into series, property, and message commands.
[OVPM](jobs/ovpm.md) | Offloads statistics from HP OpenView Performance Manager.
[PI](jobs/pi.md) | Extracts PI points archive data via JDBC driver.
[SNMP](jobs/snmp.md) | Queries SNMP devices using built-in and custom MIB files.
[Socrata](jobs/socrata.md) | Downloads JSON documents published in Socrata schema and converts them into series, property, and message commands.
[TCP](jobs/tcp.md) | Connects to hostnames/IP addresses and stores connection status.

## Administration

* [Monitoring](monitoring.md)
* [Logging](logging.md)

## Examples

**Name** | **Job Type** | **Description**
----- | ----- | ----
[ActiveMQ](jobs/examples/activemq) | JMX | Collect metrics about brokers, queues, pub/sub topics
[Derby Database](jobs/examples/derby) | JMX | Collect uptime metrics for the database
[File](jobs/examples/file) | File | Download CSV files
[HP OpenView](jobs/examples/hp-openview) | OVPM | Offload CODA metrics from OVPM
[Jetty](jobs/examples/jetty) | JMX | Collect sessions, requests, status from the Jetty server
[JSON](jobs/examples/json) | JSON | Download JSON file and convert it to CSV format
[JVM](jobs/examples/jvm) | JMX | Collect key JVM performance metrics
[MySQL](jobs/examples/mysql) | JDBC | Collect database performance metrics
[nginx](jobs/examples/nginx) | File | Collect key web server metrics for nginx
[nginx-plus](jobs/examples/nginx-plus) | File | Collect extended web server metrics for nginx-plus
[Oracle EM](jobs/examples/oracle-enterprise-manager) | JDBC | Offload incremental database and application metrics collected by Oracle EM
[PI](jobs/examples/pi) | PI | Copy incremental tag values from PI Data Archive
[PostgreSQL](jobs/examples/postgres) | JDBC | Collect database performance metrics
[SCOM](jobs/examples/scom) | JDBC | Offload incremental server metrics collected by SCOM
[Socrata](jobs/examples/socrata/state-government.md) | Socrata | Download and parse datasets published in Socrata format
[SolarWinds](jobs/examples/solarwinds) | JDBC | Offload incremental network and server metrics collected by SolarWinds
[Tomcat](jobs/examples/tomcat) | JMX | Collect key container metrics exposed by Tomcat
[VMware](jobs/examples/vmware) | JDBC | Offload incremental cluster, host, VM metrics collected by VMware vCenter
