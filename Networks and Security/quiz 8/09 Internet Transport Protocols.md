## 9 Internet Transport Protocols

## Questions

#### 1. Which of the following statements correctly describe the differences between TCP and UDP?  
A) TCP is connection-oriented and provides reliable, in-order delivery of data.  
B) UDP is connectionless and does not guarantee delivery or ordering of packets.  
C) TCP uses ports only for multiplexing, while UDP does not use ports.  
D) UDP is preferred for applications where speed is more important than reliability.  

#### 2. Regarding port numbers in TCP and UDP, which of the following are true?  
A) Ports are 16-bit integers ranging from 0 to 65535.  
B) Ports below 1024 are considered privileged and usually require system-level permissions.  
C) Each TCP or UDP segment contains only the destination port, not the source port.  
D) The combination of source IP, source port, destination IP, and destination port uniquely identifies a connection.  

#### 3. Which of the following correctly describe the TCP three-way handshake process?  
A) The client sends a SYN packet with a random initial sequence number and ACK bit set.  
B) The server responds with a SYN-ACK packet, acknowledging the client's SYN and sending its own SYN.  
C) The client replies with a SYN-ACK packet to complete the handshake.  
D) The handshake ensures both hosts agree that the connection is established before data transfer begins.  

#### 4. In TCP reliable data transfer, which mechanisms are used to ensure data integrity and correct sequencing?  
A) Sequence numbers identify the byte stream position of data in each segment.  
B) TCP uses cumulative acknowledgments to confirm receipt of all bytes up to a certain point.  
C) TCP retransmits segments only when duplicate acknowledgments are received, ignoring timeouts.  
D) The receiver discards corrupted packets detected by checksum mismatch and requests retransmission.  

#### 5. Which of the following statements about TCP timeout and retransmission are accurate?  
A) TCP sets the retransmission timeout strictly equal to the most recent measured Round Trip Time (RTT).  
B) TCP estimates RTT by averaging several recent SampleRTT measurements to smooth out variations.  
C) Premature timeouts cause unnecessary retransmissions, while excessively long timeouts delay loss recovery.  
D) TCP uses separate timers for each outstanding segment to manage retransmissions efficiently.  

#### 6. Which of the following are true about the TCP connection closing process?  
A) Either side can initiate connection termination by sending a FIN packet.  
B) Both sides must send and acknowledge FIN packets to fully close the connection.  
C) The connection closes immediately after one side sends a FIN packet.  
D) The TCP state "TIME_WAIT" exists to ensure all delayed packets are properly handled before final closure.  

#### 7. Consider the TCP state machine: which of the following statements correctly describe TCP states?  
A) The "LISTEN" state means the server is waiting for an incoming connection request.  
B) The "SYN_SENT" state indicates the application has initiated a connection and is waiting for a SYN-ACK.  
C) The "CLOSE_WAIT" state means the local side has initiated connection termination and is waiting for the remote side to close.  
D) The "ESTABLISHED" state indicates normal data transfer is ongoing between the two hosts.  

#### 8. Which of the following applications or protocols typically use UDP instead of TCP, and why?  
A) VoIP, because it requires low latency and can tolerate some packet loss.  
B) DNS, because it needs fast query-response without connection overhead.  
C) HTTP, because it requires reliable, ordered delivery of web content.  
D) NFS (Network File System), because it can implement its own reliability mechanisms on top of UDP.



<br>

## Answers

#### 1. Which of the following statements correctly describe the differences between TCP and UDP?  
A) ✓ TCP is connection-oriented and provides reliable, in-order delivery of data.  
B) ✓ UDP is connectionless and does not guarantee delivery or ordering of packets.  
C) ✗ Both TCP and UDP use ports; UDP also uses ports for multiplexing.  
D) ✓ UDP is preferred for applications where speed is more important than reliability.  

**Correct:** A, B, D


#### 2. Regarding port numbers in TCP and UDP, which of the following are true?  
A) ✓ Ports are 16-bit integers ranging from 0 to 65535.  
B) ✓ Ports below 1024 are privileged and usually require system permissions.  
C) ✗ Each segment contains both source and destination ports, not just destination port.  
D) ✓ The combination of source IP, source port, destination IP, and destination port uniquely identifies a connection.  

**Correct:** A, B, D


#### 3. Which of the following correctly describe the TCP three-way handshake process?  
A) ✗ The client sends a SYN packet with ACK bit reset, not set.  
B) ✓ The server replies with SYN and ACK set, acknowledging client's SYN and sending its own SYN.  
C) ✗ The client replies with ACK only (not SYN-ACK) to complete handshake.  
D) ✓ The handshake ensures both hosts agree the connection is established before data transfer.  

**Correct:** B, D


#### 4. In TCP reliable data transfer, which mechanisms are used to ensure data integrity and correct sequencing?  
A) ✓ Sequence numbers identify the byte stream position of data in each segment.  
B) ✓ TCP uses cumulative acknowledgments to confirm receipt of all bytes up to a point.  
C) ✗ TCP retransmits on both timeout and duplicate ACKs, not only duplicate ACKs.  
D) ✓ Receiver discards corrupted packets detected by checksum mismatch and requests retransmission.  

**Correct:** A, B, D


#### 5. Which of the following statements about TCP timeout and retransmission are accurate?  
A) ✗ TCP sets timeout longer than RTT, not strictly equal to the most recent RTT.  
B) ✓ TCP estimates RTT by averaging several recent SampleRTT measurements to smooth variations.  
C) ✓ Premature timeouts cause unnecessary retransmissions; long timeouts delay loss recovery.  
D) ✗ TCP uses a single retransmission timer for the oldest unacknowledged segment, not separate timers per segment.  

**Correct:** B, C


#### 6. Which of the following are true about the TCP connection closing process?  
A) ✓ Either side can initiate termination by sending a FIN packet.  
B) ✓ Both sides must send and acknowledge FIN packets to fully close the connection.  
C) ✗ Connection does not close immediately after one FIN; proper handshake and states are required.  
D) ✓ TIME_WAIT state ensures all delayed packets are handled before final closure.  

**Correct:** A, B, D


#### 7. Consider the TCP state machine: which of the following statements correctly describe TCP states?  
A) ✓ LISTEN means server is waiting for incoming connection requests.  
B) ✓ SYN_SENT means application has initiated connection and is waiting for SYN-ACK.  
C) ✗ CLOSE_WAIT means local side received FIN and is waiting for application to close, not that local side initiated close.  
D) ✓ ESTABLISHED means normal data transfer is ongoing.  

**Correct:** A, B, D


#### 8. Which of the following applications or protocols typically use UDP instead of TCP, and why?  
A) ✓ VoIP uses UDP for low latency and tolerates some packet loss.  
B) ✓ DNS uses UDP for fast query-response without connection overhead.  
C) ✗ HTTP requires reliable, ordered delivery, so it uses TCP.  
D) ✓ NFS can use UDP and implement its own reliability mechanisms on top.  

**Correct:** A, B, D