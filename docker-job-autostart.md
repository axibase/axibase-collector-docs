# Job Autostart on Docker

## Overview

To automatically start a job on Docker, use the following Collector parameters:

**Name** | **Description**
----- | -----
`-job-enable` | Enable a specified job by name. Supports job names separated by commas.
`-job-path` | Import a job from a specified file or HTTP(s) content. Supports comma separated lists of files. If the `job-enable` parameter is not defined, **ALL** jobs in the file will be started.
`-job-execute` | Run specified jobs by name after the start-up. Multiple job names can be specified, separated by comma.

## Autostart Pre-configured Job

To automatically start one of the [pre-configured jobs](pre-configured-jobs.md), use the `-job-enable` parameter with [pre-configured ATSD](installation-on-docker.md#start-container):

```properties
docker run \
 --detach \
 --publish-all \
 --restart=always \
 --name=axibase-collector \
 axibase/collector:latest \
  -atsd-url=https://collector-user:collector-password@atsd_host:atsd_https_port \
  -job-enable=job_name
```
 
For example, for a job with the name 'json-socrata':

```properties
docker run \
 --detach \
 --publish-all \
 --restart=always \
 --name=axibase-collector \
 axibase/collector:latest \
  -atsd-url=https://collector-user:collector-password@atsd_host:atsd_https_port \
  -job-enable=json-socrata
```

## Autostart Job from File

To automatically start a job from file, use the `-job-path` and `-job-enable` parameters:

```properties
docker run \
 --detach \
 --publish-all \
 --restart=always \
 --name=axibase-collector \
 axibase/collector:latest \
  -atsd-url=https://collector-user:collector-password@atsd_host:atsd_https_port \
  -job-path=path_to_file \
  -job-enable=job_name
```
 
For example, for a job with the name 'json-socrata' from the file `/tmp/job.xml`:

```properties
docker run \
 --detach \
 --publish-all \
 --restart=always \
 --name=axibase-collector \
 axibase/collector:latest \
  -atsd-url=https://collector-user:collector-password@atsd_host:atsd_https_port \
  -job-path=/tmp/job.xml \
  -job-enable=json-socrata
```

For example, for a remote job file:

```properties
docker run \
 --detach \
 --publish-all \
 --restart=always \
 --name=axibase-collector \
 axibase/collector:latest \
  -atsd-url=https://collector-user:collector-password@atsd_host:atsd_https_port \
  -job-path=https://raw.githubusercontent.com/axibase/axibase-collector-docs/master/job-templates/icmp-ping.xml
```

## Autostart Multiple Jobs

```properties
docker run \
 --detach \
 --publish-all \
 --restart=always \
 --name=axibase-collector \
 axibase/collector:latest \
  -atsd-url=https://collector-user:collector-password@atsd_host:atsd_https_port \
  -job-path=/tmp/jobs.xml \
  -job-enable=json-job,tcp-job
```

## Execute Job Immediately

To execute a job immediately, use the `-job-execute` parameter:

```properties
docker run \
 --detach \
 --publish-all \
 --restart=always \
 --name=axibase-collector \
 axibase/collector:latest \
  -atsd-url=https://collector-user:collector-password@atsd_host:atsd_https_port \
  -job-execute=job_name
```

For example, for a job with the name 'json-socrata':

```properties
docker run \
 --detach \
 --publish-all \
 --restart=always \
 --name=axibase-collector \
 axibase/collector:latest \
  -atsd-url=https://collector-user:collector-password@atsd_host:atsd_https_port \
  -job-execute=json-socrata
```
