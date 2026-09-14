## 6 Internet Protocol (IPv4)

## Questions

#### 1. Which of the following fields are part of the IPv4 datagram header?  
A) Source and destination IP addresses  
B) Fragment offset for fragmentation and reassembly  
C) MAC address of the sender  
D) Time to live (TTL)  

#### 2. Regarding IP addressing and subnetting, which statements are true?  
A) The broadcast address is the first address in a network and can be assigned to a host.  
B) CIDR allows the network portion of an IP address to be of arbitrary length.  
C) A larger network has more bits allocated for the network part and fewer bits for the host part.  
D) Hosts with the same network part of the IP address can communicate without a router.  

#### 3. Which of the following describe the role and operation of the Address Resolution Protocol (ARP)?  
A) ARP broadcasts a request asking “Who has this IP address?”  
B) ARP resolves IP addresses to MAC addresses on the local network.  
C) ARP is used to route packets between different IP networks.  
D) ARP sends unicast frames to discover the MAC address of a host.  

#### 4. What are the main functions and characteristics of Network Address Translation (NAT)?  
A) NAT modifies the source IP address and port number of outgoing packets.  
B) NAT allows multiple devices on a local network to share a single public IP address.  
C) NAT requires maintaining a translation table to map internal addresses to external ones.  
D) NAT enables devices inside the local network to be directly addressable from the Internet.  

#### 5. Which of the following are true about ICMP (Internet Control Message Protocol)?  
A) An ICMP message includes a type, code, and part of the original IP datagram causing the error.  
B) ICMP messages are carried inside IP datagrams.  
C) ICMP is used for error reporting and network diagnostics like ping.  
D) ICMP operates at the transport layer alongside TCP and UDP.  

#### 6. How does DHCP (Dynamic Host Configuration Protocol) facilitate IP address assignment?  
A) DHCP servers assign IP addresses permanently to hosts.  
B) DHCP allows hosts to renew their IP address lease dynamically.  
C) Hosts broadcast a DHCP Discover message to find available DHCP servers.  
D) DHCP requires manual configuration of IP addresses on each host.  

#### 7. Consider the hierarchical addressing and routing aggregation in IP networks. Which statements are correct?  
A) Hierarchical addressing allows multiple networks to be routed with a single routing table entry.  
B) Route aggregation reduces the size of routing tables by grouping addresses with common prefixes.  
C) Each router interface must have a unique IP address belonging to different networks.  
D) Hierarchical addressing eliminates the need for routers in large internetworks.  

#### 8. In the context of IP datagram forwarding, which of the following are accurate?  
A) Routers use forwarding tables to determine the next hop for a datagram based on the destination network.  
B) If the destination is on the same network as the sender, the datagram is sent directly using link-layer addressing.  
C) The IP datagram’s source and destination addresses remain unchanged as it travels through routers.  
D) The IP header’s TTL field is incremented by one at each router to track the number of hops.  



<br>

## Answers

#### 1. Which of the following fields are part of the IPv4 datagram header?  
A) ✓ Source and destination IP addresses are essential parts of the IPv4 header.  
B) ✓ Fragment offset is included in the IPv4 header for fragmentation and reassembly.  
C) ✗ MAC address is a link-layer address, not part of the IP header.  
D) ✓ Time to live (TTL) is a standard IPv4 header field used to limit packet lifetime.  

**Correct:** A, B, D


#### 2. Regarding IP addressing and subnetting, which statements are true?  
A) ✗ Broadcast address is the last address in a network and cannot be assigned to a host.  
B) ✓ CIDR allows flexible network prefix lengths, not limited to classful boundaries.  
C) ✗ Larger networks have fewer bits for the network part and more bits for the host part.  
D) ✓ Hosts with the same network part can communicate directly without a router.  

**Correct:** B, D


#### 3. Which of the following describe the role and operation of the Address Resolution Protocol (ARP)?  
A) ✓ ARP broadcasts a request asking “Who has this IP address?” to find the MAC.  
B) ✓ ARP resolves IP addresses to MAC addresses on the local network.  
C) ✗ ARP does not route packets between networks; it operates only on local links.  
D) ✗ ARP uses broadcast frames, not unicast, to discover MAC addresses.  

**Correct:** A, B


#### 4. What are the main functions and characteristics of Network Address Translation (NAT)?  
A) ✓ NAT modifies source IP and port numbers of outgoing packets to map internal to external addresses.  
B) ✓ NAT allows multiple devices to share a single public IP address.  
C) ✓ NAT maintains a translation table to map internal addresses and ports to external ones.  
D) ✗ Devices inside the local network are not directly addressable from outside due to NAT.  

**Correct:** A, B, C


#### 5. Which of the following are true about ICMP (Internet Control Message Protocol)?  
A) ✓ ICMP messages include type, code, and part of the original IP datagram causing the error.  
B) ✓ ICMP messages are encapsulated inside IP datagrams.  
C) ✓ ICMP is used for error reporting and network diagnostics such as ping.  
D) ✗ ICMP operates at the network layer, not the transport layer like TCP/UDP.  

**Correct:** A, B, C


#### 6. How does DHCP (Dynamic Host Configuration Protocol) facilitate IP address assignment?  
A) ✗ DHCP assigns IP addresses temporarily with leases, not permanently.  
B) ✓ DHCP allows hosts to renew their IP address lease dynamically.  
C) ✓ Hosts broadcast DHCP Discover messages to locate DHCP servers.  
D) ✗ DHCP eliminates the need for manual IP configuration by automating address assignment.  

**Correct:** B, C


#### 7. Consider the hierarchical addressing and routing aggregation in IP networks. Which statements are correct?  
A) ✓ Hierarchical addressing enables routing multiple networks with a single routing table entry.  
B) ✓ Route aggregation reduces routing table size by grouping addresses with common prefixes.  
C) ✓ Each router interface must have a unique IP address on different networks to route properly.  
D) ✗ Hierarchical addressing does not eliminate routers; routers are essential for inter-network communication.  

**Correct:** A, B, C


#### 8. In the context of IP datagram forwarding, which of the following are accurate?  
A) ✓ Routers use forwarding tables to determine the next hop based on the destination network.  
B) ✓ If destination is on the same network, the datagram is sent directly using link-layer addressing.  
C) ✓ Source and destination IP addresses remain unchanged as the datagram passes through routers.  
D) ✗ TTL is decremented by one at each router to prevent infinite looping, not incremented.  

**Correct:** A, B, C