## 8 Transport Layer

## Questions

#### 1. What are the primary objectives of the transport layer?  
A) To ensure data encryption and confidentiality  
B) To provide an efficient, reliable, and cost-effective service  
C) To provide end-to-end delivery of data  
D) To shield upper layers from the peculiarities of the network  

#### 2. Which of the following statements correctly distinguish the transport layer from the network layer?  
A) The network layer provides end-to-end delivery, while the transport layer provides hop-by-hop delivery  
B) The transport layer operates mostly inside routers, while the network layer operates in end stations  
C) The transport layer operates in end stations, while the network layer operates mostly inside the network  
D) The transport layer can improve the reliability of the service provided by the network layer  

#### 3. Which functions are performed by the transport layer but not by the data link layer?  
A) Multiplexing multiple connections on the same host  
B) Error control  
C) Operating on a single physical link  
D) Flow control  

#### 4. Which of the following are true about the position and role of the transport layer?  
A) It provides end-to-end data transmission service  
B) It is primarily dealt with by applications people  
C) It operates between layers 1 and 4  
D) It is the interface to the network for most programmers  

#### 5. Which types of transport services exist?  
A) Reliable  
B) Connection-oriented  
C) Broadcast  
D) Connectionless  

#### 6. Which of the following correctly describe TCP and UDP?  
A) UDP supports both unicast and multicast communication  
B) UDP is connectionless and unacknowledged at the transport layer  
C) TCP supports multicast communication  
D) TCP is connection-oriented and reliable  

#### 7. Which transport service primitives are essential for establishing and managing connections?  
A) Disconnect  
B) Send  
C) Connect  
D) Listen  

#### 8. What elements are fundamental to transport protocols?  
A) Flow control and buffering  
B) Addressing  
C) Routing algorithms  
D) Connection establishment and release  

#### 9. How is a transport layer connection uniquely identified on a host?  
A) By a transport address called TSAP  
B) By the host IP address alone  
C) By the MAC address of the host  
D) By a combination of host address and port number  

#### 10. Why are ports necessary in transport layer communication?  
A) To allow more than one connection between the same pair of hosts  
B) To enable multiplexing of different services on a single host  
C) To encrypt data between hosts  
D) To allow multiple connections or datagrams to be distinguished on the same host  

#### 11. In client-server operation, what is the role of the server regarding ports?  
A) The server listens on a specific port waiting for client connections  
B) The server uses ports only for multicast communication  
C) The server hands the connection to the appropriate service process after accepting a connection  
D) The server initiates connections to clients on random ports  

#### 12. Which of the following are true about connection establishment in transport protocols?  
A) Sequence numbers may be used to handle lost, delayed, or duplicate packets  
B) It requires a handshake to confirm connection acceptance  
C) It always succeeds regardless of network reliability  
D) It involves the client sending a connection request and the server accepting it  

#### 13. What challenges does connection release in transport protocols address?  
A) Encrypting the connection termination messages  
B) Preventing data loss during connection termination  
C) Ensuring both sides agree the connection is closed  
D) Avoiding indefinite waiting for the other side to close the connection  

#### 14. Regarding flow control and buffering, which statements are correct?  
A) The sender should send data as fast as possible without considering buffer space  
B) The sender may send more data than the buffer space if willing to risk data loss  
C) Flow control is only necessary at the physical layer  
D) The sender keeps copies of sent data to allow retransmission if needed  

#### 15. How does the transport layer handle multiplexing?  
A) By using multiple network connections for the same task, such as download acceleration  
B) By keeping multiple connections to/from the same host separate  
C) By encrypting data streams to separate them  
D) By assigning unique IP addresses to each connection on the same host  



<br>

## Answers

#### 1. What are the primary objectives of the transport layer?  
A) ✗ To ensure data encryption and confidentiality — Encryption is typically handled at other layers (e.g., presentation or application).  
B) ✓ To provide an efficient, reliable, and cost-effective service — These are key goals of the transport layer.  
C) ✓ To provide end-to-end delivery of data — This is a core function of the transport layer.  
D) ✓ To shield upper layers from the peculiarities of the network — The transport layer abstracts network details from upper layers.  

**Correct:** B, C, D


#### 2. Which of the following statements correctly distinguish the transport layer from the network layer?  
A) ✗ The network layer provides end-to-end delivery, while the transport layer provides hop-by-hop delivery — The network layer is hop-by-hop; transport is end-to-end.  
B) ✗ The transport layer operates mostly inside routers, while the network layer operates in end stations — This is reversed.  
C) ✓ The transport layer operates in end stations, while the network layer operates mostly inside the network — Correct distinction.  
D) ✓ The transport layer can improve the reliability of the service provided by the network layer — Transport can add reliability on top of network service.  

**Correct:** C, D


#### 3. Which functions are performed by the transport layer but not by the data link layer?  
A) ✓ Multiplexing multiple connections on the same host — This is unique to the transport layer.  
B) ✓ Error control — Both layers do error control, but transport layer does it end-to-end.  
C) ✗ Operating on a single physical link — This is a function of the data link layer, not transport.  
D) ✓ Flow control — Both layers do flow control, but transport does it end-to-end, DLL on a single link.  

**Correct:** A, B, D


#### 4. Which of the following are true about the position and role of the transport layer?  
A) ✗ It provides end-to-end data transmission service — Layers 1-4 collectively provide this; transport uses this service but does not alone provide it.  
B) ✓ It is primarily dealt with by applications people — Transport layer is the boundary between network and application layers.  
C) ✗ It operates between layers 1 and 4 — Transport is layer 4; layers 1-3 are below it.  
D) ✓ It is the interface to the network for most programmers — Transport layer APIs are commonly used by applications.  

**Correct:** B, D


#### 5. Which types of transport services exist?  
A) ✓ Reliable — Some transport services provide reliability (e.g., TCP).  
B) ✓ Connection-oriented — One main type of transport service.  
C) ✗ Broadcast — Broadcast is not a transport service type; it is a network or link layer concept.  
D) ✓ Connectionless — Another main type of transport service.  

**Correct:** A, B, D


#### 6. Which of the following correctly describe TCP and UDP?  
A) ✓ UDP supports both unicast and multicast communication — UDP can be used for multicast.  
B) ✓ UDP is connectionless and unacknowledged at the transport layer — UDP does not guarantee delivery or acknowledgments.  
C) ✗ TCP supports multicast communication — TCP is unicast only; multicast is not supported.  
D) ✓ TCP is connection-oriented and reliable — This is the defining characteristic of TCP.  

**Correct:** A, B, D


#### 7. Which transport service primitives are essential for establishing and managing connections?  
A) ✓ Disconnect — Used to release the connection properly.  
B) ✓ Send — Used to transmit data after connection is established.  
C) ✓ Connect — Client initiates connection establishment.  
D) ✓ Listen — Server waits for incoming connections.  

**Correct:** A, B, C, D


#### 8. What elements are fundamental to transport protocols?  
A) ✓ Flow control and buffering — Essential for managing data flow and storage.  
B) ✓ Addressing — Needed to identify endpoints.  
C) ✗ Routing algorithms — Routing is a network layer function, not transport.  
D) ✓ Connection establishment and release — Core to managing connections.  

**Correct:** A, B, D


#### 9. How is a transport layer connection uniquely identified on a host?  
A) ✓ By a transport address called TSAP — TSAP is the transport service access point.  
B) ✗ By the host IP address alone — IP address identifies the host but not the specific connection.  
C) ✗ By the MAC address of the host — MAC addresses operate at the data link layer, not transport.  
D) ✓ By a combination of host address and port number — This combination uniquely identifies a connection endpoint.  

**Correct:** A, D


#### 10. Why are ports necessary in transport layer communication?  
A) ✓ To allow more than one connection between the same pair of hosts — Ports differentiate multiple connections between same hosts.  
B) ✓ To enable multiplexing of different services on a single host — Different services listen on different ports.  
C) ✗ To encrypt data between hosts — Encryption is not a function of ports.  
D) ✓ To allow multiple connections or datagrams to be distinguished on the same host — Ports enable multiplexing.  

**Correct:** A, B, D


#### 11. In client-server operation, what is the role of the server regarding ports?  
A) ✓ The server listens on a specific port waiting for client connections — Servers wait on well-known or assigned ports.  
B) ✗ The server uses ports only for multicast communication — Ports are used for all types of communication, not just multicast.  
C) ✓ The server hands the connection to the appropriate service process after accepting a connection — Server dispatches connection to service handler.  
D) ✗ The server initiates connections to clients on random ports — Clients initiate connections, servers listen.  

**Correct:** A, C


#### 12. Which of the following are true about connection establishment in transport protocols?  
A) ✓ Sequence numbers may be used to handle lost, delayed, or duplicate packets — Sequence numbers help maintain order and detect duplicates.  
B) ✓ It requires a handshake to confirm connection acceptance — Handshake ensures both sides agree on connection.  
C) ✗ It always succeeds regardless of network reliability — Network issues can cause connection failures.  
D) ✓ It involves the client sending a connection request and the server accepting it — This is the basic connection setup process.  

**Correct:** A, B, D


#### 13. What challenges does connection release in transport protocols address?  
A) ✗ Encrypting the connection termination messages — Encryption is not part of connection release.  
B) ✓ Preventing data loss during connection termination — Data must be fully delivered before closing.  
C) ✓ Ensuring both sides agree the connection is closed — Proper termination requires mutual agreement.  
D) ✓ Avoiding indefinite waiting for the other side to close the connection — Timeouts or handshakes prevent hanging connections.  

**Correct:** B, C, D


#### 14. Regarding flow control and buffering, which statements are correct?  
A) ✗ The sender should send data as fast as possible without considering buffer space — Ignoring buffer space risks data loss.  
B) ✓ The sender may send more data than the buffer space if willing to risk data loss — This is possible but risky.  
C) ✗ Flow control is only necessary at the physical layer — Flow control is critical at transport layer as well.  
D) ✓ The sender keeps copies of sent data to allow retransmission if needed — Necessary for reliability.  

**Correct:** B, D


#### 15. How does the transport layer handle multiplexing?  
A) ✓ By using multiple network connections for the same task, such as download acceleration — Transport layer can manage multiple connections for performance.  
B) ✓ By keeping multiple connections to/from the same host separate — Prevents data mix-up between services.  
C) ✗ By encrypting data streams to separate them — Encryption is unrelated to multiplexing.  
D) ✗ By assigning unique IP addresses to each connection on the same host — IP addresses are per host, not per connection.  

**Correct:** A, B