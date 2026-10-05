## 5 The Network Layer

## Questions

#### 1. Which of the following are primary functions of the Network Layer?  
A) Establishing, maintaining, and terminating connections  
B) Error detection and correction at the bit level  
C) Isolating upper layers from data transmission technologies  
D) Addressing and routing  

#### 2. In packet switching networks, which statements are true?  
A) Data streams are divided into packets, each with a header and data  
B) Packets are switched through nodes from source to destination  
C) Packet switching requires a dedicated physical circuit between hosts  
D) Each packet must follow the same path through the network  

#### 3. Which characteristics correctly describe connectionless networks?  
A) Network generally provides error control for each packet  
B) No need to establish a connection before sending packets  
C) Routing decisions are made on a per-packet basis  
D) Each packet contains the destination address  

#### 4. In connection-oriented networks, which of the following are true?  
A) Routing is performed on a per-connection basis  
B) Each packet contains the full destination address  
C) Network generally provides error control  
D) A connection is established before data transfer begins  

#### 5. Regarding forwarding tables in connectionless and connection-oriented networks, which statements are correct?  
A) Connection-oriented forwarding tables map incoming connection IDs to outgoing connection IDs  
B) Connectionless forwarding tables maintain state information about connections  
C) Connectionless forwarding tables map destination addresses to next hops  
D) Connection-oriented forwarding tables do not require unique connection identifiers  

#### 6. Comparing connectionless and connection-oriented networks, which of the following are valid distinctions?  
A) Quality of Service is easier to provide in connection-oriented networks  
B) Congestion control is more difficult in connection-oriented networks  
C) Connection-oriented networks maintain state in routers, connectionless do not  
D) Connectionless networks require connection setup, connection-oriented do not  

#### 7. Which of the following are examples of hierarchical addressing?  
A) Telephone numbers  
B) Postal addresses  
C) Personal names  
D) Ethernet MAC addresses  

#### 8. What are the key differences between forwarding and routing in the network layer?  
A) Routing is performed on a per-packet basis at each router  
B) Routing builds forwarding tables based on network conditions and policies  
C) Forwarding is the process of switching packets from input to output lines based on a forwarding table  
D) Forwarding involves computing the best path to each destination  

#### 9. Which properties are desirable in a routing algorithm?  
A) Correctness and simplicity  
B) Robustness and stability  
C) Fairness and optimality  
D) Complexity and unpredictability  

#### 10. Which statements about static (non-adaptive) routing are true?  
A) Routing tables are pre-defined and do not change dynamically  
B) It uses routing protocols to compute routes periodically  
C) It is labor-intensive to maintain and not resilient to failures  
D) It is suitable for large, highly dynamic networks  

#### 11. In dynamic (adaptive) routing, which factors influence route computation?  
A) Communication cost and policy  
B) Fixed pre-defined routes  
C) Congestion and error rate  
D) Link speed and delay  

#### 12. Which routing mechanisms involve routers exchanging information periodically to compute best paths?  
A) Source Routing  
B) Link State Routing  
C) Distance Vector Routing  
D) Flooding  

#### 13. Regarding hierarchical routing, which statements are correct?  
A) It may involve multiple levels of hierarchy  
B) Gateways handle routing between regions  
C) It is unnecessary in large networks with over 100,000 nodes  
D) It groups routers into regions to simplify routing tables  

#### 14. Which of the following statements about multicast routing are true?  
A) Packets are sent to a subset of hosts belonging to multicast groups  
B) Multicast routing requires establishing a connection between all group members  
C) Packets are sent to all nodes in the network  
D) Routers keep track of which multicast groups are accessible via each link  

#### 15. Which techniques are used for Quality of Service (QoS) in networks?  
A) Buffering to handle traffic bursts  
B) Over provisioning of resources  
C) Traffic shaping to regulate flow  
D) Ignoring traffic classes and treating all packets equally  



<br>

## Answers

#### 1. Which of the following are primary functions of the Network Layer?  
A) ✓ Establishing, maintaining, and terminating connections is a core network layer function.  
B) ✗ Error detection and correction at the bit level is handled by the Data Link layer, not Network.  
C) ✓ Isolating upper layers from data transmission technologies is a key role of the network layer.  
D) ✓ Addressing and routing are fundamental network layer tasks.  

**Correct:** A, C, D


#### 2. In packet switching networks, which statements are true?  
A) ✓ Data streams are divided into packets, each with a header and data, by definition of packet switching.  
B) ✓ Packets are switched through nodes from source to destination, which is how packet switching works.  
C) ✗ Packet switching does not require a dedicated physical circuit; that is circuit switching.  
D) ✗ Packets do not have to follow the same path; they can take different routes.  

**Correct:** A, B


#### 3. Which characteristics correctly describe connectionless networks?  
A) ✗ Generally, connectionless networks do not provide error control.  
B) ✓ No connection setup is needed before sending packets in connectionless networks.  
C) ✓ Routing decisions are made independently for each packet.  
D) ✓ Each packet contains the destination address to enable independent routing.  

**Correct:** B, C, D


#### 4. In connection-oriented networks, which of the following are true?  
A) ✓ Routing is done on a per-connection basis, not per packet.  
B) ✗ Packets carry connection IDs, not full destination addresses.  
C) ✓ The network generally provides error control in connection-oriented networks.  
D) ✓ A connection is established before data transfer begins.  

**Correct:** A, C, D


#### 5. Regarding forwarding tables in connectionless and connection-oriented networks, which statements are correct?  
A) ✓ Connection-oriented forwarding tables map incoming connection IDs to outgoing connection IDs.  
B) ✗ Connectionless forwarding tables do not maintain state information about connections.  
C) ✓ Connectionless forwarding tables map destination addresses to next hops.  
D) ✗ Connection-oriented forwarding tables require unique connection identifiers for each link.  

**Correct:** A, C


#### 6. Comparing connectionless and connection-oriented networks, which of the following are valid distinctions?  
A) ✓ Quality of Service is easier to provide in connection-oriented networks due to established paths.  
B) ✗ Congestion control is generally easier in connection-oriented networks, not more difficult.  
C) ✓ Connection-oriented networks maintain state in routers; connectionless do not.  
D) ✗ Connectionless networks do not require connection setup; connection-oriented do.  

**Correct:** A, C


#### 7. Which of the following are examples of hierarchical addressing?  
A) ✓ Telephone numbers are hierarchical (country code, area code, number).  
B) ✓ Postal addresses are hierarchical (country, city, street, etc.).  
C) ✗ Personal names are flat and not structured hierarchically.  
D) ✗ Ethernet MAC addresses are flat, not hierarchical.  

**Correct:** A, B


#### 8. What are the key differences between forwarding and routing in the network layer?  
A) ✗ Routing is not performed on a per-packet basis; forwarding is.  
B) ✓ Routing builds forwarding tables based on network conditions and policies.  
C) ✓ Forwarding switches packets from input to output lines based on forwarding tables.  
D) ✗ Forwarding does not compute best paths; routing does.  

**Correct:** B, C


#### 9. Which properties are desirable in a routing algorithm?  
A) ✓ Correctness and simplicity are essential for reliable routing.  
B) ✓ Robustness and stability ensure the network adapts and remains consistent.  
C) ✓ Fairness and optimality help balance load and efficiency.  
D) ✗ Complexity and unpredictability are undesirable in routing algorithms.  

**Correct:** A, B, C


#### 10. Which statements about static (non-adaptive) routing are true?  
A) ✓ Routing tables are pre-defined and do not change dynamically.  
B) ✗ Static routing does not use routing protocols to compute routes periodically.  
C) ✓ It is labor-intensive to maintain and not resilient to failures.  
D) ✗ Static routing is unsuitable for large, dynamic networks.  

**Correct:** A, C


#### 11. In dynamic (adaptive) routing, which factors influence route computation?  
A) ✓ Communication cost and policy influence routing decisions.  
B) ✗ Fixed pre-defined routes are characteristic of static routing, not dynamic.  
C) ✓ Congestion and error rate are considered in adaptive routing.  
D) ✓ Link speed and delay affect route selection.  

**Correct:** A, C, D


#### 12. Which routing mechanisms involve routers exchanging information periodically to compute best paths?  
A) ✗ Source Routing has the source specify the route, not routers exchanging info.  
B) ✓ Link State Routing involves routers sharing link state information periodically.  
C) ✓ Distance Vector Routing involves periodic exchange of routing tables.  
D) ✗ Flooding sends packets on all unused links without routing table exchange.  

**Correct:** B, C


#### 13. Regarding hierarchical routing, which statements are correct?  
A) ✓ Multiple levels of hierarchy may be used in large networks.  
B) ✓ Gateways handle routing between regions.  
C) ✗ Hierarchical routing is necessary in large networks; it is not unnecessary.  
D) ✓ Routers are grouped into regions to simplify routing tables.  

**Correct:** A, B, D


#### 14. Which of the following statements about multicast routing are true?  
A) ✓ Multicast sends packets to a subset of hosts in multicast groups.  
B) ✗ Multicast routing does not require a connection between all group members.  
C) ✗ Sending packets to all nodes is broadcast, not multicast.  
D) ✓ Routers keep track of which multicast groups are accessible via each link.  

**Correct:** A, D


#### 15. Which techniques are used for Quality of Service (QoS) in networks?  
A) ✓ Buffering helps handle traffic bursts and smooth delivery.  
B) ✓ Over provisioning increases resources to meet demand.  
C) ✓ Traffic shaping regulates flow to prevent congestion.  
D) ✗ Ignoring traffic classes contradicts QoS principles.  

**Correct:** A, B, C