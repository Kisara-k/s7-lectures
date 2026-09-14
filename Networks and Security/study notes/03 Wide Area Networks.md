## 3 Wide Area Networks

## Study Notes

### 1. 🌐 What Are Wide Area Networks (WANs) and Metropolitan Area Networks (MANs)?

When we talk about computer networks, we often hear about LANs, WANs, and MANs. These terms describe networks based on their size and coverage area.

- **Wide Area Network (WAN):**  
  A WAN is a network that covers a very large geographical area, typically spanning more than 30 kilometers in diameter. Unlike LANs (Local Area Networks), which are usually confined to a single building or campus (less than 1 km), WANs connect multiple LANs across cities, countries, or even continents. WANs are usually operated by telecommunications service providers because they require large infrastructure and resources.

- **Metropolitan Area Network (MAN):**  
  A MAN covers a smaller area than a WAN but larger than a LAN, typically up to about 50 kilometers. It usually connects multiple LANs within a city or metropolitan region. For example, a MAN might connect offices from Moratuwa to Ja-Ela in Colombo. Like WANs, MANs are often managed by telecom providers.

#### Convergence of Technologies  
Traditionally, LANs, MANs, and WANs used different technologies. However, nowadays, technologies like Ethernet are common across all three types of networks, simplifying network design and management.


### 2. 🔗 Leased Lines: Dedicated Connections for Reliable Communication

A **leased line** is a dedicated communication link between two points that is always available, 24/7. Think of it as a private highway reserved just for your data, without sharing with others.

- **Characteristics:**
  - Always on and dedicated to the user.
  - Has a fixed data carrying capacity (e.g., 64 kbps or 2 Mbps).
  - Costs a fixed monthly fee regardless of how much data you send.

- **Types:**
  - **Analog leased lines:** Older technology, less common today.
  - **Digital leased lines:** Most common today, offering speeds from 64 kbps (suitable for a few computers) up to 2 Mbps (for larger offices).

- **Uses:**
  - Voice communication (e.g., tie lines between offices).
  - Data communication for corporate networks and internet access.
  - Combined voice and data services.

Leased lines are reliable but can be expensive, especially for long distances or high speeds.


### 3. 📦 Packet Switching: Efficient Data Transmission for Bursty Traffic

Unlike leased lines, which dedicate a fixed path, **packet switching** breaks data into small chunks called packets and sends them independently through the network.

- **How it works:**
  - Data is divided into packets.
  - Each packet is sent one after another.
  - Packets from different users or connections can be mixed together in the network.
  - The network routes each packet toward its destination independently.

- **Advantages:**
  - More efficient for bursty traffic (data sent in bursts rather than a steady stream).
  - Network resources are shared dynamically.

- **Types of Packet Switching:**
  - **Datagram:** Each packet is routed independently, like sending letters without a fixed route.
  - **Virtual Circuit:** A logical path is established for the duration of a connection, and packets carry connection identifiers instead of full destination addresses.


### 4. 🛤️ X.25 and Frame Relay: Early Packet-Switched WAN Technologies

#### X.25  
- An early standard for packet-switched networks, introduced in the 1960s.
- Used by banks, airlines, and other organizations for reliable data communication.
- Very slow by today’s standards (~64 kbps) and expensive.
- Provided error control and reliable delivery but with high overhead.

#### Frame Relay  
- Developed in the late 1980s as a faster, simpler replacement for X.25.
- Uses virtual circuits but assumes the network is reliable, so it does not perform error correction.
- Designed to interconnect corporate LANs over a WAN.
- Supports multiple virtual circuits over a single physical link.
- Customers lease Frame Relay service from public networks.
- Uses a **Committed Information Rate (CIR)**, which guarantees a minimum data rate for each virtual circuit.

Frame Relay became popular in the 1990s for corporate WANs due to its efficiency and lower cost compared to X.25.


### 5. 📶 Asynchronous Transfer Mode (ATM): High-Speed Cell Switching for Voice, Video, and Data

ATM is a WAN technology designed to handle voice, video, and data traffic efficiently by using small fixed-size units called **cells**.

- **ATM Cells:**
  - Each cell is 53 bytes: 5 bytes of header + 48 bytes of data.
  - Fixed size allows very fast processing and switching.

- **Why Cell Switching?**
  - Voice and video require low delay and consistent timing.
  - Older packet switching methods (like X.25 and Frame Relay) have variable delays unsuitable for real-time traffic.
  - ATM integrates voice, video, and data on the same network with minimal delay.

- **Features:**
  - Scalable and flexible.
  - Supports various charging schemes based on actual usage (number of cells sent).
  - Typically uses optical fiber for high-speed transmission.

- **ATM Layers and Virtual Circuits:**
  - ATM uses virtual circuits identified by a two-part address: Virtual Path Identifier (VPI) and Virtual Channel Identifier (VCI).
  - Each switch maintains state information for each virtual circuit.
  - Resources like bandwidth and buffers can be allocated per virtual circuit to guarantee performance.

- **Usage:**
  - Initially envisioned as an end-to-end network technology.
  - In practice, often used as a link layer technology connecting IP backbone routers.


### 6. 🏷️ Multi-Protocol Label Switching (MPLS): Combining the Best of Packet Switching and Circuit Switching

MPLS is a modern WAN technology that improves network scalability, performance, and flexibility by combining features of packet switching and circuit switching.

- **What is MPLS?**
  - It is "multi-protocol" because it works with various Layer 2 technologies (Ethernet, ATM, Frame Relay).
  - Uses labels to forward packets instead of routing based on IP addresses at every hop.
  - Labels are assigned at the edge of the MPLS network and used to switch packets through the core.

- **Key Benefits:**
  - **Network Scalability:** Handles large networks efficiently.
  - **Traffic Engineering:** Allows control over the path data takes, optimizing network usage.
  - **VPN Support:** Enables secure virtual private networks over shared infrastructure.
  - **Quality of Service (QoS):** Supports prioritization of traffic types.

- **How MPLS Works:**
  - At the network edge, packets are labeled.
  - Inside the MPLS network, switches forward packets based on labels, which is faster than traditional IP routing.
  - MPLS supports dynamic routing and connection-oriented behavior.

- **Where is MPLS Used?**
  - Mainly in service provider or carrier networks.
  - Not typically deployed in private enterprise networks.


### 7. 🏠 Ethernet First Mile (EFM): Bringing Ethernet to Homes and Offices

EFM is a standard (IEEE 802.3ah) designed to extend Ethernet connectivity from service providers directly to customers’ premises, including homes and small offices.

- **Media Types:**
  - Copper cables (traditional phone lines or twisted pair).
  - Fiber optic cables.

- **EFM over Copper (EFMC):**
  - Uses DSL-like modulation to send Ethernet frames over copper.
  - Typical speeds:
    - 10 Mbps up to 750 meters (short range).
    - 2 Mbps up to 2,700 meters (long range).
  - Some products exceed these speeds and distances.

- **EFM over Fiber (EFMF):**
  - Supports point-to-point and Passive Optical Networks (PON).
  - Dual fiber standards (separate fibers for sending and receiving):
    - 100BASE-LX10 (100 Mbps)
    - 1000BASE-LX10 (1 Gbps)
  - Single fiber standards (using one fiber for both directions):
    - 100BASE-BX10
    - 1000BASE-BX10

EFM helps provide high-speed, reliable Ethernet connections directly to end users, improving access network performance.


### 8. 📋 Summary: The Evolution and Future of WAN Technologies

- WANs and MANs cover large geographical areas and are essential for connecting dispersed networks.
- Traditional WAN technologies like leased lines and X.25 have largely been replaced by more efficient packet-switched technologies such as Frame Relay, ATM, and MPLS.
- ATM introduced cell switching to support integrated voice, video, and data with low latency.
- MPLS is a key modern technology that combines the flexibility of packet switching with the performance of circuit switching, widely used by service providers.
- Ethernet, once confined to LANs, is now extending into MANs and WANs, especially with standards like Ethernet First Mile.
- WAN technology continues to evolve rapidly, driven by the need for higher speeds, better quality of service, and more flexible network management.