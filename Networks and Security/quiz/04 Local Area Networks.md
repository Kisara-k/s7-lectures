## 4 Local Area Networks

## Questions

#### 1. Which of the following are typical attributes of a Local Area Network (LAN)?  
A) LAN transmission capacity is usually higher than WAN  
B) LAN channels are usually publicly owned  
C) LAN error rates are generally better than WAN error rates  
D) LAN connections typically span several kilometers  

#### 2. What distinguishes broadband LANs from baseband LANs?  
A) Broadband uses digital technology with voltage levels  
B) Broadband uses analogue technology and modems  
C) Baseband uses Frequency Division Multiplexing (FDM)  
D) Baseband uses Time Division Multiplexing (TDM) or protocols for multiple access  

#### 3. In the IEEE 802 standards, how is the Data Link layer structured?  
A) It is split into Logical Link Control (LLC) and Media Access Control (MAC) sublayers  
B) LLC is a subset of HDLC  
C) MAC includes protocols such as 802.3, 802.4, and 802.5  
D) LLC handles physical layer signaling  

#### 4. Which of the following statements about IEEE 802.3 (CSMA/CD) are true?  
A) It is the most widely used LAN access method on a bus topology  
B) It uses token passing to avoid collisions  
C) It defines both MAC and Physical layers  
D) The frame format includes frame control and ending delimiter fields  

#### 5. Regarding the CSMA/CD back-off algorithm, which statements are correct?  
A) After detecting a collision, a station transmits a 32-bit jam signal  
B) The back-off delay is a random multiple of the slot time  
C) The maximum number of retransmission attempts is 10  
D) The slot time for 10/100 Mbps Ethernet is 512 bit times  

#### 6. What are the key functions of the Physical layer in IEEE 802.3 Ethernet?  
A) Data encoding and decoding using Manchester code  
B) Media access management and collision handling  
C) Carrier sensing and collision detection on the channel  
D) Frame encapsulation and error detection  

#### 7. Which of the following correctly describe Token Ring (IEEE 802.5) operation?  
A) A token circulates around the ring granting transmission rights  
B) Stations transmit only when they possess the token  
C) The token contains an indicator showing if the ring is free or busy  
D) Collisions are detected and resolved using CSMA/CD  

#### 8. How does Token Bus (IEEE 802.4) differ from Token Ring (IEEE 802.5)?  
A) Token Bus uses a logical ring over a physical bus topology  
B) Token Bus frames include access control and frame status fields  
C) Token Bus determines the logical ring by numeric address values  
D) Token Bus waits for acknowledgment from the successor before passing the token  

#### 9. Which of the following are true about Ethernet frame structure?  
A) The preamble consists of 56 bits of alternating 1s and 0s  
B) The Start Frame Delimiter (SFD) is 8 bits long with a pattern 10101011  
C) The maximum frame size including preamble is 1518 bytes  
D) The Type/Length field indicates either the length or the higher layer protocol number  

#### 10. What are the main rules for media access control in Ethernet?  
A) A station transmits immediately when it detects no carrier for the Inter Frame Gap (IFG) period  
B) Stations wait for the channel to be idle before transmitting  
C) Collisions are ignored in half duplex mode  
D) The IFG duration is 96 bit times to allow recovery between frames  

#### 11. Which statements about slot time and its considerations in Ethernet are correct?  
A) Slot time is the time needed for a signal to propagate to the farthest station and back  
B) The original 10 Mbps Ethernet slot time supports cable lengths up to 2800 meters  
C) Gigabit Ethernet uses a slot time of 512 bit times like 10/100 Mbps Ethernet  
D) Gigabit Ethernet extends slot time to 4096 bits using carrier extension  

#### 12. Regarding Gigabit Ethernet operation, which are true?  
A) Full duplex Gigabit Ethernet allows simultaneous transmission and reception  
B) Half duplex Gigabit Ethernet uses the same slot time as 10/100 Mbps Ethernet  
C) Carrier extension is used to increase minimum frame size for collision detection  
D) Frame bursting reduces efficiency for small frames  

#### 13. What are the characteristics of full duplex Ethernet?  
A) It requires a point-to-point link such as twisted pair or fiber optic  
B) Collision detection is mandatory and always performed  
C) The full bandwidth is available for simultaneous transmit and receive  
D) It is specified by IEEE 802.3x standard  

#### 14. Which of the following statements about VLANs and IEEE 802.1Q are correct?  
A) VLANs allow grouping of switch ports as independent hubs  
B) VLAN tagging adds 4 bytes to the Ethernet frame, increasing max frame size to 1522 bytes  
C) The Tag Protocol Identifier (TPID) field identifies a tagged frame with value 0x8100  
D) VLAN identifiers use 16 bits to uniquely identify VLANs  

#### 15. Which of the following are true about the back-off operation in CSMA/CD?  
A) The random back-off integer “r” is chosen from 0 to 2^k - 1, where k = min(n,10) and n is the number of attempts  
B) After 16 unsuccessful retransmissions, the interface reports transmission failure  
C) The back-off delay is always a fixed multiple of the slot time regardless of collision count  
D) After a successful transmission, the back-off counter is reset to zero



<br>

## Answers

#### 1. Which of the following are typical attributes of a Local Area Network (LAN)?  
A) ✓ LAN transmission capacity is usually higher than WAN — LANs typically have higher bit rates (1 Mbps to 100 Mbps) than WANs.  
B) ✗ LAN channels are usually publicly owned — LAN channels are privately owned, not public.  
C) ✓ LAN error rates are generally better than WAN error rates — LANs have much lower error rates (e.g., 1:10^8) compared to WANs.  
D) ✗ LAN connections typically span several kilometers — LANs usually cover a few meters to several hundred meters, not kilometers.  

**Correct:** A, C


#### 2. What distinguishes broadband LANs from baseband LANs?  
A) ✗ Broadband uses digital technology with voltage levels — This describes baseband, not broadband.  
B) ✓ Broadband uses analogue technology and modems — Broadband uses analogue signals and modems with FDM.  
C) ✗ Baseband uses Frequency Division Multiplexing (FDM) — Baseband uses digital signaling, not FDM.  
D) ✓ Baseband uses Time Division Multiplexing (TDM) or protocols for multiple access — Baseband can use TDM or protocols to handle multiple access.  

**Correct:** B, D


#### 3. In the IEEE 802 standards, how is the Data Link layer structured?  
A) ✓ It is split into Logical Link Control (LLC) and Media Access Control (MAC) sublayers — IEEE 802 splits Data Link into LLC and MAC.  
B) ✓ LLC is a subset of HDLC — LLC is based on HDLC protocol subset.  
C) ✓ MAC includes protocols such as 802.3, 802.4, and 802.5 — MAC covers these standards.  
D) ✗ LLC handles physical layer signaling — LLC operates at Data Link layer, not Physical layer.  

**Correct:** A, B, C


#### 4. Which of the following statements about IEEE 802.3 (CSMA/CD) are true?  
A) ✓ It is the most widely used LAN access method on a bus topology — Ethernet (802.3) is the most common CSMA/CD implementation on bus.  
B) ✗ It uses token passing to avoid collisions — Token passing is used in Token Ring/Bus, not CSMA/CD.  
C) ✓ It defines both MAC and Physical layers — 802.3 defines MAC and Physical layers.  
D) ✗ The frame format includes frame control and ending delimiter fields — 802.3 frame format excludes frame control and ending delimiter.  

**Correct:** A, C


#### 5. Regarding the CSMA/CD back-off algorithm, which statements are correct?  
A) ✓ After detecting a collision, a station transmits a 32-bit jam signal — Jam signal enforces collision detection.  
B) ✓ The back-off delay is a random multiple of the slot time — Delay is random integral multiples of slot time.  
C) ✗ The maximum number of retransmission attempts is 10 — Maximum retries are 16, not 10.  
D) ✓ The slot time for 10/100 Mbps Ethernet is 512 bit times — Slot time is defined as 512 bit times for 10/100 Mbps.  

**Correct:** A, B, D


#### 6. What are the key functions of the Physical layer in IEEE 802.3 Ethernet?  
A) ✓ Data encoding and decoding using Manchester code — Physical layer encodes/decodes signals with Manchester code.  
B) ✗ Media access management and collision handling — These are Data Link layer (MAC) functions.  
C) ✓ Carrier sensing and collision detection on the channel — Physical layer senses carrier and detects collisions.  
D) ✗ Frame encapsulation and error detection — These are Data Link layer functions.  

**Correct:** A, C


#### 7. Which of the following correctly describe Token Ring (IEEE 802.5) operation?  
A) ✓ A token circulates around the ring granting transmission rights — Token passing controls access.  
B) ✓ Stations transmit only when they possess the token — Token possession is required to transmit.  
C) ✓ The token contains an indicator showing if the ring is free or busy — Token indicates ring status.  
D) ✗ Collisions are detected and resolved using CSMA/CD — Token Ring does not use CSMA/CD; collisions are avoided by token.  

**Correct:** A, B, C


#### 8. How does Token Bus (IEEE 802.4) differ from Token Ring (IEEE 802.5)?  
A) ✓ Token Bus uses a logical ring over a physical bus topology — Logical ring is formed over bus.  
B) ✗ Token Bus frames include access control and frame status fields — 802.4 frames lack these fields, unlike 802.5.  
C) ✓ Token Bus determines the logical ring by numeric address values — Successor determined by address order.  
D) ✓ Token Bus waits for acknowledgment from the successor before passing the token — Sender waits for evidence of transmission.  

**Correct:** A, C, D


#### 9. Which of the following are true about Ethernet frame structure?  
A) ✓ The preamble consists of 56 bits of alternating 1s and 0s — Preamble is 56 bits alternating pattern.  
B) ✓ The Start Frame Delimiter (SFD) is 8 bits long with a pattern 10101011 — SFD is 8 bits with that pattern.  
C) ✗ The maximum frame size including preamble is 1518 bytes — 1518 bytes excludes preamble and SFD.  
D) ✓ The Type/Length field indicates either the length or the higher layer protocol number — Field serves dual purpose depending on value.  

**Correct:** A, B, D


#### 10. What are the main rules for media access control in Ethernet?  
A) ✓ A station transmits immediately when it detects no carrier for the Inter Frame Gap (IFG) period — Transmit after IFG if no carrier.  
B) ✓ Stations wait for the channel to be idle before transmitting — Must wait for absence of carrier.  
C) ✗ Collisions are ignored in half duplex mode — Collisions are detected and handled in half duplex.  
D) ✓ The IFG duration is 96 bit times to allow recovery between frames — IFG is 96 bit times for recovery.  

**Correct:** A, B, D


#### 11. Which statements about slot time and its considerations in Ethernet are correct?  
A) ✓ Slot time is the time needed for a signal to propagate to the farthest station and back — Slot time covers round-trip propagation.  
B) ✓ The original 10 Mbps Ethernet slot time supports cable lengths up to 2800 meters — 512 bit time corresponds to 2800m coax cable.  
C) ✗ Gigabit Ethernet uses a slot time of 512 bit times like 10/100 Mbps Ethernet — Gigabit Ethernet extends slot time to 4096 bits.  
D) ✓ Gigabit Ethernet extends slot time to 4096 bits using carrier extension — Carrier extension increases slot time.  

**Correct:** A, B, D


#### 12. Regarding Gigabit Ethernet operation, which are true?  
A) ✓ Full duplex Gigabit Ethernet allows simultaneous transmission and reception — Full duplex supports simultaneous TX/RX.  
B) ✓ Half duplex Gigabit Ethernet uses the same slot time as 10/100 Mbps Ethernet — Half duplex uses 512 bit slot time.  
C) ✓ Carrier extension is used to increase minimum frame size for collision detection — Carrier extension pads short frames.  
D) ✗ Frame bursting reduces efficiency for small frames — Frame bursting improves efficiency for small frames.  

**Correct:** A, B, C


#### 13. What are the characteristics of full duplex Ethernet?  
A) ✓ It requires a point-to-point link such as twisted pair or fiber optic — Full duplex needs dedicated link.  
B) ✗ Collision detection is mandatory and always performed — Collisions are ignored or not applicable in full duplex.  
C) ✓ The full bandwidth is available for simultaneous transmit and receive — Full bandwidth used in both directions.  
D) ✓ It is specified by IEEE 802.3x standard — 802.3x defines full duplex operation.  

**Correct:** A, C, D


#### 14. Which of the following statements about VLANs and IEEE 802.1Q are correct?  
A) ✓ VLANs allow grouping of switch ports as independent hubs — VLANs logically separate ports into groups.  
B) ✓ VLAN tagging adds 4 bytes to the Ethernet frame, increasing max frame size to 1522 bytes — Tag adds 4 bytes, increasing max frame size.  
C) ✓ The Tag Protocol Identifier (TPID) field identifies a tagged frame with value 0x8100 — TPID is 0x8100 for VLAN tags.  
D) ✗ VLAN identifiers use 16 bits to uniquely identify VLANs — VLAN ID uses 12 bits, not 16.  

**Correct:** A, B, C


#### 15. Which of the following are true about the back-off operation in CSMA/CD?  
A) ✓ The random back-off integer “r” is chosen from 0 to 2^k - 1, where k = min(n,10) and n is the number of attempts — Back-off uses this formula.  
B) ✓ After 16 unsuccessful retransmissions, the interface reports transmission failure — Max retries is 16 before failure.  
C) ✗ The back-off delay is always a fixed multiple of the slot time regardless of collision count — Delay range increases with collision count.  
D) ✓ After a successful transmission, the back-off counter is reset to zero — Counter resets after success.  

**Correct:** A, B, D