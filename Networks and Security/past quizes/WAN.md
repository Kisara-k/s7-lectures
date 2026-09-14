# Quiz on IP, IPv6, Routing, Transport Layer, UDP/TCP and WANs

### 1. Very often, frame relay charges are based on
A) number of bytes sent  
B) number of packets sent  
C) time of day  
D) number of minutes connected  
E) committed information rate

### 2. What statement/s is/are true regarding the possible number of host IP addresses of a /28 CIDR based subnet?
A) Recommended to divide into 2 subnets to maximise the use of IP addresses  
B) 14 host IPs are recommended  
C) Can be extended beyond 16 IPs using cascaded switches  
D) 16 host IPs can be used

### 3. When a client host initiates a connection, it sends a TCP packet with _ bit set.

**Answer:** ______

### 4. An IPv6 address is _____ bits long.

**Answer:** ______

### 5. In Dijkstra's lowest cost path algorithm, a node is added to the set of nodes with known costs if it _____.
A) has the lowest current cost out of the remaining nodes  
B) has the lowest number of hops to the source  
C) is the next hop on the shortest path from the source to the destination  
D) is closest to the current node  
E) is of a different colour than the remaining nodes

### 6. Multi-Protocol Label Switching (MPLS) works _____ of the OSI stack.
A) between layers 2 and 3  
B) at Layer3  
C) between layers 1 and 2  
D) at Layer 2  
E) at layer 1

### 7. Transport layer provides facilities to:
A) achieve ordered delievery when multiplexing happens at network layer  
B) manage multiple conenctiions on the same host  
C) achieve ordered delievery when fragmentation and de-fragmentation happen at network layer  
D) send multiple application protocol data within the same stream

### 8. What is not a transport layer primitive?
A) Accept  
B) Receive  
C) Connect  
D) Listen

### 9. A major problem of using NAT to save IP address space is that _____.
A) some hosts cannot be accessed from other hosts  
B) hosts behind a NAT are less secure  
C) it cannot handle UDP  
D) the same IP address may be used by several hosts  
E) we will run out of port numbers

### 10. The following IPv4 fields are not present in an IPv6 header (select all that apply).
A) hop limit  
B) fragment offset  
C) class  
D) type of service  
E) header checksum

### 11. The principal objective of IPv6 header simplification is to _____.
A) reduce the header length  
B) reduce the number of header fields  
C) support multicasting  
D) reduce processing by routers  
E) increase the address length

### 12. ATM has a lower _____ than Frame Relay and X.25.
A) error rate  
B) bandwidth  
C) switching delay  
D) reliability

### 13. Identify the following types of routing.

- Routes change infrequently: ______  
- Each router knows about directly connected links, and exchanges info with neighbors: ______  
- Routing changes in response to link cost changes: ______  
- Routing based on complete topology and cost information: ______

### 14. A _____ address is only valid on its local network.

**Answer:** ______

### 15. "Length" field of IP datagram is used to indicate:
A) Length of the optional fields  
B) Addition of length of the header and the payload  
C) Total payload length  
D) Total header length

### 16. A network of size /48 is normally assigned to (select all that apply) _____.
A) government organisations  
B) small businesses  
C) homes  
D) universities  
E) mail servers  
F) web servers

### 17. Committed Information Rate (CIR) is the _____ data rate on a virtual circuit.
A) available  
B) guaranteed  
C) minimum  
D) maximum

### 18. The most important design goal of IPv6 is _____.
A) Efficiency  
B) More address space  
C) Encryption and Authentication  
D) Small routing table  
E) Multicast addresses

### 19. Ethernet First Mile (EFM) is used (select all that apply)
A) for mobile applications  
B) to connect residences to the internet  
C) to build corporate networks between branches  
D) only in networks less than a mile long  
E) to connect hosts within a building

### 20. The objective of routing is to find the path with the minimum _____ between a source and a destination.

**Answer:** ______

### 21. The result of the routing process on each router is building a _____.

**Answer:** ______

### 22. When more than one network is connected to a router:
A) Router interfaces should have IP addresses from the same subnet  
B) Each network may have IP adresses of its own subnet  
C) Not necessary to worry about assigning IP addresses based on subnets  
D) All networks should have network addresses from a larger subnet

### 23. Match the routing algorithms with the routing protocol names

| Routing algorithm | Protocol |
|---|---|
| Link State | ______ |
| Path Vector | ______ |
| Distance Vector | ______ |

### 24. The *Border Gateway Protocol (BGP)*
A) does not use TCP  
B) sends packets on the lowest cost route  
C) sends routing information every 30 seconds  
D) routes to networks, not individual hosts  
E) uses Path Vectors

### 25. During the initial adoption of IPv6 _____.
A) IPv6 packets are tunneled over IPv4 networks  
B) Layer 2 switches are upgraded  
C) Layer-2 switches are replaced by Layer-3 switches  
D) New IPv6 name servers are set up  
E) all mail servers must handle IPv6

### 26. What is not a TCP state?
A) CLOSED  
B) SYN RESENT  
C) CLOSE WAIT  
D) LAST ACK

### 27. What is not true of UDP?
A) UDP can be used for reliable applications  
B) UDP should be used if reliability cannot be achieved using TCP  
C) UDP can be used when less overhead in transport layer is preferred  
D) UDP options have a less overhead than TCP

### 28. Cell switching is more efficient than packet switching because
A) a cell has an 8-byte header  
B) all packets are the same size  
C) a packet is smaller than a cell  
D) a packet is larger than a cell  
E) all cells are the same size

### 29. MPLS networks are: (select all that apply)
A) support Virtual Private Networks (VPNs)  
B) support Traffic Engineering  
C) Scalable  
D) datagram-oriented  
E) statically routed

### 30. All packets belonging to the same _____ have the same MPLS label.
A) host  
B) network  
C) flow  
D) service

### 31. In _____ routing, each node computes best path to get to each other node, based on its knowledge about the network topology and link costs.

**Answer:** ______

### 32. Routing is done by _____.
A) end stations  
B) intermediate stations  
C) hosts  
D) connections  
E) datagrams

### 33. The host part of an IPv6 address is generally _____ bits long.

**Answer:** ______

# Answer Key & Explanations

### 1. Very often, frame relay charges are based on
A) ✗ Charging is not normally based simply on total bytes sent.  
B) ✗ Packet count is not the usual Frame Relay billing basis tested here.  
C) ✗ Time of day is not the defining basis.  
D) ✗ Frame Relay is not normally billed as a dial-up connection by minutes connected.  
E) ✓ The service is commonly specified and charged according to its Committed Information Rate (CIR).

**Correct:** E

### 2. What statement/s is/are true regarding the possible number of host IP addresses of a /28 CIDR based subnet?
A) ✗ Splitting the subnet again would reduce, not maximize, the number of usable hosts in each resulting subnet.  
B) ✓ A /28 has 16 total addresses and normally 14 usable host addresses after network and broadcast addresses.  
C) ✗ Adding cascaded switches does not enlarge the IP subnet's address space.  
D) ✗ All 16 addresses cannot be assigned to hosts because two are reserved for network and broadcast.

**Correct:** B

### 3. When a client host initiates a connection, it sends a TCP packet with _ bit set.

**Correct:** SYN  
**Explanation:** TCP connection establishment begins when the client sends a segment with the SYN flag set.

### 4. An IPv6 address is _____ bits long.

**Correct:** 128  
**Explanation:** IPv6 expands the address size from IPv4's 32 bits to 128 bits.

### 5. In Dijkstra's lowest cost path algorithm, a node is added to the set of nodes with known costs if it _____.
A) ✓ Dijkstra finalizes the remaining node with the smallest current tentative path cost.  
B) ✗ Lowest hop count is not necessarily the lowest weighted cost.  
C) ✗ Being a next hop to some destination is not the selection rule.  
D) ✗ The algorithm considers total source-to-node cost, not merely closeness to the current node.  
E) ✗ Colour is only an implementation/illustration detail.

**Correct:** A

### 6. Multi-Protocol Label Switching (MPLS) works _____ of the OSI stack.
A) ✓ MPLS is commonly described as “Layer 2.5,” operating between the data-link and network layers.  
B) ✗ It is not simply an ordinary Layer-3 protocol.  
C) ✗ It does not sit between the physical and data-link layers.  
D) ✗ It uses Layer-2-style label switching but is not confined to Layer 2.  
E) ✗ MPLS does not operate at the physical layer.

**Correct:** A

### 7. Transport layer provides facilities to:
A) ✗ Network-layer multiplexing is not the reason transport provides ordered delivery in the way stated here.  
B) ✓ Port numbers and transport endpoints allow multiple simultaneous connections/processes on one host.  
C) ✗ IP fragmentation/reassembly is a network-layer concern; transport does not order IP fragments themselves.  
D) ✓ In the course framing, transport multiplexing lets application data streams share the underlying network service while remaining distinguishable.

**Correct:** B,D

### 8. What is not a transport layer primitive?
A) ✓ In the primitive set used by this course/text, the standard primitives include LISTEN, CONNECT, SEND, RECEIVE and DISCONNECT; ACCEPT is not listed as one of them.  
B) ✗ RECEIVE is a transport-service primitive.  
C) ✗ CONNECT is a transport-service primitive.  
D) ✗ LISTEN is a transport-service primitive.

**Correct:** A

### 9. A major problem of using NAT to save IP address space is that _____.
A) ✓ NAT interferes with direct end-to-end reachability; an internal host is not generally addressable from outside without a mapping/forwarding rule.  
B) ✗ NAT often hides internal addressing; it does not inherently make hosts less secure.  
C) ✗ NAT can handle UDP using port/address mappings.  
D) ✗ Sharing one public address is the intended benefit, not the principal problem.  
E) ✗ Port exhaustion can be a scaling issue, but it is not the main conceptual disadvantage asked here.

**Correct:** A

### 10. The following IPv4 fields are not present in an IPv6 header (select all that apply).
A) ✗ IPv6 has a Hop Limit field.  
B) ✓ Fragment Offset is not in the IPv6 base header; fragmentation information is placed in a Fragment extension header.  
C) ✗ “Class” is not an IPv4 base-header field in the sense implied here, and IPv6 has a Traffic Class field.  
D) ✓ The IPv4 Type of Service field is not present under that name; IPv6 uses Traffic Class instead.  
E) ✓ IPv6 removes the IPv4 header checksum to reduce per-hop processing.

**Correct:** B,D,E

### 11. The principal objective of IPv6 header simplification is to _____.
A) ✗ The IPv6 base header is actually a fixed 40 bytes, larger than the minimum IPv4 header.  
B) ✗ Fewer fields help, but that is a means rather than the principal objective.  
C) ✗ Multicast support is a separate IPv6 feature.  
D) ✓ A simpler fixed header reduces work that routers must perform while forwarding packets.  
E) ✗ Increasing address length is a major IPv6 goal, but not the purpose of header simplification itself.

**Correct:** D

### 12. ATM has a lower _____ than Frame Relay and X.25.
A) ✗ Lower error rate is not the main comparison intended.  
B) ✗ ATM was designed for high bandwidth, not lower bandwidth.  
C) ✓ Fixed-size ATM cells can be switched quickly and predictably, producing lower switching delay.  
D) ✗ “Lower reliability” would not be an advantage and is not the intended property.

**Correct:** C

### 13. Identify the following types of routing.
- **Routes change infrequently → Static Routing** — routes are manually configured and normally remain unchanged until an administrator edits them.  
- **Each router knows about directly connected links, and exchanges info with neighbors → Local Routing** — decisions are based on local/neighbor information in the terminology used by this quiz.  
- **Routing changes in response to link cost changes → Dynamic Routing** — routes adapt when network conditions change.  
- **Routing based on complete topology and cost information → Global Routing** — path computation uses a network-wide topology view.

**Correct:** Static Routing; Local Routing; Dynamic Routing; Global Routing

### 14. A _____ address is only valid on its local network.

**Correct:** link-local  
**Explanation:** A link-local IPv6 address is intended only for communication on the local link and is not routed globally.

### 15. "Length" field of IP datagram is used to indicate:
A) ✗ It is not limited to optional fields.  
B) ✓ IPv4 Total Length gives the combined size of the header and payload.  
C) ✗ Payload length alone excludes the header.  
D) ✗ Header length is represented separately by the IHL field in IPv4.

**Correct:** B

### 16. A network of size /48 is normally assigned to (select all that apply) _____.
A) ✓ In the allocation model used in this course, a large organization such as a government organization may receive a /48 site prefix.  
B) ✗ The quiz does not treat a small business as the normal /48 case.  
C) ✗ Homes are not the normal /48 case in this course's allocation example.  
D) ✓ A university/site may be assigned a /48 prefix.  
E) ✗ Individual mail servers do not normally receive an entire /48 merely for being mail servers.  
F) ✗ Individual web servers likewise do not normally receive a /48 on that basis.

**Correct:** A,D

### 17. Committed Information Rate (CIR) is the _____ data rate on a virtual circuit.
A) ✗ “Available” can fluctuate and is not what CIR promises.  
B) ✓ CIR is the contracted/guaranteed information rate for the virtual circuit.  
C) ✗ Although it behaves like a committed baseline, the term used here is guaranteed rate.  
D) ✗ The network may sometimes allow bursts above CIR, so it is not the maximum rate.

**Correct:** B

### 18. The most important design goal of IPv6 is _____.
A) ✗ Efficiency improved, but it was not the main driving goal.  
B) ✓ The primary motivation was vastly expanding IP address space.  
C) ✗ Security support was important but not the central design driver.  
D) ✗ Routing scalability matters, but the headline goal was address-space expansion.  
E) ✗ Multicast is a feature, not the most important overall goal.

**Correct:** B

### 19. Ethernet First Mile (EFM) is used (select all that apply)
A) ✗ EFM is an access/first-mile Ethernet technology rather than a mobile-radio technology.  
B) ✓ It can provide Ethernet access from residences toward a provider network/Internet.  
C) ✓ It can also be used for business access, including connecting corporate sites/branches through provider access networks.  
D) ✗ “First Mile” is a functional name; it is not restricted to a literal distance under one mile.  
E) ✗ Ordinary in-building host connectivity is standard LAN Ethernet rather than the access use emphasized by EFM.

**Correct:** B,C

### 20. The objective of routing is to find the path with the minimum _____ between a source and a destination.

**Correct:** cost  
**Explanation:** Routing algorithms choose paths according to a metric or cost, which may reflect distance, bandwidth, delay, policy, or other factors.

### 21. The result of the routing process on each router is building a _____.

**Correct:** routing table  
**Explanation:** Routing protocols and algorithms determine reachability and next-hop information that is recorded in the routing table.

### 22. When more than one network is connected to a router:
A) ✗ Different router interfaces connecting different IP networks should not all belong to the same subnet.  
B) ✓ Each attached network can have its own subnet, with the router interface on that network assigned an address from that subnet.  
C) ✗ Correct subnet assignment is essential for IP routing.  
D) ✗ The networks do not all have to be subdivisions of one larger local subnet.

**Correct:** B

### 23. Match the routing algorithms with the routing protocol names
- **Link State → OSPF** — OSPF floods link-state information.  
- **Path Vector → BGP** — BGP carries path/AS-path information.  
- **Distance Vector → RIP** — RIP advertises route distances to neighbours.

**Correct:** Link State–OSPF; Path Vector–BGP; Distance Vector–RIP

### 24. The *Border Gateway Protocol (BGP)*
A) ✗ BGP runs over TCP, conventionally TCP port 179.  
B) ✗ BGP is policy-based and does not simply choose a numerically lowest-cost path in the IGP sense.  
C) ✗ Periodic 30-second full routing advertisements are characteristic of RIP, not BGP.  
D) ✓ BGP advertises reachability to IP prefixes/networks rather than routes to individual end hosts.  
E) ✓ BGP is a path-vector protocol and uses AS-path information.

**Correct:** D,E

### 25. During the initial adoption of IPv6 _____.
A) ✓ Tunneling IPv6 packets across IPv4 infrastructure was an important transition mechanism while IPv4 networks still dominated.  
B) ✗ Ordinary Layer-2 switches generally do not need wholesale upgrading merely because IP changes from v4 to v6.  
C) ✗ IPv6 adoption does not require replacing Layer-2 switches with Layer-3 switches.  
D) ✗ DNS had to support IPv6 records, but setting up entirely new name servers is not the defining transition mechanism.  
E) ✗ IPv6 deployment could be gradual; all mail servers did not need to support it immediately.

**Correct:** A

### 26. What is not a TCP state?
A) ✗ CLOSED is a standard TCP state.  
B) ✓ `SYN RESENT` is not a standard TCP state; the standard names include SYN-SENT and SYN-RECEIVED.  
C) ✗ CLOSE-WAIT is a standard TCP state.  
D) ✗ LAST-ACK is a standard TCP state.

**Correct:** B

### 27. What is not true of UDP?
A) ✓ In the course's transport-layer framing, UDP itself does not provide reliable delivery; reliability would have to be added by the application.  
B) ✓ If an application fundamentally needs TCP-style reliable ordered transport, choosing UDP because TCP “cannot achieve” reliability is not the correct reasoning.  
C) ✗ This is true: UDP is useful when low transport-layer overhead is preferred.  
D) ✗ Interpreting the wording as “UDP has less overhead than TCP,” this is true because the UDP header and protocol machinery are simpler.

**Correct:** A,B

### 28. Cell switching is more efficient than packet switching because
A) ✗ ATM cells have a 5-byte header, not an 8-byte header.  
B) ✗ Packet switching generally permits variable-length packets.  
C) ✗ Packets are not defined as being smaller than cells.  
D) ✗ Variable packet sizes are not what makes cell switching efficient.  
E) ✓ Fixed-size cells simplify hardware switching and make processing/delay more predictable.

**Correct:** E

### 29. MPLS networks are: (select all that apply)
A) ✓ MPLS is widely used to implement provider VPN services.  
B) ✓ Explicit label-switched paths can support traffic engineering.  
C) ✓ MPLS is designed to scale across large provider networks.  
D) ✗ MPLS forwarding follows labels/label-switched paths rather than treating every hop as ordinary independent datagram forwarding.  
E) ✗ MPLS is not inherently statically routed; paths can be established using dynamic routing/signaling.

**Correct:** A,B,C

### 30. All packets belonging to the same _____ have the same MPLS label.
A) ✗ MPLS labels are not simply assigned per host.  
B) ✗ An entire network can contain many distinct forwarding classes.  
C) ✓ In the terminology used by this quiz, packets in the same flow/forwarding equivalence class receive the same MPLS treatment and label.  
D) ✗ A broad service can contain multiple differently labelled flows.

**Correct:** C

### 31. In _____ routing, each node computes best path to get to each other node, based on its knowledge about the network topology and link costs.

**Correct:** link state  
**Explanation:** A link-state router learns topology and link metrics, then runs a shortest-path algorithm such as Dijkstra's algorithm locally.

### 32. Routing is done by _____.
A) ✗ End stations originate and receive data but do not normally route transit traffic.  
B) ✓ Intermediate stations such as routers forward traffic between networks.  
C) ✗ Hosts are end systems in this distinction.  
D) ✗ A connection is not a device that performs routing.  
E) ✗ A datagram is the data unit being routed, not the entity performing routing.

**Correct:** B

### 33. The host part of an IPv6 address is generally _____ bits long.

**Correct:** 64  
**Explanation:** A conventional IPv6 subnet uses a /64 prefix, leaving a 64-bit interface/host identifier.
