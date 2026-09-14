## 3 Wide Area Networks

## Questions

#### 1. Which of the following statements correctly distinguish Wide Area Networks (WANs) from Local Area Networks (LANs)?  
A) WANs often use leased lines and packet switching technologies, while LANs primarily use Ethernet.  
B) LANs and WANs have always used the same underlying technologies without any convergence.  
C) WANs typically span areas greater than 30 km in diameter, while LANs are generally less than 1 km.  
D) WANs are usually operated by individual organizations, whereas LANs are run by telecom service providers.  

#### 2. Regarding packet switching, which of the following are true?  
A) Datagram packet switching routes each packet independently without a fixed path.  
B) Packet switching is more efficient than leased lines for bursty traffic patterns.  
C) Virtual circuit packet switching establishes a dedicated physical circuit for the entire connection.  
D) X.25 is a modern, high-speed packet switching technology widely used today.  

#### 3. Frame Relay technology is characterized by which of the following features?  
A) Customers pay based on the Committed Information Rate (CIR) negotiated at setup.  
B) It uses permanent virtual circuits to carry aggregate traffic between routers.  
C) Frame Relay was designed primarily for voice and video transmission with low latency.  
D) It provides error control at the network layer to ensure reliable transmission.  

#### 4. Why does Asynchronous Transfer Mode (ATM) use small fixed-size cells instead of variable-length packets?  
A) To simplify header processing and improve scalability across different services.  
B) Because ATM networks are designed only for data traffic, not voice or video.  
C) To enable fast switching suitable for integrated voice, video, and data services.  
D) Because small cells reduce the overall bandwidth required for transmission.  

#### 5. Which of the following correctly describe MPLS (Multi-Protocol Label Switching)?  
A) MPLS operates only on IP networks and cannot be applied to other Layer 2 protocols.  
B) MPLS supports traffic engineering, VPNs, and network scalability as key applications.  
C) MPLS provides connection-oriented switching by applying labels at the edge of the MPLS domain.  
D) MPLS replaces IP routing protocols such as BGP and OSPF within service provider networks.  

#### 6. Ethernet First Mile (EFM) technologies include which of the following characteristics?  
A) EFM standards support both point-to-point and passive optical network (PON) topologies.  
B) EFM aims to provide high-speed connectivity to homes and offices, with speeds up to 10 Mbps at 750 meters over copper.  
C) EFM over fiber supports only dual-fiber standards such as 100BASE-LX10 and 1000BASE-LX10.  
D) EFM over copper uses DSL modulation schemes to carry Ethernet frames.  

#### 7. Which of the following statements about leased lines are accurate?  
A) Leased lines are typically bursty and inefficient for continuous data transmission.  
B) Leased lines provide a dedicated, always-available connection with a fixed monthly cost regardless of usage.  
C) Leased lines are commonly used for corporate data networks, voice tie lines, and combined voice and data services.  
D) Most leased lines today are analog and operate at speeds between 64 kb/s and 2 Mb/s.  

#### 8. Consider the addressing scheme in ATM networks. Which of the following are true?  
A) ATM switches maintain state information for each virtual circuit passing through them to allocate resources.  
B) Each ATM cell carries the destination IP address to route the cell through the network.  
C) ATM uses a two-part addressing scheme consisting of Virtual Path Identifier (VPI) and Virtual Circuit Identifier (VCI).  
D) The two-part addressing simplifies and speeds up network routing by grouping virtual circuits into virtual paths.  



<br>

## Answers

#### 1. Which of the following statements correctly distinguish Wide Area Networks (WANs) from Local Area Networks (LANs)?  
A) ✓ WANs often use leased lines and packet switching; LANs primarily use Ethernet.  
B) ✗ Technologies for LANs, MANs, and WANs have been converging, not always the same.  
C) ✓ WANs typically span areas greater than 30 km, LANs generally less than 1 km.  
D) ✗ Opposite is true: WANs are run by telecom providers, LANs by individual organizations.  

**Correct:** A, C


#### 2. Regarding packet switching, which of the following are true?  
A) ✓ Datagram routing sends each packet independently without fixed path.  
B) ✓ Packet switching is more efficient than leased lines for bursty traffic.  
C) ✗ Virtual circuit switching uses logical connections, not dedicated physical circuits.  
D) ✗ X.25 is old, slow (~64 kb/s), and expensive, not widely used today.  

**Correct:** A, B


#### 3. Frame Relay technology is characterized by which of the following features?  
A) ✓ Customers pay based on Committed Information Rate negotiated at setup.  
B) ✓ Uses permanent virtual circuits to carry aggregate traffic between routers.  
C) ✗ Frame Relay was designed for data networks, not optimized for voice/video low latency.  
D) ✗ Frame Relay assumes reliable network, so no error control at network layer.  

**Correct:** A, B


#### 4. Why does Asynchronous Transfer Mode (ATM) use small fixed-size cells instead of variable-length packets?  
A) ✓ Uniform size simplifies header processing and improves scalability.  
B) ✗ ATM is designed for voice, video, and data, not just data traffic.  
C) ✓ Small cells enable fast switching suitable for integrated voice, video, and data.  
D) ✗ Small cells do not reduce overall bandwidth; they improve processing speed and latency.  

**Correct:** A, C


#### 5. Which of the following correctly describe MPLS (Multi-Protocol Label Switching)?  
A) ✗ MPLS is multi-protocol and can be applied to various Layer 2 protocols, not only IP.  
B) ✓ Supports traffic engineering, VPNs, and network scalability as key applications.  
C) ✓ MPLS provides connection-oriented switching by applying labels at domain edges.  
D) ✗ MPLS uses IP routing protocols like BGP and OSPF; it does not replace them.  

**Correct:** B, C


#### 6. Ethernet First Mile (EFM) technologies include which of the following characteristics?  
A) ✓ EFM supports both point-to-point and passive optical network (PON) topologies.  
B) ✓ EFM aims to provide up to 10 Mbps at 750m over copper (EFMC SR).  
C) ✗ EFM over fiber supports both dual-fiber and single-fiber standards, not only dual-fiber.  
D) ✓ EFM over copper uses DSL modulation schemes with Ethernet frames.  

**Correct:** A, B, D


#### 7. Which of the following statements about leased lines are accurate?  
A) ✗ Leased lines are dedicated and continuous, not bursty or inefficient for continuous transmission.  
B) ✓ Leased lines provide dedicated, always-available links with fixed monthly cost regardless of usage.  
C) ✓ Used for corporate data, voice tie lines, and combined voice/data services.  
D) ✗ Most leased lines today are digital, not analog.  

**Correct:** B, C


#### 8. Consider the addressing scheme in ATM networks. Which of the following are true?  
A) ✓ ATM switches maintain state for each VC to allocate resources and provide circuit-like performance.  
B) ✗ ATM cells carry VC identifiers, not destination IP addresses.  
C) ✓ ATM uses two-part addressing: Virtual Path Identifier (VPI) and Virtual Circuit Identifier (VCI).  
D) ✓ Two-part addressing groups virtual circuits into virtual paths, simplifying routing.  

**Correct:** A, C, D