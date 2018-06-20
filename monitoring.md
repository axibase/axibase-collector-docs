# Monitoring

Axibase Collector sends job status messages to ATSD upon completion, job execution is monitored using the built-in [Rule Engine](https://axibase.com/docs/atsd/rule-engine/).

Job status messages contain the following fields:

Field | Description
---|---
Type | `collector-job`
Source | `job_name`
Severity | `NORMAL` if okay, `MAJOR` on `PARTIAL_FAIL`, and `CRITICAL` in case of `ERROR`
Entity | Axibase Collector hostname
Tag `status` | COMPLETED, PARTIAL_FAIL, FAIL
Tag `job_name` |
Tag `job_type` |
Message | Completed in `N` ms. Items read: `N`. Commands sent: `N`. The Collector includes an error in the message if an error is raised.

Some job types provide an extended set of tags and a modified message:

* FILE job
  * Tag [`error type`](./jobs/completion-messages.md)
  * Message: Completed in `N` ms. Files read: `N`. Files sent: `N`. <br>Failed requests: `N` COMPLETED_COUNT=N ERROR_COUNT=N FILE_COUNT=N <br> ROWS_PROCESSED=N. An error description is included in the message if an error is raised.

![Collector Messages](./images/collector_messages_atsd.png)
