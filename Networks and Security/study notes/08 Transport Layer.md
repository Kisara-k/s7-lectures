## 8 Transport Layer

## Study Notes

### 1. 🚚 Introduction to the Transport Layer

The Transport Layer is a crucial part of the network communication model. It sits above the Network Layer and below the Application Layer, acting as a bridge between the two. Its main job is to provide **end-to-end delivery of data** between devices (or hosts) on a network. This means it ensures that data sent from one device reaches the correct application on another device reliably and efficiently.

The Transport Layer has several important objectives:

- **End-to-end delivery:** It guarantees that data travels from the source application on one host to the destination application on another host.
- **Efficiency, reliability, and cost-effectiveness:** It aims to deliver data in a way that is fast, accurate, and uses network resources wisely.
- **Shielding upper layers:** It hides the complexities and peculiarities of the underlying network from the applications, so developers don’t have to worry about how data is routed or fragmented.

In summary, the Transport Layer makes sure that communication between applications on different devices is smooth, reliable, and transparent.


### 2. 🛤️ Transport Layer vs Network Layer

It’s important to understand how the Transport Layer differs from the Network Layer:

- The **Network Layer** mainly operates **inside the network**, especially in routers. Its job is to move packets from one network to another, handling routing and addressing.
- The **Transport Layer** operates **at the end stations** (the devices themselves), managing communication between applications on these devices.

While the Network Layer provides a basic service of moving packets, the Transport Layer can **improve this service** by adding reliability and better control. For example, the Network Layer might deliver packets out of order or lose some packets, but the Transport Layer can detect these issues and fix them, providing a more reliable connection.


### 3. 🔧 Functions of the Transport Layer

The Transport Layer performs several key functions to ensure smooth communication:

- **Data delivery:** It guarantees that data sent from one end reaches the other end correctly.
- **Handling network peculiarities:** The network might fragment data into smaller pieces or combine multiple data streams. The Transport Layer manages these issues by:
  - **Fragmentation:** Breaking data into smaller chunks if needed.
  - **Multiplexing:** Combining multiple data streams into one.
  - **Inverse multiplexing:** Splitting one data stream across multiple network connections.
- **Managing multiple connections:** A single device can have many simultaneous connections. The Transport Layer keeps these connections separate and organized.
- **Connection management:** It establishes and terminates connections between devices, including naming and addressing these connections.
- **Flow control:** It regulates the rate of data transmission to prevent overwhelming the receiver.


### 4. 🔄 Transport Layer vs Data Link Layer

The Transport Layer shares some functions with the Data Link Layer (DLL), such as:

- Managing connections
- Controlling flow
- Error control

However, the key difference is **scope**:

- The **Data Link Layer** works on a **single link** between two directly connected devices (like between your computer and your router).
- The **Transport Layer** works **end-to-end**, meaning it manages communication across the entire network path, from the source device to the destination device.


### 5. 🏗️ Position and Role of the Transport Layer

In the OSI model, the Transport Layer is Layer 4. Layers 1 to 4 (Physical, Data Link, Network, and Transport) provide the **end-to-end data transmission service**. These layers are mostly the concern of network engineers.

Layers 5 to 7 (Session, Presentation, Application) use the services provided by the Transport Layer and are more relevant to application developers.

The Transport Layer acts as the **interface to the network for most programmers**, meaning it’s the layer where applications interact with the network to send and receive data.


### 6. 📡 Types of Transport Services

The Transport Layer can provide different types of services depending on the needs of the application:

- **Connection-oriented service:** A connection is established before data is sent, and it remains active until the communication is complete. This service is reliable because it ensures data arrives in order and without errors.
- **Connectionless service:** Data is sent without establishing a connection first. This is faster but less reliable because there is no guarantee that data will arrive or arrive in order.
- **Reliable service:** Guarantees data delivery, error checking, and retransmission if needed.
- **Unreliable service:** Does not guarantee delivery or error correction.
- **Multicast service:** Sends data to multiple recipients simultaneously.


### 7. 🌐 Internet Transport Protocols: TCP and UDP

Two main protocols operate at the Transport Layer on the Internet:

- **TCP (Transmission Control Protocol):**
  - Connection-oriented: establishes a connection before data transfer.
  - Reliable: ensures data is delivered correctly and in order.
  - Unicast: sends data to a single recipient.
  
- **UDP (User Datagram Protocol):**
  - Connectionless: no connection setup.
  - Unreliable: no guarantee of delivery or order.
  - Supports unicast and multicast.
  
TCP is used when reliability is critical (e.g., web browsing, email), while UDP is used for applications where speed is more important than reliability (e.g., video streaming, online gaming).


### 8. 🛠️ Transport Service Primitives

Transport protocols provide a set of basic operations (primitives) that applications use to communicate:

- **Listen:** Wait for an incoming connection request.
- **Connect:** Establish a connection to a remote host.
- **Send:** Transmit data.
- **Receive:** Wait for data to arrive.
- **Disconnect:** Terminate the connection.

These primitives form the basic building blocks for communication between applications.


### 9. 🧩 Elements of Transport Protocols

Transport protocols consist of several key elements:

- **Addressing:** Identifying the correct application on a host using a transport address, often called a TSAP (Transport Service Access Point). This is usually a combination of the host’s IP address and a port number.
- **Connection Establishment:** The process of setting up a communication session between two hosts.
- **Connection Release:** Properly closing the connection to avoid data loss or hanging connections.
- **Flow Control and Buffering:** Managing the rate of data transmission and temporarily storing data to prevent loss.
- **Multiplexing:** Handling multiple simultaneous connections on the same host, ensuring data is delivered to the correct application.


### 10. 🔢 Addressing and Ports

Each host can have multiple applications communicating over the network simultaneously. To keep these communications separate, the Transport Layer uses **ports**:

- A **port** is a number that identifies a specific application or service on a host.
- Multiple connections can exist between the same two hosts but use different ports to distinguish them.
- For example, web servers typically listen on port 80 (HTTP), while email servers might listen on port 25 (SMTP).

This system allows multiple services to run on the same device without interfering with each other.


### 11. 🤝 Client-Server Operation

Many Internet services follow a **client-server model**:

- **Servers** provide services and listen on specific ports, waiting for clients to connect.
- **Clients** initiate connections to these ports to use the services.

For example, a web server listens on port 80. When a client wants to access a website, it connects to port 80 on the server’s IP address. The server then hands off the connection to the appropriate service process to handle the client’s requests.


### 12. 🔗 Connection Establishment and Release

#### Connection Establishment

To start communication, the client sends a **connection request** to the server. The server responds by accepting the connection, and then data transfer begins.

However, networks are not always perfect. Packets can be lost, delayed, or duplicated. To handle this, protocols use **sequence numbers** to keep track of data and ensure everything arrives correctly.

#### Connection Release

When communication is finished, both sides must agree to close the connection to avoid data loss or hanging connections. This often involves a **three-way handshake** to confirm the connection is properly closed.

There are scenarios where packets involved in connection release might be lost, so protocols include mechanisms to handle these cases gracefully.


### 13. ⚖️ Flow Control and Buffering

Flow control is about managing the speed of data transmission:

- The sender should send data as fast as possible but not so fast that the receiver’s buffer overflows.
- The sender keeps copies of sent data in case retransmission is needed.
- The amount of data sent depends on the available buffer space at the receiver.
- If the sender sends more data than the receiver can handle, data loss may occur.

Buffering helps by temporarily storing data until the receiver is ready to process it.


### 14. 🔀 Multiplexing

Multiplexing allows the Transport Layer to handle multiple connections simultaneously:

- It keeps data streams separate so that, for example, web traffic doesn’t get mixed with email traffic.
- It can also use multiple network connections for the same task to improve performance, such as download accelerators that split a file into parts and download them in parallel.


### Summary

The Transport Layer is essential for reliable, efficient communication between applications on different devices. It manages connections, ensures data integrity, controls flow, and multiplexes multiple streams. Understanding its functions and protocols like TCP and UDP is fundamental to grasping how modern networks and the Internet work.