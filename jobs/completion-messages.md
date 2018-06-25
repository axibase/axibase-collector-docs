# Job Completion Messages

| **Error Type** | **Description** |
|---|:---|
`FILE_NOT_FOUND` | No target file present in the specified directory.
`FILE_EMPTY` | Target file found but completely empty (no annotation, header, or data).
`NO_DATA` | Target file found but does not contain any data (contained an annotation and header, but no timestamps and values).
`UPLOAD_ERROR` | ATSD not available during the scheduled job execution.
`PARSE_ERROR` | File not parsed by ATSD. For example: the timestamp is in a different format.
`NETWORK_ERROR` | Network connection not established by Collector.
`LINE_COUNT_ERROR` | Target file contained less lines than specified in the **Minimum Line Count** setting.
`FIRST_LINE_ERROR` | First line of the target file does not match the **First Line** setting.
`READ_ERROR` | File not read from source path. For example: source path is a directory instead of file.
`PROCESS_ERROR` | Files not written to success directory. For example: success `dir` does not exist.
