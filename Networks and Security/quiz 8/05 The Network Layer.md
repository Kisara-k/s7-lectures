## 5 The Network Layer

## Questions

#### 1. Which of the following are primary functions of the Network Layer?  
A) Establishing, maintaining, and terminating connections  
B) Error detection and correction at the bit level  
C) Isolating upper layers from data transmission technologies  
D) Addressing and routing  

#### 2. In connectionless packet switching, which statements are true?  
A) Routing decisions are made on a per-packet basis  
B) Each packet contains the full destination address  
C) A connection must be established before sending packets  
D) Routers maintain state information about each packet flow  

#### 3. How does connection-oriented switching differ from connectionless switching?  
A) Routers maintain state information about virtual circuits in connection-oriented networks  
B) Each packet in connection-oriented networks carries the full destination address  
C) Connection-oriented networks generally do not provide error control  
D) Connection-oriented networks require a setup phase before data transfer  

#### 4. Which of the following are characteristics of hierarchical addressing?  
A) Addresses are flat and have no internal structure  
B) Simplifies routing tables by allowing default routes for unknown prefixes  
C) Is typically used only at the physical layer  
D) Uses prefixes to represent regions or groups  

#### 5. Which properties are desirable in a routing algorithm?  
A) Complexity and fairness  
B) Robustness and optimality  
C) Instability and simplicity  
D) Correctness and stability  

#### 6. Regarding dynamic (adaptive) routing, which statements are correct?  
A) Source routing is a form of dynamic routing  
B) Intermediate stations exchange routing information periodically  
C) Routing decisions can be based on link speed, delay, congestion, and cost  
D) Routing tables are static and pre-defined  

#### 7. What are the main differences between forwarding and routing?  
A) Routing is performed on a per-packet basis at each router  
B) Routing builds forwarding tables based on network conditions and policies  
C) Forwarding is the process of switching packets from input to output lines based on a forwarding table  
D) Forwarding involves computing the best path to each destination  

#### 8. Which of the following statements about Quality of Service (QoS) and congestion control are true?  
A) Differentiated Services classify traffic into classes with different priorities and bandwidth  
B) Buffering and traffic shaping are techniques used to improve QoS  
C) Open-loop congestion control takes action only after congestion occurs  
D) Telephony applications typically require low delay and low jitter for acceptable QoS  



<br>

## Answers

#### 1. Which of the following are primary functions of the Network Layer?  
A) ✓ Establishing, maintaining, and terminating connections is a core network layer function.  
B) ✗ Error detection and correction at the bit level is handled by the Data Link layer, not Network.  
C) ✓ Isolating upper layers from data transmission technologies is a key role of the network layer.  
D) ✓ Addressing and routing are fundamental network layer responsibilities.  

**Correct:** A, C, D


#### 2. In connectionless packet switching, which statements are true?  
A) ✓ Routing decisions are made independently for each packet (per-packet basis).  
B) ✓ Each packet contains the full destination address for routing decisions.  
C) ✗ Connectionless networks do not require connection setup before sending packets.  
D) ✗ Routers do not maintain state information about flows in connectionless switching.  

**Correct:** A, B


#### 3. How does connection-oriented switching differ from connectionless switching?  
A) ✓ Routers maintain state information about virtual circuits (connection IDs) in connection-oriented networks.  
B) ✗ Packets in connection-oriented networks carry connection identifiers, not full destination addresses.  
C) ✗ Connection-oriented networks generally provide error control, unlike connectionless.  
D) ✓ Connection-oriented networks require a connection setup phase before data transfer.  

**Correct:** A, D


#### 4. Which of the following are characteristics of hierarchical addressing?  
A) ✗ Flat addressing has no internal structure; hierarchical addressing does.  
B) ✓ Hierarchical addressing simplifies routing tables by allowing default routes for unknown prefixes.  
C) ✗ Hierarchical addressing is used at multiple layers, especially network and application, not only physical.  
D) ✓ Hierarchical addressing uses prefixes to represent regions or groups.  

**Correct:** B, D


#### 5. Which properties are desirable in a routing algorithm?  
A) ✗ Complexity is undesirable; fairness is desirable but complexity is not.  
B) ✓ Robustness allows recovery from failures; optimality ensures best routes.  
C) ✗ Instability is undesirable; simplicity is desirable but instability is not.  
D) ✓ Correctness ensures routes are valid; stability prevents route flapping.  

**Correct:** B, D


#### 6. Regarding dynamic (adaptive) routing, which statements are correct?  
A) ✗ Source routing is a separate routing type where the source specifies the route, not dynamic routing.  
B) ✓ Intermediate stations exchange routing information periodically to adapt routes.  
C) ✓ Routing decisions consider link speed, delay, congestion, cost, etc.  
D) ✗ Dynamic routing updates routes based on network changes, not static tables.  

**Correct:** B, C


#### 7. What are the main differences between forwarding and routing?  
A) ✗ Routing is not performed per-packet; forwarding is per-packet. Routing is periodic or event-driven.  
B) ✓ Routing builds and updates forwarding tables based on network topology and policies.  
C) ✓ Forwarding switches packets from input to output lines using forwarding tables.  
D) ✗ Computing best paths is part of routing, not forwarding.  

**Correct:** B, C


#### 8. Which of the following statements about Quality of Service (QoS) and congestion control are true?  
A) ✓ Differentiated Services classify traffic into classes with different priorities and bandwidth.  
B) ✓ Buffering and traffic shaping are common QoS techniques to manage traffic flow.  
C) ✗ Open-loop congestion control attempts to avoid congestion before it occurs, not after.  
D) ✓ Telephony requires low delay and low jitter for acceptable QoS.  

**Correct:** A, B, D