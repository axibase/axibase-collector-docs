# Using `axibase_nginx_plus_collector` Script for Monitoring nginx Plus Servers

To collect information from your nginx PLUS servers, download the [provided scripts](https://github.com/axibase/axibase-collector/tree/master/jobs/examples/nginx-plus/axibase-nginx-plus-collector/src) and run the `axibase_nginx_plus_collector.py` script with the appropriate options.
The help message can be printed after running:

```sh
python axibase_nginx_plus_collector.py --help
```

Supported options:

|Option|Extended option|    Description                                         |                 Default               |
|:----:|:-------------:|:------------------------------------------------------:|:-------------------------------------:|
|-a    | --atsd-url    | URL of target ATSD                                     | `tcp://localhost:8081`                 |
|-i    | --items       | Space separated nginx Plus servers item list           | `http://demo.nginx.com`                 |
|-q    | --quiet       | Flag indicating the script does not generate output    | False                                 |
