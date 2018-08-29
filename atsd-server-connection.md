# Storage Driver Configuration

## Overview

Data retrieved by Axibase Collector from external data sources is persisted by Collector in one or multiple ATSD databases, configured on the **Admin > Storage Drivers** page.

By default, all jobs running in Collector transmit data into the same ATSD instance using a single shared storage driver.

![](./images/storage-driver-basic.png)

The storage driver sends data into ATSD over HTTP protocol.

Via advanced configuration, each job can store data in a specific ATSD instance by using multiple storage drivers.

![](./images/storage-driver-advanced.png)

## Requirements

To store data in a specific ATSD instance, Collector uses a restricted user account defined in the target ATSD instance and authorized to write data and metadata for all or specific entities.

Create a [Collector account](https://axibase.com/docs/atsd/administration/collector-account.html) on the **Settings > User Accounts** page in the ATSD web interface.

## Initial Configuration

If no storage driver is configured for an ATSD instance, the database prompts you to create one upon login.

* Specify hostname or IP address of the target ATSD server.
* Specify `https` service port address, default port is `8443`.
* Enter [Collector account](https://axibase.com/docs/atsd/administration/collector-account.html) credentials.
* Click **Validate** to verify settings. In case of permission errors, ensure that specified Collector account has both `API_DATA_WRITE` and `API_META_WRITE` roles.
* Upon successful validation, click **Save** to create the storage driver. Collector automatically creates an HTTP connection pool and storage driver based on submitted settings.

![ATSD Configuration Page](./images/atsd_configuration.png)

## Storage Driver

Storage drivers are listed on the **Admin > Storage Drivers** page.

To create a new storage driver, open the **Storage Drivers** page and click **Add**.

Choose an existing [HTTP connection pool](#http-pool) from the **HTTP Pool** drop-down list or create a new pool by clicking ![](./images/plus-icon.png).

For a high-availability configuration, specify a [failover driver](#failover-driver) to deliver commands to a secondary ATSD database while the primary database is not available.

Click **Test** to verify settings.

![](./images/storage-driver-test.png)

If Collector contains multiple storage drivers, each unique job can be configured to send collected data into a specific ATSD instance.

![](./images/job-storage-driver.png)

## HTTP Pool

The Collector transmits data into ATSD via HTTP protocol. HTTP connection pool settings contain limits and timeouts which apply to HTTP connections initiated by Collector when sending data into ATSD.

### Create a New Pool

* Open the **Data Sources > HTTP Pools** page from the top menu and click **Add**.
* Enter a pool name.
* Enter hostname or IP address of the target ATSD server.
* Specify port `8443` and select `https` protocol.
* Clear **Ignore SSL Certificate Errors** if the target ATSD [SSL Certificate](https://axibase.com/docs/atsd/administration/ssl-ca-signed.html) is **trusted** (not self-signed).
* Set timeouts and limits based on the [recommended settings](#recommended-pool-settings) below.
* Select `Authentication Type=BASIC`, enter [Collector account](https://axibase.com/docs/atsd/administration/collector-account.html) credentials.
* Set **Test Path** to `/ping`.
* Click **Test** to verify settings.

If the settings are valid, the test returns `200 OK` status.

In case of `4xx` status codes, refer to [ATSD Authentication Codes](https://axibase.com/docs/atsd/administration/user-authentication.html#authentication-and-authorization-errors) for troubleshooting.

Sample HTTP Pool used by storage driver:

![ATSD HTTP Pool](./images/storage-driver-pool.png)

### Recommended Pool Settings

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

## Failover Driver

Collector supports an automated failover mechanism to ensure uninterrupted delivery of data.

If the primary database becomes unavailable and the `atsd-url-secondary` parameter is set, Collector switches to the secondary database. While sending data to the secondary database, Collector periodically checks the status of the primary database and switches back once the connectivity is re-established.

The following steps describe the switch-back procedure:

* Collector determines that the current database that it is connected to is a secondary database.
* The collector starts a background periodic task to re-connect to the primary database.
* The periodic re-connect interval is 5 minutes.
* The periodic re-connect task attempts to connect to the primary server. This task continues until the primary database is online or the collector shuts down.
* If the primary database is available, the collector initiates a switch-back procedure:
  * Sends a message to the secondary database that the collector is now disconnecting and specifying the URL of the primary database.
  * Sets the primary database as the current database.
  * Establishes a connection to the primary database.
  * If the above connection is successful, the periodic re-connect task is stopped.

> The failover mechanism applies only to the storage driver and does not affect delivery of commands by the built-in log aggregator. The log aggregator sends commands only to the primary database.
  
### Logging Switch-Back procedure

The switch-back procedure states are logging with the message templates:

| State | Message template |
| --- | --- |
| Job executor can't be send the batch of commands and switches to failover driver | Trying send collected data using Failover Driver `${DRIVER_URL}` |
| No drivers for procedure | Storage driver switch procedure: there is no storage drivers to check |  
| Scheduled procedure is started for storage drivers that has failover drivers | Storage driver switch procedure: procedure is started for following drivers: `${LIST_OF_DRIVER_URLS}` |
| Storage driver validation | Storage driver switch procedure: validation of storage driver `${DRIVER_URL}` finished with result: `${VALIDATION_RESULT}` |
| Storage driver switched back to primary ATSD | Storage driver switch procedure: storage Driver `${DRIVER_URL}` successfully switched back to primary |
| Storage driver continues to use failover driver| Storage driver switch procedure: storage Driver `${DRIVER_URL}` successfully switched back to primary |
| Storage driver switches to use failover driver | Storage driver switch procedure: storage Driver `${DRIVER_URL}` switches to use failover driver `${DRIVER_URL}`|
| Scheduled procedure finishes for all drivers | Storage driver switch procedure: procedure is completed |
