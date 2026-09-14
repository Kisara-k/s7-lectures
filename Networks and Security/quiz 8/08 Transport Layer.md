## 8 Transport Layer

## Questions

#### 1. What are the primary objectives of the transport layer?  
A) To provide end-to-end delivery of data  
B) To manage routing within the network  
C) To provide an efficient, reliable, and cost-effective service  
D) To shield upper layers from the peculiarities of the network  

#### 2. Which of the following statements correctly distinguish the transport layer from the network layer?  
A) The transport layer operates mostly inside routers, while the network layer operates in end stations  
B) The transport layer can provide a more reliable service than the network layer  
C) The network layer handles fragmentation and multiplexing, while the transport layer does not  
D) The transport layer operates end-to-end, whereas the network layer operates primarily inside the network  

#### 3. Which functions are performed by the transport layer but not by the data link layer?  
A) Flow control  
B) Error control  
C) Managing multiple connections on the same hosts  
D) Operating on a single link  

#### 4. Which of the following are true about transport layer addressing and ports?  
A) A transport address (TSAP) is typically a combination of a host address and a port number  
B) Ports allow multiple connections between the same pair of hosts to be distinguished  
C) Each host can only have one TSAP at a time  
D) Ports are used for multiplexing at the transport layer  

#### 5. Regarding connection establishment in transport protocols, which statements are correct?  
A) Sequence numbers may be used to handle lost, delayed, or duplicate packets  
B) Connection establishment requires only the client to send a request; the server does not acknowledge  
C) The server accepts the connection request and hands it over to the appropriate service process  
D) Connection establishment is unnecessary in connectionless transport services like UDP  

#### 6. Which of the following describe valid scenarios or challenges during connection release?  
A) Both sides must agree to close the connection to avoid data loss  
B) The final acknowledgment (ACK) can be lost, requiring retransmission  
C) Connection release can be completed unilaterally by the client without server involvement  
D) Lost responses during connection release can cause repeated disconnect requests  

#### 7. What are the key considerations in transport layer flow control and buffering?  
A) The sender should send data as fast as possible without regard to buffer space  
B) The sender keeps copies of sent data to allow retransmission if needed  
C) The sender may send more data than the buffer can hold if willing to risk data loss  
D) Flow control is only necessary in connectionless transport protocols  

#### 8. Which statements about transport layer multiplexing are correct?  
A) Multiplexing allows the transport layer to handle multiple connections to/from the same host simultaneously  
B) Multiplexing ensures that data intended for one service (e.g., web server) is not delivered to another (e.g., email)  
C) The transport layer cannot use multiple network connections for the same task  
D) Multiplexing is only relevant at the network layer, not the transport layer



<br>

## Answers

#### 1. What are the primary objectives of the transport layer?  
A) ✓ Provides end-to-end delivery of data, a core transport layer goal  
B) ✗ Routing is a network layer function, not transport  
C) ✓ Efficiency, reliability, and cost-effectiveness are key transport objectives  
D) ✓ Shielding upper layers from network peculiarities is a transport layer role  

**Correct:** A, C, D


#### 2. Which of the following statements correctly distinguish the transport layer from the network layer?  
A) ✗ Opposite is true: network layer operates inside routers, transport layer in end stations  
B) ✓ Transport layer can improve reliability beyond what network layer provides  
C) ✗ Transport layer also handles fragmentation and multiplexing, not only network layer  
D) ✓ Transport layer is end-to-end; network layer operates mostly inside the network  

**Correct:** B, D


#### 3. Which functions are performed by the transport layer but not by the data link layer?  
A) ✓ Both layers do flow control, but transport layer does it end-to-end  
B) ✗ Error control exists in both layers, but DLL is link-level only  
C) ✓ Managing multiple connections on the same hosts is unique to transport layer  
D) ✗ DLL operates on a single link, transport layer operates end-to-end  

**Correct:** A, C


#### 4. Which of the following are true about transport layer addressing and ports?  
A) ✓ TSAP is host address plus port number, defining transport address  
B) ✓ Ports distinguish multiple connections between same hosts  
C) ✗ Hosts can have multiple TSAPs (multiple ports) simultaneously  
D) ✓ Ports enable multiplexing at the transport layer  

**Correct:** A, B, D


#### 5. Regarding connection establishment in transport protocols, which statements are correct?  
A) ✓ Sequence numbers help handle lost, delayed, or duplicate packets during connection setup  
B) ✗ Server must acknowledge connection requests for reliable establishment  
C) ✓ Server hands connection to appropriate service process after acceptance  
D) ✓ Connection establishment is unnecessary in connectionless protocols like UDP  

**Correct:** A, C, D


#### 6. Which of the following describe valid scenarios or challenges during connection release?  
A) ✓ Both sides must agree to close connection to avoid data loss  
B) ✓ Final ACK can be lost, requiring retransmission or timeout handling  
C) ✗ Connection release requires cooperation from both sides, not unilateral closure  
D) ✓ Lost responses can cause repeated disconnect requests and retransmissions  

**Correct:** A, B, D


#### 7. What are the key considerations in transport layer flow control and buffering?  
A) ✗ Sender must consider buffer space to avoid data loss, not send blindly fast  
B) ✓ Sender keeps copies of sent data for possible retransmission  
C) ✓ Sender may send more than buffer space if willing to risk data loss  
D) ✗ Flow control is mainly relevant in connection-oriented protocols, not connectionless  

**Correct:** B, C


#### 8. Which statements about transport layer multiplexing are correct?  
A) ✓ Multiplexing allows multiple simultaneous connections to/from the same host  
B) ✓ Multiplexing ensures data is delivered to correct service (e.g., web vs email)  
C) ✗ Transport layer can use multiple network connections for the same task (e.g., download accelerators)  
D) ✗ Multiplexing is a transport layer function, not only network layer  

**Correct:** A, B