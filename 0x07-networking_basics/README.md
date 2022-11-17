# 0x07. Networking basics #0
## Resources
- Read or watch:

> OSI model

- OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

- It is organized from the lowest level to the highest level:

- The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal
- The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc
- Keep in mind that the OSI model is a concept, it’s not even tangible. The OSI model doesn’t perform any functions in the networking process. It is a conceptual framework so we can better understand complex interactions that are happening. Most of the functionality in the OSI model exists in all communications systems.


> Different types of network
- LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

- LAN network
- WAN network
- Internet

> MAC address
- address physical attached to a hardware device.
- The unique identifier of a network interface

> What is an IP address
- Is to devices connected to a network what postal address is to houses

> Private and public address

> IPv4 and IPv6
> Localhost
> TCP and UDP
- TCP - It is a protocol that is transferring data in a slow way but surely
- UDP - It is a protocol that is transferring data in a fast way and might loss data along in the process

> TCP/UDP ports List
- Once packets have been sent to the right network device using IP using either UDP or TCP as a mode of transportation, it needs to actually enter the network device.

- If we continue the comparison of a network device to your house, where IP address is like your postal address, UDP and TCP ports are like the windows and doors of your place. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free of use.

- While the full list of ports should not be memorized, it is important to know the most used ports, let’s start by remembering 3 of them:

```
22 for SSH
80 for HTTP
443 for HTTPS
What is ping /ICMP
```

- Positional parameters
man or help:

- The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command ping uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network.

netstat
ping