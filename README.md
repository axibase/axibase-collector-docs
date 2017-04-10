# Axibase Collector

## Overview

Axibase Collector is a Java-based ETL application that queries external data sources on schedule and uploads received data as series, properties, messages, and files into the Axibase Time Series Database.

The Collector supports [collections](/docs/collections.md)-based automation to efficiently cope data from multiple sources with the same re-usable configuration.

## Typical Use Cases

* Download CSV/TSV file from a URL or an FTP server and upload it into ATSD.
* Query a web service, convert its JSON output into tabular format, and upload it into ATSD.
* Historize metrics by querying their current values and storing them in ATSD for analytics.
* Offload prunable data from relational databases for long-term storage in ATSD.
* Collect real-time performance metrics from Java applications (JMX), network devices (SNMP), etc.

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

* [Open Data](https://project-open-data.cio.gov/v1.1/schema/) (aka Socrata)

## Supported APIs

* Amazon Web Services CloudWatch
* Docker Engine
* HP OVPM (Performance Manager)
* OSISoft PI DataArchive
* OSISoft PIOLEDBEnt

## Installation

* [Requirements](/docs/requirements.md)
* Installation:
  - Installation on [host](/docs/installation.md)
  - Installation in [Docker container](/docs/installation-on-docker.md)
* [Administrator Account](/docs/configure-administrator-account.md)
* [Collector account](https://github.com/axibase/atsd/blob/master/docs/administration/collector-account.md) in ATSD
* [ATSD Server Connection](/docs/atsd-server-connection.md)

## Jobs

* [Overview](/docs/job-generic.md)
* [Scheduling](/docs/scheduling.md)
* [Monitoring](/docs/monitoring.md)

## Automation

* [Item Lists](/docs/collections.md)

## Job Types

**Type** | **Description**
----- | -----
[AWS](/docs/jobs/aws.md) | Collects AWS statistics using CloudWatch API.
[Docker](/docs/jobs/docker.md) | Collects container, image, and volume statistics using Docker Engine API.
[JDBC](/docs/jobs/jdbc.md) | Executes SQL queries against relational databases.<br>Converts rows into series,  property, or message commands.
[File](/docs/jobs/file.md) | Downloads CSV/TSV files from remote servers or local file system and uploads them into ATSD for parsing.<br>Supports HTTP/s, FTP, SFTP, SCP, and FILE protocols.
[JSON](/docs/jobs/json.md) | Downloads JSON files, parses the documents and converts JSON fields into series, property, and message commands using JSONPath.
[Socrata](/docs/jobs/socrata.md) | Downloads JSON documents published in Socrata schema and converts them into series, property, and message commands.
[JMX](/docs/jobs/jmx.md) | Collects MBean attribute values from Java applications.
[HTTP](/docs/jobs/http.md) | Executes HTTP requests or Web Driver scripts and stores response status and response times as metrics.
[ICMP](/docs/jobs/icmp.md) | Pings hostnames/IP addresses and stores response status.
[OVPM](/docs/jobs/ovpm.md) | Offloads statistics from HP OpenView Performance Manager.
[SNMP](/docs/jobs/snmp.md) | Queries SNMP devices using built-in and custom MIB files.
[TCP](/docs/jobs/tcp.md) | Connects to hostnames/IP addresses and stores connection status.
