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

### Delivery

The collector implements a file-based cache to temporarily store commands that could not be delivered to the target database due to network and other errors.

The pending commands are retained for the duration of time specified in the **Command Retention Interval** setting on the **Admin > Application Settings** page.

| Name | Description |
|---|---|
| `Command Retention Interval` | Interval after which unsent commands are deleted from file-based collector cache.<br>Default: `86400 seconds` (1 day).<br>Minimum: `60 seconds`.<br>Must exceed the Failover Timeout.<br>Restart is required to apply changes. |

## Failover

Collector supports an automated failover mechanism to ensure uninterrupted data collection.

If the primary database becomes unavailable and the failover driver is specified, Collector switches to the secondary database. While sending data to the secondary database, Collector periodically checks the status of the primary database and switches back once the connectivity is re-established.

The following steps describe the switch-back procedure:

* Collector determines that the current database that it is connected to is a secondary database.
* The collector starts a background periodic task to re-connect to the primary database.
* The default periodic re-connect interval is `300` seconds.
* The periodic re-connect task attempts to connect to the primary server. This task continues until the primary database is online or the collector shuts down.
* If the primary database is available, the collector initiates a switch-back procedure:
  * Sends a message to the secondary database that the collector is now connecting to the primary database.
  * Sets the primary database as the current database.
  * Establishes a connection to the primary database.
  * If the above connection is successful, the periodic re-connect task is stopped.

:::tip Note
The failover mechanism applies only to the storage driver and does not affect delivery of commands by the built-in log aggregator. The log aggregator sends commands only to the primary database.
:::

### Failover Parameters

| Name | Description |
|---|---|
| `Failover Timeout` | Duration of time, starting with the first error, after which the driver switches from the primary to the secondary database.<br>Default: `300 seconds`.<br>Minimum: `15 seconds`. |
| `Failover Switchback Interval` | Interval for checking availability of the primary storage driver. Activated when sending command to the secondary driver in failover mode.<br>Default: `300 seconds`.<br>Minimum: `60 seconds`.<br>Restart is required to apply changes. |

The failover timeout can be specified for each storage driver separately whereas the switch-back interval applies to all drivers and is specified on the **Admin > Application Settings** page.

### Failover Logging

The switch-back procedure states are logged with the following messages, each containing message tags `primary_driver_url` and `secondary_driver_url`.

* Collector fails to send commands to the primary driver and attempts to switch to the secondary driver.

  ```bash
  Failed to send commands to the primary driver. Switching to secondary.
  ```

* Secondary driver is not available.

  ```bash
  Failed to send commands to the primary driver. Failed to connect to the secondary driver. Continue using primary driver.
  ```

* Secondary driver is available.

  ```bash
  Failed to send commands to the primary driver. Switched to secondary driver.
  ```  

* Re-connect procedure started for activated secondary drivers.

  ```bash
  Primary driver re-connect check procedure started.
  ```

* Primary driver validation result.

  ```bash
  Primary driver re-connect check result: ${VALIDATION_RESULT}
  ```

* Secondary storage driver continues to be in active state.

  ```bash
  Primary driver is not available. Continue sending data using secondary driver.
  ```

* Primary driver is available.

  ```bash
  Primary driver is available. Switching from secondary.
  ```

* Switched to primary driver.

  ```bash
  Primary driver is available. Switch from secondary complete.
  ```

* Failed to switch from secondary driver.

  ```bash
  Primary driver is available. Failed to switch from secondary. Continue sending data using secondary driver.
  ```

* Re-connect procedure stopped for all drivers.

  ```bash
  Primary driver re-connect check procedure stopped. All drivers are sending data to primary drivers.
  ```
