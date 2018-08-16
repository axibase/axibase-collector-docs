# Monitoring

Collector sends job status messages to ATSD upon completion, job execution is monitored using the built-in [Rule Engine](https://axibase.com/docs/atsd/rule-engine/).

Job status messages contain the following fields:

Field | Description
---|---
Type | `collector-job`
Source | `job_name`
Severity | `NORMAL` if successful<br>`MAJOR` on `PARTIAL_FAIL`<br>`CRITICAL` in case of `ERROR`
Entity | Collector hostname
Tag `status` | `COMPLETED`<br>`PARTIAL_FAIL`<br>`FAIL`
Tag `job_name` | Unique identifier of executed job.
Tag `job_type` | Protocol of executed job.
Message | Statistics about job performance.<br>Collector includes an error in the message if an error is raised.

Some job types provide an extended set of tags and a modified message:

* [FILE job](./jobs/file.md)
  * **Tag**: [`error type`](./jobs/completion-messages.md)
  * **Message**: `COMPLETED_COUNT=N ERROR_COUNT=N FILE_COUNT=N ROWS_PROCESSED=N`.
    * An error description is included in the message if an error is raised.

## Example

View Message Report in a local Collector instance:

```ls
https://atsd_hostname:8443/messages?type=collector-job&entity=36e26a5fd70a&tags%5B0%5D.key=job_name&tags%5B1%5D.key=job_type&tags%5B2%5D.key=status&interval=1-DAY
```

> Replace `atsd_hostname` with  the hostname or IP address of the target ATSD server.

![Collector Messages](./images/monitoring-1.png)
