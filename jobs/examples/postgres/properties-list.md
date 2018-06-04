# Collected PostgreSQL Properties

* `postgres.activity`:

```json
[
  {
    "type": "postgres.activity",
    "entity": "10.102.0.9",
    "key": {
      "datname": "redmine",
      "procpid": "10193",
      "usename": "readonly",
      "usesysid": "101610"
    }
    ]
```

* `postgres.info`:

```json
[{
    "type": "postgres.info",
    "entity": "10.102.0.9",
    "key": {},
    "tags": {
      "current_database": "redmine",
      "current_user": "readonly",
      "port": "5432",
      "server_address": "10.102.0.9",
      "start_time": "2016-05-26 10:03:07.871886+00",
      "version": "PostgreSQL 9.1.14 on x86_64-unknown-linux-gnu, compiled by gcc (Ubuntu/Linaro 4.6.3-1ubuntu5) 4.6.3, 64-bit"
    },
    "date": "2016-05-27T12:35:57Z"
  }
  ]
```

* `postgres.pg_class`:

```json
[{
    "type": "postgres.pg_class",
    "entity": "10.102.0.9",
    "key": {
      "relname": "attachments"
    },
    "tags": {
      "relpages": "78",
      "reltuples": "3084"
    },
    "date": "2016-05-27T12:35:57Z"
  }
  ]
```
