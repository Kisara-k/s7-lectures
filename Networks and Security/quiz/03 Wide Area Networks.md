## 3 Wide Area Networks

## Questions

#### 1. What distinguishes a Wide Area Network (WAN) from a Local Area Network (LAN)?  
A) WANs typically span over 30 km in diameter, while LANs are generally less than 1 km  
B) WANs are usually operated by telecom service providers, LANs by individual organizations  
C) WANs use only wireless technologies, LANs use only wired technologies  
D) LANs always have higher bandwidth than WANs  

#### 2. Which of the following statements about Metropolitan Area Networks (MANs) are true?  
A) MANs typically cover areas up to about 50 km in diameter  
B) MANs are usually run by telecom providers  
C) MANs are a subset of LANs  
D) MANs use completely different technologies than WANs and LANs  

#### 3. Which of the following are characteristics of leased lines?  
A) They provide a full-time dedicated link between two points  
B) They have a fixed monthly cost regardless of usage  
C) They are typically packet-switched connections  
D) Most leased lines today are digital with speeds commonly between 64 kb/s and 2 Mb/s  

#### 4. Packet switching differs from leased lines in that:  
A) It breaks data into packets sent independently through the network  
B) It guarantees a dedicated circuit for the entire connection duration  
C) It is more efficient for bursty traffic  
D) It always uses virtual circuits with connection identifiers  

#### 5. Which of the following are true about X.25 packet switching?  
A) It was introduced in the 1960s and became a standard for data communication  
B) It is very fast compared to modern networks  
C) It is expensive relative to today’s networks  
D) It is connectionless and does not maintain state for connections  

#### 6. Frame Relay technology:  
A) Is a replacement for X.25 and is virtual-circuit oriented  
B) Provides error control at the network layer  
C) Uses permanent virtual circuits to carry aggregate traffic between routers  
D) Guarantees bandwidth by negotiating a Committed Information Rate (CIR) at setup  

#### 7. Why are ATM cells fixed at 53 bytes in size?  
A) To simplify and speed up switching for voice, video, and data integration  
B) To maximize payload size for data transmission efficiency  
C) Because variable-sized packets cause unacceptable switching delays for voice/video  
D) To allow error correction within each cell  

#### 8. Which of the following statements about ATM are correct?  
A) ATM is designed to integrate voice, video, and data on the same network  
B) ATM cells have a 5-byte header and 48-byte payload  
C) ATM is only used as a link layer technology connecting IP routers in practice  
D) ATM networks do not maintain any state information for virtual circuits  

#### 9. In ATM addressing, what is the purpose of the two-part identifier consisting of VPI and VCI?  
A) To make network routing easier and faster by hierarchical addressing  
B) To identify the physical location of the switch  
C) To separate virtual paths and virtual circuits within the network  
D) To provide error detection and correction  

#### 10. Which of the following are key capabilities or applications of MPLS?  
A) Network scalability and traffic engineering  
B) Providing connection-oriented switching based on labels  
C) Operating only on private enterprise networks  
D) Supporting VPNs and IP multicast  

#### 11. MPLS is described as “multi-protocol” because:  
A) It can be applied over any Layer 2 network protocol such as PPP, ATM, or Frame Relay  
B) It supports multiple IP versions simultaneously  
C) It uses multiple routing protocols like BGP-4, OSPF, and IS-IS internally  
D) It can only be used with Ethernet networks  

#### 12. Which of the following statements about Ethernet First Mile (EFM) are true?  
A) EFM connects homes and offices using Ethernet technology  
B) EFM over copper uses DSL modulation schemes with Ethernet frames  
C) EFM only supports fiber optic media, not copper  
D) EFM aims to provide 10 Mbps at 750 meters and 2 Mbps at 2,700 meters over copper  

#### 13. Regarding Frame Relay and ATM, which of the following are accurate comparisons?  
A) Both are connection-oriented and use virtual circuits  
B) Frame Relay includes error control, ATM does not  
C) ATM uses fixed-size cells, Frame Relay uses variable-length frames  
D) Frame Relay is generally slower and less flexible than ATM  

#### 14. Which of the following best describe the evolution and convergence of WAN, MAN, and LAN technologies?  
A) Ethernet is now commonly used across LANs, MANs, and WANs  
B) WANs still exclusively use legacy technologies like X.25 and Frame Relay  
C) MPLS and Ethernet are becoming the most prevalent technologies in WANs and MANs  
D) LANs and WANs remain completely separate in technology and operation  

#### 15. Which of the following statements about packet switching types are correct?  
A) Datagram packet switching routes each packet independently without a fixed path  
B) Virtual circuit packet switching establishes a route once per connection and uses connection identifiers  
C) Virtual circuits require a dedicated physical circuit for the duration of the connection  
D) Packet switching is generally less efficient than leased lines for bursty traffic patterns



<br>

## Answers

#### 1. What distinguishes a Wide Area Network (WAN) from a Local Area Network (LAN)?  
A) ✓ WANs typically span over 30 km in diameter, while LANs are generally less than 1 km — This is a key defining difference.  
B) ✓ WANs are usually operated by telecom service providers, LANs by individual organizations — Correct distinction of management.  
C) ✗ WANs use only wireless technologies, LANs use only wired technologies — Incorrect; both can use wired or wireless.  
D) ✗ LANs always have higher bandwidth than WANs — Not necessarily true; bandwidth depends on technology, not just network type.  

**Correct:** A, B


#### 2. Which of the following statements about Metropolitan Area Networks (MANs) are true?  
A) ✓ MANs typically cover areas up to about 50 km in diameter — Correct size range for MANs.  
B) ✓ MANs are usually run by telecom providers — True, similar to WANs.  
C) ✗ MANs are a subset of LANs — Incorrect; MANs are larger than LANs.  
D) ✗ MANs use completely different technologies than WANs and LANs — Incorrect; technologies are converging.  

**Correct:** A, B


#### 3. Which of the following are characteristics of leased lines?  
A) ✓ They provide a full-time dedicated link between two points — Core feature of leased lines.  
B) ✓ They have a fixed monthly cost regardless of usage — True, cost is fixed.  
C) ✗ They are typically packet-switched connections — Leased lines are circuit-switched, dedicated links.  
D) ✓ Most leased lines today are digital with speeds commonly between 64 kb/s and 2 Mb/s — Correct typical speeds and digital nature.  

**Correct:** A, B, D


#### 4. Packet switching differs from leased lines in that:  
A) ✓ It breaks data into packets sent independently through the network — Fundamental packet switching concept.  
B) ✗ It guarantees a dedicated circuit for the entire connection duration — Packet switching does not guarantee dedicated circuits.  
C) ✓ It is more efficient for bursty traffic — Packet switching handles bursty traffic better than leased lines.  
D) ✗ It always uses virtual circuits with connection identifiers — Packet switching can be datagram or virtual circuit; not always virtual circuit.  

**Correct:** A, C


#### 5. Which of the following are true about X.25 packet switching?  
A) ✓ It was introduced in the 1960s and became a standard for data communication — Historical fact.  
B) ✗ It is very fast compared to modern networks — X.25 is slow (~64 kb/s).  
C) ✓ It is expensive relative to today’s networks — True, costs were high historically.  
D) ✗ It is connectionless and does not maintain state for connections — X.25 is connection-oriented and maintains state.  

**Correct:** A, C


#### 6. Frame Relay technology:  
A) ✓ Is a replacement for X.25 and is virtual-circuit oriented — Correct description.  
B) ✗ Provides error control at the network layer — Frame Relay assumes reliable network, no error control.  
C) ✓ Uses permanent virtual circuits to carry aggregate traffic between routers — True, PVCs are typical.  
D) ✓ Guarantees bandwidth by negotiating a Committed Information Rate (CIR) at setup — CIR defines guaranteed bandwidth.  

**Correct:** A, C, D


#### 7. Why are ATM cells fixed at 53 bytes in size?  
A) ✓ To simplify and speed up switching for voice, video, and data integration — Fixed size enables fast processing.  
B) ✗ To maximize payload size for data transmission efficiency — Payload is small (48 bytes), not maximized.  
C) ✓ Because variable-sized packets cause unacceptable switching delays for voice/video — Fixed size reduces delay variability.  
D) ✗ To allow error correction within each cell — ATM does not provide error correction in cells.  

**Correct:** A, C


#### 8. Which of the following statements about ATM are correct?  
A) ✓ ATM is designed to integrate voice, video, and data on the same network — Core ATM design goal.  
B) ✓ ATM cells have a 5-byte header and 48-byte payload — Correct cell structure.  
C) ✓ ATM is only used as a link layer technology connecting IP routers in practice — Reality differs from vision; mostly link layer use.  
D) ✗ ATM networks do not maintain any state information for virtual circuits — ATM switches maintain state per VC.  

**Correct:** A, B, C


#### 9. In ATM addressing, what is the purpose of the two-part identifier consisting of VPI and VCI?  
A) ✓ To make network routing easier and faster by hierarchical addressing — VPI/VCI split simplifies routing.  
B) ✗ To identify the physical location of the switch — Not the purpose of VPI/VCI.  
C) ✓ To separate virtual paths and virtual circuits within the network — VPI identifies path, VCI identifies circuit.  
D) ✗ To provide error detection and correction — Addressing does not provide error control.  

**Correct:** A, C


#### 10. Which of the following are key capabilities or applications of MPLS?  
A) ✓ Network scalability and traffic engineering — MPLS supports both.  
B) ✓ Providing connection-oriented switching based on labels — Core MPLS function.  
C) ✗ Operating only on private enterprise networks — MPLS is mostly used by service providers, not private networks.  
D) ✓ Supporting VPNs and IP multicast — MPLS supports VPNs and multicast.  

**Correct:** A, B, D


#### 11. MPLS is described as “multi-protocol” because:  
A) ✓ It can be applied over any Layer 2 network protocol such as PPP, ATM, or Frame Relay — True, supports multiple Layer 2 types.  
B) ✗ It supports multiple IP versions simultaneously — Not the reason for “multi-protocol.”  
C) ✗ It uses multiple routing protocols like BGP-4, OSPF, and IS-IS internally — MPLS uses these protocols but that’s not why it’s “multi-protocol.”  
D) ✗ It can only be used with Ethernet networks — Incorrect; MPLS works over various Layer 2 protocols.  

**Correct:** A


#### 12. Which of the following statements about Ethernet First Mile (EFM) are true?  
A) ✓ EFM connects homes and offices using Ethernet technology — Core purpose of EFM.  
B) ✓ EFM over copper uses DSL modulation schemes with Ethernet frames — Correct for EFMC.  
C) ✗ EFM only supports fiber optic media, not copper — EFM supports both copper and fiber.  
D) ✓ EFM aims to provide 10 Mbps at 750 meters and 2 Mbps at 2,700 meters over copper — Correct performance targets.  

**Correct:** A, B, D


#### 13. Regarding Frame Relay and ATM, which of the following are accurate comparisons?  
A) ✓ Both are connection-oriented and use virtual circuits — True for both technologies.  
B) ✗ Frame Relay includes error control, ATM does not — Frame Relay assumes reliable network, no error control; ATM also does not do error control.  
C) ✓ ATM uses fixed-size cells, Frame Relay uses variable-length frames — Correct difference in data unit size.  
D) ✓ Frame Relay is generally slower and less flexible than ATM — ATM is more scalable and flexible.  

**Correct:** A, C, D


#### 14. Which of the following best describe the evolution and convergence of WAN, MAN, and LAN technologies?  
A) ✓ Ethernet is now commonly used across LANs, MANs, and WANs — True, Ethernet is converging these networks.  
B) ✗ WANs still exclusively use legacy technologies like X.25 and Frame Relay — Incorrect; MPLS and Ethernet dominate now.  
C) ✓ MPLS and Ethernet are becoming the most prevalent technologies in WANs and MANs — Correct trend.  
D) ✗ LANs and WANs remain completely separate in technology and operation — Technologies are converging, not separate.  

**Correct:** A, C


#### 15. Which of the following statements about packet switching types are correct?  
A) ✓ Datagram packet switching routes each packet independently without a fixed path — Correct definition.  
B) ✓ Virtual circuit packet switching establishes a route once per connection and uses connection identifiers — True for virtual circuits.  
C) ✗ Virtual circuits require a dedicated physical circuit for the duration of the connection — Virtual circuits are logical, not physical circuits.  
D) ✗ Packet switching is generally less efficient than leased lines for bursty traffic patterns — Packet switching is more efficient for bursty traffic.  

**Correct:** A, B