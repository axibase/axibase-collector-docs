# Jetty Web Server

## Overview

This document describes how to collect JMX metrics exposed by [Jetty (Web server)](http://www.eclipse.org/jetty/) for long-term retention and monitoring in Axibase Time Series Database.

## Requirements

* Jetty 6.+

## Installation Steps

### Enable JMX in Java Application

Configure your Java application for JMX monitoring as described [here](../../jmx.md).

### Import Jetty job into Axibase Collector

* Open **Jobs:Import** and upload the [jetty-job.xml](configs/jetty_job.xml) file.

### Configure Jetty JMX Connection

* Open the **Jobs:JMX** page and select the `jmx-jetty` job.
* For each JMX Configuration:
* Provide connection parameters to the target Jetty:

![](./images/jetty_jmx_configuration.png)

* Click the [Test] button and make sure that the result is correct:

![](./images/jetty_test_jmx_configuration.png)

### Schedule the Job

* Open the `JMX Job` page and click the [Run] button for the Jetty JMX job.
* Make sure that the job status is `COMPLETED` and `Items Read` and `Sent commands` are greater than 0.

![](./images/test_run.png)

* If there are no errors, set job status to 'Enabled' and save the job.

### Verify Metrics in ATSD

* Log in to ATSD.
* Click on Metrics tab and filter metrics by name `jmx.jetty*`.

![](./images/jetty_metrics.png)

## Viewing Data in ATSD

### Metrics

* List of collected [Jetty metrics](metric-list.md).

### Properties

* List of collected [Jetty properties](properties-list.md).

### Entity Group

* Open **Admin:Entity Groups**, click the [Import] button, and upload  [jetty_entity_group.xml](configs/jetty_entity_group.xml).
* Select the imported `jetty-web-server` group.
* Verify that the group contains your Jetty hosts.

### Entity Views

* Open **Configuration:Entity Views**, click the [Import] button, and upload  [jetty_entity_view.xml](configs/jetty_entity_view.xml).
* Select the imported `Java Applications` view.
* Select the Entity Group that you created earlier.
* Click on the [View] button and browse information about your entities.

![](./images/jetty_entity_view.png)

### Portal

* Open the **Configuration: Portals**, click the [Import] button, and upload [jetty_portal.xml](configs/jetty_portal.xml).
* Click the Assign link and associate the portal with the entity group you created earlier.
* Open Entity tabs, find the java application by name, and click on its portal icon.

![](./images/jetty_portal_icon.png)

[**Jetty Live Portal**](http://apps.axibase.com/chartlab/4bcd2299)
![](./images/jetty_portal.png)
