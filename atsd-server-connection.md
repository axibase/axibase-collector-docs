# ATSD Server Connection

## Overview

In order for Axibase Collector to function properly, Collector needs to know where to send data collected from remote data sources.

This document describes how to add a storage driver for sending data into ATSD.

## Collector Account

* Create a [collector account](https://axibase.com/docs/atsd/administration/collector-account.html) in ATSD to be used for inserting data into ATSD.

## Connection to ATSD

Since Axibase Collector transmits data to ATSD using the http/https protocol, you need to configure a HTTP connection pool by specifying connection properties, as well as various timeouts and limits.

### Basic Configuration

The configuration page opens after the first login.

* Choose the protocol, which is used to connect to the ATSD installation. `https` is recommended.
* Write the server hostname/IP address of the ATSD installation.
* Choose the server port of the ATSD installation.
* Write the collector account credentials, which are [created previously](#collector-account).

    Ensure that the user has roles `API_DATA_WRITE` and `API_META_WRITE`.
* To check connection press `Validate` button.
* If connection is successfully established, click `Save` button.

![ATSD Configuration Page](./images/atsd_configuration.png)

This configures an **HTTP Pool** (**Data Sources > HTTP Pools**) and a **Storage Driver** (**Admin > Storage Drivers**) for you.

### Advanced Configuration

Press `Skip` button on the configuration page after the first login to proceed to main page.
Configure an **HTTP Pool** and a **Storage Driver** to establish connection to ATSD.

#### HTTP Pool

* Open **Data Sources > HTTP Pools** and click **Add** to arrive at the appropriate form.
* Enter a pool name.
* Set connection parameters to the target ATSD instance: hostname/IP address; port (`8443`); https protocol.
* Check **Ignore SSL Certificate Errors** to ignore certificate errors since ATSD certificate is self-signed by default.
* Apply connection limits using the [recommended settings](#recommended-http-pool-settings) below.
* Select `Authentication Type=BASIC`. Set **Test Path** to `/ping`.
* Enter [collector account](https://axibase.com/docs/atsd/administration/collector-account.html) credentials.

    Ensure that the user has roles `API_DATA_WRITE` and `API_META_WRITE`.

#### Test HTTP Pool

Click **Test** to verify the settings:

* Response code is `200 OK` if the connection is successful and credentials are valid.
* Response code is `401 Unauthorized` if credentials are not valid.
* Response code is `403 Forbidden` if the specified user is not authorized to access the specified **Test Path**.

##### Recommended HTTP Pool Settings

**Setting** | **Value**
----- | -----
Max Connections | `16`
Use Cookies | `false`
Connection Pool Timeout | `15`
Connect Timeout | `15`
Close Idle Connections interval | `60`
Read Timeout | `15`
Socket Linger | `0`
Socket Reuse | `true`
Socket Keep-Alive | `true`

##### ATSD HTTP Pool Configuration Example

![ATSD HTTP Pool](./images/atsd_pool.png)

### Storage Driver Configuration

* Open the **Admin > Storage Drivers** page and click **Add**.
* Choose ATSD HTTP pool configured previously.
* Set **Transport Type** to **HTTP_BATCH**.
* Keep API path as `/api/v1`.
* Click **Test**. ATSD returns response code `200 OK` if the connection is successful.

![ATSD Server Test](./images/atsd_server.png)
