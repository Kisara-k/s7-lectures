## 6 Internet Protocol (IPv4)

## Study Notes

### 1. 🌐 Introduction to the Internet Protocol (IPv4)

The Internet Protocol, commonly known as **IPv4**, is the fundamental network layer protocol that enables communication across interconnected networks, collectively called the Internet. It is responsible for addressing, routing, and delivering data packets from a source device to a destination device, even if they are on different networks.

In the Internet architecture, the **Internet Layer** sits between the **Transport Layer** (which handles end-to-end communication like TCP and UDP) and the **Link Layer** (which deals with physical network connections). IPv4 is the dominant protocol at this layer, although IPv6 is increasingly used as its successor.

IPv4 provides a universal addressing scheme and packet format that routers use to forward data across multiple networks, ensuring that information reaches the correct destination.


### 2. 📦 IPv4 Datagram Format: How Data is Packaged

An **IPv4 datagram** is the basic unit of data transmission at the Internet Layer. It contains both control information (header) and the actual data (payload).

#### Key parts of the IPv4 datagram header:

- **Version Number (4 bits):** Always 4 for IPv4, indicating the protocol version.
- **Header Length:** Specifies the size of the header in bytes.
- **Type of Service (ToS):** Indicates the priority and handling instructions for the packet.
- **Total Length:** The entire size of the datagram (header + data) in bytes.
- **Identification, Flags, Fragment Offset:** Used for fragmentation and reassembly of packets if they are too large for a network segment.
- **Time to Live (TTL):** Limits the packet’s lifetime by decrementing at each router; prevents infinite looping.
- **Protocol:** Specifies the upper-layer protocol (e.g., TCP, UDP) that should receive the payload.
- **Header Checksum:** Error-checking for the header to detect corruption.
- **Source IP Address:** 32-bit address of the sender.
- **Destination IP Address:** 32-bit address of the receiver.
- **Options (optional):** Extra features like timestamps or routing instructions.

The payload typically contains a TCP or UDP segment, which carries the actual application data.


### 3. 🏷️ IP Addressing: Identifying Devices on the Network

An **IP address** is a unique 32-bit number assigned to each device interface connected to a network. It serves as the device’s identifier on the Internet.

#### Structure of an IPv4 Address:

- Written in **dotted decimal notation**: four numbers separated by dots (e.g., 192.168.1.1).
- Each number represents 8 bits (one byte), so the full address is 32 bits.
- The address is divided into two parts:
  - **Network part:** The high-order bits that identify the network.
  - **Host part:** The low-order bits that identify the specific device (host) on that network.

Devices with the same network part are on the **same local network** and can communicate directly without routing.

#### Interfaces and IP Addresses:

- A **host** usually has one network interface with one IP address.
- A **router** has multiple interfaces, each with its own IP address, connecting different networks.


### 4. 🧩 Network Masks and CIDR: Flexible Addressing

#### Network Masks:

A **network mask** is used to separate the network part and the host part of an IP address. It is a 32-bit number where bits corresponding to the network part are set to 1, and bits for the host part are set to 0.

For example, a mask of `255.255.255.0` means the first 24 bits are network bits, and the last 8 bits are host bits.

#### CIDR (Classless Inter-Domain Routing):

Originally, IP addresses were divided into fixed classes (A, B, C), which was inefficient because it wasted many addresses. CIDR allows the network portion of an IP address to be any length, making address allocation more flexible and efficient.

CIDR notation looks like this: `a.b.c.d/x`, where `x` is the number of bits in the network part.

This flexibility helps conserve IP addresses and supports hierarchical routing.


### 5. 🛠️ How Devices Get IP Addresses

#### For Hosts:

- **Static assignment:** Manually configured by a system administrator.
- **Dynamic assignment:** Using **DHCP (Dynamic Host Configuration Protocol)**, where a host requests an IP address from a DHCP server when it joins the network. The server leases an address for a period, which can be renewed.

#### For Networks:

- Networks receive IP address blocks from their **Internet Service Provider (ISP)**.
- ISPs get large blocks from **Regional Internet Registries (RIRs)** like APNIC.
- RIRs receive address blocks from **ICANN (Internet Corporation for Assigned Names and Numbers)**.

This hierarchical allocation ensures organized distribution of IP addresses worldwide.


### 6. 🚦 Routing and Packet Forwarding: Getting Data from Source to Destination

When a device wants to send data to another device, the IP datagram must travel through potentially multiple networks and routers.

#### Forwarding Process:

- The source device looks up the destination network in its **forwarding table**.
- If the destination is on the same network, the datagram is sent directly using the link layer.
- If the destination is on a different network, the datagram is sent to the **next-hop router**.
- Each router repeats this process, forwarding the datagram closer to the destination network.
- When the datagram reaches the destination network, it is delivered to the destination host.

#### Address Resolution Protocol (ARP):

On a local network, devices communicate using **MAC addresses** (hardware addresses). If a device knows the IP address but not the MAC address of the destination, it uses ARP:

- Sends a broadcast asking, “Who has this IP address?”
- The device with that IP replies with its MAC address.
- The sender can then send the frame directly to the MAC address.


### 7. ⚠️ ICMP: Internet Control Message Protocol

ICMP is a companion protocol to IP used for sending error messages and operational information.

#### Common ICMP messages:

- **Echo request/reply:** Used by the `ping` command to test connectivity.
- **Destination unreachable:** Indicates that a host, network, or port cannot be reached.
- **Time exceeded:** Sent when TTL expires, indicating a packet was discarded.
- **Redirect:** Suggests a better route for a packet.

ICMP messages are carried inside IP datagrams and help diagnose network problems.


### 8. 🔄 DHCP: Dynamic Host Configuration Protocol

DHCP automates the process of assigning IP addresses to hosts dynamically.

#### How DHCP works:

1. **Discover:** Host broadcasts a request looking for DHCP servers.
2. **Offer:** DHCP server responds with an available IP address.
3. **Request:** Host requests the offered IP address.
4. **Acknowledgment:** Server confirms the assignment.

DHCP leases addresses temporarily, allowing efficient reuse and supporting mobile devices that join different networks.


### 9. 🔀 NAT: Network Address Translation

#### The Problem:

IPv4 addresses are limited, and there are more devices than available unique IP addresses.

#### The Solution: NAT

- NAT allows multiple devices on a private local network to share a single public IP address.
- Inside the local network, devices use private IP addresses (e.g., 10.0.0.x).
- When a device sends data to the Internet, the NAT router replaces the source IP and port with its own public IP and a unique port number.
- When replies come back, the NAT router translates the address and port back to the original device.

#### Benefits of NAT:

- Conserves public IP addresses.
- Provides a layer of security by hiding internal network structure.
- Allows changing internal addresses without affecting external communication.

#### Challenges:

- NAT breaks the **end-to-end principle** of the Internet, complicating some applications like peer-to-peer.
- Requires careful handling of port numbers and translation tables.


### 10. 📝 Summary

To wrap up, here are the key points covered:

- The **Internet Protocol (IPv4)** is the core protocol for addressing and routing packets across interconnected networks.
- IPv4 datagrams have a structured header and payload, enabling routers to forward packets correctly.
- IP addresses uniquely identify devices and are divided into network and host parts.
- **CIDR** and network masks allow flexible and efficient IP address allocation.
- Devices obtain IP addresses either statically or dynamically via **DHCP**.
- Routing uses forwarding tables and protocols like **ARP** to deliver packets.
- **ICMP** provides error reporting and diagnostic messages.
- **NAT** helps overcome IPv4 address shortages by allowing multiple devices to share a single public IP.

Understanding these concepts is essential for grasping how the Internet works at the network layer and how data moves reliably from one device to another.