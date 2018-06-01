# Placeholders

## Overview

The following placeholders are supported to format strings, calculate dates, and download multiple files.

| **Name** | **Description** |
|:---|:---|
| `${ITEM}` | Current element in the Item List.|
| `${PATH}` | URL path or the file's absolute path. |
| `${FILE}` | File's name (1). |
| `${DIRECTORY}` | File's parent directory. |
| `${TIME()}` | Text output of the `TIME` function. |
| `${DATE_ITEM()}` | Current element in the Date Item list.|

* (1) In the case of HTTP protocol, the placeholder `${FILE}` returns part of the URL after the last slash and before query string. For example: `http://examples.com/data/stats.csv?city=Denver` -> `${FILE}` = `stats.csv`

## Usage

| **Name** | **Supported Fields** | **Supported Protocols** |
|:---|:---|:---|
| `${ITEM}` | Path, First Line Contains, Default Entity, Metric Prefix, Custom Tags, Success Directory, Error Directory | All |
| `${PATH}` | First Line Contains, Default Entity, Metric Prefix | All |
| `${FILE}` | First Line Contains, Default Entity, Metric Prefix | All |
| `${DIRECTORY}` | First Line Contains, Default Entity, Metric Prefix | FILE, FTP, SFTP, SCP |
| `${TIME()}` | First Line Contains, Path, Success Directory, Error Directory | All |
| `${DATE_ITEM()}` | Path | All |

* To URL-encode placeholder value, for example, if it may contain special characters and is included in the Path, apply the `url` function as follows: `${ITEM?url}`.

## Syntax

The placeholder is prefixed with `$` and enclosed in curly brackets `{}`.

```ls
${PLACEHOLDER}
```

Examples:

`${ITEM}`

```ls
file:///opt/files/inbound/${TIME("previous_day", "yyyy-MM-dd")}/daily.csv
```

## Functions

### `TIME` Function

The `TIME` function calculates time based on the [calendar](https://axibase.com/docs/atsd/shared/calendar.html) expression. The syntax outputs its value in the specified `time_format`.

Syntax: `${TIME("end_time_syntax", "time_format")}`

Example: `${TIME("previous_hour", "yyyy-MM-dd/HH")}`

The time format can be specified using `y`, `M`, `d`, `H`, `m`, or `s`. See [SimpleDateFormat](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html) for reference.

If the `TIME` function returns a number, it can be used in addition or subtraction expressions:

Example: `${TIME("2016-01-01","M") - 1}` -- subtract 1 from month.

### `DATE_ITEM` Function

The `DATE_ITEM` function returns an array of strings.

It creates an array of dates between start and end time arguments, and formats these dates into strings with the specified date format.

If the path contains the `${DATE_ITEM()}` placeholder, it should execute a separate file request for each string in the array.

Syntax: `${DATE_ITEM(startDate, endDate, periodCount, periodUnit, timeFormat)}`

`startDate` and `endDate` support [calendar](https://axibase.com/docs/atsd/shared/calendar.html) expressions.

Example: `${DATE_ITEM("current_day - 7 * DAY", "now", 1, "HOUR", "yyyy/MM/dd/HH")}`

### String Functions

Placeholder values can be further modified with built-in [string functions](#string-functions).

```ls
${PLACEHOLDER?function(arguments)}
```

Example: `${FILE?keep_before("_")}`

| **Function** | **Description** |
|:---|:---|
| [`keep_after`](#keep_after) | Removes part of the string before the first occurrence of the given substring. |
| [`keep_after_last`](#keep_after_last) | Removes part of the string before the last occurrence of the given substring. |
| [`keep_before`](#keep_before) | Removes part of the string that starts with the first occurrence of the given substring. |
| [`keep_before_last`](#keep_before_last) | Removes part of the string that starts with the last occurrence of the given substring. |
| [`replace`](#replace) | Replace all occurrences of the given string in the original string with another string. |
| [`remove_beginning`](#remove_beginning) | Removes the given substring from the beginning of the string. |
| [`remove_ending`](#remove_ending) | Removes the given substring from the end of the string. |

Multiple functions can be chained (executed from left to right):

```ls
${PLACEHOLDER?functionA(arguments)?functionB(arguments)}
```

Example: `${FILE?keep_before("_")?replace(".csv", "")}`

Input: **ftp.example.com/data/95014_Cupertino_20160625_DAILY.csv**

| **Expression** | **Result** |
|:---|:---|
| `${FILE}` | 95014_Cupertino_20160625_DAILY.csv |
| `${FILE?keep_before('_')}` | 95014 |
| `${FILE?keep_after('_')?keep_before('_')}` | Cupertino |
| `${FILE?split('_')[0]}` | 95014 |
| `${FILE?split('_')[1]}` | Cupertino |
| `${FILE?split('_')[n]}` | Nth token after split by underscore |
| `${FILE?keep_after_last('_')?keep_before('.')}` | DAILY |

### String Function Examples

The following examples are based on the [`Path`](file.md#download) field.
The Path field can be used to define [`Default Entity`](file.md#upload).

#### keep_after

* `file:///opt/files/cpu_busy.*`
* `${PATH?keep_after('.')}`

| Matching Paths | Output |
|:---|:---|
| /opt/files/cpu_busy.nurswgvml.106<br>/opt/files/cpu_busy.nurswgvml.107 | nurswgvml.106<br>nurswgvml.107 |

#### keep_after_last

* `/2.2/tags/docker/info?key=privateKey((&site=${ITEM}`
* `${ITEM?keep_after_last("-")}`

| ITEM value | Output |
|:---|:---|
| so-stackoverflow | stackoverflow |

#### keep_before

* `ftp://user:password@10.10.0.10:21/home/user/nurswgvml106_*`
* `${FILE?keep_before('_')}`

| Matching Paths | Output |
|:---|:---|
| /home/user/nurswgvml106_temperature.csv | nurswgvml106 |

#### keep_before_last

* `file:///opt/files/*_busy.csv`
* `${FILE?keep_before_last('_')}`

| Matching Paths | Output |
|:---|:---|
| /opt/files/nurswgvml106_cpu_busy.csv<br>/opt/files/nurswgvml107_cpu_busy.csv | nurswgvml106_cpu<br>nurswgvml107_cpu |

#### replace

* `file:///opt/files/*`
* `${FILE?replace(' ','.')}`

| Matching Paths | Output |
|:---|:---|
| /opt/files/nurswgvml106 cpu_busy | nurswgvml106.cpu_busy |

#### remove_beginning

* `file:///opt/files/*`
* `${PATH?remove_beginning('/opt/files/')}`

| Matching Paths | Output |
|:---|:---|
| /opt/files/nurswgvml106<br>/opt/files/nurswgvml107 | nurswgvml106<br>nurswgvml107 |

#### remove_ending

* `file:///opt/files/*.cpu_busy.csv`
* `${FILE?remove_ending('.cpu_busy.csv')}`

| Matching Paths | Output |
|:---|:---|
| /opt/files/nurswgvml106.cpu_busy.csv<br>/opt/files/nurswgvml107.cpu_busy.csv | nurswgvml106<br>nurswgvml107 |

### `LOOKUP` function

The `LOOKUP` function provides key-to-value mapping in the specified Item List. It is available in [JSON](json.md), [JDBC](jdbc.md), [PI](pi.md) jobs to resolve entities.

* Syntax

The LOOKUP function has several implementations.

`LOOKUP(itemList, key, separator='=')`

Treat Item List as a properties file. Key is a substring of item list row before the separator, value is a substring after the separator. If `separator` parameter is not specified, '=' will be used as a separator.

| Parameter name | Parameter type | Description |
| :--------------|:---------------|:------------|
| itemList       | String         | Name of the Item List |
| key            | String         | Lookup Key  |
| separator      | String (optional) | Key/value separator |

`LOOKUP(itemList, key, keyColumnIndex, valueColumnIndex, separator=',')`

Treat Item List as a CSV structure.

| Parameter name | Parameter type | Description |
| :--------------|:---------------|:------------|
| itemList       | String         | Name of the Item List |
| key            | String         | Lookup Key  |
| keyColumnIndex | Integer        | Index of column in a CSV row that will be used as the key column, starting with 1 |
| valueColumnIndex | Integer      | Index of column in a CSV row that will be used as the value column, starting with 1 |
| separator      | String (optional) | CSV columns separator |

#### LOOKUP Examples

Consider the Item List **'us-regions'** with items:

```txt
1=New-England
2=Middle-Atlantic
3=East-North-Central
4=West-North-Central
5=South-Atlantic
6=East-South-Central
7=West-South-Central
8=Mountain
9=Pacific
```

```sh
${LOOKUP('us-regions', '9')} => Pacific
${LOOKUP('us-regions', '2', '=')} => Middle-Atlantic
```

Consider the Item List **'meteo-stations'**:

```txt
94274,QLD,IDQ60801
94341,QLD,IDQ60801
94683,SA,IDS60801
94677,SA,IDS60801
94141,NT,IDD60801
94131,NT,IDD60801
94461,WA,IDW60801
94319,WA,IDW60801
```

```sh
${LOOKUP('meteo-stations', '94461', 1, 2)} => WA
${LOOKUP('meteo-stations', '94683', 1, 3, ',')} => IDS60801
${LOOKUP('meteo-stations', '94141', ',')} => NT,IDD60801
```
