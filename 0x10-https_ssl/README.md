# 0x10. HTTPS SSL

## What is HTTPS?

HTTPS (Hypertext Transfer Protocol Secure) is a version of the HTTP (Hypertext Transfer Protocol) that includes a security component. HTTPS encrypts the communication between a web server and a web client, such as a browser, to protect against eavesdropping and tampering.

When a user connects to a website using HTTPS, the website's server and the user's browser establish a secure, encrypted connection using a protocol called SSL (Secure Sockets Layer) or TLS (Transport Layer Security). This encryption ensures that any data exchanged between the server and the client, such as login credentials, credit card information, or personal data, cannot be intercepted and read by a third party.

One way to tell if a website is using HTTPS is to look at the URL in the address bar of your browser. If it starts with "https://" instead of "http://," that means the website is using HTTPS. Additionally, many browsers will display a lock icon in the address bar to indicate that a website is using HTTPS.

In summary, HTTPS is a protocol used to secure web communication, it encrypts the data exchanged between the website's server and the client's browser to protect against eavesdropping and tampering.

## Main elements that SSL is providing

SSL (Secure Sockets Layer) is the predecessor of TLS (Transport Layer Security) which provides two main elements of security for online communications:

Authentication: SSL/TLS verifies that the website the user is connecting to is the legitimate website and not an imposter. This is accomplished by the website providing a digital certificate, which is verified by a trusted third-party certificate authority.

Encryption: SSL/TLS encrypts the communication between the user's browser and the website's server, making sure that any data exchanged between them, such as login credentials, credit card information, or personal data, cannot be intercepted and read by a third party.

## HAProxy SSL

HAProxy is a popular open-source load balancer and reverse proxy that can be used to terminate SSL connections

- Install the haproxy

```
sudo apt-get -y install haproxy
```

- verify that HAProxy is working:

```
haproxy -v
```

- respond with:

```
HA-Proxy version 1.6.3 2015/12/25
Copyright 2000-2015 Willy Tarreau <willy@haproxy.org>
```

HAProxy main configuration file is located at `/etc/haproxy/haproxy.cfg`

default settings /etc/haproxy/haproxy.cfg file has

```
global
        log /dev/log    local0
        log /dev/log    local1 notice
        chroot /var/lib/haproxy
        stats socket /run/haproxy/admin.sock mode 660 level admin
        stats timeout 30s
        user haproxy
        group haproxy
        daemon

        # Default SSL material locations
        ca-base /etc/ssl/certs
        crt-base /etc/ssl/private

        # Default ciphers to use on SSL-enabled listening sockets.
        # For more information, see ciphers(1SSL). This list is from:
        #  https://hynek.me/articles/hardening-your-web-servers-ssl-ciphers/
        ssl-default-bind-ciphers ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+3DES:!aNULL:!MD5:!DSS
        ssl-default-bind-options no-sslv3

defaults
        log     global
        mode    http
        option  httplog
        option  dontlognull
        timeout connect 5000
        timeout client  50000
        timeout server  50000
        errorfile 400 /etc/haproxy/errors/400.http
        errorfile 403 /etc/haproxy/errors/403.http
        errorfile 408 /etc/haproxy/errors/408.http
        errorfile 500 /etc/haproxy/errors/500.http
        errorfile 502 /etc/haproxy/errors/502.http
        errorfile 503 /etc/haproxy/errors/503.http
        errorfile 504 /etc/haproxy/errors/504.http
```

Global section contains settings that apply to the HAProxy process itself. This section contains user, group, log directives, and stats.
Defaults section contains all of the proxies settings.

Restart the haproxy service after editing `/etc/haproxy/haproxy.cfg`

## Load Balancing HAProxy

At the bottom of the /etc/haproxy/haproxy.cfg add

- frontend: Defines a reverse proxy which will listen for incoming requests on a specific IP address and port.
- backend: Defines a pool of servers that the frontend will forward requests to.
- listen: A shorthand notation which combines frontend and backend features into a single command.

add the fronted to the `/etc/haproxy/haproxy.cfg`

```
frontend firstbalance
        bind *:80
        option forwardfor
        default_backend webservers
```

The bind gets an ip and using the \* accepts all ips
The option will save the users ip by using the `forwardfor` options
Default_backend directive, to forward requests to a pool of servers defined in a backend section called webservers. We can distribute the load across many servers.

add the `backend` after the frontend

```
backend webservers
        balance roundrobin
        server webserver1 Your-Webserver1-IP:80 check
        server webserver2 Your-Webserver2-IP:80 check
        option httpchk
```

Traffic is routed using the roundrobin algorithm by default.
Traffic can be resolved debending on user location using access control lists acl directive in the frontend section.
`leastconn` algorithm is a good choice for servers that may hold on to connections longer.
Health checking by adding the check parameter to the webserver1 and webserver2 servers directive.

Health check with check parameter measures the ability to make a tcp connection. A drawback of enabling health checks with the check parameter is that success is measured only by the ability to make a TCP connection to the back-end servers IP address and port. So, even if the web servers begins responding with HTTP 500 Internal Server Error, the checks will still pass as long as a connection can be made. So, visitors might be sent to web pages that are displaying errors.

This can be fixed by checking for a successful http response in the range of 2xx-3xx is good. Added the option httpchk directive to the back-end to enable this heath check

## TLS termination proxy

A TLS termination proxy is a device or service that sits in front of one or more servers, intercepts incoming HTTPS traffic, and then establishes a new HTTPS connection to the backend servers on behalf of the client. The proxy decrypts the incoming traffic and then re-encrypts it before forwarding it to the backend servers. This allows the backend servers to communicate with clients over plain HTTP, while still providing encryption and authentication for the client-server communication.

TLS termination proxies are commonly used in load balancing and reverse proxy scenarios, where a single IP address is used to represent multiple servers and the load balancer or reverse proxy needs to decrypt the incoming traffic in order to route it to the appropriate server.

There are different software that can be used as a TLS termination proxy, such as HAProxy, Nginx, Apache, etc. The process of setting up a TLS termination proxy using those software are similar with some changes in the configuration file.
