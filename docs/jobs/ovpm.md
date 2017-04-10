# OVPM Job
OVPM protocol is used to retrieve data from the HP OpenView Performance Manager.
#### Job Settings
Apart from the general job settings that are specified in the [Axibase Collector Jobs](../job-generic.md), OVMP job has an additional job-specific parameter. <br>

**Max. serial errors threshold** - defines the maximum amount of consecutive errors after which no more queries will be sent.

![](https://axibase.com/wp-content/uploads/2015/08/ovpm_settings.png)

#### OVPM Configuration
To configure an OVPM job, click Create OVPM configuration.
Use the table below to set configuration parameters.

| Field        | Description           |
|:------------- |:--------------|
|  Name    | Configuration name.   |
| HTTP Pool  | Data source. |
| Path  | 	Relative path to OVPM CSV endpoint. |
| OVPM encoding | 	Character set that is used to parse the resulting data. |
| Interval  | Data interval that will be downloaded. |
| Query With Time  | When executing the job, the server will be set to the maximum time of the previous data. |
| Time Zone | Time zone in which the data is collected. |
| Max Rows Per Request  | Maximum amount of rows that will be retrieved.  |
| Data Refresh Interval, seconds | OVPM sampling interval. |
| Error Threshold  | Amount of error requests after which no more queries will be sent. |
| Error Delay Interval, seconds  | Interval during which the current entity will be excluded from queries, in the case that there are previous errors.  |
| Entity Group | List of hosts, entity groups created in Axibase Collector. |
| Batch Entities  | Defines the number of entities grouped in one query. |
| Tag Columns | Columns containing tags. |
|  Metrics | List of metrics that will be collected. |
| Put Type  | Type of data: metric, property, or both. |
| Default Property Type  | Default property type. |
| Property Type Column  | Column containing the property types. |
| Property Keys Columns  | Columns containing the property keys. |
| Property Values Columns  | Columns containing the property values. |

![](https://axibase.com/wp-content/uploads/2016/03/ovpm_config.png)
