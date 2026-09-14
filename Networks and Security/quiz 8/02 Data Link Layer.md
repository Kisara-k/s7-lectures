## 2 Data Link Layer

## Questions

#### 1. Which of the following are primary functions of the Data Link Layer?  
A) Synchronisation  
B) Routing  
C) Error control  
D) Media access control  

#### 2. In bit-oriented framing, how are frames typically delimited?  
A) By fixed-length byte counts  
B) By special flag sequences  
C) By STX and ETX characters  
D) By checksum values  

#### 3. Which of the following statements about error control methods are true?  
A) Forward Error Correction adds redundancy to allow recovery without retransmission  
B) Automatic Repeat Request (ARQ) relies on retransmission of erroneous frames  
C) Parity bits can correct all types of errors in a frame  
D) Residual errors after error detection are always zero  

#### 4. In Continuous ARQ protocols, what is the role of the send state variable V(S) and the receive state variable V(R)?  
A) V(S) indicates the sequence number of the next frame to be sent  
B) V(R) indicates the sequence number of the last acknowledged frame  
C) V(R) indicates the sequence number of the expected frame  
D) V(S) is used to detect collisions on the medium  

#### 5. Which of the following are true about flow control mechanisms at the Data Link Layer?  
A) In-band flow control uses signals like X-on/X-off embedded in the data stream  
B) Out-of-band flow control uses separate control signals such as CTS/RTS  
C) Flow control is unrelated to error control and operates independently  
D) Sliding window protocols can be used to manipulate flow control  

#### 6. Regarding Medium Access Control (MAC) methods, which statements are correct?  
A) Polling systems involve a primary station querying secondary stations for data  
B) Time Division Multiple Access (TDMA) assigns fixed time slots to stations for transmission  
C) Token Ring networks use a token passed around a logical ring to control access  
D) Pure Aloha avoids collisions by sensing the channel before transmission  

#### 7. Which of the following correctly describe Carrier Sense Multiple Access with Collision Detection (CSMA/CD)?  
A) Stations transmit only when the channel is sensed free  
B) Collisions are detected during transmission and cause immediate abort  
C) Stations wait a fixed, predetermined time before retransmitting after a collision  
D) Random backoff times are used to reduce the chance of repeated collisions  

#### 8. What are the key differences between Token Ring and Token Bus networks?  
A) Token Ring uses a physical ring topology, while Token Bus uses a bus topology with a virtual ring  
B) Token Bus circulates the token via the bus but follows a logical ring sequence  
C) Token Ring requires a centralized controller to maintain the token  
D) Token Bus combines ring and bus topologies to improve fault tolerance



<br>

## Answers

#### 1. Which of the following are primary functions of the Data Link Layer?  
A) ✓ Synchronisation is a core function to identify frame boundaries.  
B) ✗ Routing is a Network Layer function, not Data Link Layer.  
C) ✓ Error control is essential to detect and correct errors in frames.  
D) ✓ Media access control manages access to shared physical media.  

**Correct:** A, C, D


#### 2. In bit-oriented framing, how are frames typically delimited?  
A) ✗ Fixed-length byte counts are used in fixed-length framing, not bit-oriented.  
B) ✓ Bit-oriented framing uses special flag sequences (e.g., 01111110) to delimit frames.  
C) ✗ STX and ETX characters are used in character-oriented framing, not bit-oriented.  
D) ✗ Checksum values detect errors but do not delimit frames.  

**Correct:** B


#### 3. Which of the following statements about error control methods are true?  
A) ✓ Forward Error Correction adds redundancy to recover data without retransmission.  
B) ✓ ARQ relies on retransmission of frames detected as erroneous.  
C) ✗ Parity bits can detect some errors but cannot correct all types or multiple errors.  
D) ✗ Residual errors after detection are low but not always zero.  

**Correct:** A, B


#### 4. In Continuous ARQ protocols, what is the role of the send state variable V(S) and the receive state variable V(R)?  
A) ✓ V(S) is the sequence number of the next frame to be sent.  
B) ✗ V(R) does not indicate the last acknowledged frame but the expected frame number.  
C) ✓ V(R) indicates the sequence number of the expected frame at the receiver.  
D) ✗ V(S) is unrelated to collision detection; it tracks frame sequence numbers.  

**Correct:** A, C


#### 5. Which of the following are true about flow control mechanisms at the Data Link Layer?  
A) ✓ In-band flow control uses control characters like X-on/X-off within the data stream.  
B) ✓ Out-of-band flow control uses separate signals such as CTS/RTS for controlling flow.  
C) ✗ Flow control is related to error control; sliding window protocols combine both.  
D) ✓ Sliding window protocols manipulate window size to control flow and error recovery.  

**Correct:** A, B, D


#### 6. Regarding Medium Access Control (MAC) methods, which statements are correct?  
A) ✓ Polling systems have a primary station that queries secondary stations for data.  
B) ✓ TDMA assigns fixed time slots to stations to avoid collisions.  
C) ✓ Token Ring uses a token passed around a logical ring to control transmission rights.  
D) ✗ Pure Aloha does not sense the channel before transmission, leading to collisions.  

**Correct:** A, B, C


#### 7. Which of the following correctly describe Carrier Sense Multiple Access with Collision Detection (CSMA/CD)?  
A) ✓ Stations transmit only when the channel is sensed free.  
B) ✓ Collisions are detected during transmission and cause immediate abort.  
C) ✗ Stations wait a random, not fixed, time before retransmitting to avoid repeated collisions.  
D) ✓ Random backoff times reduce the chance of repeated collisions after a collision.  

**Correct:** A, B, D


#### 8. What are the key differences between Token Ring and Token Bus networks?  
A) ✓ Token Ring uses a physical or logical ring; Token Bus uses a bus topology with a virtual ring.  
B) ✓ Token Bus circulates the token logically in ring order but physically via the bus.  
C) ✗ Token Ring can use centralized or distributed token maintenance; centralized is not mandatory.  
D) ✗ Token Bus does not inherently improve fault tolerance by combining topologies; complexity increases.  

**Correct:** A, B