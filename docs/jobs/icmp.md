# ICMP Job

ICMP (Internet Control Message Protocol) is one of the main protocols of the TCP/IP suite. It is used by network devices to send error messages or to relay query messages.

## ICMP Job Configuration

| Field       | Description   |
|:-------------|:--------------|
| Configuration Name     | Name of the configuration. |
| Collection     |  Name of the collection you want to use. |
| Metric Name | Name of the metric you want to use. |
| Ping Type | Type of Ping request. |
| Request Timeout, seconds | Time Axibase Collector will wait for the response before the request expires. |
| Failure Retests | Number of attempts to re-establish the connection.  |
| Failure Retest Delay, seconds|  Delay between attempts to re-establish the connection.  |
| ICMP Request TTL, seconds |  Request time to live value in seconds.   |
| Packets Size, bytes | Size of packets to transfer.   |
| IP Version |   Version on IP protocol.  |

### Configuration Example

The image below shows ICMP configuration example.

![ICMP Configuration](./images/icmp_job.png)
