## 2 Data Link Layer

## Study Notes

### 1. 🧩 Introduction to the Data Link Layer

The Data Link Layer (DLL) is the second layer in the OSI (Open Systems Interconnection) model, sitting just above the Physical Layer and below the Network Layer. Its main role is to provide reliable communication between two directly connected nodes by packaging raw bits from the physical layer into meaningful data units called **frames**. It ensures that data is transferred error-free, in the correct sequence, and without overwhelming the receiver.

The DLL performs several critical functions that make communication over a physical medium efficient and reliable. These include **synchronization**, **error control**, **flow control**, **data compression**, and **encryption**. Additionally, when multiple devices share the same communication medium (like in a local area network), the DLL manages **media access control** to avoid collisions and coordinate transmissions.


### 2. ⏳ Synchronization: Defining Data Boundaries

One of the fundamental tasks of the Data Link Layer is **synchronization**. This means the receiver must know exactly where each unit of data (frame) begins and ends. Without this, the receiver cannot correctly interpret the incoming stream of bits.

- **Data Units:** At the DLL, data is divided into units called **frames**. Each frame contains a header, the actual data (payload), and a trailer.
- **Types of Synchronization:**
  - **Fixed-length synchronization:** Frames have a fixed size, so the receiver knows the frame boundaries by counting bytes or bits. This is common in asynchronous transmission or cell-based networks.
  - **Variable-length synchronization:** Frames can vary in size, so special markers or delimiters are used to indicate the start and end of each frame.

#### Frame Delimitation Methods

- **Character Count:** The frame header includes a count of the number of characters in the frame.
- **Character-Oriented Framing:** Special characters like **STX** (start of text) and **ETX** (end of text) mark the frame boundaries.
- **Bit-Oriented Framing:** Frames are delimited by a unique bit pattern called a **flag sequence** (e.g., `01111110`). To prevent confusion when this pattern appears in the data, a technique called **bit stuffing** is used, where extra bits are inserted to differentiate data from flags.

#### Challenges in Synchronization

- **Data Loss:** If the start or end markers are lost or corrupted, the receiver cannot correctly identify frame boundaries.
- **Data Errors:** Errors in the control characters or flags can cause misinterpretation of frame boundaries.
- **Control Characters in Data:** Sometimes, the special characters used for framing may appear in the actual data, which requires techniques like byte stuffing or bit stuffing to avoid confusion.


### 3. 🛡️ Error Control: Detecting and Correcting Transmission Errors

Physical transmission of data is prone to errors due to noise, interference, or signal degradation. Errors can manifest as missing bits, extra bits, or bits flipped from 0 to 1 or vice versa. These errors often occur in bursts, meaning several bits in a row may be affected.

#### Why Error Control is Important

The Data Link Layer must ensure that the data received is exactly what was sent. To do this, it uses **error detection** and **error correction** techniques.

#### Error Detection Techniques

To detect errors, extra bits called **Error Detection Codes (EDC)** are added to the frame. Common methods include:

- **Parity Bits:** A simple method where a single bit is added to make the number of 1s either even (even parity) or odd (odd parity).
- **Checksum:** A value calculated by summing the data bytes and sending this sum along with the data. The receiver recalculates and compares.
- **Cyclic Redundancy Check (CRC):** A more powerful method that treats the data as a polynomial and divides it by a generator polynomial. The remainder is sent as the CRC code. CRC can detect many types of errors with high reliability.

Despite these methods, some errors may still go undetected (called **residual errors**), but the probability is kept very low.

#### Error Correction Methods

Once an error is detected, the system must decide how to handle it:

- **Forward Error Correction (FEC):** Extra redundant data is added so the receiver can correct some errors without needing retransmission. This is useful in one-way communication or where retransmission is costly (e.g., satellite links, CD-ROMs).
- **Automatic Repeat Request (ARQ):** The receiver requests retransmission of corrupted frames. There are two main ARQ types:
  - **Stop-and-Wait ARQ:** The sender transmits one frame and waits for an acknowledgment (ACK) before sending the next. Simple but inefficient for long delays.
  - **Continuous ARQ (Sliding Window Protocol):** Multiple frames are sent before waiting for ACKs. Both sender and receiver maintain sequence numbers to track frames. If an error is detected, a negative acknowledgment (NAK) is sent, and retransmission occurs.


### 4. 🔄 Flow Control: Managing Data Transmission Rate

Flow control ensures that the sender does not overwhelm the receiver with data faster than it can process. Without flow control, the receiver’s buffer could overflow, leading to data loss.

#### Flow Control Methods

- **In-band flow control:** Uses special control characters embedded in the data stream, such as **X-on/X-off**, where the receiver signals the sender to pause or resume transmission.
- **Out-of-band flow control:** Uses separate control signals like **CTS (Clear to Send)** and **RTS (Request to Send)** to manage transmission permissions.
- Flow control often works hand-in-hand with error control, especially in sliding window protocols, by adjusting the window size based on the receiver’s capacity.


### 5. 📉 Data Compression and 🔐 Encryption

#### Data Compression

Data compression reduces the size of the data to be transmitted, improving efficiency. It relies on the fact that some symbols or patterns occur more frequently than others. By encoding frequent symbols with fewer bits and less frequent ones with more bits, overall data size is reduced. Compression algorithms often use probability theory and context (previous symbols) to predict and encode data efficiently.

#### Encryption

Encryption at the Data Link Layer ensures **privacy** (confidentiality) and **authenticity** of data. It scrambles the data using an algorithm and a key so that only authorized parties can read it.

- **Single-key (symmetric) encryption:** The same key is used for both encryption and decryption.
- **Public-key (asymmetric) encryption:** Uses a pair of keys (public and private) for encryption and decryption, enhancing security.


### 6. 📡 Medium Access Control (MAC): Sharing the Communication Channel

When multiple devices share the same physical medium (like a LAN), the Data Link Layer must control who can transmit and when to avoid collisions and ensure fair access.

#### Types of MAC Protocols

- **Primary/Secondary (Master/Slave):** One device (primary) controls the communication, polling secondary devices to see if they have data to send.
  - **Polling:** The primary asks each secondary device if it has data.
  - **Select:** The primary tells a secondary device it can send data.
  - Used in systems like RS-232 serial communication.

- **Non-Polling Systems:** Devices coordinate access without a central controller.
  - **RTS/CTS:** Devices request and clear permission to send.
  - **Time Division Multiple Access (TDMA):** The channel is divided into time slots assigned to different devices. Common in satellite networks.

- **Peer-to-Peer Systems:** All devices have equal status and coordinate access themselves.
  - **Time Division Multiplexing (TDM):** Each device transmits in a pre-assigned time slot.
  - **Aloha:** Devices transmit whenever they have data, risking collisions, and retransmit if collisions occur.
  - **Carrier Sense Multiple Access (CSMA):** Devices listen to the channel and transmit only if it is free.
    - **CSMA with Collision Detection (CSMA/CD):** Devices detect collisions during transmission and stop sending immediately, then retry after a random delay.
  - **Collision-Free Carrier Sense:** Uses timers or arbiters to schedule transmissions and avoid collisions.
  - **Token Ring:** Devices are arranged logically in a ring. A special token circulates; only the device holding the token can transmit.
  - **Token Bus:** Similar to Token Ring but uses a bus topology with a virtual ring for token passing.


### 7. 🔄 Summary and Key Takeaways

The Data Link Layer is essential for reliable, efficient communication over a physical medium. It packages data into frames, synchronizes transmission, detects and corrects errors, controls data flow, compresses and encrypts data, and manages access to shared media. Understanding these functions and protocols helps in designing and troubleshooting network communication systems.