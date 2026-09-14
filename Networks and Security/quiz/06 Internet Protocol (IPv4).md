## 6 Internet Protocol (IPv4)

## Questions

#### 1. Which of the following fields are part of the IPv4 datagram header?  
A) Time to live (TTL)  
B) Source IP address  
C) MAC address  
D) Fragment offset  

#### 2. In IPv4 addressing, what does the network part of the address represent?  
A) The host identifier within a network  
B) The high-order bits identifying the network segment  
C) The physical location of the device  
D) The low-order bits identifying the subnet mask  

#### 3. Which statements about CIDR (Classless Inter-Domain Routing) are true?  
A) It allows the network portion of an IP address to be of arbitrary length  
B) It eliminates the need for subnet masks  
C) It improves address space utilization compared to classful addressing  
D) It uses fixed network classes like Class A, B, and C  

#### 4. What is the purpose of the broadcast address in an IPv4 network?  
A) To identify the network itself  
B) To send packets to all hosts on the network simultaneously  
C) To assign IP addresses dynamically  
D) To specify the default gateway  

#### 5. How does a host typically obtain its IP address dynamically?  
A) By manually configuring it in a system file  
B) Through DHCP, which involves a discover, offer, request, and acknowledgment process  
C) By querying the DNS server  
D) By broadcasting an ARP request  

#### 6. Which of the following are functions of the ICMP protocol?  
A) Error reporting such as destination unreachable  
B) Echo request and reply for ping operations  
C) Routing table updates between routers  
D) Congestion control via source quench messages  

#### 7. When a router receives an IP datagram destined for a host on a directly connected network, what happens?  
A) The router forwards the datagram to the next hop router  
B) The router sends the datagram directly to the host using link-layer addressing  
C) The router drops the datagram if the host is unreachable  
D) The router encapsulates the datagram in a new IP header  

#### 8. What problem does the Address Resolution Protocol (ARP) solve?  
A) Mapping IP addresses to MAC addresses on a local network  
B) Assigning IP addresses dynamically to hosts  
C) Translating domain names to IP addresses  
D) Discovering the route to a remote network  

#### 9. Which of the following statements about NAT (Network Address Translation) are correct?  
A) NAT allows multiple devices on a local network to share a single public IP address  
B) NAT violates the end-to-end principle of the Internet architecture  
C) NAT requires routers to modify transport layer port numbers in outgoing packets  
D) NAT makes devices inside the local network directly addressable from the Internet  

#### 10. How does a NAT router handle incoming datagrams from the Internet destined for a host inside the local network?  
A) It forwards the datagram unchanged to the host’s private IP address  
B) It replaces the destination IP and port with the corresponding private IP and port from its translation table  
C) It broadcasts the datagram to all hosts on the local network  
D) It drops the datagram if no matching translation entry exists  

#### 11. Which of the following are true about IP address classes in classful addressing?  
A) Class B networks allocate 16 bits for the network part and 16 bits for the host part  
B) Class C networks support more hosts than Class A networks  
C) Classful addressing is inefficient and largely obsolete due to address space exhaustion  
D) Multicast addresses belong to Class D  

#### 12. What is the significance of the TTL (Time to Live) field in an IP datagram?  
A) It specifies the maximum number of hops a datagram can traverse before being discarded  
B) It indicates the time in seconds the datagram is valid  
C) It is decremented by one at each router the datagram passes through  
D) It is used to prioritize packets in the network  

#### 13. Which of the following are true regarding hierarchical addressing and route aggregation?  
A) It allows multiple networks to be represented by a single routing table entry  
B) It reduces the size of routing tables in routers  
C) It requires each host to have a unique global IP address without subnetting  
D) It enables ISPs to allocate address blocks to customers efficiently  

#### 14. In the context of DHCP, what is the correct sequence of messages exchanged between a host and a DHCP server?  
A) DHCP offer → DHCP discover → DHCP request → DHCP ack  
B) DHCP discover → DHCP offer → DHCP request → DHCP ack  
C) DHCP request → DHCP discover → DHCP offer → DHCP ack  
D) DHCP discover → DHCP request → DHCP offer → DHCP ack  

#### 15. Which of the following statements about IP fragmentation and reassembly are correct?  
A) The fragment offset field indicates the position of a fragment’s data within the original datagram  
B) Routers may fragment datagrams if the next link’s MTU is smaller than the datagram size  
C) The identification field is used to match fragments belonging to the same original datagram  
D) Fragmentation is handled only at the destination host, not by intermediate routers



<br>

## Answers

#### 1. Which of the following fields are part of the IPv4 datagram header?  
A) ✓ Time to live (TTL) is a standard IPv4 header field used to limit packet lifetime.  
B) ✓ Source IP address is included in the IPv4 header to identify the sender.  
C) ✗ MAC address is a link-layer address, not part of the IP header.  
D) ✓ Fragment offset is part of the IPv4 header for fragmentation/reassembly.  

**Correct:** A, B, D


#### 2. In IPv4 addressing, what does the network part of the address represent?  
A) ✗ The host identifier is the low-order bits, not the network part.  
B) ✓ The network part is the high-order bits identifying the network segment.  
C) ✗ Physical location is not encoded in the IP address.  
D) ✗ The low-order bits represent the host part, not the network part.  

**Correct:** B


#### 3. Which statements about CIDR (Classless Inter-Domain Routing) are true?  
A) ✓ CIDR allows arbitrary length for the network portion of the address.  
B) ✗ CIDR still uses subnet masks (network masks) to define network boundaries.  
C) ✓ CIDR improves address space utilization compared to classful addressing.  
D) ✗ CIDR replaces fixed classes; classful addressing uses fixed classes.  

**Correct:** A, C


#### 4. What is the purpose of the broadcast address in an IPv4 network?  
A) ✗ The network address identifies the network, not the broadcast address.  
B) ✓ Broadcast address is used to send packets to all hosts on the network.  
C) ✗ Broadcast address is not used for dynamic IP assignment.  
D) ✗ Default gateway is a router address, not the broadcast address.  

**Correct:** B


#### 5. How does a host typically obtain its IP address dynamically?  
A) ✗ Manual configuration is static, not dynamic.  
B) ✓ DHCP uses discover, offer, request, and acknowledgment messages.  
C) ✗ DNS resolves names to IPs, not IP assignment.  
D) ✗ ARP resolves IP to MAC, not IP assignment.  

**Correct:** B


#### 6. Which of the following are functions of the ICMP protocol?  
A) ✓ ICMP reports errors like destination unreachable.  
B) ✓ ICMP supports echo request/reply used by ping.  
C) ✗ Routing updates are handled by routing protocols, not ICMP.  
D) ✓ Source quench is an ICMP message for congestion control (though rarely used).  

**Correct:** A, B, D


#### 7. When a router receives an IP datagram destined for a host on a directly connected network, what happens?  
A) ✗ No next hop router needed if host is directly connected.  
B) ✓ Router sends datagram directly to host using link-layer addressing.  
C) ✗ Router does not drop datagram if host is reachable.  
D) ✗ No new IP header encapsulation occurs in this case.  

**Correct:** B


#### 8. What problem does the Address Resolution Protocol (ARP) solve?  
A) ✓ ARP maps IP addresses to MAC addresses on local networks.  
B) ✗ DHCP assigns IP addresses dynamically, not ARP.  
C) ✗ DNS resolves domain names, unrelated to ARP.  
D) ✗ Route discovery is done by routing protocols, not ARP.  

**Correct:** A


#### 9. Which of the following statements about NAT (Network Address Translation) are correct?  
A) ✓ NAT allows multiple devices to share a single public IP address.  
B) ✓ NAT violates the end-to-end principle by modifying transport info.  
C) ✓ NAT modifies source port numbers to maintain unique connections.  
D) ✗ Devices inside local network are not directly addressable from outside.  

**Correct:** A, B, C


#### 10. How does a NAT router handle incoming datagrams from the Internet destined for a host inside the local network?  
A) ✗ NAT must translate the destination address; it cannot forward unchanged.  
B) ✓ NAT replaces destination IP and port with private IP and port from its table.  
C) ✗ NAT does not broadcast incoming datagrams to all hosts.  
D) ✓ NAT drops datagrams if no matching translation entry exists.  

**Correct:** B, D


#### 11. Which of the following are true about IP address classes in classful addressing?  
A) ✓ Class B uses 16 bits for network and 16 bits for host parts.  
B) ✗ Class C supports fewer hosts than Class A, not more.  
C) ✓ Classful addressing is inefficient and obsolete due to address exhaustion.  
D) ✓ Multicast addresses belong to Class D.  

**Correct:** A, C, D


#### 12. What is the significance of the TTL (Time to Live) field in an IP datagram?  
A) ✓ TTL limits the number of hops before discarding a datagram.  
B) ✗ TTL is not measured in seconds but in hops.  
C) ✓ TTL is decremented by one at each router hop.  
D) ✗ TTL is not used for packet prioritization.  

**Correct:** A, C


#### 13. Which of the following are true regarding hierarchical addressing and route aggregation?  
A) ✓ Multiple networks can be represented by a single routing table entry.  
B) ✓ This reduces routing table size in routers.  
C) ✗ Hosts still need unique IPs; subnetting is part of hierarchical addressing.  
D) ✓ ISPs allocate address blocks efficiently using hierarchical addressing.  

**Correct:** A, B, D


#### 14. In the context of DHCP, what is the correct sequence of messages exchanged between a host and a DHCP server?  
A) ✗ Incorrect order; offer must follow discover.  
B) ✓ Correct order: discover → offer → request → ack.  
C) ✗ Request cannot precede discover and offer.  
D) ✗ Offer cannot come after request.  

**Correct:** B


#### 15. Which of the following statements about IP fragmentation and reassembly are correct?  
A) ✓ Fragment offset indicates the fragment’s position in the original datagram.  
B) ✓ Routers may fragment datagrams if MTU is smaller than datagram size.  
C) ✓ Identification field matches fragments belonging to the same datagram.  
D) ✗ Fragmentation can be done by intermediate routers, not only destination hosts.  

**Correct:** A, B, C