# Monitoring

Collector sends job status messages to ATSD upon completion which contain the following fields:

Field | Description
---|---
Type | `collector-job`
Source | `job_name`
Severity | `NORMAL` if successful<br>`MAJOR` on `PARTIAL_FAIL`<br>`CRITICAL` in case of `ERROR`
Entity | Collector hostname.
Tag `job_name` | Job name.
Tag `status` | `COMPLETED`, `PARTIAL_FAIL`, `FAIL`
Tag `job_type` | Job type, such as `FILE`, `JDBC`, `JSON`, etc.
Message | Job result  summary or error details if the job completed encountered an execution error.

Some job types provide an extended set of tags, for example [`error type`](./jobs/completion-messages.md) reported by the [`FILE`](./jobs/file.md) job.

Job execution can be monitored using the built-in [Rule Engine](https://axibase.com/docs/atsd/rule-engine/) in ATSD.

## Example

Collector sends job completion messages to the primary ATSD instance which can be viewed on the **Message Search** page under `collector-job` type or by accessing the following link.

```ls
https://atsd_hostname:8443/messages?type=collector-job&entity=36e26a5fd70a&tags%5B0%5D.key=job_name&tags%5B1%5D.key=job_type&tags%5B2%5D.key=status&interval=1-DAY
```

> Replace `atsd_hostname` with  the hostname or IP address of the target ATSD server.

![Collector Messages](./images/monitoring-1.png)
