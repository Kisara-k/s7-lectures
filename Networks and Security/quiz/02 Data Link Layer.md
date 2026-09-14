## 2 Data Link Layer

## Questions

#### 1. Which of the following are primary functions of the Data Link Layer?  
A) Synchronisation  
B) Routing  
C) Error control  
D) Media access control  

#### 2. What is the main objective of synchronisation at the Data Link Layer?  
A) To encrypt data for privacy  
B) To identify the beginning and end of data units  
C) To compress data for efficient transmission  
D) To detect and correct errors  

#### 3. Which of the following are valid methods of frame delimitation?  
A) Character count  
B) Bit-oriented framing using flag sequences  
C) Packet switching  
D) Character-oriented framing using STX and ETX characters  

#### 4. What problems can arise from synchronisation methods in the Data Link Layer?  
A) Data loss due to missing flags or control characters  
B) Increased throughput due to compression  
C) Data errors caused by control characters appearing in data  
D) Guaranteed error-free transmission  

#### 5. Which error detection techniques are commonly used at the Data Link Layer?  
A) Parity bits  
B) Checksum  
C) Cyclic Redundancy Check (CRC)  
D) Forward Error Correction (FEC)  

#### 6. Forward Error Correction (FEC) is best suited for which of the following scenarios?  
A) Simplex transmission where retransmission is not possible  
B) High-latency links such as satellite communication  
C) Low-latency voice and video communication requiring minimal delay  
D) Networks where error correction is not needed  

#### 7. In Automatic Repeat Request (ARQ) protocols, what is the role of the sequence numbers V(S) and V(R)?  
A) V(S) is the sequence number of the next frame to be sent  
B) V(R) is the sequence number of the expected frame to be received  
C) V(S) and V(R) are used to encrypt data frames  
D) They maintain the sliding window for flow control  

#### 8. Which of the following statements about Continuous ARQ (sliding window) protocols are true?  
A) The sender can send multiple frames before needing an acknowledgment  
B) NAKs (Negative Acknowledgments) are used to request retransmission of erroneous frames  
C) The window size is unlimited and can be any number  
D) A 3-bit field is often used for sequence numbering, limiting the window size to 7  

#### 9. Which flow control methods are used at the Data Link Layer?  
A) In-band flow control such as X-on/X-off  
B) Out-of-band flow control such as CTS/RTS  
C) Token passing  
D) Packet switching  

#### 10. Which of the following statements about data compression at the Data Link Layer are correct?  
A) It is based on probability theory and symbol frequency  
B) It assumes all symbols have equal probability  
C) It can use the probability of previous symbols to predict the next symbol  
D) It is primarily used to detect errors in transmission  

#### 11. Which of the following are true about encryption at the Data Link Layer?  
A) It ensures privacy and authenticity of data  
B) It uses only single-key encryption algorithms  
C) It can use public-key (two-key) encryption algorithms  
D) It replaces error control mechanisms  

#### 12. In Medium Access Control (MAC), what distinguishes primary/secondary systems from peer-to-peer systems?  
A) Primary/secondary systems use polling or non-polling methods  
B) Peer-to-peer systems rely on a master station to control access  
C) Peer-to-peer systems include protocols like CSMA and Token Ring  
D) Primary/secondary systems always use token passing  

#### 13. Which of the following are characteristics of the Aloha protocol?  
A) Stations transmit whenever they have data, leading to possible collisions  
B) Collisions are detected and retransmissions are scheduled  
C) Performance improves as traffic increases  
D) It is a collision-free protocol  

#### 14. How does CSMA/CD improve channel utilization compared to pure CSMA?  
A) By monitoring the channel while transmitting and aborting on collision detection  
B) By waiting a random time before retransmission to avoid repeated collisions  
C) By guaranteeing collision-free transmission through token passing  
D) By using fixed time slots for each station  

#### 15. Which of the following statements about Token Ring and Token Bus networks are correct?  
A) Token Ring uses a logical ring structure and passes a token to control access  
B) Token Bus combines ring topology with bus physical topology  
C) Token Ring networks always have a centralized token management system  
D) Token Bus networks circulate a token via the bus in a predetermined sequence



<br>

## Answers

#### 1. Which of the following are primary functions of the Data Link Layer?  
A) ✓ Synchronisation is a core function to identify frame boundaries.  
B) ✗ Routing is a Network Layer function, not Data Link Layer.  
C) ✓ Error control is essential to detect and correct errors in frames.  
D) ✓ Media access control manages access to shared physical media.  

**Correct:** A, C, D


#### 2. What is the main objective of synchronisation at the Data Link Layer?  
A) ✗ Encryption is a separate function, not related to synchronisation.  
B) ✓ Synchronisation identifies the start and end of data units (frames).  
C) ✗ Compression is unrelated to synchronisation.  
D) ✗ Error detection/correction is separate from synchronisation.  

**Correct:** B


#### 3. Which of the following are valid methods of frame delimitation?  
A) ✓ Character count is a method where frame length is specified.  
B) ✓ Bit-oriented framing uses flag sequences to delimit frames.  
C) ✗ Packet switching is a network-layer concept, not frame delimitation.  
D) ✓ Character-oriented framing uses special characters (STX/ETX) to mark frames.  

**Correct:** A, B, D


#### 4. What problems can arise from synchronisation methods in the Data Link Layer?  
A) ✓ Data loss can occur if flags or control characters are lost.  
B) ✗ Compression improves throughput, not a synchronisation problem.  
C) ✓ Control characters appearing in data can cause framing errors.  
D) ✗ Synchronisation does not guarantee error-free transmission.  

**Correct:** A, C


#### 5. Which error detection techniques are commonly used at the Data Link Layer?  
A) ✓ Parity bits are a simple error detection method.  
B) ✓ Checksum is used to detect errors in data frames.  
C) ✓ CRC is a powerful error detection code widely used.  
D) ✗ Forward Error Correction is an error correction, not detection, technique.  

**Correct:** A, B, C


#### 6. Forward Error Correction (FEC) is best suited for which of the following scenarios?  
A) ✓ Simplex transmission where retransmission is impossible benefits from FEC.  
B) ✓ High-latency links like satellite use FEC to avoid retransmission delays.  
C) ✗ Low-latency voice/video usually prefer ARQ or no correction due to delay.  
D) ✗ Networks not needing error correction do not use FEC.  

**Correct:** A, B


#### 7. In Automatic Repeat Request (ARQ) protocols, what is the role of the sequence numbers V(S) and V(R)?  
A) ✓ V(S) is the sequence number of the next frame to send.  
B) ✓ V(R) is the sequence number of the next expected frame to receive.  
C) ✗ They are not used for encryption.  
D) ✓ They maintain the sliding window for flow and error control.  

**Correct:** A, B, D


#### 8. Which of the following statements about Continuous ARQ (sliding window) protocols are true?  
A) ✓ Sender can send multiple frames before waiting for ACKs.  
B) ✓ NAKs request retransmission of erroneous frames.  
C) ✗ Window size is limited by sequence number bits (e.g., 7 for 3-bit).  
D) ✓ 3-bit sequence numbers limit window size to 7 frames.  

**Correct:** A, B, D


#### 9. Which flow control methods are used at the Data Link Layer?  
A) ✓ In-band flow control like X-on/X-off is used.  
B) ✓ Out-of-band flow control like CTS/RTS is also used.  
C) ✗ Token passing is a MAC protocol, not a flow control method.  
D) ✗ Packet switching is unrelated to flow control at this layer.  

**Correct:** A, B


#### 10. Which of the following statements about data compression at the Data Link Layer are correct?  
A) ✓ Compression relies on unequal symbol probabilities.  
B) ✗ It assumes symbols have equal probability, which is false.  
C) ✓ Probability of next symbol can depend on previous symbols.  
D) ✗ Compression is not used for error detection.  

**Correct:** A, C


#### 11. Which of the following are true about encryption at the Data Link Layer?  
A) ✓ Encryption ensures privacy and authenticity.  
B) ✗ Only single-key encryption is not true; public-key is also used.  
C) ✓ Public-key (two-key) encryption can be used.  
D) ✗ Encryption does not replace error control mechanisms.  

**Correct:** A, C


#### 12. In Medium Access Control (MAC), what distinguishes primary/secondary systems from peer-to-peer systems?  
A) ✓ Primary/secondary use polling or non-polling methods.  
B) ✗ Peer-to-peer systems do not rely on a master station.  
C) ✓ Peer-to-peer systems include CSMA, Token Ring, etc.  
D) ✗ Primary/secondary do not always use token passing.  

**Correct:** A, C


#### 13. Which of the following are characteristics of the Aloha protocol?  
A) ✓ Stations transmit whenever they have data, causing collisions.  
B) ✓ Collisions are detected and retransmissions occur.  
C) ✗ Performance degrades as traffic increases, not improves.  
D) ✗ Aloha is not collision-free.  

**Correct:** A, B


#### 14. How does CSMA/CD improve channel utilization compared to pure CSMA?  
A) ✓ Stations monitor channel during transmission and abort on collision.  
B) ✓ Random wait times reduce repeated collisions.  
C) ✗ Token passing guarantees collision-free but is not part of CSMA/CD.  
D) ✗ Fixed time slots are used in TDMA, not CSMA/CD.  

**Correct:** A, B


#### 15. Which of the following statements about Token Ring and Token Bus networks are correct?  
A) ✓ Token Ring uses a logical ring and token passing for access control.  
B) ✓ Token Bus combines ring logic with bus physical topology.  
C) ✗ Token Ring can be centralized or distributed; not always centralized.  
D) ✓ Token Bus circulates token via bus in a predetermined sequence.  

**Correct:** A, B, D