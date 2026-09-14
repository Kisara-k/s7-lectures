## 8 Transport Layer

## Questions

#### 1. What are the primary objectives of the transport layer?  
A) To provide end-to-end delivery of data  
B) To ensure data encryption and confidentiality  
C) To provide an efficient, reliable, and cost-effective service  
D) To shield upper layers from the peculiarities of the network  

#### 2. Which of the following statements correctly distinguish the transport layer from the network layer?  
A) The transport layer operates mostly inside routers, while the network layer operates in end stations  
B) The transport layer operates in end stations, while the network layer operates mostly inside the network  
C) The transport layer can improve the reliability of the service provided by the network layer  
D) The network layer provides end-to-end delivery, while the transport layer provides hop-by-hop delivery  

#### 3. Which functions are performed by the transport layer but not by the data link layer?  
A) Flow control  
B) Error control  
C) Multiplexing multiple connections on the same host  
D) Operating on a single physical link  

#### 4. Which of the following are true about the position and role of the transport layer?  
A) It is the interface to the network for most programmers  
B) It operates between layers 1 and 4  
C) It provides end-to-end data transmission service  
D) It is primarily dealt with by applications people  

#### 5. Which types of transport services exist?  
A) Connection-oriented  
B) Connectionless  
C) Reliable  
D) Broadcast  

#### 6. Which of the following correctly describe TCP and UDP?  
A) TCP is connection-oriented and reliable  
B) UDP is connectionless and unacknowledged at the transport layer  
C) TCP supports multicast communication  
D) UDP supports both unicast and multicast communication  

#### 7. Which transport service primitives are essential for establishing and managing connections?  
A) Listen  
B) Connect  
C) Send  
D) Disconnect  

#### 8. What elements are fundamental to transport protocols?  
A) Addressing  
B) Connection establishment and release  
C) Routing algorithms  
D) Flow control and buffering  

#### 9. How is a transport layer connection uniquely identified on a host?  
A) By the host IP address alone  
B) By a transport address called TSAP  
C) By a combination of host address and port number  
D) By the MAC address of the host  

#### 10. Why are ports necessary in transport layer communication?  
A) To allow multiple connections or datagrams to be distinguished on the same host  
B) To enable multiplexing of different services on a single host  
C) To encrypt data between hosts  
D) To allow more than one connection between the same pair of hosts  

#### 11. In client-server operation, what is the role of the server regarding ports?  
A) The server listens on a specific port waiting for client connections  
B) The server initiates connections to clients on random ports  
C) The server hands the connection to the appropriate service process after accepting a connection  
D) The server uses ports only for multicast communication  

#### 12. Which of the following are true about connection establishment in transport protocols?  
A) It requires a handshake to confirm connection acceptance  
B) Sequence numbers may be used to handle lost, delayed, or duplicate packets  
C) It always succeeds regardless of network reliability  
D) It involves the client sending a connection request and the server accepting it  

#### 13. What challenges does connection release in transport protocols address?  
A) Ensuring both sides agree the connection is closed  
B) Preventing data loss during connection termination  
C) Avoiding indefinite waiting for the other side to close the connection  
D) Encrypting the connection termination messages  

#### 14. Regarding flow control and buffering, which statements are correct?  
A) The sender should send data as fast as possible without considering buffer space  
B) The sender keeps copies of sent data to allow retransmission if needed  
C) The sender may send more data than the buffer space if willing to risk data loss  
D) Flow control is only necessary at the physical layer  

#### 15. How does the transport layer handle multiplexing?  
A) By keeping multiple connections to/from the same host separate  
B) By using multiple network connections for the same task, such as download acceleration  
C) By encrypting data streams to separate them  
D) By assigning unique IP addresses to each connection on the same host



<br>

## Answers

#### 1. What are the primary objectives of the transport layer?  
A) ✓ To provide end-to-end delivery of data — This is a core function of the transport layer.  
B) ✗ To ensure data encryption and confidentiality — Encryption is typically handled at other layers (e.g., presentation or application).  
C) ✓ To provide an efficient, reliable, and cost-effective service — These are key goals of the transport layer.  
D) ✓ To shield upper layers from the peculiarities of the network — The transport layer abstracts network details from upper layers.  

**Correct:** A, C, D


#### 2. Which of the following statements correctly distinguish the transport layer from the network layer?  
A) ✗ The transport layer operates mostly inside routers, while the network layer operates in end stations — This is reversed.  
B) ✓ The transport layer operates in end stations, while the network layer operates mostly inside the network — Correct distinction.  
C) ✓ The transport layer can improve the reliability of the service provided by the network layer — Transport can add reliability on top of network service.  
D) ✗ The network layer provides end-to-end delivery, while the transport layer provides hop-by-hop delivery — The network layer is hop-by-hop; transport is end-to-end.  

**Correct:** B, C


#### 3. Which functions are performed by the transport layer but not by the data link layer?  
A) ✓ Flow control — Both layers do flow control, but transport does it end-to-end, DLL on a single link.  
B) ✓ Error control — Both layers do error control, but transport layer does it end-to-end.  
C) ✓ Multiplexing multiple connections on the same host — This is unique to the transport layer.  
D) ✗ Operating on a single physical link — This is a function of the data link layer, not transport.  

**Correct:** A, B, C


#### 4. Which of the following are true about the position and role of the transport layer?  
A) ✓ It is the interface to the network for most programmers — Transport layer APIs are commonly used by applications.  
B) ✗ It operates between layers 1 and 4 — Transport is layer 4; layers 1-3 are below it.  
C) ✗ It provides end-to-end data transmission service — Layers 1-4 collectively provide this; transport uses this service but does not alone provide it.  
D) ✓ It is primarily dealt with by applications people — Transport layer is the boundary between network and application layers.  

**Correct:** A, D


#### 5. Which types of transport services exist?  
A) ✓ Connection-oriented — One main type of transport service.  
B) ✓ Connectionless — Another main type of transport service.  
C) ✓ Reliable — Some transport services provide reliability (e.g., TCP).  
D) ✗ Broadcast — Broadcast is not a transport service type; it is a network or link layer concept.  

**Correct:** A, B, C


#### 6. Which of the following correctly describe TCP and UDP?  
A) ✓ TCP is connection-oriented and reliable — This is the defining characteristic of TCP.  
B) ✓ UDP is connectionless and unacknowledged at the transport layer — UDP does not guarantee delivery or acknowledgments.  
C) ✗ TCP supports multicast communication — TCP is unicast only; multicast is not supported.  
D) ✓ UDP supports both unicast and multicast communication — UDP can be used for multicast.  

**Correct:** A, B, D


#### 7. Which transport service primitives are essential for establishing and managing connections?  
A) ✓ Listen — Server waits for incoming connections.  
B) ✓ Connect — Client initiates connection establishment.  
C) ✓ Send — Used to transmit data after connection is established.  
D) ✓ Disconnect — Used to release the connection properly.  

**Correct:** A, B, C, D


#### 8. What elements are fundamental to transport protocols?  
A) ✓ Addressing — Needed to identify endpoints.  
B) ✓ Connection establishment and release — Core to managing connections.  
C) ✗ Routing algorithms — Routing is a network layer function, not transport.  
D) ✓ Flow control and buffering — Essential for managing data flow and storage.  

**Correct:** A, B, D


#### 9. How is a transport layer connection uniquely identified on a host?  
A) ✗ By the host IP address alone — IP address identifies the host but not the specific connection.  
B) ✓ By a transport address called TSAP — TSAP is the transport service access point.  
C) ✓ By a combination of host address and port number — This combination uniquely identifies a connection endpoint.  
D) ✗ By the MAC address of the host — MAC addresses operate at the data link layer, not transport.  

**Correct:** B, C


#### 10. Why are ports necessary in transport layer communication?  
A) ✓ To allow multiple connections or datagrams to be distinguished on the same host — Ports enable multiplexing.  
B) ✓ To enable multiplexing of different services on a single host — Different services listen on different ports.  
C) ✗ To encrypt data between hosts — Encryption is not a function of ports.  
D) ✓ To allow more than one connection between the same pair of hosts — Ports differentiate multiple connections between same hosts.  

**Correct:** A, B, D


#### 11. In client-server operation, what is the role of the server regarding ports?  
A) ✓ The server listens on a specific port waiting for client connections — Servers wait on well-known or assigned ports.  
B) ✗ The server initiates connections to clients on random ports — Clients initiate connections, servers listen.  
C) ✓ The server hands the connection to the appropriate service process after accepting a connection — Server dispatches connection to service handler.  
D) ✗ The server uses ports only for multicast communication — Ports are used for all types of communication, not just multicast.  

**Correct:** A, C


#### 12. Which of the following are true about connection establishment in transport protocols?  
A) ✓ It requires a handshake to confirm connection acceptance — Handshake ensures both sides agree on connection.  
B) ✓ Sequence numbers may be used to handle lost, delayed, or duplicate packets — Sequence numbers help maintain order and detect duplicates.  
C) ✗ It always succeeds regardless of network reliability — Network issues can cause connection failures.  
D) ✓ It involves the client sending a connection request and the server accepting it — This is the basic connection setup process.  

**Correct:** A, B, D


#### 13. What challenges does connection release in transport protocols address?  
A) ✓ Ensuring both sides agree the connection is closed — Proper termination requires mutual agreement.  
B) ✓ Preventing data loss during connection termination — Data must be fully delivered before closing.  
C) ✓ Avoiding indefinite waiting for the other side to close the connection — Timeouts or handshakes prevent hanging connections.  
D) ✗ Encrypting the connection termination messages — Encryption is not part of connection release.  

**Correct:** A, B, C


#### 14. Regarding flow control and buffering, which statements are correct?  
A) ✗ The sender should send data as fast as possible without considering buffer space — Ignoring buffer space risks data loss.  
B) ✓ The sender keeps copies of sent data to allow retransmission if needed — Necessary for reliability.  
C) ✓ The sender may send more data than the buffer space if willing to risk data loss — This is possible but risky.  
D) ✗ Flow control is only necessary at the physical layer — Flow control is critical at transport layer as well.  

**Correct:** B, C


#### 15. How does the transport layer handle multiplexing?  
A) ✓ By keeping multiple connections to/from the same host separate — Prevents data mix-up between services.  
B) ✓ By using multiple network connections for the same task, such as download acceleration — Transport layer can manage multiple connections for performance.  
C) ✗ By encrypting data streams to separate them — Encryption is unrelated to multiplexing.  
D) ✗ By assigning unique IP addresses to each connection on the same host — IP addresses are per host, not per connection.  

**Correct:** A, B