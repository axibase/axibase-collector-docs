# Scheduling

## Scheduled Execution

Axibase Collector executes enabled jobs based on a schedule.

The number of concurrently executing jobs is set to 32 by default and is controlled with `quartz.properties`.

Jobs execute simultaneously, whereas configurations inside the same job are executed sequentially.

Multiple instances of the same job may not run at the same time. If the job is in STARTED status and it is scheduled to execute again, the new execution will not be triggered until the current job instance finishes processing.

## Manual Execution

Jobs can be executed manually with the `Run` action, regardless of its schedule or status.

Manual execution produces the same results as a scheduled execution.

The manual mode is useful for running temporarily disabled jobs (for example when developing new jobs or troubleshooting existing jobs).

## Cron Expressions

A cron expression is a string that determines a schedule for executing a job.

Fields in a cron expression have the following order:

```ls
[seconds] [minutes] [hours] [day-of-month] [month] [day-of-week]
```

![Cron Expressions](./images/cron_expressions.png)

Field Control Symbols:

| **Name** | **Description** |
|---|---|
| * | Any value |
| ? | No specific value |
| R | Random value within allowed value range |
| , | Value list separator |
| - | Range of values |
| / | Step values |

For example, `0 0 8 * * ?` means execution at 08:00:00 every day.

Field Constraints:

| **Name** | **Allowed Values** |
|:---|:---|
| second | 0-59, R |
| minute | 0-59, R |
| hour | 0-23, R |
| day-of-month | 1-31, ? |
| month | 1-12 or JAN-DEC |
| day-of-week | 1-7 or MON-SUN, ?  |

* If the specific value is set in `day-of-week`, `day-of-month` should be set to `?`, e.g. `0 0 6 ? * MON`.
* If the specific value is set in `day-of-month`, `day-of-week` should be set to `?`, e.g. `0 0 6 */2 * ?`.

Second, minute, and hour fields support **R** (random) symbol to randomize execution time.

### Cron Expression Examples

| **Expression** | **Second** | **Minute** | **Hour** | **Day of Month** | **Month** | **Day of Week** | **Description** |
|:---|---:|---:|---:|---:|---:|---:|:---|
| `0 0/15 * * * ?` | 0 | 0/15 | * | * | * | ? | Every 15 minutes. |
| `0 5 4 * * ?`    | 0 | 5 | 4 | * | * | ? | At 04:05 every day. |
| `0/10 * * * * ?` | 0/10 | * | * | * | * | ? | Every 10 seconds. |
| `0 0/1 * * * ?`  | 0 | 0/1 | * | * | * | ? | Every minute. |
| `0 0 0 * * ?`    | 0 | 0 | 0 | * | * | ? | Every day at 00:00. |
| `R 0/5 * * * ?`  | R | 0/5 | * | * | * | ? | Every 5 minutes at a random second. |
| `R R 2 * * ?`    | R | R | 1 | * | * | ? | At a random minute and second past the 2nd hour. |
| `0 5,35 * * * ?` | 0 | 5,35 | * | * | * | ? | Every hour at the 5th and 35th minute. |
| `0 0 6 ? * MON`  | 0 | 0 | 6 | ? | * | MON | Every Monday at 06:00. |
| `0 5 0 * 8 ?`    | 0 | 5 | 0 | * | 8 | ? | At 00:05 every day in August. |
| `30 15 14 1 * ?` | 30| 15| 14| 1 | * | ? | At 14:15:30 on the 1st of every month. |
| `0 0 22 ? * 1-5` | 0 | 0 | 22| ? | * | 1-5 | At 22:00 on Mon, Tue, Wed, Thu and Fri. |
| `0 5 0-10/2 * * ?` | 0 | 5 | 0-10/2 | * | * | ? | At every 9th minute past the 0, 2, 4, 6, 8, and 10th hour. |
| `0 0 0,12 1 */2 ?` | 0 | 0 | 0,12| 1 | */2 | ? | At 00:00 and 12:00 on the 1st in <br>January, March, May, July, September and November. |

## Execution State

Jobs can have the following executing states:

* STARTING
* STARTED
* STOPPED
* STOPPING
* COMPLETED
* ABANDONED
* FAILED
