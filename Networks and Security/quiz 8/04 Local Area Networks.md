## 4 Local Area Networks

## Questions

#### 1. Which of the following statements correctly describe the major attributes of a Local Area Network (LAN)?  
A) Error rates on LANs are generally better (lower) than on WANs.  
B) LAN transmission capacity typically ranges from 1 Mbps to 100 Mbps.  
C) LAN channels are usually publicly owned and managed by carriers.  
D) LAN connections typically span several kilometers between stations.  

#### 2. Regarding IEEE 802 standards and their relationship to the OSI model, which of the following are true?  
A) IEEE 802 standards define the Physical layer only, leaving Data Link layer undefined.  
B) LLC is a subset of HDLC and provides connection-oriented and connectionless services.  
C) MAC sublayer includes protocols such as IEEE 802.3 (CSMA/CD), 802.4 (Token Bus), and 802.5 (Token Ring).  
D) The Data Link layer in IEEE 802 is split into Logical Link Control (LLC) and Media Access Control (MAC) sublayers.  

#### 3. In the CSMA/CD protocol (IEEE 802.3), which of the following are correct functions or behaviors?  
A) The back-off algorithm uses a random delay based on the number of transmission attempts, with a maximum of 16 retries.  
B) The Inter Frame Gap (IFG) is a fixed 96-bit time interval that allows stations to recover before transmitting.  
C) Stations transmit immediately when the channel is busy to reduce delay.  
D) After detecting a collision, a station transmits a 32-bit jam signal to notify others.  

#### 4. Which of the following statements about Ethernet frame structure and operation are accurate?  
A) The Ethernet preamble consists of 56 bits of alternating 1s and 0s, followed by an 8-bit Start Frame Delimiter (SFD).  
B) The Type/Length field indicates either the length of the data field or the higher layer protocol number, depending on its value.  
C) The maximum Ethernet frame size including preamble is 1518 bytes.  
D) The Frame Check Sequence (FCS) is 16 bits and used for error detection.  

#### 5. Consider the slot time and collision detection in Ethernet networks. Which of the following are true?  
A) Slot time is related to the round-trip propagation delay and the time required to send a collision enforcement jam signal.  
B) In Fast Ethernet, the 512 bit slot time limits the maximum cable length to approximately 205 meters, which is why twisted pair cables are limited to 100 meters.  
C) The slot time in 10/100 Mbps Ethernet is 512 bit times, corresponding to a maximum cable length of about 2800 meters.  
D) Gigabit Ethernet extends the slot time to 4096 bits to accommodate longer propagation delays.  

#### 6. Which of the following correctly describe VLANs and the IEEE 802.1Q standard?  
A) VLANs allow grouping of switch ports to act as independent hubs, restricting broadcast domains.  
B) The VLAN tag adds 4 bytes to the Ethernet frame, increasing the maximum frame size to 1522 bytes.  
C) The Tag Protocol Identifier (TPID) field in the VLAN tag is set to 0x8100 to identify tagged frames.  
D) VLAN identifiers use 16 bits, allowing up to 65,536 VLANs per network.  

#### 7. Regarding Token Ring (IEEE 802.5) and Token Bus (IEEE 802.4) networks, which statements are correct?  
A) In Token Bus, the logical ring is established over a physical bus topology, with token passing based on numeric address order.  
B) Token Ring uses a token passed around a physical ring to control access, with the token indicating whether the ring is free or busy.  
C) Token Bus networks do not require acknowledgment of token receipt by the successor station.  
D) Token Ring frames include access control and frame status fields, which are absent in Token Bus frames.  

#### 8. Which of the following statements about full duplex Ethernet and Gigabit Ethernet are true?  
A) Gigabit Ethernet half duplex uses the same slot time as 10/100 Mbps Ethernet but with a reduced network diameter.  
B) Full duplex Ethernet allows simultaneous transmission and reception on the same media segment without collisions.  
C) Full duplex Ethernet requires a shared medium with collision detection enabled.  
D) Carrier extension and frame bursting are techniques used in Gigabit Ethernet to improve efficiency and handle minimum frame size requirements.  



<br>

## Answers

#### 1. Which of the following statements correctly describe the major attributes of a Local Area Network (LAN)?  
A) ✓ Error rates on LANs are much better (lower) than on WANs.  
B) ✓ LAN transmission capacity typically ranges from 1 Mbps to 100 Mbps, as stated in the content.  
C) ✗ LAN channels are privately owned; public carriers are usually not involved.  
D) ✗ LAN connections typically span a few meters to several hundred meters, not several kilometers.  

**Correct:** A, B


#### 2. Regarding IEEE 802 standards and their relationship to the OSI model, which of the following are true?  
A) ✗ IEEE 802 defines both Data Link (LLC and MAC) and Physical layers, not only Physical.  
B) ✓ LLC is a subset of HDLC and provides both connection-oriented and connectionless services.  
C) ✓ MAC sublayer includes 802.3 (CSMA/CD), 802.4 (Token Bus), and 802.5 (Token Ring).  
D) ✓ The Data Link layer is split into LLC and MAC sublayers in IEEE 802.  

**Correct:** B, C, D


#### 3. In the CSMA/CD protocol (IEEE 802.3), which of the following are correct functions or behaviors?  
A) ✓ Back-off uses a random delay based on transmission attempts, with a max of 16 retries.  
B) ✓ IFG is a fixed 96-bit time interval allowing recovery before transmission.  
C) ✗ Stations wait until the channel is idle before transmitting; they do not transmit immediately when busy.  
D) ✓ After collision detection, a 32-bit jam signal is sent to notify other stations.  

**Correct:** A, B, D


#### 4. Which of the following statements about Ethernet frame structure and operation are accurate?  
A) ✓ Preamble is 56 bits of alternating 1s and 0s, followed by an 8-bit SFD (10101011).  
B) ✓ Type/Length field indicates length if ≤1518, else it indicates protocol type.  
C) ✗ Maximum Ethernet frame size excluding preamble is 1518 bytes; preamble is separate.  
D) ✗ FCS is 32 bits (CRC), not 16 bits.  

**Correct:** A, B


#### 5. Consider the slot time and collision detection in Ethernet networks. Which of the following are true?  
A) ✓ Slot time depends on round-trip propagation delay plus collision enforcement time.  
B) ✓ In Fast Ethernet, 512 bit slot time limits cable length to ~205 m; twisted pair is limited to 100 m for other reasons.  
C) ✗ 512 bit slot time corresponds to about 2800 m in coaxial cable, but this is not the maximum cable length for all media.  
D) ✓ Gigabit Ethernet extends slot time to 4096 bits to handle longer propagation delays.  

**Correct:** A, B, D


#### 6. Which of the following correctly describe VLANs and the IEEE 802.1Q standard?  
A) ✓ VLANs group switch ports as independent hubs, restricting broadcast domains.  
B) ✓ VLAN tag adds 4 bytes, increasing max frame size to 1522 bytes.  
C) ✓ TPID is 0x8100 hex to identify tagged frames.  
D) ✗ VLAN ID uses 12 bits, allowing up to 4096 VLANs, not 16 bits.  

**Correct:** A, B, C


#### 7. Regarding Token Ring (IEEE 802.5) and Token Bus (IEEE 802.4) networks, which statements are correct?  
A) ✓ Token Bus uses a logical ring over a physical bus, with token passing based on numeric address order.  
B) ✓ Token Ring uses a token passed around a physical ring indicating free or busy status.  
C) ✗ Token Bus requires acknowledgment from the successor to confirm token receipt.  
D) ✓ Token Ring frames include access control and frame status fields; Token Bus frames lack these fields.  

**Correct:** A, B, D


#### 8. Which of the following statements about full duplex Ethernet and Gigabit Ethernet are true?  
A) ✓ Gigabit Ethernet half duplex uses similar slot time but with reduced network diameter (~20 m).  
B) ✓ Full duplex allows simultaneous transmit and receive on point-to-point links without collisions.  
C) ✗ Full duplex does not require a shared medium or collision detection; collisions are ignored or absent.  
D) ✓ Carrier extension and frame bursting improve efficiency and handle minimum frame size in Gigabit Ethernet.  

**Correct:** A, B, D