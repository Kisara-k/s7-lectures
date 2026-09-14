## 9 Internet Transport Protocols

## Study Notes

### 1. 🌐 Introduction to Internet Transport Protocols

The transport layer in the Internet is responsible for delivering data between applications running on different devices. It acts as a bridge between the application layer (where programs like web browsers or email clients operate) and the network layer (which handles routing and addressing). The main goal of the transport layer is to provide communication services directly to the applications, ensuring data is sent and received correctly and efficiently.

Two primary transport protocols dominate the Internet:

- **TCP (Transmission Control Protocol):** A connection-oriented, reliable protocol designed for lossless data transfer.
- **UDP (User Datagram Protocol):** A connectionless, non-reliable protocol used when speed is more important than reliability.

Besides these, other transport protocols exist but TCP and UDP are the most widely used.


### 2. 🔢 Ports and Connections: How Data Finds Its Way

When data travels over the Internet, it’s not enough to know just the IP addresses of the sender and receiver. The transport layer uses **ports** to identify specific applications or services on each device. Think of ports as door numbers in a building: the IP address is the building address, and the port number is the door to the right apartment.

- **Ports** are 16-bit numbers ranging from 0 to 65535.
- Each data packet or segment contains:
  - Source IP address
  - Destination IP address
  - Source port number
  - Destination port number

Together, these four values uniquely identify a connection between two applications on different hosts.

#### Why ports matter:
- They allow multiple applications to use the network simultaneously without confusion.
- Each service listens on a specific port (e.g., web servers listen on port 80).
- Clients use ephemeral (temporary) ports, usually above 1024, to initiate connections.

#### Well-known ports:
- Ports below 1024 are **privileged** and usually reserved for system or well-known services.
- Examples:
  - HTTP (web) uses port 80
  - DNS uses port 53
- The official list of port assignments is maintained by IANA (Internet Assigned Numbers Authority).


### 3. 📦 UDP (User Datagram Protocol): Fast and Simple

UDP is a lightweight transport protocol designed for applications where speed is critical and occasional data loss is acceptable. Unlike TCP, UDP does not establish a connection before sending data, nor does it guarantee delivery, order, or error correction.

#### Key features of UDP:
- **Connectionless:** No handshake or setup before sending data.
- **No reliability:** Packets may be lost, duplicated, or arrive out of order.
- **Minimal overhead:** Adds only a small header to the IP packet.
- **Header fields include:**
  - Source port
  - Destination port
  - Length of the UDP datagram
  - Checksum for error detection

#### When is UDP used?
- Real-time applications like **VoIP (Voice over IP)** where delays are worse than occasional lost packets.
- **DNS (Domain Name System)** queries, which are short and can tolerate retries.
- Network file systems like **NFS**.
- Remote Procedure Calls (RPCs) where the application handles reliability.

UDP is ideal when the application itself can manage retransmissions or when speed is more important than perfect accuracy.


### 4. 🔄 TCP (Transmission Control Protocol): Reliable and Ordered Delivery

TCP is the backbone of most Internet communication, providing a reliable, ordered, and error-checked delivery of a stream of bytes between applications.

#### What makes TCP special?

- **Connection-oriented:** Before data transfer, TCP establishes a connection through a handshake process.
- **Reliable:** Ensures all data is received correctly and in order.
- **Full duplex:** Data can flow simultaneously in both directions.
- **Flow control:** Prevents the sender from overwhelming the receiver.
- **Multiplexing:** Uses ports to allow multiple connections between the same hosts.

#### TCP as a byte stream:
TCP treats data as a continuous stream of bytes without message boundaries. Each byte is numbered, allowing the receiver to reorder segments and detect missing data.


### 5. 🤝 Establishing a TCP Connection: The Three-Way Handshake

Before two applications can exchange data over TCP, they must establish a connection. This is done through a process called the **three-way handshake**, which synchronizes both ends.

#### Steps of the handshake:

1. **SYN (Synchronize) packet:** The client sends a packet with the SYN flag set and a random initial sequence number (say, x).
2. **SYN-ACK (Synchronize-Acknowledge):** The server responds with a packet that has both SYN and ACK flags set, acknowledging the client’s sequence number (ACK = x+1) and sending its own sequence number (y).
3. **ACK:** The client sends back an ACK packet acknowledging the server’s sequence number (ACK = y+1).

Once this handshake completes, the connection is established, and data transfer can begin.

If any step fails (e.g., no response), the sender will retransmit after a timeout.


### 6. 📋 TCP Data Transfer: Segments, Sequence Numbers, and Acknowledgments

After connection setup, TCP breaks the data into **segments**. Each segment contains:

- TCP header (minimum 20 bytes)
- Data payload (variable length)

#### Important header fields:

- **Source and destination ports:** Identify the connection endpoints.
- **Sequence number:** The byte number of the first byte in this segment.
- **Acknowledgment number:** The next expected byte from the other side.
- **Receive window:** How many bytes the receiver is willing to accept (flow control).
- **Flags:** Control bits like SYN, ACK, FIN, RST, PSH, URG.
- **Checksum:** For error detection.

#### How TCP ensures reliability:

- The receiver sends **cumulative acknowledgments** indicating the next byte it expects.
- If a segment is lost or corrupted, the sender retransmits it.
- TCP uses timers to detect lost segments (timeout retransmission).
- Duplicate acknowledgments can also trigger retransmissions.


### 7. ⏳ TCP Retransmission and Timeout Management

TCP must decide when to retransmit lost segments. This depends on estimating the **Round Trip Time (RTT)** — the time it takes for a segment to go to the receiver and for the acknowledgment to come back.

#### Challenges in setting timeout:

- If the timeout is too short, TCP retransmits unnecessarily (premature timeout).
- If too long, TCP reacts slowly to losses, reducing performance.

#### How TCP estimates RTT:

- Measures **SampleRTT** for each segment (time from sending to receiving ACK).
- Uses a smoothed average of recent SampleRTTs to calculate an **Estimated RTT**.
- Adjusts timeout dynamically based on this estimate.


### 8. 🛑 Closing a TCP Connection: Graceful Termination

Closing a TCP connection is a coordinated process because either side may still have data to send.

#### Steps to close:

1. One side sends a **FIN** packet indicating it has finished sending data.
2. The other side acknowledges the FIN and may send its own FIN when ready.
3. The first side acknowledges the second FIN.
4. Both sides enter a **timed wait** state to ensure all packets have been received and no duplicates remain.

This process ensures that both sides agree the connection is closed cleanly.


### 9. ⚙️ TCP State Machine: Managing Connection States

TCP maintains a state machine to track the status of each connection. Some key states include:

- **CLOSED:** No connection exists.
- **LISTEN:** Server waiting for incoming connection requests.
- **SYN_SENT:** Client has sent SYN, waiting for SYN-ACK.
- **SYN_RECEIVED:** Server has received SYN, waiting for ACK.
- **ESTABLISHED:** Connection is open and data transfer can occur.
- **FIN_WAIT_1 and FIN_WAIT_2:** States during connection termination.
- **CLOSE_WAIT:** Waiting for application to close after receiving FIN.
- **LAST_ACK:** Waiting for final acknowledgment after sending FIN.
- **TIME_WAIT:** Waiting to ensure all packets have cleared the network.

Understanding these states helps in diagnosing connection issues and understanding TCP behavior.


### Summary

The Internet transport layer uses TCP and UDP to deliver data between applications. UDP is simple and fast but unreliable, suitable for real-time or simple query applications. TCP is complex but reliable, providing ordered, error-checked, and flow-controlled data transfer through connection setup, data segmentation, acknowledgments, retransmissions, and graceful connection teardown. Ports play a crucial role in identifying services and multiplexing connections. TCP’s state machine and timeout management ensure robust communication even over unreliable networks.