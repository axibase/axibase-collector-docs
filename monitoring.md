# Monitoring

Axibase Collector sends job status messages to ATSD upon completion so that job execution may be monitored using the built-in Rule Engine.

Job status messages contain the following fields:

* Type: collector-job
* Source: job_name
* Severity: NORMAL if okay, MAJOR on PARTIAL_FAIL, and CRITICAL in case of ERROR
* Entity: Axibase Collector hostname
* Tag `status`: COMPLETED, PARTIAL_FAIL, FAIL
* Tag `job_name`
* Tag `job_type`
* Message: Completed in `N` ms. Items read: `N`. Commands sent: `N`. An error will be included in the message if an error was raised.

Some job types provide an extended set of tags and a modified message:

* FILE job
  * Tag [`error type`](./jobs/file.md#job-completion-messages)
  * Message: Completed in `N` ms. Files read: `N`. Files sent: `N`. <br>Failed requests: `N` COMPLETED_COUNT=N ERROR_COUNT=N FILE_COUNT=N <br> ROWS_PROCESSED=N. An error description will be included in the message if an error was raised.

![Collector Messages](./images/collector_messages_atsd.png)
