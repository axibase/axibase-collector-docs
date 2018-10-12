# MySQL Server

## Overview

This document describes how to collect global status metrics from `performance_schema` introduced in [MySQL](http://www.mysql.com/) `5.7+` for long-term retention and monitoring in Axibase Time Series Database.

The process involves enabling a JDBC job in Axibase Collector to poll a `global_status` table and uploading the counters to ATSD for processing.

## Requirements

* MySQL Server `5.7+`

## Installation Steps

### Create a Read-Only Account in the Target MySQL Server

```sql
CREATE USER 'axibase-ro'@'collector_host' IDENTIFIED BY '********';
GRANT SELECT ON performance_schema.* TO 'axibase-ro'@'collector_host';
FLUSH PRIVILEGES;
```

To allow connection from any IP address, use the wildcard for remote address:

```sql
CREATE USER 'axibase-ro'@'collector_host' IDENTIFIED BY '********';
GRANT SELECT ON performance_schema.* TO 'axibase-ro'@'*';
FLUSH PRIVILEGES;
```

### Allow External Connection to the Database

Modify `mysql.cnf` by setting `bind-address = 0.0.0.0`.

### Import MySQL Server Job into Axibase Collector

* Open the **Jobs** menu and select **Import** from the split-button at the bottom of the screen to upload the [mysql-server-jobs.xml](./mysql-server-jobs.xml) file.

### Configure MySQL Server Database Connection

* Open the **Data Sources > Databases** page and select the `192.0.2.1` database.
* Provide connection parameters to the target MySQL Server database as displayed below:

![](./images/mysql-datasource.png)

* Execute test query to check the connection:

```SQL
SELECT 1
```

* Query result must be `Query OK`.

### Verify Job Configuration

* Open **MySQL Server** job.
* Set **Data Source** to `192.0.2.1`.

![](./images/mysql-jdbc-job.png)

* Choose one of the target ATSD instances if your Collector instance is connected to multiple ATSD servers.
* Save the Job.
* Open each configuration, click **Test** and review output. See [Data Queries](#data-queries) below.

![](./images/test_result.png)

### Schedule the Job

* Open the **JDBC Job** page and click **Run** for the MySQL Server JDBC job.
* Ensure that the job status is **COMPLETED** and **Items Read** and **Sent commands** are greater than 0.

![](./images/test_run.png)

* If there are no errors, set job status to **Enabled** and save the job.

### Verify Metrics in ATSD

* Log in to ATSD.
* Open the **Metrics** tab and filter metrics by name `mysql.*`.

![](./images/mysql-metrics.png)

## Viewing Data in ATSD

### Metrics

* List of collected [MySQL Server metrics](./metric-list.md).

### Entity Groups

* Open the **Settings** menu and select **Entity Groups**.
* Create a new Entity Group, select the **Expression** tab from the **Members** table, and enter the following expression:

```javascript
hasMetric('mysql.global_status.uptime')
```

* Save and verify that the group contains your MySQL database hosts:

![](./images/mysql-entity-group.png)

### Portals

* Open the **Portals** page and import a MySQL portal from [portal-mysql.xml](portal-mysql.xml).
* Click the **Assign** link and associate the portal with the entity group you created earlier.
* Open the **Entities** tabs, find the `mysql` database by name, and click the portal icon.

![](./images/mysql-portal-icon.png)

[**MySQL Server Performance Live Portal**](https://apps.axibase.com/chartlab/cf72dec3)
![](./images/mysql-portal.png)

## Data Queries

* Metrics Queries select most recent statistics:

```SQL
SELECT * FROM performance_schema.global_status
```
