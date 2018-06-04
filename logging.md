# Logging

## Copy log file

Copy log file to the Docker host on which Axibase Collector container is running:

```bash
docker cp axibase-collector:/opt/axibase-collector/logs/axibase-collector.log ./
```

## Copy all log files

Archive log files from the Docker host on which Axibase Collector container is running:

```bash
docker exec -it axibase-collector tar cvf tmp/logs.tar.gz opt/axibase-collector/logs/
```

Copy the created archive to the Docker host on which Axibase Collector container is running:

```bash
docker cp axibase-collector:/tmp/logs.tar.gz ./
```

## Configure Collector to Exit and Dump Heap on OutOfMemory Error

Edit the `./axibase-collector/bin/start-collector.sh` file.

Make the following changes by adding 3 lines after **`# Exit and dump heap on OoM after`**:

Before:

```bash
...
# GC_OPTS="-Xloggc:$LOGS/gc_$RANDOM.log -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintGCTimeStamps -XX:+PrintGC"
# COLLECTOR_JAVA_OPTS="$COLLECTOR_JAVA_OPTS $GC_OPTS"

COLLECTOR_PID_FILE="$BIN/collector.pid"

if type -p java > /dev/null 2>&1; then
...
```

After:

```bash
...
# GC_OPTS="-Xloggc:$LOGS/gc_$RANDOM.log -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCDateStamps -XX:+PrintGCTimeStamps -XX:+PrintGC"
# COLLECTOR_JAVA_OPTS="$COLLECTOR_JAVA_OPTS $GC_OPTS"

# Exit and dump heap on OoM
export JAVA_TOOL_OPTIONS="-XX:OnOutOfMemoryError=\"kill \-9 %p\""
OOM_OPTS="-XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=$LOGS"
COLLECTOR_JAVA_OPTS="$COLLECTOR_JAVA_OPTS $OOM_OPTS"

COLLECTOR_PID_FILE="$BIN/collector.pid"

if type -p java > /dev/null 2>&1; then
...
```