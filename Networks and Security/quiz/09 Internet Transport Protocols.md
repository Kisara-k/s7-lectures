## 9 Internet Transport Protocols

## Questions

#### 1. Which of the following statements correctly describe the differences between TCP and UDP?  
A) TCP is connection-oriented and provides reliable data transfer, while UDP is connectionless and does not guarantee reliability.  
B) UDP uses ports for multiplexing, but TCP does not use ports.  
C) TCP provides flow control and congestion control, whereas UDP does not.  
D) UDP segments include sequence numbers for ordering, but TCP segments do not.

#### 2. Regarding port numbers in TCP and UDP, which of the following are true?  
A) Ports are 16-bit integers ranging from 0 to 65535.  
B) Ports below 1024 are considered privileged and usually require system privileges to use.  
C) Each TCP or UDP segment contains only the destination port, not the source port.  
D) The combination of source IP, source port, destination IP, and destination port uniquely identifies a connection.

#### 3. Which of the following are characteristics of UDP?  
A) It adds a checksum to detect errors in the datagram.  
B) It guarantees in-order delivery of packets.  
C) It is suitable for applications like VoIP and DNS.  
D) It establishes a connection before sending data.

#### 4. What is the maximum size of TCP data in a segment, assuming no IP or TCP options?  
A) 65535 bytes  
B) 65515 bytes  
C) 65495 bytes  
D) 65520 bytes

#### 5. Which of the following statements about TCP’s three-way handshake are correct?  
A) The client sends a SYN packet with a random initial sequence number and ACK bit set.  
B) The server responds with a SYN-ACK packet acknowledging the client’s sequence number plus one.  
C) The client completes the handshake by sending a SYN-ACK packet with updated sequence and acknowledgment numbers.  
D) If any handshake packet is lost, the sender retransmits after a timeout.

#### 6. In TCP, what does the acknowledgment number represent?  
A) The sequence number of the last byte received correctly.  
B) The sequence number of the next byte expected from the sender.  
C) The total number of bytes received so far.  
D) The number of segments acknowledged cumulatively.

#### 7. Which of the following are true about TCP flow control?  
A) The receive window specifies the number of bytes the receiver is willing to accept.  
B) Flow control prevents the sender from overwhelming the receiver.  
C) The receive window is measured in segments, not bytes.  
D) Flow control is implemented by adjusting the congestion window size.

#### 8. Which TCP flags are involved in connection establishment and termination?  
A) SYN and ACK for connection establishment.  
B) FIN and ACK for connection termination.  
C) RST for resetting a connection.  
D) PSH for urgent data during connection setup.

#### 9. Which of the following are valid reasons for TCP retransmissions?  
A) Timeout expiration without receiving an acknowledgment.  
B) Receipt of duplicate acknowledgments indicating possible packet loss.  
C) Receiving an out-of-order segment.  
D) When the sender’s buffer is full.

#### 10. How does TCP estimate the retransmission timeout (RTO)?  
A) By using the most recent SampleRTT measurement only.  
B) By averaging several recent SampleRTT measurements to smooth out variations.  
C) By setting the timeout shorter than the estimated RTT to detect losses quickly.  
D) By ignoring retransmissions when calculating SampleRTT.

#### 11. Which of the following statements about TCP connection states are correct?  
A) The "listen" state means the server is waiting for an incoming connection request.  
B) The "syn sent" state indicates the client has sent a SYN and is waiting for a SYN-ACK.  
C) The "close wait" state means the connection is fully closed.  
D) The "timed wait" state ensures all packets have been received and acknowledged before closing.

#### 12. Regarding TCP segment structure, which fields are correctly matched with their purpose?  
A) Sequence number: identifies the byte stream number of the first data byte in the segment.  
B) Acknowledgment number: cumulative acknowledgment of received bytes.  
C) Urgent pointer: used to indicate urgent data, commonly used in modern TCP implementations.  
D) Header length: specifies the length of the TCP header in 32-bit words.

#### 13. Which of the following statements about ports and services are true?  
A) Well-known ports are assigned to common services like HTTP and DNS.  
B) Clients typically use well-known ports to initiate connections.  
C) Servers listen on specific ports to accept incoming connections.  
D) The combination of client source port and server destination port is sufficient to identify a connection.

#### 14. In the context of TCP reliable data transfer, which of the following are true?  
A) TCP uses cumulative acknowledgments to confirm receipt of all bytes up to a certain point.  
B) TCP segments are retransmitted only when a timeout occurs, never on duplicate ACKs.  
C) TCP discards corrupted packets detected by checksum errors.  
D) TCP guarantees delivery of data in the exact order it was sent.

#### 15. Which of the following describe the relationship between IP, TCP, and data link layers?  
A) TCP segments are encapsulated within IP packets.  
B) IP packets are encapsulated within data link layer frames.  
C) UDP headers are added after the IP header but before the data link header.  
D) The data link layer is responsible for routing packets across the Internet.



<br>

## Answers

#### 1. Which of the following statements correctly describe the differences between TCP and UDP?  
A) ✓ TCP is connection-oriented and provides reliable data transfer, while UDP is connectionless and does not guarantee reliability.  
B) ✗ UDP uses ports for multiplexing, but TCP does not use ports. (Both use ports.)  
C) ✓ TCP provides flow control and congestion control, whereas UDP does not.  
D) ✗ UDP segments include sequence numbers for ordering, but TCP segments do not. (Only TCP uses sequence numbers.)  

**Correct:** A, C


#### 2. Regarding port numbers in TCP and UDP, which of the following are true?  
A) ✓ Ports are 16-bit integers ranging from 0 to 65535.  
B) ✓ Ports below 1024 are considered privileged and usually require system privileges to use.  
C) ✗ Each TCP or UDP segment contains only the destination port, not the source port. (Both source and destination ports are included.)  
D) ✓ The combination of source IP, source port, destination IP, and destination port uniquely identifies a connection.  

**Correct:** A, B, D


#### 3. Which of the following are characteristics of UDP?  
A) ✓ It adds a checksum to detect errors in the datagram.  
B) ✗ It guarantees in-order delivery of packets. (UDP does not guarantee order.)  
C) ✓ It is suitable for applications like VoIP and DNS.  
D) ✗ It establishes a connection before sending data. (UDP is connectionless.)  

**Correct:** A, C


#### 4. What is the maximum size of TCP data in a segment, assuming no IP or TCP options?  
A) ✗ 65535 bytes (This is max IP packet size including headers.)  
B) ✗ 65515 bytes (This is max IP packet minus IP header.)  
C) ✓ 65495 bytes (Max TCP data = 65535 - 20 (IP header) - 20 (TCP header))  
D) ✗ 65520 bytes (Incorrect calculation.)  

**Correct:** C


#### 5. Which of the following statements about TCP’s three-way handshake are correct?  
A) ✗ The client sends a SYN packet with a random initial sequence number and ACK bit set. (ACK bit is reset in first SYN.)  
B) ✓ The server responds with a SYN-ACK packet acknowledging the client’s sequence number plus one.  
C) ✗ The client completes the handshake by sending a SYN-ACK packet with updated sequence and acknowledgment numbers. (Client sends ACK only, no SYN in last step.)  
D) ✓ If any handshake packet is lost, the sender retransmits after a timeout.  

**Correct:** B, D


#### 6. In TCP, what does the acknowledgment number represent?  
A) ✗ The sequence number of the last byte received correctly. (It is the next expected byte number.)  
B) ✓ The sequence number of the next byte expected from the sender.  
C) ✗ The total number of bytes received so far. (Not cumulative count, but next expected byte.)  
D) ✗ The number of segments acknowledged cumulatively. (ACK is byte-based, not segment-based.)  

**Correct:** B


#### 7. Which of the following are true about TCP flow control?  
A) ✓ The receive window specifies the number of bytes the receiver is willing to accept.  
B) ✓ Flow control prevents the sender from overwhelming the receiver.  
C) ✗ The receive window is measured in segments, not bytes. (Measured in bytes.)  
D) ✗ Flow control is implemented by adjusting the congestion window size. (Congestion control is separate from flow control.)  

**Correct:** A, B


#### 8. Which TCP flags are involved in connection establishment and termination?  
A) ✓ SYN and ACK for connection establishment.  
B) ✓ FIN and ACK for connection termination.  
C) ✓ RST for resetting a connection.  
D) ✗ PSH for urgent data during connection setup. (PSH is for pushing data, not connection setup.)  

**Correct:** A, B, C


#### 9. Which of the following are valid reasons for TCP retransmissions?  
A) ✓ Timeout expiration without receiving an acknowledgment.  
B) ✓ Receipt of duplicate acknowledgments indicating possible packet loss.  
C) ✗ Receiving an out-of-order segment. (Out-of-order segments are buffered, not retransmitted.)  
D) ✗ When the sender’s buffer is full. (Buffer fullness does not trigger retransmission.)  

**Correct:** A, B


#### 10. How does TCP estimate the retransmission timeout (RTO)?  
A) ✗ By using the most recent SampleRTT measurement only. (This is too variable.)  
B) ✓ By averaging several recent SampleRTT measurements to smooth out variations.  
C) ✗ By setting the timeout shorter than the estimated RTT to detect losses quickly. (Timeout must be longer than RTT.)  
D) ✓ By ignoring retransmissions when calculating SampleRTT.  

**Correct:** B, D


#### 11. Which of the following statements about TCP connection states are correct?  
A) ✓ The "listen" state means the server is waiting for an incoming connection request.  
B) ✓ The "syn sent" state indicates the client has sent a SYN and is waiting for a SYN-ACK.  
C) ✗ The "close wait" state means the connection is fully closed. (It means the other side initiated close; local side still open.)  
D) ✓ The "timed wait" state ensures all packets have been received and acknowledged before closing.  

**Correct:** A, B, D


#### 12. Regarding TCP segment structure, which fields are correctly matched with their purpose?  
A) ✓ Sequence number: identifies the byte stream number of the first data byte in the segment.  
B) ✓ Acknowledgment number: cumulative acknowledgment of received bytes.  
C) ✗ Urgent pointer: used to indicate urgent data, commonly used in modern TCP implementations. (Generally not used.)  
D) ✓ Header length: specifies the length of the TCP header in 32-bit words.  

**Correct:** A, B, D


#### 13. Which of the following statements about ports and services are true?  
A) ✓ Well-known ports are assigned to common services like HTTP and DNS.  
B) ✗ Clients typically use well-known ports to initiate connections. (Clients usually use ephemeral ports ≥1024.)  
C) ✓ Servers listen on specific ports to accept incoming connections.  
D) ✗ The combination of client source port and server destination port is sufficient to identify a connection. (Must include IP addresses too.)  

**Correct:** A, C


#### 14. In the context of TCP reliable data transfer, which of the following are true?  
A) ✓ TCP uses cumulative acknowledgments to confirm receipt of all bytes up to a certain point.  
B) ✗ TCP segments are retransmitted only when a timeout occurs, never on duplicate ACKs. (Duplicate ACKs can trigger retransmission.)  
C) ✓ TCP discards corrupted packets detected by checksum errors.  
D) ✓ TCP guarantees delivery of data in the exact order it was sent.  

**Correct:** A, C, D


#### 15. Which of the following describe the relationship between IP, TCP, and data link layers?  
A) ✓ TCP segments are encapsulated within IP packets.  
B) ✓ IP packets are encapsulated within data link layer frames.  
C) ✗ UDP headers are added after the IP header but before the data link header. (UDP header is part of IP payload, before data link header.)  
D) ✗ The data link layer is responsible for routing packets across the Internet. (Routing is done by the network layer, IP.)  

**Correct:** A, B