# Job Autostart

## Overview

To automatically import and enable a job, use the following parameters:

**Name** | **Description**
----- | -----
`-job-enable` | Enable specified job by name. Accepts job names separated by commas.
`-job-path` | Import a job from a specified file or HTTP or HTTPS content. Supports comma-separated files. If the `job-enable` parameter is not defined, **ALL** jobs in the file start.
`-job-execute` | Run specified jobs by name after startup. Multiple job names can be specified, separated by comma.

> Note that imported jobs are enabled but only run according to the schedule. To run a job manually, add the `-job-execute` parameter.

## Enable preconfigured Job

To enable one of the [preconfigured jobs](./pre-configured-jobs.md), set the `-job-enable` parameter:

```sh
./axibase-collector/bin/start-collector.sh -job-enable=job_name
```

For example, to enable a job named `json-socrata`:

```sh
./axibase-collector/bin/start-collector.sh -job-enable=json-socrata
```

## Load Job from File

To load and enable a job from a file, use the `-job-path` and `-job-enable` parameters:

```sh
./axibase-collector/bin/start-collector.sh -job-path=path_to_file -job-enable=job_name
```

For example, to enable the job `my-jmx-job` loaded from the file `/tmp/job.xml`:

```sh
./axibase-collector/bin/start-collector.sh -job-path=/tmp/job.xml -job-enable=my-jmx-job
```

To load jobs from a remote file, specify the full path:

```sh
./axibase-collector/bin/start-collector.sh -job-path=https://raw.githubusercontent.com/axibase/axibase-collector/master/job-templates/icmp-ping.xml
```

## Enable Multiple Jobs

```sh
./axibase-collector/bin/start-collector.sh -job-path=/tmp/jobs.xml -job-enable=json-job,tcp-job
```

## Run Job Immediately

To execute a job immediately, use the `-job-execute` parameter:

```sh
./axibase-collector/bin/start-collector.sh -job-execute=job_name
```

For example, for a job named `my-jmx-job`:

```sh
./axibase-collector/bin/start-collector.sh -job-path=/tmp/job.xml -job-enable=my-jmx-job -job-execute=json-my-jmx-job
```
