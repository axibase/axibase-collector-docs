# Tomcat Servlet Container

## Overview

This document describes how to collect JMX metrics exposed by [Apache Tomcat](http://tomcat.apache.org/) Servlet Containers  for long-term retention and monitoring in Axibase Time Series Database.

## Requirements

* Apache Tomcat `6+`

## Installation Steps

### Enable JMX in Java Application

Configure your Java for JMX monitoring as described by the [JMX Job Documentation](../../jmx.md).

### Import Tomcat job into Axibase Collector

* On the **Jobs** page, select **Import** from the split button below the table and upload the job file depending on the version of your servlet container engine:
* [Catalina](configs/tomcat_catalina_job.xml)
* [Standalone](configs/tomcat_standalone_job.xml)

### Configure Tomcat JMX Connection

* Open the **Jobs > JMX** page and select the `jmx-tomcat` job.
* For each JMX Configuration:
  * Provide connection parameters to the target Tomcat:

![](./images/tomcat_jmx_configuration.png)

* Click **Test** and make sure that the result is similar to the below screenshot:

![](./images/tomcat_test_jmx_configuration.png)

### Schedule the Job

* Open the **JMX Job** page and click **Run** for the Tomcat JMX job.
* Make sure that the job status is **COMPLETED** and **Items Read** and **Sent commands** are greater than 0.

![](./images/test_run.png)

* If there are no errors, set job status to **Enabled** and save the job.

### Verify Metrics in ATSD

* Log in to ATSD.
* Click on the **Metrics** tab and filter metrics by name `jmx.tomcat*`.

![](./images/tomcat_metrics.png)

## Viewing Data in ATSD

### Metrics

* List of collected [Tomcat metrics](metric-list.md)

### Properties

* List of collected [Tomcat properties](properties-list.md)

### Entity group

* Open the **Settings** menu and select **Entity Groups**, click **Import**, and upload  [`tomcat_entity_group.xml`](configs/tomcat_entity_group.xml).
* Select the imported `apache-tomcat` group.
* Verify that the group contains your Tomcat hosts.

### Entity Views

* Open the **Entity Views** menu and select **Configure**, click **Import**, and upload  [`tomcat_entity_view.xml`](configs/tomcat_entity_view.xml).
* Select the imported **Apache Tomcat Containers** view.
* Select the Entity Group that you created earlier.
* Click **View** and browse information about your entities:

![](./images/tomcat_entity_view.png)

### Portal

* Open the **Portals** menu and select **Configure**, click **Import** from the split button below the table, and upload [`tomcat_portal.xml`](configs/tomcat_portal.xml).
* Click the **Assign** link and associate the portal with the entity group created earlier.
* Open the **Entities** tabs, find the java application by name, and the **Portal** icon.

![](./images/tomcat_portal_icon.png)

[**Tomcat Portal**](http://apps.axibase.com/chartlab/106bddba)

![](./images/tomcat_portal.png)
