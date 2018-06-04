# Docker Certificates

Protecting the Docker daemon socket with OpenSSL.
Make sure you replace **`$HOST`** in the following examples with the DNS name of the target Docker host.

> Credit: [https://docs.docker.com/engine/security/https/#create-a-ca-server-and-client-keys-with-openssl](https://docs.docker.com/engine/security/https/#create-a-ca-server-and-client-keys-with-openssl)

## Generate Private and Public Keys for a CA (Certificate Authority)

Create a directory for certificate files:

```txt
mkdir /home/ubuntu/certs
cd /home/ubuntu/certs
```

Generate a private key:

```sh
openssl genrsa -aes256 -out ca-key.pem 4096
```

Generate a certificate request using the pass phrase for `ca-key.pem`:

```sh
openssl req -new -x509 -days 365 -key ca-key.pem -sha256 -out ca.pem
```

Fill out the fields.

Make sure you set Common Name to the DNS name of the Docker host: **`$HOST`**

```properties
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:CA
Locality Name (eg, city) []:Cupertino
Organization Name (eg, company) [Internet Widgits Pty Ltd]:MyCompany
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:$HOST
Email Address []:
```

## Create a Server Key and Certificate Signing Request (CSR)

```sh
openssl genrsa -out server-key.pem 4096
```

```sh
openssl req -subj "/CN=$HOST" -sha256 -new -key server-key.pem -out server.csr
```

## Sign the Public Key with our CA

TLS connections need to be specified when creating the certificate, as they can be made via the IP address as well as the DNS name. For example, to allow connections
using `10.10.10.20` and `127.0.0.1`:

```sh
echo subjectAltName = IP:10.10.10.20,IP:127.0.0.1 > extfile.cnf
```

```sh
openssl x509 -req -days 365 -sha256 -in server.csr -CA ca.pem -CAkey ca-key.pem \
      -CAcreateserial -out server-cert.pem -extfile extfile.cnf
```

## Create a Client Key and Certificate Signing Request for Client Authentication

```sh
openssl genrsa -out key.pem 4096
```

```sh
openssl req -subj '/CN=client' -new -key key.pem -out client.csr
```

To make the key suitable for client authentication, create an extensions config file:

```sh
echo extendedKeyUsage = clientAuth > extfile.cnf
```

Sign the public key:

```sh
openssl x509 -req -days 365 -sha256 -in client.csr -CA ca.pem -CAkey ca-key.pem \
      -CAcreateserial -out cert.pem -extfile extfile.cnf
```

After generating `cert.pem` and `server-cert.pem`, you can safely remove the
two certificate signing requests:

```sh
rm -v client.csr server.csr
```

## Set Permissions to Private Keys

With a default `umask` of 022, your secret keys will be *world-readable* and
writable for you and your group.

In order to protect your keys from accidental damage, you will want to remove their
write permissions. To make them only readable by you, change file modes as follows:

```sh
chmod -v 0400 ca-key.pem key.pem server-key.pem
```

Certificates can be world-readable, but you might want to remove write access to
prevent accidental damage:

```sh
chmod -v 0444 ca.pem server-cert.pem cert.pem
```

Now you can make the Docker daemon only accept connections from clients
providing a certificate trusted by our CA.
