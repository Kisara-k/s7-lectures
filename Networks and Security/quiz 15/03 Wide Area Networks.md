## 3 Wide Area Networks

## Questions

#### 1. What distinguishes a Wide Area Network (WAN) from a Local Area Network (LAN)?  
A) WANs are usually operated by telecom service providers, LANs by individual organizations  
B) WANs use only wireless technologies, LANs use only wired technologies  
C) WANs typically span over 30 km in diameter, while LANs are generally less than 1 km  
D) LANs always have higher bandwidth than WANs  

#### 2. Which of the following statements about Metropolitan Area Networks (MANs) are true?  
A) MANs are usually run by telecom providers  
B) MANs typically cover areas up to about 50 km in diameter  
C) MANs are a subset of LANs  
D) MANs use completely different technologies than WANs and LANs  

#### 3. Which of the following are characteristics of leased lines?  
A) They have a fixed monthly cost regardless of usage  
B) They provide a full-time dedicated link between two points  
C) Most leased lines today are digital with speeds commonly between 64 kb/s and 2 Mb/s  
D) They are typically packet-switched connections  

#### 4. Packet switching differs from leased lines in that:  
A) It is more efficient for bursty traffic  
B) It always uses virtual circuits with connection identifiers  
C) It breaks data into packets sent independently through the network  
D) It guarantees a dedicated circuit for the entire connection duration  

#### 5. Which of the following are true about X.25 packet switching?  
A) It is very fast compared to modern networks  
B) It was introduced in the 1960s and became a standard for data communication  
C) It is expensive relative to today’s networks  
D) It is connectionless and does not maintain state for connections  

#### 6. Frame Relay technology:  
A) Guarantees bandwidth by negotiating a Committed Information Rate (CIR) at setup  
B) Is a replacement for X.25 and is virtual-circuit oriented  
C) Provides error control at the network layer  
D) Uses permanent virtual circuits to carry aggregate traffic between routers  

#### 7. Why are ATM cells fixed at 53 bytes in size?  
A) To simplify and speed up switching for voice, video, and data integration  
B) To allow error correction within each cell  
C) Because variable-sized packets cause unacceptable switching delays for voice/video  
D) To maximize payload size for data transmission efficiency  

#### 8. Which of the following statements about ATM are correct?  
A) ATM cells have a 5-byte header and 48-byte payload  
B) ATM is designed to integrate voice, video, and data on the same network  
C) ATM networks do not maintain any state information for virtual circuits  
D) ATM is only used as a link layer technology connecting IP routers in practice  

#### 9. In ATM addressing, what is the purpose of the two-part identifier consisting of VPI and VCI?  
A) To provide error detection and correction  
B) To identify the physical location of the switch  
C) To make network routing easier and faster by hierarchical addressing  
D) To separate virtual paths and virtual circuits within the network  

#### 10. Which of the following are key capabilities or applications of MPLS?  
A) Providing connection-oriented switching based on labels  
B) Operating only on private enterprise networks  
C) Supporting VPNs and IP multicast  
D) Network scalability and traffic engineering  

#### 11. MPLS is described as “multi-protocol” because:  
A) It supports multiple IP versions simultaneously  
B) It can only be used with Ethernet networks  
C) It uses multiple routing protocols like BGP-4, OSPF, and IS-IS internally  
D) It can be applied over any Layer 2 network protocol such as PPP, ATM, or Frame Relay  

#### 12. Which of the following statements about Ethernet First Mile (EFM) are true?  
A) EFM over copper uses DSL modulation schemes with Ethernet frames  
B) EFM aims to provide 10 Mbps at 750 meters and 2 Mbps at 2,700 meters over copper  
C) EFM only supports fiber optic media, not copper  
D) EFM connects homes and offices using Ethernet technology  

#### 13. Regarding Frame Relay and ATM, which of the following are accurate comparisons?  
A) Frame Relay includes error control, ATM does not  
B) Frame Relay is generally slower and less flexible than ATM  
C) ATM uses fixed-size cells, Frame Relay uses variable-length frames  
D) Both are connection-oriented and use virtual circuits  

#### 14. Which of the following best describe the evolution and convergence of WAN, MAN, and LAN technologies?  
A) MPLS and Ethernet are becoming the most prevalent technologies in WANs and MANs  
B) WANs still exclusively use legacy technologies like X.25 and Frame Relay  
C) LANs and WANs remain completely separate in technology and operation  
D) Ethernet is now commonly used across LANs, MANs, and WANs  

#### 15. Which of the following statements about packet switching types are correct?  
A) Virtual circuits require a dedicated physical circuit for the duration of the connection  
B) Virtual circuit packet switching establishes a route once per connection and uses connection identifiers  
C) Packet switching is generally less efficient than leased lines for bursty traffic patterns  
D) Datagram packet switching routes each packet independently without a fixed path  



<br>

## Answers

#### 1. What distinguishes a Wide Area Network (WAN) from a Local Area Network (LAN)?  
A) ✓ WANs are usually operated by telecom service providers, LANs by individual organizations — Correct distinction of management.  
B) ✗ WANs use only wireless technologies, LANs use only wired technologies — Incorrect; both can use wired or wireless.  
C) ✓ WANs typically span over 30 km in diameter, while LANs are generally less than 1 km — This is a key defining difference.  
D) ✗ LANs always have higher bandwidth than WANs — Not necessarily true; bandwidth depends on technology, not just network type.  

**Correct:** A, C


#### 2. Which of the following statements about Metropolitan Area Networks (MANs) are true?  
A) ✓ MANs are usually run by telecom providers — True, similar to WANs.  
B) ✓ MANs typically cover areas up to about 50 km in diameter — Correct size range for MANs.  
C) ✗ MANs are a subset of LANs — Incorrect; MANs are larger than LANs.  
D) ✗ MANs use completely different technologies than WANs and LANs — Incorrect; technologies are converging.  

**Correct:** A, B


#### 3. Which of the following are characteristics of leased lines?  
A) ✓ They have a fixed monthly cost regardless of usage — True, cost is fixed.  
B) ✓ They provide a full-time dedicated link between two points — Core feature of leased lines.  
C) ✓ Most leased lines today are digital with speeds commonly between 64 kb/s and 2 Mb/s — Correct typical speeds and digital nature.  
D) ✗ They are typically packet-switched connections — Leased lines are circuit-switched, dedicated links.  

**Correct:** A, B, C


#### 4. Packet switching differs from leased lines in that:  
A) ✓ It is more efficient for bursty traffic — Packet switching handles bursty traffic better than leased lines.  
B) ✗ It always uses virtual circuits with connection identifiers — Packet switching can be datagram or virtual circuit; not always virtual circuit.  
C) ✓ It breaks data into packets sent independently through the network — Fundamental packet switching concept.  
D) ✗ It guarantees a dedicated circuit for the entire connection duration — Packet switching does not guarantee dedicated circuits.  

**Correct:** A, C


#### 5. Which of the following are true about X.25 packet switching?  
A) ✗ It is very fast compared to modern networks — X.25 is slow (~64 kb/s).  
B) ✓ It was introduced in the 1960s and became a standard for data communication — Historical fact.  
C) ✓ It is expensive relative to today’s networks — True, costs were high historically.  
D) ✗ It is connectionless and does not maintain state for connections — X.25 is connection-oriented and maintains state.  

**Correct:** B, C


#### 6. Frame Relay technology:  
A) ✓ Guarantees bandwidth by negotiating a Committed Information Rate (CIR) at setup — CIR defines guaranteed bandwidth.  
B) ✓ Is a replacement for X.25 and is virtual-circuit oriented — Correct description.  
C) ✗ Provides error control at the network layer — Frame Relay assumes reliable network, no error control.  
D) ✓ Uses permanent virtual circuits to carry aggregate traffic between routers — True, PVCs are typical.  

**Correct:** A, B, D


#### 7. Why are ATM cells fixed at 53 bytes in size?  
A) ✓ To simplify and speed up switching for voice, video, and data integration — Fixed size enables fast processing.  
B) ✗ To allow error correction within each cell — ATM does not provide error correction in cells.  
C) ✓ Because variable-sized packets cause unacceptable switching delays for voice/video — Fixed size reduces delay variability.  
D) ✗ To maximize payload size for data transmission efficiency — Payload is small (48 bytes), not maximized.  

**Correct:** A, C


#### 8. Which of the following statements about ATM are correct?  
A) ✓ ATM cells have a 5-byte header and 48-byte payload — Correct cell structure.  
B) ✓ ATM is designed to integrate voice, video, and data on the same network — Core ATM design goal.  
C) ✗ ATM networks do not maintain any state information for virtual circuits — ATM switches maintain state per VC.  
D) ✓ ATM is only used as a link layer technology connecting IP routers in practice — Reality differs from vision; mostly link layer use.  

**Correct:** A, B, D


#### 9. In ATM addressing, what is the purpose of the two-part identifier consisting of VPI and VCI?  
A) ✗ To provide error detection and correction — Addressing does not provide error control.  
B) ✗ To identify the physical location of the switch — Not the purpose of VPI/VCI.  
C) ✓ To make network routing easier and faster by hierarchical addressing — VPI/VCI split simplifies routing.  
D) ✓ To separate virtual paths and virtual circuits within the network — VPI identifies path, VCI identifies circuit.  

**Correct:** C, D


#### 10. Which of the following are key capabilities or applications of MPLS?  
A) ✓ Providing connection-oriented switching based on labels — Core MPLS function.  
B) ✗ Operating only on private enterprise networks — MPLS is mostly used by service providers, not private networks.  
C) ✓ Supporting VPNs and IP multicast — MPLS supports VPNs and multicast.  
D) ✓ Network scalability and traffic engineering — MPLS supports both.  

**Correct:** A, C, D


#### 11. MPLS is described as “multi-protocol” because:  
A) ✗ It supports multiple IP versions simultaneously — Not the reason for “multi-protocol.”  
B) ✗ It can only be used with Ethernet networks — Incorrect; MPLS works over various Layer 2 protocols.  
C) ✗ It uses multiple routing protocols like BGP-4, OSPF, and IS-IS internally — MPLS uses these protocols but that’s not why it’s “multi-protocol.”  
D) ✓ It can be applied over any Layer 2 network protocol such as PPP, ATM, or Frame Relay — True, supports multiple Layer 2 types.  

**Correct:** D


#### 12. Which of the following statements about Ethernet First Mile (EFM) are true?  
A) ✓ EFM over copper uses DSL modulation schemes with Ethernet frames — Correct for EFMC.  
B) ✓ EFM aims to provide 10 Mbps at 750 meters and 2 Mbps at 2,700 meters over copper — Correct performance targets.  
C) ✗ EFM only supports fiber optic media, not copper — EFM supports both copper and fiber.  
D) ✓ EFM connects homes and offices using Ethernet technology — Core purpose of EFM.  

**Correct:** A, B, D


#### 13. Regarding Frame Relay and ATM, which of the following are accurate comparisons?  
A) ✗ Frame Relay includes error control, ATM does not — Frame Relay assumes reliable network, no error control; ATM also does not do error control.  
B) ✓ Frame Relay is generally slower and less flexible than ATM — ATM is more scalable and flexible.  
C) ✓ ATM uses fixed-size cells, Frame Relay uses variable-length frames — Correct difference in data unit size.  
D) ✓ Both are connection-oriented and use virtual circuits — True for both technologies.  

**Correct:** B, C, D


#### 14. Which of the following best describe the evolution and convergence of WAN, MAN, and LAN technologies?  
A) ✓ MPLS and Ethernet are becoming the most prevalent technologies in WANs and MANs — Correct trend.  
B) ✗ WANs still exclusively use legacy technologies like X.25 and Frame Relay — Incorrect; MPLS and Ethernet dominate now.  
C) ✗ LANs and WANs remain completely separate in technology and operation — Technologies are converging, not separate.  
D) ✓ Ethernet is now commonly used across LANs, MANs, and WANs — True, Ethernet is converging these networks.  

**Correct:** A, D


#### 15. Which of the following statements about packet switching types are correct?  
A) ✗ Virtual circuits require a dedicated physical circuit for the duration of the connection — Virtual circuits are logical, not physical circuits.  
B) ✓ Virtual circuit packet switching establishes a route once per connection and uses connection identifiers — True for virtual circuits.  
C) ✗ Packet switching is generally less efficient than leased lines for bursty traffic patterns — Packet switching is more efficient for bursty traffic.  
D) ✓ Datagram packet switching routes each packet independently without a fixed path — Correct definition.  

**Correct:** B, D