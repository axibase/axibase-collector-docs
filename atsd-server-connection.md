# Storage Driver Configuration

## Overview

Data retrieved by Axibase Collector from external data sources is persisted by the Collector in one or multiple ATSD databases configured on the **Admin > Storage Drivers** page.

In the basic configuration all jobs running in the Collector transmit data into the same ATSD instance using a single shared storage driver.

![](./images/storage-driver-basic.png)

The storage driver sends data into ATSD over the HTTP protocol.

In the advanced mode each job stores data in a specific ATSD instance using multiple storage drivers.

![](./images/storage-driver-advanced.png)

## Requirements

To store data in a particular ATSD instance, the Collector must use a restricted user account, defined in the target ATSD instance, authorized to write data and metadata for all or specific entities.

The [collector account](https://axibase.com/docs/atsd/administration/collector-account.html) can be created on the **Settings > User Accounts** page in the ATSD web interface.

## Initial Configuration

If the storage driver is not yet configured, the user is asked to create a storage driver on initial login into the Collector.

* Specify the hostname or IP address of the target ATSD server.
* Specify `https` service port address. The default is `8443`.
* Enter the [collector account](https://axibase.com/docs/atsd/administration/collector-account.html) credentials.
* Click **Validate** to verify settings. In case of permission errors, ensure that the collector account has both `API_DATA_WRITE` and `API_META_WRITE` roles.
* If validation is successful, click **Save** to create the storage driver. The collector will automatically create an HTTP connection pool and a storage driver based on the submitted settings.

![ATSD Configuration Page](./images/atsd_configuration.png)

## Storage Driver

The storage drivers are listed on the **Admin > Storage Drivers** page.

To create a new storage driver, open the **Storage Drivers** page and click **Add**.

Choose an [HTTP connection pool](#http-pool) from the **HTTP Pool** drop-down list. Open the pool or create a new pool, if necessary, by clicking on the plus icon.

Click **Test** to verify settings.

![](./images/storage-driver-test.png)

If the Collector has multiple storage drivers defined, each job can be configured to send collected data into a specific ATSD instance.

![](./images/job-storage-driver.png)

## HTTP Pool

The Collector transmits data into ATSD via the HTTP protocol. The HTTP connection pool settings contain various limits and timeouts applied to HTTP connections initiated by Collector when sending data into ATSD.

### Creating New Pool

* Open the **Data Sources > HTTP Pools** page in the top menu and click **Add**.
* Enter a pool name.
* Enter the hostname or IP address to the target ATSD server.
* Select `8443` port and the `https` protocol.
* Uncheck **Ignore SSL Certificate Errors** if the target ATSD [SSL certificate](https://axibase.com/docs/atsd/administration/ssl-ca-signed.html) is trusted (not self-signed).
* Set timeouts and limits based on the [recommended settings](#recommended-pool-settings) below.
* Select `Authentication Type=BASIC`, enter [collector account](https://axibase.com/docs/atsd/administration/collector-account.html) credentials.
* Set **Test Path** to `/ping`.
* Click **Test** to verify settings.

If the settings are valid, the test displays `200 OK` status.

In case of `4xx` status codes, refer to [ATSD Authentication Codes](https://axibase.com/docs/atsd/administration/user-authentication.html#authentication-and-authorization-errors) for more details.

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