## 5 The Network Layer

## Study Notes

### 1. 🌐 Introduction to the Network Layer

The **Network Layer** is a crucial part of the OSI (Open Systems Interconnection) model, responsible for managing how data is sent from one device to another across multiple networks. It acts as a bridge between the Transport Layer above it and the Data Link Layer below it. The main job of the Network Layer is to **establish, maintain, and terminate connections** between devices, while also **isolating the upper layers from the details of the underlying data transmission technologies**.

In simpler terms, the Network Layer makes sure that data can travel from your computer to another computer somewhere else in the world, even if the data has to pass through many intermediate devices and networks along the way.

#### Key Functions of the Network Layer:
- **Connection management:** Setting up, maintaining, and ending communication sessions.
- **Addressing:** Assigning unique identifiers to devices so they can be found on the network.
- **Routing:** Determining the best path for data to travel through the network.
- **Packet switching:** Breaking data into smaller pieces (packets) and sending them independently.


### 2. 📦 Packet Switching: How Data Travels

One of the fundamental concepts in the Network Layer is **packet switching**. Instead of sending a continuous stream of data, the data is divided into smaller chunks called **packets**. Each packet contains two parts:
- A **header**, which includes control information like the destination address.
- The **data** itself, which is the actual content being sent.

#### How Packet Switching Works:
- The data stream is split into packets.
- Each packet travels independently through the network.
- Intermediate devices called **routers** or **switches** receive packets and forward them toward their destination.
- Packets may take different routes but eventually arrive at the destination, where they are reassembled into the original data.

This method is efficient because it allows the network to share resources among many users and routes packets around congested or broken links.


### 3. 🔄 Types of Networks: Connectionless vs Connection-Oriented

Networks can be broadly classified into two types based on how they handle data transmission:

#### Connectionless Networks (Datagram Service)
- No need to establish a connection before sending data.
- Each packet is treated independently and routed based on its destination address.
- Routers use **forwarding tables** to decide where to send each packet next.
- Generally, there is **no error control** or guarantee that packets arrive in order.
- Example: The Internet Protocol (IP) is connectionless.

#### Connection-Oriented Networks
- A connection is established between the sender and receiver before data transfer begins.
- Data is sent as a sequence of packets over this connection.
- Routing is done based on the connection, not individual packets.
- The network often provides **error control** and ensures packets arrive in order.
- Example: Telephone networks and some virtual circuit networks.

#### Key Differences:
| Feature               | Connectionless                 | Connection-Oriented           |
|-----------------------|-------------------------------|------------------------------|
| Setup                 | No connection setup needed    | Connection setup required    |
| Addressing            | Destination address in packet | Connection ID used           |
| Router State          | Stateless                     | Stateful (maintains connection info) |
| Routing               | Per-packet                   | Per-connection               |
| Error Control         | Usually none                  | Usually provided             |
| Quality of Service    | Difficult                    | Possible                    |
| Congestion Control    | Difficult                    | Possible                    |


### 4. 🏷️ Addressing: Identifying Devices on the Network

Addressing is essential because it allows the network to identify where data should be sent. Without unique addresses, packets would have no destination.

#### Types of Addresses:
- **Names:** Human-readable identifiers (e.g., personal names).
- **NIC Numbers:** Unique hardware addresses like MAC addresses.
- **Postal Addresses:** Physical mailing addresses.
- **Telephone Numbers:** Used in telephony networks.

#### Addressing Schemes:
- **Flat Addressing:** Addresses have no hierarchy or structure. For example, Ethernet MAC addresses are flat and unique but don’t provide location information.
- **Hierarchical Addressing:** Addresses are structured in layers, making routing easier. For example, postal addresses or IP addresses have parts that indicate country, region, city, etc.

In networking, addressing happens at multiple layers:
- Physical Layer: Hardware addresses.
- Data Link Layer: MAC addresses.
- Network Layer: IP addresses.
- Application Layer: Domain names or user IDs.


### 5. 🛣️ Routing: Finding the Path for Data

Routing is the process of determining the path that data packets take from the source to the destination across a network.

#### Roles in Routing:
- **End systems (hosts):** These are the devices that send and receive data but do not forward traffic.
- **Intermediate systems (routers):** Devices that forward packets between different networks or subnets.

#### Forwarding vs Routing:
- **Forwarding:** The action of moving a packet from an input interface to the appropriate output interface on a router, based on a forwarding table.
- **Routing:** The process of building and updating the forwarding tables, often using routing algorithms and protocols.

#### Desirable Properties of Routing Algorithms:
- **Correctness:** Always find a valid path if one exists.
- **Simplicity:** Easy to implement and understand.
- **Robustness:** Can handle failures and changes in the network.
- **Stability:** Avoid frequent route changes.
- **Fairness:** Avoid favoring some routes unfairly.
- **Optimality:** Find the best path according to some metric.


### 6. 🧭 Types of Routing Algorithms

Routing algorithms can be classified based on how routes are determined and updated:

#### Static (Non-Adaptive) Routing
- Routes are manually configured and do not change unless manually updated.
- Suitable for small or stable networks.
- Not resilient to failures or changes.
- Uses hierarchical addressing to simplify routing tables.

#### Dynamic (Adaptive) Routing
- Routers exchange information periodically to update routes.
- Routes adapt to network changes like congestion or failures.
- Can be centralized (one router computes routes) or distributed (each router computes routes independently).
- Takes into account factors like link speed, delay, congestion, error rate, cost, and policy.

#### Source Routing
- The sender specifies the entire route the packet should take.
- Less common in modern networks.


### 7. 🛤️ Routing Mechanisms

Several routing mechanisms are used in networks:

- **Shortest Path Routing:** Calculates the shortest path between nodes using algorithms like Dijkstra’s.
- **Flooding:** Sends packets on all possible paths to ensure delivery (inefficient but reliable).
- **Distance Vector Routing:** Each router maintains a table of distances to all destinations and shares it with neighbors.
- **Link State Routing:** Routers maintain a map of the network topology and compute routes independently.
- **Broadcast Routing:** Sends packets to all nodes in a network.


### 8. 🌍 Hierarchical Routing for Large Networks

In very large networks like the Internet, it’s impossible for routers to keep track of every node. Hierarchical routing groups routers into regions or domains:

- Each region handles internal routing.
- **Gateways** or border routers manage routing between regions.
- This reduces the size of routing tables and improves scalability.
- Sometimes multiple levels of hierarchy are used.


### 9. 📡 Multicast Routing: Sending to Multiple Recipients

Multicast routing allows sending a single packet to a specific group of hosts rather than all hosts or just one.

- Routers keep track of which multicast groups are reachable via which links.
- Packets are forwarded only to links that lead to group members.
- Efficient for applications like video conferencing or streaming to multiple users.


### 10. 🚦 Congestion and Congestion Control

**Congestion** happens when the network is overloaded with traffic, causing delays and packet loss.

- **Offered traffic:** The amount of data sent into the network.
- **Delivered traffic:** The amount of data successfully received.

When offered traffic approaches or exceeds network capacity, congestion occurs.

#### Congestion Control Techniques:
- **Open-loop control:** Prevent congestion by controlling traffic before it happens (e.g., traffic shaping).
- **Closed-loop control:** Detect congestion and react by adjusting traffic flow (e.g., dropping packets, throttling senders).


### 11. 🎯 Quality of Service (QoS)

Different applications have different requirements for network performance:

| Application      | Reliability | Delay | Jitter (delay variation) | Bandwidth |
|------------------|-------------|-------|--------------------------|-----------|
| Email            | High        | Not critical | Don’t care             | Low       |
| File Transfer    | High        | Not critical | Don’t care             | Medium    |
| Web Browsing     | High        | Not critical | Don’t care             | Medium    |
| Remote Login     | High        | Not critical | Low                    | Low       |
| Audio Streaming  | Low         | Not critical | Significant            | Medium    |
| Video Streaming  | Low         | Not critical | Significant            | High      |
| Telephony        | Low         | Critical     | Low                    | Low       |
| Video Conferencing| Low        | Critical     | High                   | High      |

#### QoS Techniques:
- **Over-provisioning:** Providing more capacity than needed.
- **Buffering:** Temporarily storing packets to smooth traffic.
- **Traffic Shaping:** Controlling the flow of packets to avoid bursts.

#### QoS Technologies:
- **Integrated Services (IntServ):** Guarantees QoS for each flow (e.g., RSVP protocol).
- **Differentiated Services (DiffServ):** Classifies traffic into different priority levels and treats them accordingly.


### 12. 🔗 Internetworking: Connecting Different Networks

Networks often differ in protocols, addressing schemes, packet sizes, and QoS requirements. **Internetworking** is the process of connecting these diverse networks to form a larger network (like the Internet).

#### Methods of Interconnection:
- **Physical Layer:** Repeaters and hubs.
- **Data Link Layer:** Bridges and switches.
- **Network Layer:** Routers.
- **Transport Layer:** Transport gateways.
- **Application Layer:** Application gateways.

Each method operates at a different layer of the OSI model and serves different purposes in connecting networks.


### Summary

The Network Layer is essential for enabling communication across diverse and complex networks. It handles addressing, routing, and packet switching, ensuring data reaches its destination efficiently and reliably. Understanding the differences between connectionless and connection-oriented networks, routing algorithms, congestion control, and QoS helps in designing and managing modern networks effectively.