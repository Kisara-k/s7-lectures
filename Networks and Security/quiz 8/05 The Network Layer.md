## 5 The Network Layer

## Questions

#### 1. Which of the following are primary functions of the Network Layer?  
A) Establishing, maintaining, and terminating connections  
B) Isolating upper layers from data transmission technologies  
C) Error detection and correction at the bit level  
D) Addressing and routing  

#### 2. In connectionless packet switching, which statements are true?  
A) A connection must be established before sending packets  
B) Each packet contains the full destination address  
C) Routing decisions are made on a per-packet basis  
D) Routers maintain state information about each packet flow  

#### 3. How does connection-oriented switching differ from connectionless switching?  
A) Connection-oriented networks require a setup phase before data transfer  
B) Each packet in connection-oriented networks carries the full destination address  
C) Routers maintain state information about virtual circuits in connection-oriented networks  
D) Connection-oriented networks generally do not provide error control  

#### 4. Which of the following are characteristics of hierarchical addressing?  
A) Addresses are flat and have no internal structure  
B) Uses prefixes to represent regions or groups  
C) Simplifies routing tables by allowing default routes for unknown prefixes  
D) Is typically used only at the physical layer  

#### 5. Which properties are desirable in a routing algorithm?  
A) Correctness and stability  
B) Complexity and fairness  
C) Robustness and optimality  
D) Instability and simplicity  

#### 6. Regarding dynamic (adaptive) routing, which statements are correct?  
A) Routing tables are static and pre-defined  
B) Intermediate stations exchange routing information periodically  
C) Routing decisions can be based on link speed, delay, congestion, and cost  
D) Source routing is a form of dynamic routing  

#### 7. What are the main differences between forwarding and routing?  
A) Forwarding is the process of switching packets from input to output lines based on a forwarding table  
B) Routing builds forwarding tables based on network conditions and policies  
C) Forwarding involves computing the best path to each destination  
D) Routing is performed on a per-packet basis at each router  

#### 8. Which of the following statements about Quality of Service (QoS) and congestion control are true?  
A) Open-loop congestion control takes action only after congestion occurs  
B) Differentiated Services classify traffic into classes with different priorities and bandwidth  
C) Buffering and traffic shaping are techniques used to improve QoS  
D) Telephony applications typically require low delay and low jitter for acceptable QoS



<br>

## Answers

#### 1. Which of the following are primary functions of the Network Layer?  
A) ✓ Establishing, maintaining, and terminating connections is a core network layer function.  
B) ✓ Isolating upper layers from data transmission technologies is a key role of the network layer.  
C) ✗ Error detection and correction at the bit level is handled by the Data Link layer, not Network.  
D) ✓ Addressing and routing are fundamental network layer responsibilities.  

**Correct:** A, B, D


#### 2. In connectionless packet switching, which statements are true?  
A) ✗ Connectionless networks do not require connection setup before sending packets.  
B) ✓ Each packet contains the full destination address for routing decisions.  
C) ✓ Routing decisions are made independently for each packet (per-packet basis).  
D) ✗ Routers do not maintain state information about flows in connectionless switching.  

**Correct:** B, C


#### 3. How does connection-oriented switching differ from connectionless switching?  
A) ✓ Connection-oriented networks require a connection setup phase before data transfer.  
B) ✗ Packets in connection-oriented networks carry connection identifiers, not full destination addresses.  
C) ✓ Routers maintain state information about virtual circuits (connection IDs) in connection-oriented networks.  
D) ✗ Connection-oriented networks generally provide error control, unlike connectionless.  

**Correct:** A, C


#### 4. Which of the following are characteristics of hierarchical addressing?  
A) ✗ Flat addressing has no internal structure; hierarchical addressing does.  
B) ✓ Hierarchical addressing uses prefixes to represent regions or groups.  
C) ✓ Hierarchical addressing simplifies routing tables by allowing default routes for unknown prefixes.  
D) ✗ Hierarchical addressing is used at multiple layers, especially network and application, not only physical.  

**Correct:** B, C


#### 5. Which properties are desirable in a routing algorithm?  
A) ✓ Correctness ensures routes are valid; stability prevents route flapping.  
B) ✗ Complexity is undesirable; fairness is desirable but complexity is not.  
C) ✓ Robustness allows recovery from failures; optimality ensures best routes.  
D) ✗ Instability is undesirable; simplicity is desirable but instability is not.  

**Correct:** A, C


#### 6. Regarding dynamic (adaptive) routing, which statements are correct?  
A) ✗ Dynamic routing updates routes based on network changes, not static tables.  
B) ✓ Intermediate stations exchange routing information periodically to adapt routes.  
C) ✓ Routing decisions consider link speed, delay, congestion, cost, etc.  
D) ✗ Source routing is a separate routing type where the source specifies the route, not dynamic routing.  

**Correct:** B, C


#### 7. What are the main differences between forwarding and routing?  
A) ✓ Forwarding switches packets from input to output lines using forwarding tables.  
B) ✓ Routing builds and updates forwarding tables based on network topology and policies.  
C) ✗ Computing best paths is part of routing, not forwarding.  
D) ✗ Routing is not performed per-packet; forwarding is per-packet. Routing is periodic or event-driven.  

**Correct:** A, B


#### 8. Which of the following statements about Quality of Service (QoS) and congestion control are true?  
A) ✗ Open-loop congestion control attempts to avoid congestion before it occurs, not after.  
B) ✓ Differentiated Services classify traffic into classes with different priorities and bandwidth.  
C) ✓ Buffering and traffic shaping are common QoS techniques to manage traffic flow.  
D) ✓ Telephony requires low delay and low jitter for acceptable QoS.  

**Correct:** B, C, D