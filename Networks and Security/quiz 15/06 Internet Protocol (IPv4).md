## 6 Internet Protocol (IPv4)

## Questions

#### 1. Which of the following fields are part of the IPv4 datagram header?  
A) Fragment offset  
B) Source IP address  
C) Time to live (TTL)  
D) MAC address  

#### 2. In IPv4 addressing, what does the network part of the address represent?  
A) The low-order bits identifying the subnet mask  
B) The host identifier within a network  
C) The physical location of the device  
D) The high-order bits identifying the network segment  

#### 3. Which statements about CIDR (Classless Inter-Domain Routing) are true?  
A) It allows the network portion of an IP address to be of arbitrary length  
B) It uses fixed network classes like Class A, B, and C  
C) It eliminates the need for subnet masks  
D) It improves address space utilization compared to classful addressing  

#### 4. What is the purpose of the broadcast address in an IPv4 network?  
A) To send packets to all hosts on the network simultaneously  
B) To specify the default gateway  
C) To identify the network itself  
D) To assign IP addresses dynamically  

#### 5. How does a host typically obtain its IP address dynamically?  
A) Through DHCP, which involves a discover, offer, request, and acknowledgment process  
B) By broadcasting an ARP request  
C) By querying the DNS server  
D) By manually configuring it in a system file  

#### 6. Which of the following are functions of the ICMP protocol?  
A) Routing table updates between routers  
B) Congestion control via source quench messages  
C) Error reporting such as destination unreachable  
D) Echo request and reply for ping operations  

#### 7. When a router receives an IP datagram destined for a host on a directly connected network, what happens?  
A) The router sends the datagram directly to the host using link-layer addressing  
B) The router forwards the datagram to the next hop router  
C) The router drops the datagram if the host is unreachable  
D) The router encapsulates the datagram in a new IP header  

#### 8. What problem does the Address Resolution Protocol (ARP) solve?  
A) Translating domain names to IP addresses  
B) Assigning IP addresses dynamically to hosts  
C) Discovering the route to a remote network  
D) Mapping IP addresses to MAC addresses on a local network  

#### 9. Which of the following statements about NAT (Network Address Translation) are correct?  
A) NAT violates the end-to-end principle of the Internet architecture  
B) NAT makes devices inside the local network directly addressable from the Internet  
C) NAT allows multiple devices on a local network to share a single public IP address  
D) NAT requires routers to modify transport layer port numbers in outgoing packets  

#### 10. How does a NAT router handle incoming datagrams from the Internet destined for a host inside the local network?  
A) It replaces the destination IP and port with the corresponding private IP and port from its translation table  
B) It broadcasts the datagram to all hosts on the local network  
C) It forwards the datagram unchanged to the host’s private IP address  
D) It drops the datagram if no matching translation entry exists  

#### 11. Which of the following are true about IP address classes in classful addressing?  
A) Classful addressing is inefficient and largely obsolete due to address space exhaustion  
B) Multicast addresses belong to Class D  
C) Class C networks support more hosts than Class A networks  
D) Class B networks allocate 16 bits for the network part and 16 bits for the host part  

#### 12. What is the significance of the TTL (Time to Live) field in an IP datagram?  
A) It is used to prioritize packets in the network  
B) It is decremented by one at each router the datagram passes through  
C) It indicates the time in seconds the datagram is valid  
D) It specifies the maximum number of hops a datagram can traverse before being discarded  

#### 13. Which of the following are true regarding hierarchical addressing and route aggregation?  
A) It allows multiple networks to be represented by a single routing table entry  
B) It reduces the size of routing tables in routers  
C) It enables ISPs to allocate address blocks to customers efficiently  
D) It requires each host to have a unique global IP address without subnetting  

#### 14. In the context of DHCP, what is the correct sequence of messages exchanged between a host and a DHCP server?  
A) DHCP discover → DHCP request → DHCP offer → DHCP ack  
B) DHCP discover → DHCP offer → DHCP request → DHCP ack  
C) DHCP offer → DHCP discover → DHCP request → DHCP ack  
D) DHCP request → DHCP discover → DHCP offer → DHCP ack  

#### 15. Which of the following statements about IP fragmentation and reassembly are correct?  
A) Fragmentation is handled only at the destination host, not by intermediate routers  
B) The fragment offset field indicates the position of a fragment’s data within the original datagram  
C) The identification field is used to match fragments belonging to the same original datagram  
D) Routers may fragment datagrams if the next link’s MTU is smaller than the datagram size  



<br>

## Answers

#### 1. Which of the following fields are part of the IPv4 datagram header?  
A) ✓ Fragment offset is part of the IPv4 header for fragmentation/reassembly.  
B) ✓ Source IP address is included in the IPv4 header to identify the sender.  
C) ✓ Time to live (TTL) is a standard IPv4 header field used to limit packet lifetime.  
D) ✗ MAC address is a link-layer address, not part of the IP header.  

**Correct:** A, B, C


#### 2. In IPv4 addressing, what does the network part of the address represent?  
A) ✗ The low-order bits represent the host part, not the network part.  
B) ✗ The host identifier is the low-order bits, not the network part.  
C) ✗ Physical location is not encoded in the IP address.  
D) ✓ The network part is the high-order bits identifying the network segment.  

**Correct:** D


#### 3. Which statements about CIDR (Classless Inter-Domain Routing) are true?  
A) ✓ CIDR allows arbitrary length for the network portion of the address.  
B) ✗ CIDR replaces fixed classes; classful addressing uses fixed classes.  
C) ✗ CIDR still uses subnet masks (network masks) to define network boundaries.  
D) ✓ CIDR improves address space utilization compared to classful addressing.  

**Correct:** A, D


#### 4. What is the purpose of the broadcast address in an IPv4 network?  
A) ✓ Broadcast address is used to send packets to all hosts on the network.  
B) ✗ Default gateway is a router address, not the broadcast address.  
C) ✗ The network address identifies the network, not the broadcast address.  
D) ✗ Broadcast address is not used for dynamic IP assignment.  

**Correct:** A


#### 5. How does a host typically obtain its IP address dynamically?  
A) ✓ DHCP uses discover, offer, request, and acknowledgment messages.  
B) ✗ ARP resolves IP to MAC, not IP assignment.  
C) ✗ DNS resolves names to IPs, not IP assignment.  
D) ✗ Manual configuration is static, not dynamic.  

**Correct:** A


#### 6. Which of the following are functions of the ICMP protocol?  
A) ✗ Routing updates are handled by routing protocols, not ICMP.  
B) ✓ Source quench is an ICMP message for congestion control (though rarely used).  
C) ✓ ICMP reports errors like destination unreachable.  
D) ✓ ICMP supports echo request/reply used by ping.  

**Correct:** B, C, D


#### 7. When a router receives an IP datagram destined for a host on a directly connected network, what happens?  
A) ✓ Router sends datagram directly to host using link-layer addressing.  
B) ✗ No next hop router needed if host is directly connected.  
C) ✗ Router does not drop datagram if host is reachable.  
D) ✗ No new IP header encapsulation occurs in this case.  

**Correct:** A


#### 8. What problem does the Address Resolution Protocol (ARP) solve?  
A) ✗ DNS resolves domain names, unrelated to ARP.  
B) ✗ DHCP assigns IP addresses dynamically, not ARP.  
C) ✗ Route discovery is done by routing protocols, not ARP.  
D) ✓ ARP maps IP addresses to MAC addresses on local networks.  

**Correct:** D


#### 9. Which of the following statements about NAT (Network Address Translation) are correct?  
A) ✓ NAT violates the end-to-end principle by modifying transport info.  
B) ✗ Devices inside local network are not directly addressable from outside.  
C) ✓ NAT allows multiple devices to share a single public IP address.  
D) ✓ NAT modifies source port numbers to maintain unique connections.  

**Correct:** A, C, D


#### 10. How does a NAT router handle incoming datagrams from the Internet destined for a host inside the local network?  
A) ✓ NAT replaces destination IP and port with private IP and port from its table.  
B) ✗ NAT does not broadcast incoming datagrams to all hosts.  
C) ✗ NAT must translate the destination address; it cannot forward unchanged.  
D) ✓ NAT drops datagrams if no matching translation entry exists.  

**Correct:** A, D


#### 11. Which of the following are true about IP address classes in classful addressing?  
A) ✓ Classful addressing is inefficient and obsolete due to address exhaustion.  
B) ✓ Multicast addresses belong to Class D.  
C) ✗ Class C supports fewer hosts than Class A, not more.  
D) ✓ Class B uses 16 bits for network and 16 bits for host parts.  

**Correct:** A, B, D


#### 12. What is the significance of the TTL (Time to Live) field in an IP datagram?  
A) ✗ TTL is not used for packet prioritization.  
B) ✓ TTL is decremented by one at each router hop.  
C) ✗ TTL is not measured in seconds but in hops.  
D) ✓ TTL limits the number of hops before discarding a datagram.  

**Correct:** B, D


#### 13. Which of the following are true regarding hierarchical addressing and route aggregation?  
A) ✓ Multiple networks can be represented by a single routing table entry.  
B) ✓ This reduces routing table size in routers.  
C) ✓ ISPs allocate address blocks efficiently using hierarchical addressing.  
D) ✗ Hosts still need unique IPs; subnetting is part of hierarchical addressing.  

**Correct:** A, B, C


#### 14. In the context of DHCP, what is the correct sequence of messages exchanged between a host and a DHCP server?  
A) ✗ Offer cannot come after request.  
B) ✓ Correct order: discover → offer → request → ack.  
C) ✗ Incorrect order; offer must follow discover.  
D) ✗ Request cannot precede discover and offer.  

**Correct:** B


#### 15. Which of the following statements about IP fragmentation and reassembly are correct?  
A) ✗ Fragmentation can be done by intermediate routers, not only destination hosts.  
B) ✓ Fragment offset indicates the fragment’s position in the original datagram.  
C) ✓ Identification field matches fragments belonging to the same datagram.  
D) ✓ Routers may fragment datagrams if MTU is smaller than datagram size.  

**Correct:** B, C, D