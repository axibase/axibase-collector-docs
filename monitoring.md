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
Tag `job_name` |
Tag `job_type` |
Message | **Message Text**: Completed in `n` ms. Items read: `n`. Commands sent: `n`.<br>Collector includes an error in the message if an error is raised.

Some job types provide an extended set of tags and a modified message:

* [FILE job](./jobs/file.md)
  * Tag: [`error type`](./jobs/completion-messages.md)
  * Message: Completed in `N` ms. Files read: `N`. Files sent: `N`. <br>Failed requests: `N` `COMPLETED_COUNT=N ERROR_COUNT=N FILE_COUNT=N` <br> `ROWS_PROCESSED=N`.
    * An error description is included in the message if an error is raised.

![Collector Messages](./images/collector_messages_atsd.png)
