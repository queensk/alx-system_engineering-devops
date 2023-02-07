# 0x0E. Web stack debugging #1

To diagnose the issue of Nginx not listening on port 80 in an Ubuntu container, you can follow these steps:

1. Check if Nginx is running using the command: service nginx status
2. Check if Nginx is bound to the correct IP address using the command: sudo netstat -tulpn | grep nginx
3. Check if the Nginx configuration file (usually located at /etc/nginx/nginx.conf) has the correct listen directive and is set to listen on port 80: listen 80;
4. Check if there are any firewall rules or iptables that are blocking traffic to port 80. You can check using the command: sudo iptables -L
5. Check if any other services are listening on port 80 using the command: sudo lsof -i:80
   If after checking all of the above, you still can't determine the cause of the issue, you may want to try restarting the Nginx service and/or the Ubuntu container itself.

Here is a bash script that automates the process of diagnosing the issue:

bash code

```
#!/bin/bash

# Check if Nginx is running
nginx_status=$(service nginx status)
if [[ $nginx_status != *"active (running)"* ]]; then
  echo "Nginx is not running"
  exit 1
fi

# Check if Nginx is bound to the correct IP address
nginx_binding=$(sudo netstat -tulpn | grep nginx)
if [[ $nginx_binding != *"0.0.0.0:80"* ]]; then
  echo "Nginx is not bound to the correct IP address or port"
  exit 1
fi

# Check if the Nginx configuration file has the correct listen directive
nginx_listen=$(sudo cat /etc/nginx/nginx.conf | grep "listen 80;")
if [[ $nginx_listen != *"listen 80;"* ]]; then
  echo "Nginx listen directive is not set to port 80"
  exit 1
fi

# Check if there are any firewall rules blocking traffic to port 80
firewall_rules=$(sudo iptables -L | grep ":80")
if [[ $firewall_rules != "" ]]; then
  echo "There are firewall rules blocking traffic to port 80"
  exit 1
fi

# Check if any other services are listening on port 80
services_listening=$(sudo lsof -i:80)
if [[ $services_listening != "" ]]; then
  echo "There is another service listening on port 80"
  exit 1
fi

echo "Nginx should be listening on port 80"
```
