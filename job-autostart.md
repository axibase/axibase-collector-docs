# Job Autostart

## Overview

To automatically import and enable a job, use the following parameters:

**Name** | **Description**
----- | -----
`-job-enable` | Enable specified job by name. Support job names separated by commas.
`-job-path` | Import a job from a specified file or HTTP(s) content. Supports comma seperated files. If the `job-enable` parameter is not defined, **ALL** jobs in the file will be started.
`-job-execute` | Run specified jobs by name after the start-up. Multiple job names can be specified, separated by comma.

> Note that the imported jobs will be enabled but will only run according to the schedule. To run a job manually, add the `-job-execute` parameter.

## Enable Pre-configured Job

To enable one of the [pre-configured jobs](pre-configured-jobs.md), set the `-job-enable` parameter:

```sh
./axibase-collector/bin/start-collector.sh -job-enable=job_name
```

For example, to enable a job with the name 'json-socrata':

```sh
./axibase-collector/bin/start-collector.sh -job-enable=json-socrata
```

## Load Job from File

To load and enable a job from file, use the `-job-path` and `-job-enable` parameters:

```sh
./axibase-collector/bin/start-collector.sh -job-path=path_to_file -job-enable=job_name
```

For example, to enable a 'my-jmx-job' job loaded from the file `/tmp/job.xml`:

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

For example, for a job with the name 'my-jmx-job':

```sh
./axibase-collector/bin/start-collector.sh -job-path=/tmp/job.xml -job-enable=my-jmx-job -job-execute=json-my-jmx-job
```
