# IP Quiz

### 1. In an IP network, an end-system is generally called a _____.

**Answer:** ______

### 2. A device which forwards packets from one IP network to another is called a _____.

**Answer:** ______

### 3. A reasonable value for the contents of the *version* header is _____.

**Answer:** ______

### 4. A packet is _____ when its TTL reaches 0.
A) discarded and an ICMP message returned  
B) returned to the sending host  
C) stored on the host till the output link is free  
D) forwarded to the next router and an ICMP message generated  
E) discarded without generating an ICMP packet

### 5. An IP address identifies _____.
A) an interface  
B) a router  
C) a subnet  
D) a datagram  
E) a host

### 6. _____ addressing is no longer used due to inefficient address allocation.

**Answer:** ______

### 7. For each of the netmasks, match the dotted quad notation with the CIDR netmask length.

| Netmask | CIDR length |
|---|---|
| 255.255.192.0 | ______ |
| 255.255.255.192 | ______ |
| 255.0.0.0 | ______ |
| 255.255.255.240 | ______ |
| 255.255.255.252 | ______ |

### 8. In *classless interdomain routing (CIDR)*, an IP address is divided into _____ parts.
A) continent, country and network  
B) network, subnet and host  
C) network and host  
D) network, link and host  
E) country, area and network

### 9. The maximum number of hosts (including the router interface) in a network with the netmask /27 is: _____.
A) 31  
B) 30  
C) 27  
D) 224  
E) 32

### 10. The *last* IP address (broadcast address) in the network 10.8.96.0/23 is _____.

**Answer:** ______

### 11. The network 64.23.32.0/19 is to be divided into 16 equal-sized networks. The *second* of these sub-networks (i.e., sub-network number 1) is (give your answer in the CIDR notation).

**Answer:** ______

### 12. A packet with a destination address *not* in the local network is forwarded to a _____.

**Answer:** ______

### 13. The *address resolution protocol (ARP)* _____.
A) resolves a hostname into an IP address  
B) converts an Ethernet address into a MAC address  
C) returns an IP address given a MAC address  
D) returns an IP address given an Ethernet address  
E) returns a MAC address given an IP address

### 14. ICMP messages are used to (select all that apply)
A) configure routers  
B) report errors  
C) deliver IP packets  
D) communicate network-level information  
E) test the reachability of a host

### 15. *Network Address Translation (NAT)* was introduced _____.
A) to connect corporate networks to the Internet  
B) to allow IPv6 hosts to use IPv4 networks  
C) to convert packets between IPv4 and IPv6 networks  
D) to allow IPv4 hosts to use IPv6 networks  
E) due to the shortage of IPv4 addresses

### 16. A disadvantage of NAT is that _____.
A) hosts in a network cannot be addressed from the Internet  
B) it does not support IP6  
C) the ISP cannot be changed without re-numbering the network  
D) it is not widely used  
E) it only supports PCs

# Answer Key & Explanations

### 1. In an IP network, an end-system is generally called a _____.

**Correct:** host  
**Explanation:** A host is an end system that originates or receives network communication.

### 2. A device which forwards packets from one IP network to another is called a _____.

**Correct:** router  
**Explanation:** A router forwards IP packets between different networks.

### 3. A reasonable value for the contents of the *version* header is _____.

**Correct:** 4  
**Explanation:** An IPv4 packet carries the value `4` in its IP version field.

### 4. A packet is _____ when its TTL reaches 0.
A) ✓ The router discards the packet and normally returns an ICMP Time Exceeded message.  
B) ✗ The original IP packet is not simply returned to its sender.  
C) ✗ TTL expiration is unrelated to waiting for an output link.  
D) ✗ A router must not forward a packet after its TTL has expired.  
E) ✗ The packet is discarded, but an ICMP Time Exceeded message is normally generated.

**Correct:** A

### 5. An IP address identifies _____.
A) ✓ An IP address is assigned to a network interface.  
B) ✗ A router normally has multiple interfaces and therefore multiple IP addresses.  
C) ✗ A subnet is identified by a network prefix, not by one interface address alone.  
D) ✗ A datagram carries addresses but is not itself what an IP address identifies.  
E) ✗ Saying it identifies a host is an oversimplification; technically the address identifies an interface.

**Correct:** A

### 6. _____ addressing is no longer used due to inefficient address allocation.

**Correct:** class-full (classful)  
**Explanation:** Classful addressing fixed networks into A/B/C sizes, often wasting address space; CIDR replaced it.

### 7. For each of the netmasks, match the dotted quad notation with the CIDR netmask length.
- **255.255.192.0 → /18** — 18 leading 1-bits.  
- **255.255.255.192 → /26** — 26 leading 1-bits.  
- **255.0.0.0 → /8** — 8 leading 1-bits.  
- **255.255.255.240 → /28** — 28 leading 1-bits.  
- **255.255.255.252 → /30** — 30 leading 1-bits.

**Correct:** /18, /26, /8, /28, /30 respectively

### 8. In *classless interdomain routing (CIDR)*, an IP address is divided into _____ parts.
A) ✗ CIDR does not encode continent or country fields.  
B) ✗ CIDR does not require a separate fixed subnet field.  
C) ✓ CIDR treats the address as a variable-length network prefix plus a host portion.  
D) ✗ There is no separate link field in the CIDR address structure.  
E) ✗ Country and area are not IP address fields.

**Correct:** C

### 9. The maximum number of hosts (including the router interface) in a network with the netmask /27 is: _____.
A) ✗ A /27 contains 32 total addresses, but one is the network address and one is the broadcast address.  
B) ✓ A /27 therefore has `32 - 2 = 30` usable host/interface addresses.  
C) ✗ 27 is the prefix length, not the host count.  
D) ✗ 224 is unrelated to the number of usable addresses in a /27.  
E) ✗ 32 is the total number of addresses, not the usable host count.

**Correct:** B

> **Source discrepancy:** The original Moodle review marks **A) 31** as correct. Standard IPv4 subnetting gives **30 usable host addresses** for a /27, so the original quiz key appears to be wrong on this item.

### 10. The *last* IP address (broadcast address) in the network 10.8.96.0/23 is _____.

**Correct:** 10.8.97.255  
**Explanation:** A /23 spans `10.8.96.0` through `10.8.97.255`; the final address is the broadcast address.

### 11. The network 64.23.32.0/19 is to be divided into 16 equal-sized networks. The *second* of these sub-networks (i.e., sub-network number 1) is (give your answer in the CIDR notation).

**Correct:** 64.23.34.0/23  
**Explanation:** Dividing a /19 into 16 subnets adds 4 prefix bits, producing /23 networks. They advance by 2 in the third octet: 32, 34, 36, ...

### 12. A packet with a destination address *not* in the local network is forwarded to a _____.

**Correct:** router  
**Explanation:** The host sends non-local traffic to a router/default gateway for forwarding.

### 13. The *address resolution protocol (ARP)* _____.
A) ✗ Hostname-to-IP resolution is performed by DNS.  
B) ✗ An Ethernet address and a MAC address refer to the same Layer-2 address concept.  
C) ✗ ARP does not normally map MAC addresses back to IP addresses.  
D) ✗ This is not ARP's normal direction of resolution.  
E) ✓ ARP resolves a local IPv4 address to the corresponding MAC address.

**Correct:** E

### 14. ICMP messages are used to (select all that apply)
A) ✗ ICMP is not a router configuration protocol.  
B) ✓ ICMP reports network-layer errors such as destination unreachable and time exceeded.  
C) ✗ Normal IP payload delivery is performed by IP, not ICMP.  
D) ✓ ICMP carries control and diagnostic information about IP-layer conditions.  
E) ✓ ICMP Echo Request/Reply is used by tools such as `ping` to test reachability.

**Correct:** B,D,E

### 15. *Network Address Translation (NAT)* was introduced _____.
A) ✗ Connecting corporate networks to the Internet is broader than NAT's original motivation.  
B) ✗ NAT is not primarily an IPv6-to-IPv4 host compatibility mechanism.  
C) ✗ Protocol translation between IPv4 and IPv6 is a different function.  
D) ✗ NAT was not introduced to let IPv4 hosts use IPv6 networks.  
E) ✓ NAT helped conserve public IPv4 addresses by allowing many private hosts to share fewer public addresses.

**Correct:** E

### 16. A disadvantage of NAT is that _____.
A) ✓ NAT breaks straightforward end-to-end addressing; internal hosts are not normally directly reachable from the Internet without explicit mappings.  
B) ✗ The statement is too broad and is not the principal disadvantage tested here.  
C) ✗ NAT can actually reduce the need to renumber internal private addresses when changing ISPs.  
D) ✗ NAT is widely deployed.  
E) ✗ NAT is not limited to PCs.

**Correct:** A
