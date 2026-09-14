## 8 Transport Layer

## Questions

#### 1. What are the primary objectives of the transport layer?  
A) To provide an efficient, reliable, and cost-effective service  
B) To provide end-to-end delivery of data  
C) To shield upper layers from the peculiarities of the network  
D) To manage routing within the network  

#### 2. Which of the following statements correctly distinguish the transport layer from the network layer?  
A) The transport layer operates mostly inside routers, while the network layer operates in end stations  
B) The transport layer operates end-to-end, whereas the network layer operates primarily inside the network  
C) The network layer handles fragmentation and multiplexing, while the transport layer does not  
D) The transport layer can provide a more reliable service than the network layer  

#### 3. Which functions are performed by the transport layer but not by the data link layer?  
A) Error control  
B) Managing multiple connections on the same hosts  
C) Operating on a single link  
D) Flow control  

#### 4. Which of the following are true about transport layer addressing and ports?  
A) Ports allow multiple connections between the same pair of hosts to be distinguished  
B) Ports are used for multiplexing at the transport layer  
C) Each host can only have one TSAP at a time  
D) A transport address (TSAP) is typically a combination of a host address and a port number  

#### 5. Regarding connection establishment in transport protocols, which statements are correct?  
A) The server accepts the connection request and hands it over to the appropriate service process  
B) Connection establishment requires only the client to send a request; the server does not acknowledge  
C) Sequence numbers may be used to handle lost, delayed, or duplicate packets  
D) Connection establishment is unnecessary in connectionless transport services like UDP  

#### 6. Which of the following describe valid scenarios or challenges during connection release?  
A) Both sides must agree to close the connection to avoid data loss  
B) Lost responses during connection release can cause repeated disconnect requests  
C) The final acknowledgment (ACK) can be lost, requiring retransmission  
D) Connection release can be completed unilaterally by the client without server involvement  

#### 7. What are the key considerations in transport layer flow control and buffering?  
A) Flow control is only necessary in connectionless transport protocols  
B) The sender may send more data than the buffer can hold if willing to risk data loss  
C) The sender should send data as fast as possible without regard to buffer space  
D) The sender keeps copies of sent data to allow retransmission if needed  

#### 8. Which statements about transport layer multiplexing are correct?  
A) Multiplexing ensures that data intended for one service (e.g., web server) is not delivered to another (e.g., email)  
B) The transport layer cannot use multiple network connections for the same task  
C) Multiplexing allows the transport layer to handle multiple connections to/from the same host simultaneously  
D) Multiplexing is only relevant at the network layer, not the transport layer  



<br>

## Answers

#### 1. What are the primary objectives of the transport layer?  
A) ✓ Efficiency, reliability, and cost-effectiveness are key transport objectives  
B) ✓ Provides end-to-end delivery of data, a core transport layer goal  
C) ✓ Shielding upper layers from network peculiarities is a transport layer role  
D) ✗ Routing is a network layer function, not transport  

**Correct:** A, B, C


#### 2. Which of the following statements correctly distinguish the transport layer from the network layer?  
A) ✗ Opposite is true: network layer operates inside routers, transport layer in end stations  
B) ✓ Transport layer is end-to-end; network layer operates mostly inside the network  
C) ✗ Transport layer also handles fragmentation and multiplexing, not only network layer  
D) ✓ Transport layer can improve reliability beyond what network layer provides  

**Correct:** B, D


#### 3. Which functions are performed by the transport layer but not by the data link layer?  
A) ✗ Error control exists in both layers, but DLL is link-level only  
B) ✓ Managing multiple connections on the same hosts is unique to transport layer  
C) ✗ DLL operates on a single link, transport layer operates end-to-end  
D) ✓ Both layers do flow control, but transport layer does it end-to-end  

**Correct:** B, D


#### 4. Which of the following are true about transport layer addressing and ports?  
A) ✓ Ports distinguish multiple connections between same hosts  
B) ✓ Ports enable multiplexing at the transport layer  
C) ✗ Hosts can have multiple TSAPs (multiple ports) simultaneously  
D) ✓ TSAP is host address plus port number, defining transport address  

**Correct:** A, B, D


#### 5. Regarding connection establishment in transport protocols, which statements are correct?  
A) ✓ Server hands connection to appropriate service process after acceptance  
B) ✗ Server must acknowledge connection requests for reliable establishment  
C) ✓ Sequence numbers help handle lost, delayed, or duplicate packets during connection setup  
D) ✓ Connection establishment is unnecessary in connectionless protocols like UDP  

**Correct:** A, C, D


#### 6. Which of the following describe valid scenarios or challenges during connection release?  
A) ✓ Both sides must agree to close connection to avoid data loss  
B) ✓ Lost responses can cause repeated disconnect requests and retransmissions  
C) ✓ Final ACK can be lost, requiring retransmission or timeout handling  
D) ✗ Connection release requires cooperation from both sides, not unilateral closure  

**Correct:** A, B, C


#### 7. What are the key considerations in transport layer flow control and buffering?  
A) ✗ Flow control is mainly relevant in connection-oriented protocols, not connectionless  
B) ✓ Sender may send more than buffer space if willing to risk data loss  
C) ✗ Sender must consider buffer space to avoid data loss, not send blindly fast  
D) ✓ Sender keeps copies of sent data for possible retransmission  

**Correct:** B, D


#### 8. Which statements about transport layer multiplexing are correct?  
A) ✓ Multiplexing ensures data is delivered to correct service (e.g., web vs email)  
B) ✗ Transport layer can use multiple network connections for the same task (e.g., download accelerators)  
C) ✓ Multiplexing allows multiple simultaneous connections to/from the same host  
D) ✗ Multiplexing is a transport layer function, not only network layer  

**Correct:** A, C