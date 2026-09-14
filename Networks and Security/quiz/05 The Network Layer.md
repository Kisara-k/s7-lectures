## 5 The Network Layer

## Questions

#### 1. Which of the following are primary functions of the Network Layer?  
A) Establishing, maintaining, and terminating connections  
B) Isolating upper layers from data transmission technologies  
C) Error detection and correction at the bit level  
D) Addressing and routing  

#### 2. In packet switching networks, which statements are true?  
A) Data streams are divided into packets, each with a header and data  
B) Packets are switched through nodes from source to destination  
C) Each packet must follow the same path through the network  
D) Packet switching requires a dedicated physical circuit between hosts  

#### 3. Which characteristics correctly describe connectionless networks?  
A) No need to establish a connection before sending packets  
B) Routing decisions are made on a per-packet basis  
C) Network generally provides error control for each packet  
D) Each packet contains the destination address  

#### 4. In connection-oriented networks, which of the following are true?  
A) A connection is established before data transfer begins  
B) Routing is performed on a per-connection basis  
C) Each packet contains the full destination address  
D) Network generally provides error control  

#### 5. Regarding forwarding tables in connectionless and connection-oriented networks, which statements are correct?  
A) Connectionless forwarding tables map destination addresses to next hops  
B) Connection-oriented forwarding tables map incoming connection IDs to outgoing connection IDs  
C) Connectionless forwarding tables maintain state information about connections  
D) Connection-oriented forwarding tables do not require unique connection identifiers  

#### 6. Comparing connectionless and connection-oriented networks, which of the following are valid distinctions?  
A) Connectionless networks require connection setup, connection-oriented do not  
B) Connection-oriented networks maintain state in routers, connectionless do not  
C) Quality of Service is easier to provide in connection-oriented networks  
D) Congestion control is more difficult in connection-oriented networks  

#### 7. Which of the following are examples of hierarchical addressing?  
A) Ethernet MAC addresses  
B) Postal addresses  
C) Telephone numbers  
D) Personal names  

#### 8. What are the key differences between forwarding and routing in the network layer?  
A) Forwarding is the process of switching packets from input to output lines based on a forwarding table  
B) Routing builds forwarding tables based on network conditions and policies  
C) Forwarding involves computing the best path to each destination  
D) Routing is performed on a per-packet basis at each router  

#### 9. Which properties are desirable in a routing algorithm?  
A) Correctness and simplicity  
B) Robustness and stability  
C) Fairness and optimality  
D) Complexity and unpredictability  

#### 10. Which statements about static (non-adaptive) routing are true?  
A) Routing tables are pre-defined and do not change dynamically  
B) It is suitable for large, highly dynamic networks  
C) It is labor-intensive to maintain and not resilient to failures  
D) It uses routing protocols to compute routes periodically  

#### 11. In dynamic (adaptive) routing, which factors influence route computation?  
A) Link speed and delay  
B) Congestion and error rate  
C) Communication cost and policy  
D) Fixed pre-defined routes  

#### 12. Which routing mechanisms involve routers exchanging information periodically to compute best paths?  
A) Distance Vector Routing  
B) Link State Routing  
C) Flooding  
D) Source Routing  

#### 13. Regarding hierarchical routing, which statements are correct?  
A) It groups routers into regions to simplify routing tables  
B) Gateways handle routing between regions  
C) It is unnecessary in large networks with over 100,000 nodes  
D) It may involve multiple levels of hierarchy  

#### 14. Which of the following statements about multicast routing are true?  
A) Packets are sent to all nodes in the network  
B) Packets are sent to a subset of hosts belonging to multicast groups  
C) Routers keep track of which multicast groups are accessible via each link  
D) Multicast routing requires establishing a connection between all group members  

#### 15. Which techniques are used for Quality of Service (QoS) in networks?  
A) Over provisioning of resources  
B) Buffering to handle traffic bursts  
C) Traffic shaping to regulate flow  
D) Ignoring traffic classes and treating all packets equally



<br>

## Answers

#### 1. Which of the following are primary functions of the Network Layer?  
A) ✓ Establishing, maintaining, and terminating connections is a core network layer function.  
B) ✓ Isolating upper layers from data transmission technologies is a key role of the network layer.  
C) ✗ Error detection and correction at the bit level is handled by the Data Link layer, not Network.  
D) ✓ Addressing and routing are fundamental network layer tasks.  

**Correct:** A, B, D


#### 2. In packet switching networks, which statements are true?  
A) ✓ Data streams are divided into packets, each with a header and data, by definition of packet switching.  
B) ✓ Packets are switched through nodes from source to destination, which is how packet switching works.  
C) ✗ Packets do not have to follow the same path; they can take different routes.  
D) ✗ Packet switching does not require a dedicated physical circuit; that is circuit switching.  

**Correct:** A, B


#### 3. Which characteristics correctly describe connectionless networks?  
A) ✓ No connection setup is needed before sending packets in connectionless networks.  
B) ✓ Routing decisions are made independently for each packet.  
C) ✗ Generally, connectionless networks do not provide error control.  
D) ✓ Each packet contains the destination address to enable independent routing.  

**Correct:** A, B, D


#### 4. In connection-oriented networks, which of the following are true?  
A) ✓ A connection is established before data transfer begins.  
B) ✓ Routing is done on a per-connection basis, not per packet.  
C) ✗ Packets carry connection IDs, not full destination addresses.  
D) ✓ The network generally provides error control in connection-oriented networks.  

**Correct:** A, B, D


#### 5. Regarding forwarding tables in connectionless and connection-oriented networks, which statements are correct?  
A) ✓ Connectionless forwarding tables map destination addresses to next hops.  
B) ✓ Connection-oriented forwarding tables map incoming connection IDs to outgoing connection IDs.  
C) ✗ Connectionless forwarding tables do not maintain state information about connections.  
D) ✗ Connection-oriented forwarding tables require unique connection identifiers for each link.  

**Correct:** A, B


#### 6. Comparing connectionless and connection-oriented networks, which of the following are valid distinctions?  
A) ✗ Connectionless networks do not require connection setup; connection-oriented do.  
B) ✓ Connection-oriented networks maintain state in routers; connectionless do not.  
C) ✓ Quality of Service is easier to provide in connection-oriented networks due to established paths.  
D) ✗ Congestion control is generally easier in connection-oriented networks, not more difficult.  

**Correct:** B, C


#### 7. Which of the following are examples of hierarchical addressing?  
A) ✗ Ethernet MAC addresses are flat, not hierarchical.  
B) ✓ Postal addresses are hierarchical (country, city, street, etc.).  
C) ✓ Telephone numbers are hierarchical (country code, area code, number).  
D) ✗ Personal names are flat and not structured hierarchically.  

**Correct:** B, C


#### 8. What are the key differences between forwarding and routing in the network layer?  
A) ✓ Forwarding switches packets from input to output lines based on forwarding tables.  
B) ✓ Routing builds forwarding tables based on network conditions and policies.  
C) ✗ Forwarding does not compute best paths; routing does.  
D) ✗ Routing is not performed on a per-packet basis; forwarding is.  

**Correct:** A, B


#### 9. Which properties are desirable in a routing algorithm?  
A) ✓ Correctness and simplicity are essential for reliable routing.  
B) ✓ Robustness and stability ensure the network adapts and remains consistent.  
C) ✓ Fairness and optimality help balance load and efficiency.  
D) ✗ Complexity and unpredictability are undesirable in routing algorithms.  

**Correct:** A, B, C


#### 10. Which statements about static (non-adaptive) routing are true?  
A) ✓ Routing tables are pre-defined and do not change dynamically.  
B) ✗ Static routing is unsuitable for large, dynamic networks.  
C) ✓ It is labor-intensive to maintain and not resilient to failures.  
D) ✗ Static routing does not use routing protocols to compute routes periodically.  

**Correct:** A, C


#### 11. In dynamic (adaptive) routing, which factors influence route computation?  
A) ✓ Link speed and delay affect route selection.  
B) ✓ Congestion and error rate are considered in adaptive routing.  
C) ✓ Communication cost and policy influence routing decisions.  
D) ✗ Fixed pre-defined routes are characteristic of static routing, not dynamic.  

**Correct:** A, B, C


#### 12. Which routing mechanisms involve routers exchanging information periodically to compute best paths?  
A) ✓ Distance Vector Routing involves periodic exchange of routing tables.  
B) ✓ Link State Routing involves routers sharing link state information periodically.  
C) ✗ Flooding sends packets on all unused links without routing table exchange.  
D) ✗ Source Routing has the source specify the route, not routers exchanging info.  

**Correct:** A, B


#### 13. Regarding hierarchical routing, which statements are correct?  
A) ✓ Routers are grouped into regions to simplify routing tables.  
B) ✓ Gateways handle routing between regions.  
C) ✗ Hierarchical routing is necessary in large networks; it is not unnecessary.  
D) ✓ Multiple levels of hierarchy may be used in large networks.  

**Correct:** A, B, D


#### 14. Which of the following statements about multicast routing are true?  
A) ✗ Sending packets to all nodes is broadcast, not multicast.  
B) ✓ Multicast sends packets to a subset of hosts in multicast groups.  
C) ✓ Routers keep track of which multicast groups are accessible via each link.  
D) ✗ Multicast routing does not require a connection between all group members.  

**Correct:** B, C


#### 15. Which techniques are used for Quality of Service (QoS) in networks?  
A) ✓ Over provisioning increases resources to meet demand.  
B) ✓ Buffering helps handle traffic bursts and smooth delivery.  
C) ✓ Traffic shaping regulates flow to prevent congestion.  
D) ✗ Ignoring traffic classes contradicts QoS principles.  

**Correct:** A, B, C