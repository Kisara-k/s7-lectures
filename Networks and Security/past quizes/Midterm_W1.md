# Midterm W1

### 1. An OSI layer which handles Repeating or amplification to extend range of transmission is:

**Answer:** ______

### 2. Although the OSI Network protocols are not used now, we still study the OSI Reference Model. Why?

**Answer:** ______

### 3. A system uses go-back-N ARQ and uses a 3-bit field to store state variables. After the sender has sent frame 2, it receives a NAK(5). It will resend the frames
A) 5  
B) 2  
C) 5,6,7,0,1,2  
D) 2,3,4  
E) 6,7,1  
F) 2,3,4,5

### 4. A primary station **polls** a secondary to find out if
A) it has been selected  
B) it has received data  
C) it has data to send

### 5. All packets belonging to the same _____ have the same MPLS label.
A) service  
B) host  
C) network  
D) flow

### 6. ATM is popular in _____.
A) low-speed networks  
B) backbone networks  
C) wireless mobile networks  
D) local area networks

### 7. Which of the following is *not* correct?
A) Several VLANS can exist in one switch  
B) Tag Control Information informs a VLAN switch that it is a VLAN frame  
C) Tag Control Information provides the VLAN number  
D) One VLAN can be spanned across several switches

### 8. Two types of media used in Ethernet First Mile are:
A) fibre and copper  
B) radio and laser  
C) radio and microwave  
D) copper and microwave  
E) copper and radio

### 9. Name two common media types used in Ethernet and show the typical range of speeds supported on each of the media types.

**Answer:** ______

### 10. The functions of the Network Layer are: (select all that apply)
A) routing  
B) terminating connections  
C) synchronisation  
D) addressing  
E) error correction

### 11. Nodes on a connectionless network _____ the destination address of packets passing through them.
A) always increment  
B) usually change  
C) never change  
D) always change  
E) always decrement

### 12. The result of the routing process on each router is to build a _____ table.

**Answer:** ______

### 13. In the internet model, an internet consists of a set of _____ connected by _____.
A) networks, hosts  
B) Ethernets, bridges  
C) networks, routers  
D) networks, gateways  
E) Ethernets, switches

### 14. Briefly explain how two packets could be delivered by a connectionless network in a different order from which they were transmitted.

**Answer:** ______

### 15. The *time-to-live (TTL)* field contains _____ of a packet.
A) the age, in seconds  
B) the remaining lifetime, in seconds  
C) the remaining lifetime, in milliseconds  
D) the remaining number of hops  
E) the age, in milliseconds

### 16. In *classless interdomain routing (CIDR)*, an IP address is divided into _____ parts.
A) network and host  
B) network, link and host  
C) country, area and network  
D) continent, country and network  
E) network, subnet and host

### 17. A network with 5 hosts should have a netmask of (use the /xx notation)

**Answer:** ______

### 18. The network 64.23.32.0/19 is to be divided into 16 equal-sized networks. The *third* of these sub-networks (i.e., sub-network number 2) is (give your answer in the CIDR notation).

**Answer:** ______

### 19. DHCP *leases* IP addresses to _____.
A) reduce the cost of IP addresses  
B) allow two or more hosts to share an IP address  
C) reuse the addresses of hosts no longer on the network  
D) allow hosts to temporarily use an IP address from a different network  
E) change IP addresses frequently

### 20. *Network Address Translation (NAT)* was introduced _____.
A) to allow IPv4 hosts to use IPv6 networks  
B) to convert packets between IPv4 and IPv6 networks  
C) to allow IPv6 hosts to use IPv4 networks  
D) to connect corporate networks to the Internet  
E) due to the shortage of IPv4 addresses

### 21. In Dijkstra's lowest cost path algorithm, a node is added to the set of nodes with known costs if it _____.
A) is of a different colour than the remaining nodes  
B) is the next hop on the shortest path from the source to the destination  
C) has the lowest current cost out of the remaining nodes  
D) is closest to the current node  
E) has the lowest number of hops to the source

### 22. In OSPF, each router sends out an update
A) when it receives an update from another node  
B) whenever a link goes down or comes up  
C) the cost of a local link changes or when it receives an update from another node  
D) every 1 minute  
E) each time link cost information changes

### 23. Match the routing algorithms with the routing protocol names

| Routing algorithm | Protocol |
|---|---|
| Link State | ______ |
| Path Vector | ______ |
| Distance Vector | ______ |

### 24. A *privacy address* is formed by using _____ as the lower 64 bits of an IPv6 address.
A) the inverse of the MAC address  
B) another host's MAC address  
C) a NAT address  
D) a modified MAC address  
E) a 64-bit random number

# Answer Key & Explanations

### 1. An OSI layer which handles Repeating or amplification to extend range of transmission is:

**Correct:** Physical layer  
**Explanation:** Repeaters and signal regeneration/amplification operate on raw physical signals at Layer 1.

### 2. Although the OSI Network protocols are not used now, we still study the OSI Reference Model. Why?

**Correct:** It provides a structured standard/reference model for network communication and separates the required networking functions into layers.  
**Explanation:** Even when the OSI protocol suite itself is not used, the model remains useful for describing, designing, and troubleshooting network functions.

### 3. A system uses go-back-N ARQ and uses a 3-bit field to store state variables. After the sender has sent frame 2, it receives a NAK(5). It will resend the frames
A) ✗ Go-Back-N does not retransmit only frame 5 when later frames have already been sent.  
B) ✗ Frame 2 is the latest sent frame, not the first frame requested by NAK(5).  
C) ✓ With 3-bit sequence numbers the numbering wraps modulo 8; starting from 5, all outstanding frames through 2 are resent: 5,6,7,0,1,2.  
D) ✗ This starts at the wrong sequence number.  
E) ✗ This omits required outstanding frames and skips 0.  
F) ✗ This also starts at the wrong frame and does not reflect the wraparound sequence.

**Correct:** C

### 4. A primary station **polls** a secondary to find out if
A) ✗ Selection is used when the primary wants to send data to a secondary.  
B) ✗ Polling is not asking whether the secondary has already received data.  
C) ✓ Polling asks whether the secondary has data waiting to be transmitted.

**Correct:** C

### 5. All packets belonging to the same _____ have the same MPLS label.
A) ✗ A service may contain many distinct forwarding flows/classes.  
B) ✗ Labels are not assigned simply per host.  
C) ✗ Labels are not necessarily common to every packet in an entire network.  
D) ✓ In the terminology used by this course, packets in the same flow/forwarding class receive the same MPLS label.

**Correct:** D

### 6. ATM is popular in _____.
A) ✗ ATM was not mainly designed for low-speed networking.  
B) ✓ ATM's high-speed, fixed-size cell switching made it suitable for backbone networks.  
C) ✗ It is not primarily a wireless mobile-network technology.  
D) ✗ Ethernet became the dominant LAN technology instead.

**Correct:** B

### 7. Which of the following is *not* correct?
A) ✗ This statement is correct: one physical switch can support several VLANs.  
B) ✓ The 802.1Q **Tag Protocol Identifier (TPID)** identifies a tagged VLAN frame; the Tag Control Information does not perform that specific job.  
C) ✗ The TCI contains the VLAN Identifier (VID), so it provides the VLAN number.  
D) ✗ A single VLAN can span multiple switches using tagged trunk links.

**Correct:** B

### 8. Two types of media used in Ethernet First Mile are:
A) ✓ EFM standards include Ethernet over copper and Ethernet over fibre.  
B) ✗ Radio is not one of the two media types intended here.  
C) ✗ Neither pair matches EFM's copper/fibre access media.  
D) ✗ Microwave is not the second medium intended by the standard.  
E) ✗ Radio is not the intended EFM medium here.

**Correct:** A

### 9. Name two common media types used in Ethernet and show the typical range of speeds supported on each of the media types.

**Correct:** Example accepted answer: **fibre optic — roughly 100 Mbps to 10 Gbps; UTP copper — roughly 10 Mbps to 100 Mbps (or higher depending on Ethernet generation).**  
**Explanation:** Fibre supports long-distance/high-rate Ethernet, while twisted-pair copper is commonly used for shorter LAN links. The exact upper rates depend on the Ethernet standard being discussed.

### 10. The functions of the Network Layer are: (select all that apply)
A) ✓ Routing/path selection is a core network-layer function.  
B) ✓ In a connection-oriented network-layer service, connection establishment/termination is handled at this layer.  
C) ✗ Synchronisation is not a primary network-layer function.  
D) ✓ Logical addressing is a core network-layer function.  
E) ✗ End-to-end error correction is not normally a network-layer responsibility.

**Correct:** A,B,D

### 11. Nodes on a connectionless network _____ the destination address of packets passing through them.
A) ✗ Routers do not increment destination addresses.  
B) ✗ The destination address normally remains the same end-to-end.  
C) ✓ Forwarding nodes inspect the destination address but do not normally change it.  
D) ✗ It is not rewritten at every node.  
E) ✗ Destination addresses are not numeric counters that are decremented.

**Correct:** C

### 12. The result of the routing process on each router is to build a _____ table.

**Correct:** forwarding table  
**Explanation:** Routing calculations produce the information used to forward packets. Many texts call the resulting structure a *routing table*; this question's wording and the course answer use *forwarding table*.

### 13. In the internet model, an internet consists of a set of _____ connected by _____.
A) ✗ Hosts reside on networks; they are not what interconnects networks.  
B) ✗ Bridges interconnect LAN segments rather than defining the general Internet model.  
C) ✓ An internet is a collection of networks interconnected by routers.  
D) ✗ “Gateway” can be used broadly, but the specific Internet-layer device here is a router.  
E) ✗ This is too specific to Ethernet and switching.

**Correct:** C

### 14. Briefly explain how two packets could be delivered by a connectionless network in a different order from which they were transmitted.

**Correct:** Each datagram is routed independently, so two packets can take different routes or experience different queueing delays; the later packet can therefore arrive first.  
**Explanation:** A connectionless network does not reserve one fixed ordered path for all packets.

### 15. The *time-to-live (TTL)* field contains _____ of a packet.
A) ✗ TTL is not used as an increasing age counter.  
B) ✗ Although TTL was historically expressed in time units, in normal IP forwarding it functions as a hop limit.  
C) ✗ TTL is not a millisecond lifetime field.  
D) ✓ Each router decrements TTL, so it represents the remaining forwarding-hop allowance.  
E) ✗ It does not contain the packet's age in milliseconds.

**Correct:** D

### 16. In *classless interdomain routing (CIDR)*, an IP address is divided into _____ parts.
A) ✓ CIDR divides the address into a variable-length network prefix and a host portion.  
B) ✗ CIDR has no separate link field.  
C) ✗ Geographic fields are not part of the IP address format.  
D) ✗ CIDR does not encode continent/country fields.  
E) ✗ CIDR does not require a fixed separate subnet field.

**Correct:** A

### 17. A network with 5 hosts should have a netmask of (use the /xx notation)

**Correct:** /29  
**Explanation:** A /29 provides 8 total addresses and 6 usable host addresses, enough for 5 hosts.

### 18. The network 64.23.32.0/19 is to be divided into 16 equal-sized networks. The *third* of these sub-networks (i.e., sub-network number 2) is (give your answer in the CIDR notation).

**Correct:** 64.23.36.0/23  
**Explanation:** Splitting a /19 into 16 subnets adds 4 prefix bits, giving /23. The subnets begin at third-octet values 32 (#0), 34 (#1), 36 (#2), and so on.

### 19. DHCP *leases* IP addresses to _____.
A) ✗ Leasing is not primarily about the monetary cost of addresses.  
B) ✗ DHCP assigns an address to a client; it does not make multiple active hosts share one address.  
C) ✓ When a lease expires or a host leaves, the address can return to the pool and be reused.  
D) ✗ A DHCP server normally assigns an address valid on the client's own network.  
E) ✗ Address reuse is the goal; frequent arbitrary changes are not.

**Correct:** C

### 20. *Network Address Translation (NAT)* was introduced _____.
A) ✗ NAT was not introduced as an IPv4-over-IPv6 access method.  
B) ✗ IPv4/IPv6 protocol translation is a different transition mechanism.  
C) ✗ This was not NAT's original purpose.  
D) ✗ Connecting corporate networks is broader than the main motivation for NAT.  
E) ✓ NAT conserves scarce public IPv4 address space by allowing many private addresses behind fewer public addresses.

**Correct:** E

### 21. In Dijkstra's lowest cost path algorithm, a node is added to the set of nodes with known costs if it _____.
A) ✗ Node colour is only an implementation/visualization detail.  
B) ✗ The next hop to a destination is not the criterion for finalizing a node.  
C) ✓ Dijkstra repeatedly selects the unfinalized node with the smallest current tentative cost.  
D) ✗ “Closest to the current node” is not the algorithm's selection rule.  
E) ✗ Dijkstra minimizes path cost, not necessarily hop count.

**Correct:** C

### 22. In OSPF, each router sends out an update
A) ✗ Receiving an update alone is incomplete as the rule; OSPF also originates updates when local link state changes.  
B) ✗ Link up/down is one trigger, but not the only relevant change.  
C) ✓ A router originates an update when local link cost/state changes and floods received link-state information onward.  
D) ✗ OSPF is not based on a fixed one-minute periodic full routing update.  
E) ✗ This mentions local link-cost changes but omits the flooding of received updates.

**Correct:** C

### 23. Match the routing algorithms with the routing protocol names
- **Link State → OSPF** — OSPF is a link-state IGP.  
- **Path Vector → BGP** — BGP carries AS-path information.  
- **Distance Vector → RIP** — RIP advertises distance-vector routes.

**Correct:** Link State–OSPF; Path Vector–BGP; Distance Vector–RIP

### 24. A *privacy address* is formed by using _____ as the lower 64 bits of an IPv6 address.
A) ✗ Simply inverting a MAC address does not provide privacy.  
B) ✗ Another host's MAC address would be invalid and could create conflicts.  
C) ✗ NAT is not used to create the IPv6 interface identifier.  
D) ✗ Modified EUI-64 derives an identifier from the device's MAC address and is not the privacy mechanism asked for.  
E) ✓ IPv6 privacy extensions use a randomized interface identifier rather than exposing a stable MAC-derived identifier.

**Correct:** E
