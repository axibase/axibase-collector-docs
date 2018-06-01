# PostgreSQL Data Queries

## PostgreSQL Base Queries

* Metrics Queries select the most recent statistics:

```SQL
SELECT * FROM pg_stat_database WHERE datname NOT LIKE 'template%'
```

```SQL
SELECT reltuples, relpages, relname FROM pg_class WHERE relkind = 'r' AND relname NOT LIKE 'pg_%' ORDER BY relpages DESC limit 10;
```

```SQL
SELECT * FROM pg_stat_activity
```

```SQL
SELECT * FROM pg_stat_database_conflicts WHERE datname NOT LIKE 'template%'
```

```SQL
SELECT * FROM pg_stat_bgwriter
```

```SQL
SELECT * FROM pg_stat_user_tables where idx_scan > 0
```

```SQL
SELECT * FROM pg_stat_user_indexes WHERE idx_scan > 0
```

```SQL
SELECT * FROM pg_statio_user_tables WHERE heap_blks_read > 10
```

```SQL
SELECT * FROM pg_statio_user_indexes WHERE idx_blks_hit > 1000
```

```SQL
SELECT reltuples, relpages, relname FROM pg_class WHERE relkind = 'r' AND relname NOT LIKE 'pg_%' ORDER BY relpages
DESC limit 10;
```
