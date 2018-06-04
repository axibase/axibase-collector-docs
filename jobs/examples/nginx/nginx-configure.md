# NGINX Server Configuration

## Verify that `ngx_http_stub_status_module` is Present

```sh
nginx -V 2>&1 | grep -o with-http_stub_status_module
```

If the output contains the module name, the module is installed.

If the response is empty, upgrade to a [newer version of NGINX](http://nginx.org/en/CHANGES) or recompile your NGINX server with the *-with-http_stub_status_module* option.

Sample `nginx -V` output:

```sh
$ nginx -V
nginx version: nginx/1.4.6 (Ubuntu)
built by gcc 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04)
TLS SNI support enabled
configure arguments: --with-cc-opt='-g -O2 -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security -D_FORTIFY_SOURCE=2' --with-ld-opt='-Wl,-Bsymbolic-functions -Wl,-z,relro' --prefix=/usr/share/nginx --conf-path=/etc/nginx/nginx.conf --http-log-path=/var/log/nginx/access.log --error-log-path=/var/log/nginx/error.log --lock-path=/var/lock/nginx.lock --pid-path=/run/nginx.pid --http-client-body-temp-path=/var/lib/nginx/body --http-fastcgi-temp-path=/var/lib/nginx/fastcgi --http-proxy-temp-path=/var/lib/nginx/proxy --http-scgi-temp-path=/var/lib/nginx/scgi --http-uwsgi-temp-path=/var/lib/nginx/uwsgi --with-debug --with-pcre-jit --with-ipv6 --with-http_ssl_module --with-http_stub_status_module --with-http_realip_module --with-http_addition_module --with-http_dav_module --with-http_geoip_module --with-http_gzip_static_module --with-http_image_filter_module --with-http_spdy_module --with-http_sub_module --with-http_xslt_module --with-mail --with-mail_ssl_module
```

## Configure Status Page

Open the `nginx.conf` file and review the [configuration example](http://nginx.org/en/docs/http/ngx_http_stub_status_module.html#example) provided in NGINX documentation.

```sh
sudo nano /etc/nginx/nginx.conf
```

Enable the page on the `/nginx_status` URL so that it's accessible at *<your_server_address>/nginx_status*.

```ls
location /nginx_status {
    stub_status;
}
```

Reload the server to apply changes:

```sh
sudo nginx -s reload
```

Verify that status page is accessible by opening *<your_server_address>/nginx_status*:

```ls
Active connections: 291
server accepts handled requests
 16630948 16630948 31070465
Reading: 6 Writing: 179 Waiting: 106
```

## Restrict Access to the Status Page

Once you verify that the status page is enabled, restrict access to this page only to the IP address of the server where Axibase Collector is installed.

Add the following lines at the **beginning** of the *location /nginx_status* directive:

```java
   allow <collector_ip_address>;
   deny all;
```

 For example, if your collector is located at `10.102.0.6`, the configuration should look as follows:

```ls
location /nginx_status {
    allow 10.102.0.6;
    deny all;
    stub_status;
}
```

Reload the server:

```sh
sudo nginx -s reload
```

Repeat the process for each NGINX server that you would like to monitor.
