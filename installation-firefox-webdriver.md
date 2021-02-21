# Firefox WebDriver Installation

## Install Firefox 26

Repository: `https://ftp.mozilla.org/pub/firefox/releases/26.0/`

### wget

```sh
wget -qO- https://ftp.mozilla.org/pub/firefox/releases/26.0/linux-x86_64/en-US/firefox-26.0.tar.bz2 | tar -C /opt -xvj
```

## Install Xvfb (X Virtual Framebuffer)

### Xvfb on Ubuntu or Debian

```sh
sudo apt-get update
sudo apt-get install xvfb
```

#### Xvfb on RHEL, Fedora, CentOS

```sh
sudo yum install xorg-x11-Xvfb
```

## Run Xvfb

```sh
Xvfb :99
```

## Setup Collector Script

Before starting Collector with the Firefox webdriver, modify the startup script. Uncomment and set path to `firefox` binary:

```sh
#COLLECTOR_JAVA_OPTS="$COLLECTOR_JAVA_OPTS -Dwebdriver.firefox.bin="
#export DISPLAY=:99
````

For example:

```sh
COLLECTOR_JAVA_OPTS="$COLLECTOR_JAVA_OPTS -Dwebdriver.firefox.bin=/opt/firefox/firefox"
export DISPLAY=:99
```
