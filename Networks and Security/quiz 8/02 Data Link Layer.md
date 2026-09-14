## 2 Data Link Layer

## Questions

#### 1. Which of the following are primary functions of the Data Link Layer?  
A) Error control  
B) Synchronisation  
C) Media access control  
D) Routing  

#### 2. In bit-oriented framing, how are frames typically delimited?  
A) By special flag sequences  
B) By STX and ETX characters  
C) By checksum values  
D) By fixed-length byte counts  

#### 3. Which of the following statements about error control methods are true?  
A) Automatic Repeat Request (ARQ) relies on retransmission of erroneous frames  
B) Parity bits can correct all types of errors in a frame  
C) Residual errors after error detection are always zero  
D) Forward Error Correction adds redundancy to allow recovery without retransmission  

#### 4. In Continuous ARQ protocols, what is the role of the send state variable V(S) and the receive state variable V(R)?  
A) V(S) is used to detect collisions on the medium  
B) V(S) indicates the sequence number of the next frame to be sent  
C) V(R) indicates the sequence number of the expected frame  
D) V(R) indicates the sequence number of the last acknowledged frame  

#### 5. Which of the following are true about flow control mechanisms at the Data Link Layer?  
A) Sliding window protocols can be used to manipulate flow control  
B) In-band flow control uses signals like X-on/X-off embedded in the data stream  
C) Flow control is unrelated to error control and operates independently  
D) Out-of-band flow control uses separate control signals such as CTS/RTS  

#### 6. Regarding Medium Access Control (MAC) methods, which statements are correct?  
A) Time Division Multiple Access (TDMA) assigns fixed time slots to stations for transmission  
B) Polling systems involve a primary station querying secondary stations for data  
C) Pure Aloha avoids collisions by sensing the channel before transmission  
D) Token Ring networks use a token passed around a logical ring to control access  

#### 7. Which of the following correctly describe Carrier Sense Multiple Access with Collision Detection (CSMA/CD)?  
A) Stations transmit only when the channel is sensed free  
B) Stations wait a fixed, predetermined time before retransmitting after a collision  
C) Random backoff times are used to reduce the chance of repeated collisions  
D) Collisions are detected during transmission and cause immediate abort  

#### 8. What are the key differences between Token Ring and Token Bus networks?  
A) Token Ring requires a centralized controller to maintain the token  
B) Token Ring uses a physical ring topology, while Token Bus uses a bus topology with a virtual ring  
C) Token Bus combines ring and bus topologies to improve fault tolerance  
D) Token Bus circulates the token via the bus but follows a logical ring sequence  



<br>

## Answers

#### 1. Which of the following are primary functions of the Data Link Layer?  
A) ✓ Error control is essential to detect and correct errors in frames.  
B) ✓ Synchronisation is a core function to identify frame boundaries.  
C) ✓ Media access control manages access to shared physical media.  
D) ✗ Routing is a Network Layer function, not Data Link Layer.  

**Correct:** A, B, C


#### 2. In bit-oriented framing, how are frames typically delimited?  
A) ✓ Bit-oriented framing uses special flag sequences (e.g., 01111110) to delimit frames.  
B) ✗ STX and ETX characters are used in character-oriented framing, not bit-oriented.  
C) ✗ Checksum values detect errors but do not delimit frames.  
D) ✗ Fixed-length byte counts are used in fixed-length framing, not bit-oriented.  

**Correct:** A


#### 3. Which of the following statements about error control methods are true?  
A) ✓ ARQ relies on retransmission of frames detected as erroneous.  
B) ✗ Parity bits can detect some errors but cannot correct all types or multiple errors.  
C) ✗ Residual errors after detection are low but not always zero.  
D) ✓ Forward Error Correction adds redundancy to recover data without retransmission.  

**Correct:** A, D


#### 4. In Continuous ARQ protocols, what is the role of the send state variable V(S) and the receive state variable V(R)?  
A) ✗ V(S) is unrelated to collision detection; it tracks frame sequence numbers.  
B) ✓ V(S) is the sequence number of the next frame to be sent.  
C) ✓ V(R) indicates the sequence number of the expected frame at the receiver.  
D) ✗ V(R) does not indicate the last acknowledged frame but the expected frame number.  

**Correct:** B, C


#### 5. Which of the following are true about flow control mechanisms at the Data Link Layer?  
A) ✓ Sliding window protocols manipulate window size to control flow and error recovery.  
B) ✓ In-band flow control uses control characters like X-on/X-off within the data stream.  
C) ✗ Flow control is related to error control; sliding window protocols combine both.  
D) ✓ Out-of-band flow control uses separate signals such as CTS/RTS for controlling flow.  

**Correct:** A, B, D


#### 6. Regarding Medium Access Control (MAC) methods, which statements are correct?  
A) ✓ TDMA assigns fixed time slots to stations to avoid collisions.  
B) ✓ Polling systems have a primary station that queries secondary stations for data.  
C) ✗ Pure Aloha does not sense the channel before transmission, leading to collisions.  
D) ✓ Token Ring uses a token passed around a logical ring to control transmission rights.  

**Correct:** A, B, D


#### 7. Which of the following correctly describe Carrier Sense Multiple Access with Collision Detection (CSMA/CD)?  
A) ✓ Stations transmit only when the channel is sensed free.  
B) ✗ Stations wait a random, not fixed, time before retransmitting to avoid repeated collisions.  
C) ✓ Random backoff times reduce the chance of repeated collisions after a collision.  
D) ✓ Collisions are detected during transmission and cause immediate abort.  

**Correct:** A, C, D


#### 8. What are the key differences between Token Ring and Token Bus networks?  
A) ✗ Token Ring can use centralized or distributed token maintenance; centralized is not mandatory.  
B) ✓ Token Ring uses a physical or logical ring; Token Bus uses a bus topology with a virtual ring.  
C) ✗ Token Bus does not inherently improve fault tolerance by combining topologies; complexity increases.  
D) ✓ Token Bus circulates the token logically in ring order but physically via the bus.  

**Correct:** B, D