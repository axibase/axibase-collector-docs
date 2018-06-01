# HTTP

HTTP (Hypertext Transfer Protocol) is the underlying protocol used by the World Wide Web that defines how messages are formatted and transmitted.

## HTTP Job Configuration

Use the table below to create HTTP job configuration.

| Field         | Description |
|:------------- |:-------------|
| Name     | Name of the configuration. |
| HTTP Pool |  Name of one of the configured HTTP pools that you want to use. |
| Path |   Path to target files located on the remote or local file system from which they will be read.  |
| Response Text |  Text that Axibase Collector will look for in the response from the server.   |
| Response Text Match Type |  Defines how Collector will  search for the necessary response text. <br> Possible options: <br>  `CONTAINS` - select this option if you want Collector to search for a partial match. <br>  `EQUALS` - select this option if you want to search for the exact match. <br> `REGEXP` - select this option if you want to use regular expressions for the search. |
| Failure Retest |  Number of attempts to re-establish the connection.   |
| Failure Retest Interval |   Delay between attempts to re-establish connection.    |
| Enable Web Driver |  Defines whether you want to enable the Web Driver tool.  |
| Driver Script | Selenium script. *  |
| Driver Timeout, seconds |  Defines the amount of time the Driver will wait to complete the request before it returns the timeout exception message.*  |
| Driver File Encoding |  Encoding of the file you are requesting with the script. * |

_*These fields become available if you select the Enable Web Driver check box._

### <code>http.status</code> Metric Values Based on HTTP Response Codes

| Metric Value | Response Code |
|:------------- |:-------------|
| 0 | No error. HTTP status = 200. No match configured or response text matched. |
| 1 | ConnectException |
| 2 | NoRouteToHostException |
| 3 | UnknownHostException |
| 4 | SocketTimeoutException |
| 5 | Other exceptions without HTTP response status |
| 200 | HTTP response status = 200, but response text failed to match. |
| xxx | HTTP response status. For example 500 (Server Error). |

### Configuration Example

![HTTP Configuration](./images/httpconfiguration.png)
