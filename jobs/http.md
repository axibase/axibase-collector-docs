# HTTP

HTTP (Hypertext Transfer Protocol) is the underlying protocol used by the World Wide Web that defines how messages are formatted and transmitted.

## HTTP Job Configuration

![](./images/http-job.png)

Use the table below to create an HTTP job configuration.

| Field         | Description |
|:------------- |:-------------|
| Enabled | The job is active and queried data is stored|
| Name     | Name of the HTTP job configuration. |
| `cron` Expression | Run the job on a [`cron`](../scheduling.md#cron-expressions) schedule.
| Item List| Apply the HTTP job to an [Item List](../collections.md#item-lists) `*`.|
| HTTP Pool |  Name of a configured [HTTP pool](../atsd-server-connection.md#http-pool) to use `*`. |
| Path |   Path to target files located on the remote or local file system from which HTTP job reads.  |
| Collect SSL Metrics | Collect SSL certificate expiration and status metrics: `http.ssl_certificate_expiration_days` and `http.ssl_certificate_status`.<br>Possible values: <br>`0`: Valid<br>`1`: Self-signed<br>`2`: Certificate is already expired.<br>`3`: Certificate is not yet valid.<br>`4`: Incorrect hostname.<br>`5`: Failed to retrieve SSL certificate.
String Matching | Define how Collector searches for response text.<br>Possible values:<br>`Contains String`: Search for partial match.<br>`Equals String`: Search for exact match.<br>`Matches String`: Search via regular expression.<br>`Does Not Contain String`: Search those strings which do not contain the target string defined in **Search String**.
Search String | Text for which Collector searches.
Retry Count | Number of attempts to re-establish a lost connection.|
Retry Delay, seconds | Delay between attempts to re-establish a lost connection.
Metric Prefix | Common prefix added to metric names, for example `jmx.activemq`.<br>This field supports the following [placeholders](./placeholders.md):<br>`$(domain)`: Domain of the `mbean`<br>`$(name)`: Value of the `mbean` attribute `name`.<br>`$(type)`: Value of the `mbean` attribute `type`.

> `*` Apply the HTTP job to **either** an Item List or HTTP Pool, but not both.

### `http.status` Metric Values Based on HTTP Response Codes

| Metric Value | Response Code |
|:------------- |:-------------|
| `0` | No error. TCP connection successful. HTTP status code `2xx` or `3xx`. String search succesful, if enabled. |
| `1` | `ConnectException` |
| `2` | `NoRouteToHostException` |
| `3` | `UnknownHostException` |
| `4` | `SocketTimeoutException` |
| `5` | Other exceptions without HTTP status code.|
| `10` | TCP connection successful. HTTP status code `2xx` or `3xx`, but string search failed. |
| `11` | TCP connection successful. HTTP status code other than `2xx`, `3xx`, or `4xx`. |

### Configuration Example

![](./images/http-config-example.png)