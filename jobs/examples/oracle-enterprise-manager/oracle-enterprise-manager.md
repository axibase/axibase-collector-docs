# Oracle Enterprise Manager
## Overview
[Oracle Enterprise
Manager](http://www.oracle.com/us/products/enterprise-manager/index.html "Oracle Enterprise Manager") is
a set of web-based tools aimed at managing software and hardware
produced by Oracle Corporation as well as by some non-Oracle entities.

## Supported versions

- Oracle Enterprise Manager 11.x and newest.

## Job files

You can download the oem-jobs.xml file and import it from the Jobs tab in Axibase Collector for a quick setup. Be sure to select your ATSD server and Data Source after you have imported the collector job xml file.
> [oracle-em-jobs.xml](oracle-em-job.xml)

### Queries

This file contains two jobs with different queries to Oracle database.

### Metric Queries

- Propeties
    - Query 1
    ```SQL
    SELECT
      ENTITY_NAME,
      ENTITY_TYPE || '.' || REPLACE(REPLACE(METRIC_GROUP_LABEL, ',', ' '), ' ', '_') || '.' ||
        REPLACE(REPLACE(TRIM(REPLACE(REPLACE(REPLACE(REPLACE(METRIC_COLUMN_LABEL, ' - ', '-'), ',', ' '), ')', ' '), '(', ' ')), ' ', '_'), '__', '_') AS METRIC,
      NULLIF(KEY_PART_1, '%') AS KEY,
      NULLIF(KEY_PART_2, '%') AS KEY_2,
      NULLIF(KEY_PART_3, '%') AS KEY_3,
      NULLIF(KEY_PART_4, '%') AS KEY_4,
      NULLIF(KEY_PART_5, '%') AS KEY_5,
      NULLIF(KEY_PART_6, '%') AS KEY_6,
      NULLIF(KEY_PART_7, '%') AS KEY_7,
  COLLECTION_TIME_UTC, VALUE
  FROM SYSMAN.gc$metric_values
  WHERE ENTITY_TYPE = 'oracle_database' AND METRIC_GROUP_LABEL_NLSID IS NOT NULL AND COLLECTION_TIME_UTC >= ?
  ORDER BY COLLECTION_TIME_UTC
    ```
    -Query 2


## Installation steps


## Verifying configurations


## Metric list


## Entity group list
Entities collecting Oracle Enterprise Manager data are automatically grouped in ATSD.

Oracle Enterprise Manager entity group names:

- Oracle EM Databases
- Oracle EM Hosts


## Portal List
Default visualization portals for Oracle Enterprise Manager entities are included in ATSD.
Default Oracle Enterprise Manager portal names:
##### Launch live Oracle Databases Portal in Axibase Chart Lab.

[Launch](http://axibase.com/chartlab/32a3fe3e)

![](images/oracle_databases_poral3.png "Oracle Databases")

##### Oracle Host Portal
![](images/oracle_host_portal.png "Oracle Host")

##### Launch live Oracle Host Portal in Axibase Chart Lab.

[Launch](http://axibase.com/chartlab/32a3fe3e/2/)
