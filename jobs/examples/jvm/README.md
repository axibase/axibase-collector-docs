# Java Virtual Machine

## Overview

This document describes how to collect JMX metrics exposed by Java applications for long-term retention and monitoring in Axibase Time Series Database.

This integration enables both performance monitoring (garbage collection, load, threads, heap/offheap memory), availability monitoring (system uptime counter), as well as configuration tracking by notifying any changes in the system properties.

## Requirements

* JRE/JDK 6+

## Installation Steps

### Enable JMX in Java Application

Configure your Java application for JMX data collection as described [here](../../jmx.md).

### Import JVM Job into Axibase Collector

* Open **Jobs:Import** and upload the [jmx-jvm-job.xml](configs/jvm_job.xml) file.

### Configure JMV JMX Connection

* Open the **Jobs:JMX** page and select the `jmx-jvm` job.
* For each JMX Configuration:
* Provide connection parameters to the target JVM:

![](./images/jvm_jmx_configuration.png)

* Click the [Test] button:

![](./images/jvm_test_jmx_configuration.png)

### Schedule the Job

* Open the `JMX Job` page and click the [Run] button for the JVM JMX job.
* Make sure that the job status is `COMPLETED` and `Items Read` and `Sent commands` are greater than 0.

![](./images/test_run.png)

* If there are no errors, set the job status to 'Enabled' and save the job.

### Verify Metrics in ATSD

* Log in to ATSD.
* Click on Metrics tab and filter metrics by name `jmx.jvm*`.

![](./images/jvm_metrics.png)

## Viewing Data in ATSD

### Metrics

* List of collected [JVM metrics](metric-list.md).

### Properties

* List of collected [JVM properties](properties-list.md).

### Entity group

* Open **Admin:Entity Groups**, click the [Import] button, and upload  [jvm_entity_group.xml](configs/jvm_entity_group.xml).
* Select the imported `java-virtual-machine` group.
* Verify that the group contains your JVM hosts.

### Entity Views

* Open **Configuration:Entity Views**, click the [Import] button, and upload  [jvm_entity_view.xml](configs/jvm_entity_view.xml).
* Select the imported `Java Applications` view.
* Select the Entity Group that you created earlier.
* Click on the [View] button and browse information about your entities:

![](./images/jvm_entity_view.png)

### Portal

* Open **Configuration: Portals**, click the [Import] button, and upload [jvm_portal.xml](configs/jvm_portal.xml).
* Click the Assign link and associate the portal with the entity group you created earlier.
* Open the Entity tab, find the java application by name, and click on its portal icon:

![](./images/jvm_portal_icon.png)

[**JVM Live Portal**](http://apps.axibase.com/chartlab/e6911d9d)
![](./images/jvm_portal.png)

### Rules

### Setting up Mail Client

* Configure [Mail Client](https://axibase.com/docs/atsd/administration/mail-client.html).

#### Import Rules

* Open the **Configuration: Rules** page, click the [Import] button, and upload [jvm_rules.xml](configs/jvm_rules.xml).
* For each created rule: open it in the Rule Editor and change recipient address on the *Email Notifications* tab.
* These rules will automatically apply to all JVM based applications monitored by Axibase Collector.

Imported rules:

| **Rule** |  **Description** |
| :--- | :--- |
| jvm_application_restart | Raise an alert when an application has been restarted less than 5 minutes ago.  |
| jvm_cpu_load | Raise an alert when an application cpu load exceeds the set threshold. |
| jvm_garbage_collection_rate |  Raise an alert when an application Garbage Collector rate exceeds the set threshold. |
| jvm_garbage_collection_time |   Raise an alert when an application Garbage Collector time exceeds the set threshold. |
| jvm_heap_memory_usage | Raise an alert when an application heap memory usage exceeds the set threshold. |
| jvm_runtime_property_changed | Raise an alert when an application property is changed. |
| jvm_system_load | Raise an alert when an application system load exceeds the set threshold. |

To create your own rules, refer to [Rule Engine documentation](https://axibase.com/docs/atsd/rule-engine/).
