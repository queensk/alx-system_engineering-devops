# 0x13. Firewall

UFW stands for Uncomplicated Firewall, it is a user-friendly frontend for iptables that makes it easier to configure firewall rules in Linux systems. UFW is a default firewall configuration tool for Ubuntu and can be used to manage incoming and outgoing traffic.

Here are the ufw commands to configure the firewall:

1. Install ufw: sudo apt-get install ufw
2. Allow incoming traffic for SSH (port 22): sudo ufw allow 22/tcp
3. Allow incoming traffic for HTTPS SSL (port 443): sudo ufw allow 443/tcp
4. Allow incoming traffic for HTTP (port 80): sudo ufw allow 80/tcp
5. Enable the firewall: sudo ufw enable
6. Check the status of the firewall to verify the rules: sudo ufw status verbose
