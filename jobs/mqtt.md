# MQTT Job

## Overview

The MQTT job provides a way to continuously read messages from one or multiple topics in an MQTT broker. The messages are parsed as CSV, JSON or plain text and converted into series, property, and message [commands](https://axibase.com/docs/atsd/api/network/) in the Axibase Time Series Database.

## Job Settings

MQTT job settings provide an additional **MQTT Broker** field to configure MQTT broker connection which in turn allows you to select a specific [consumer](./mqtt-broker.md) to use.

![MQTT job settings](./images/mqtt_job_configuration.png)

### Job Configuration

To configure a MQTT job, click **Create Configuration**.
Set parameters as follows.

**Field** | **Description**
----- | -----------
Topic | The topic to subscribe to, which can include wildcards
Payload Format | Message payload format: `CSV`, `JSON`, `TEXT`

## CSV Format

If `CSV` format is selected, the message payload is automatically split into lines and the expression in the **Command Template** field is applied to each line separately.

### Variables

The following variables can be included in the command template and passed to functions:

**Name**| **Description**
---|---
`job` | Current job name.
`configuration` | Current configuration Name.
`topic` | Message source topic.
`receiveTime` | Message delivery in Unix milliseconds.
`host` | Broker host.
`port` | Broker port.
`text` | Message payload, the entire text consisting of all lines.
`line` | Current line in the CSV document.

### Methods

**Name**| **Description**
---|---
`cell(int n)` | `n` - column index, starts with `1` for the first column.<br>Returns the value of `n-th` cell in the current line by index.<br>Returns an empty string if the index is out of range.

### Configuration Example

Sample message payload, consisting of two lines without a header:

```
br-1116,2019-04-16T11:16:59.189Z,,temperature,90.44,pressure,4.0
br-1489,2019-04-16T11:16:59.148Z,,temperature,30.31,pressure,4.6
```

Command template, applied to each line:

```
series d:${cell(2)} e:${cell(1)} t:topic=${topic} m:${cell(4)}=${cell(5)} m:${cell(6)}=${cell(7)}
```

Series commands produced by applying the template to each line:

```
series d:2019-04-16T11:16:59.189Z e:br-1116 t:topic=/test/bioreactor m:temperature=90.44 m:pressure=4.0
series d:2019-04-16T11:16:59.148Z e:br-1489 t:topic=/test/bioreactor m:temperature=30.31 m:pressure=4.6
```

![](./images/mqtt_csv_configuration.png)

Example:

![](./images/mqtt_csv_tes_result.png)

## JSON Format

If `JSON` format is selected, the payload is parsed as a JSON document and the ATSD `series` command [fields](https://axibase.com/docs/atsd/api/network/series.html) are extracted from the named fields in the JSON document.

### Entity Fields

**Name** | **Description**
---| ---
Entity | Entity name, specified literally or extracted from the specific field in the document.
Entity Prefix | Text added to the entity name. For example, if prefix is `custom.`, and the entity field value is `my-host`, the resulting entity name is `custom.my-host`.

### Time Fields

**Name** | **Description**
---| ---
Time Default | Literal time value specified if the JSON document contains no date field.
Time Field   | Name of the JSON field containing the event date.
Time Format  | Date pattern applied when parsing the date.
Time Zone    | Timezone applied if the parsed date is lacking timezone information, otherwise the Collector time zone is in effect.

### Series Fields

**Name** | **Description**
--- | ---
Metric Prefix | Text added to the metric name. See **Entity Name** for reference.
Included Fields | By default, all numeric fields from nested objects are included in the series command as metrics. To override, specify the list of included fields by name, separated by comma.
Excluded Fields | List of particular field names excluded from the command. Applies when **Included Fields** is empty.
Annotation Fields | List of field names whose values are saved as text annotation.

### Configuration Example

![MQTT Configuration Example](./images/mqtt_configuration_json.png)

![MQTT JSON mapping settings](./images/kafka_json_mapping_settings.png)

![](./images/mqtt_json_mapping_result.png)


## TEXT Format

If `TEXT` format is selected, enter an expression in the **Command Template** field to convert message text to an ATSD network command.

### Variables

All variables for `CSV` mode are available in `TEXT` mode as well except the `line` variable.

### Configuration Example

![](./images/mqtt_text_configuration.png)

![](./images/mqtt_text_mapping_result.png)

