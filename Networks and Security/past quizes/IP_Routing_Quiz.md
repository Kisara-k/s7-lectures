# IP Routing Quiz

### 1. Select the **correct** statement(s) regarding routing mechanisms
A) Router needs more resources if it use links state routing algorithms for route selection  
B) Static routing is simple and having updated routing information than dynamic routing  
C) BGP can be implemented only in high-end routers  
D) Dynamic routing is used when the network setup is complex and connected to several WANs

### 2. Select the **incorrect** statement about an autonomous system (AS)
A) AS number is unique to an autonomous system  
B) One autonomous system can have multiple uplinks  
C) IP block for an Autonomous system is issued by a regional Internet Registry (RIR)  
D) BGP is an intra-AS routing protocol

### 3. Match the routing algorithms with the routing protocol names

| Routing algorithm | Protocol |
|---|---|
| Distance Vector | ______ |
| Link State | ______ |
| Path Vector | ______ |

### 4. Path vector protocol is applied in
A) IGP  
B) OSPF  
C) BGP  
D) RIP

### 5. Intra-AS routing protocols are ...
A) EIGP  
B) RIP  
C) BGP  
D) IGP  
E) EGP

### 6. In _____ routing, Each node keeps a list of the “shortest distance” to every other node, and the best way to reach it.

**Answer:** ______

### 7. In _____ routing, each node computes best path to get to each other node, based on its knowledge about the network topology and link costs.

**Answer:** ______

### 8. Two or more networks are aggregated when routing to
A) reduce the number of IP addresses used  
B) save memory space on routers  
C) reduce the number of hops taken by a packet  
D) increase the number of hosts on a network  
E) connect two or more hosts to the same network

### 9. Use the network diagram shown below to answer question 9 & 10

```text
                         INTERNET
                            |
                         Router B
                       192.248.0.1
                            |
                      Network C
                    57 Computers

LAN A              10.0.1.0/30
120 Computers       ? -------- 10.0.1.2
     \              /             \
      \         Router A -------- Router B
       \          /
        LAN B
     22 Computers
```

Usable IP IP blocks for LAN A, LAN B and LAN C are respectively

A) 10.0.0.0/25, 10.0.0.64/27, 10.2.2.0/26  
B) 10.0.1.0/25, 10.1.0.0/27, 10.0.0.64/26  
C) 10.0.1.0/25, 10.1.0.0/27, 10.2.2.0/26  
D) 10.0.0.0/25, 10.1.0.0/27, 10.2.2.0/26

### 10. If there is a default route entry configured at Router A, select the default route entry from the followings
A) 0.0.0.0 0.0.0.0 via 10.0.1.1  
B) 0.0.0.0 0.0.0.0 via 10.0.1.2  
C) 0.0.0.0 0.0.0.0 via 192.248.0.1  
D) 0.0.0.0 0.0.0.0 via 10.0.1.3

# Answer Key & Explanations

### 1. Select the **correct** statement(s) regarding routing mechanisms
A) ✓ Link-state routing requires more memory and processing because routers maintain topology information and run shortest-path calculations.  
B) ✗ Static routing is simple, but it does not automatically keep routing information updated as the network changes.  
C) ✓ In the context of this quiz, BGP is treated as a resource-intensive protocol used on high-end routers.  
D) ✓ Dynamic routing is useful in complex networks where routes must adapt automatically, especially across several WAN connections.

**Correct:** A,C,D

### 2. Select the **incorrect** statement about an autonomous system (AS)
A) ✗ An AS is identified by an autonomous system number intended to uniquely identify it.  
B) ✗ An AS can be multihomed and therefore have multiple uplinks.  
C) ✗ Address blocks are allocated through the regional Internet registry system.  
D) ✓ BGP is primarily an inter-AS routing protocol, so describing it as intra-AS is the incorrect statement.

**Correct:** D

### 3. Match the routing algorithms with the routing protocol names
- **Distance Vector → RIP** — RIP exchanges distance-vector route information.  
- **Link State → OSPF** — OSPF distributes link-state information and computes shortest paths.  
- **Path Vector → BGP** — BGP advertises paths between autonomous systems.

**Correct:** Distance Vector–RIP; Link State–OSPF; Path Vector–BGP

### 4. Path vector protocol is applied in
A) ✗ IGP is a category of intra-AS protocols, not the path-vector protocol asked for.  
B) ✗ OSPF uses link-state routing.  
C) ✓ BGP is the standard path-vector routing protocol.  
D) ✗ RIP uses distance-vector routing.

**Correct:** C

### 5. Intra-AS routing protocols are ...
A) ✓ EIGP/EIGRP is used for routing within an autonomous system.  
B) ✓ RIP is an interior routing protocol.  
C) ✗ BGP is primarily used between autonomous systems.  
D) ✓ IGP means *Interior Gateway Protocol*, the class of protocols used within an AS.  
E) ✗ EGP refers to exterior routing between autonomous systems.

**Correct:** A,B,D

### 6. In _____ routing, Each node keeps a list of the “shortest distance” to every other node, and the best way to reach it.

**Correct:** Distance vector  
**Explanation:** A distance-vector router maintains a best-known distance and next hop for destinations and exchanges this information with neighbours.

### 7. In _____ routing, each node computes best path to get to each other node, based on its knowledge about the network topology and link costs.

**Correct:** Link state  
**Explanation:** Link-state routers learn the network topology and link costs, then independently calculate shortest paths.

### 8. Two or more networks are aggregated when routing to
A) ✗ Route aggregation does not reduce how many IP addresses the underlying networks use.  
B) ✓ Aggregation replaces several routing entries with a summarized entry, reducing routing-table memory requirements.  
C) ✗ Aggregation does not directly reduce the number of hops a packet travels.  
D) ✗ It does not increase the host capacity of an individual network.  
E) ✗ It summarizes routes; it does not connect hosts to the same LAN.

**Correct:** B

### 9. Usable IP IP blocks for LAN A, LAN B and LAN C are respectively
A) ✓ **This is the answer marked correct by the original quiz.** The required prefix sizes are /25 for 120 computers, /27 for 22 computers, and /26 for 57 computers.  
B) ✗ The original quiz does not accept this combination.  
C) ✗ The original quiz does not accept this combination.  
D) ✗ The original quiz does not accept this combination.

**Correct:** A

> **Note:** The original quiz's accepted option A is internally inconsistent under standard IPv4 subnetting because `10.0.0.64/27` lies inside `10.0.0.0/25`. The answer above preserves the quiz's own marked answer rather than silently changing it.

### 10. If there is a default route entry configured at Router A, select the default route entry from the followings
A) ✗ `10.0.1.1` would be Router A's side of the point-to-point link, not the next-hop router.  
B) ✓ Router B is Router A's next hop toward external destinations, and its interface is `10.0.1.2`.  
C) ✗ `192.248.0.1` is beyond Router B and is not directly reachable as Router A's next hop.  
D) ✗ A `/30` network here does not provide `10.0.1.3` as a usable router interface address; it is the broadcast address.

**Correct:** B
