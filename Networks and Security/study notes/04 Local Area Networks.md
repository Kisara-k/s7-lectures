## 4 Local Area Networks

## Study Notes

### 1. 🌐 Introduction to Local Area Networks (LANs)

Local Area Networks, or LANs, are networks that connect computers and devices within a relatively small geographic area, such as a home, office, or campus. Unlike Wide Area Networks (WANs) that cover large distances, LANs typically span from a few meters to several hundred meters. The main purpose of a LAN is to enable fast and efficient communication and resource sharing among connected devices.

#### Key Characteristics of LANs:
- **Short Distance:** Devices are usually connected within a limited area, from a few meters up to a few hundred meters.
- **High Data Rates:** LANs support higher data transmission speeds compared to WANs, typically ranging from 1 Mbps to 100 Mbps or more.
- **Private Ownership:** LAN channels are usually privately owned and managed, meaning public carriers are not involved.
- **Low Error Rates:** LANs have much lower error rates than WANs, making communication more reliable.
- **Typical Error Rate:** For LANs, the error rate is about 1 in 10^8 bits, whereas WANs have higher error rates (1 in 10^3 to 1 in 10^6).


### 2. 📡 Broadband vs Baseband LANs

LANs can use two main types of signaling technologies: **Broadband** and **Baseband**.

#### Broadband LANs:
- Use **analog technology** and modems to transmit data.
- Employ **Frequency Division Multiplexing (FDM)**, which divides the channel into multiple frequency bands (carriers and subchannels) to allow simultaneous transmissions.
- Suitable for carrying multiple signals over the same medium.

#### Baseband LANs:
- Use **digital technology**, where voltage levels represent data bits.
- Can use **Time Division Multiplexing (TDM)** to allow multiple devices to share the medium by dividing time into slots.
- Often rely on protocols to manage multiple access to the medium.
- Baseband is the most common method in modern LANs like Ethernet.


### 3. 📏 Major Attributes of a LAN

Understanding the fundamental attributes of LANs helps in grasping how they function and differ from other networks:

- **Connection Distance:** LANs connect devices within a limited physical area.
- **Data Transport:** They transport data between user stations and computers.
- **Transmission Capacity:** LANs offer higher bit rates (1 Mbps to 100 Mbps or more).
- **Ownership:** LAN channels are typically privately owned.
- **Error Rate:** LANs have very low error rates compared to WANs.


### 4. 📚 IEEE LAN Standards and Their Relationship to OSI Model

The IEEE (Institute of Electrical and Electronics Engineers) has developed a set of standards for LANs, known as the IEEE 802 standards. These standards define how devices communicate on a LAN.

#### Key IEEE 802 Standards:
- **802.1:** Higher layers and network management.
- **802.2:** Logical Link Control (LLC) layer.
- **802.3:** Ethernet and CSMA/CD (Carrier Sense Multiple Access with Collision Detection).
- **802.4:** Token Bus.
- **802.5:** Token Ring.

#### Relationship to OSI Model:
- The **Data Link Layer** in the OSI model is split into two sublayers in IEEE 802:
  - **Logical Link Control (LLC):** Manages communication between devices and provides error and flow control.
  - **Media Access Control (MAC):** Controls how devices access the physical medium.

LLC is a subset of HDLC (High-Level Data Link Control), while MAC includes protocols like Ethernet (802.3), Token Bus (802.4), and Token Ring (802.5).


### 5. 🔄 Media Access Control (MAC) and CSMA/CD (IEEE 802.3)

#### What is MAC?
The Media Access Control sublayer manages how devices share the physical communication medium. It ensures that data frames are transmitted without collisions or manages collisions when they occur.

#### CSMA/CD Explained:
- **Carrier Sense Multiple Access with Collision Detection (CSMA/CD)** is a protocol used primarily in Ethernet networks to control access to the shared medium.
- **Carrier Sense:** Devices listen to the channel before transmitting to check if it is free.
- **Multiple Access:** Multiple devices can attempt to use the channel.
- **Collision Detection:** If two devices transmit simultaneously, a collision occurs, which is detected by the devices.

#### How CSMA/CD Works:
1. A device listens to the channel (carrier sense).
2. If the channel is idle (no carrier), it waits for a short Inter Frame Gap (IFG) and then transmits.
3. If two devices transmit at the same time, a collision is detected.
4. Devices send a jam signal to notify others of the collision.
5. Devices wait a random back-off time before attempting to retransmit.

#### History:
- Developed by Xerox Corporation.
- Standardized as IEEE 802.3 after collaboration with Intel and DEC.


### 6. 🛠 Functions of Data Link and Physical Layers in CSMA/CD

#### Data Link Layer Functions:
- **Encapsulation/Decapsulation:** Adding/removing source and destination addresses, error detection fields.
- **Media Access Management:** Controls frame transmission and reception, buffers frames, and handles collisions.

#### Physical Layer Functions:
- **Data Encoding/Decoding:** Converts binary data to signals (e.g., Manchester encoding) and vice versa.
- **Channel Access:** Sends signals onto the medium, senses carrier presence, and detects collisions.


### 7. 🔄 Token Ring and Token Bus Networks (IEEE 802.5 and 802.4)

#### Token Ring (IEEE 802.5):
- Uses a **token-passing** method to control access.
- A token circulates around the ring; only the device holding the token can transmit.
- The token indicates whether the ring is free or busy.
- After transmission, the token is released back to the ring.
- Provides **priority access** and orderly transmission.

#### Token Bus (IEEE 802.4):
- Similar to Token Ring but uses a **logical ring** over a physical bus topology.
- The token is passed based on the numeric address of devices.
- If a device fails to pass the token, a new successor is chosen.
- Frame format is similar to Token Ring but lacks some control fields.


### 8. 🖧 Ethernet in Detail

Ethernet is the most widely used LAN technology, standardized as IEEE 802.3. It uses CSMA/CD for media access control and supports various physical media types.

#### Ethernet Frame Structure:
- **Preamble (56 bits):** Alternating 1s and 0s to synchronize devices.
- **Start Frame Delimiter (SFD, 8 bits):** Marks the start of the frame.
- **Destination Address (48 bits):** MAC address of the receiver.
- **Source Address (48 bits):** MAC address of the sender.
- **Type/Length (16 bits):** Indicates either the length of the data or the protocol type.
- **Data (46-1500 bytes):** Payload.
- **Frame Check Sequence (FCS, 32 bits):** CRC for error detection.


### 9. ⏳ Media Access Control Rules and Back-off Algorithm

#### Media Access Control Rules:
1. When a signal is on the channel, it is called a **carrier**.
2. A device wanting to transmit waits until the channel is idle (no carrier).
3. After the channel is idle, the device waits for an **Inter Frame Gap (IFG)** before transmitting.
4. If two devices transmit simultaneously, a **collision** occurs, detected by both.

#### Back-off Algorithm:
- If no carrier is detected for the IFG period, the device transmits immediately.
- If a collision occurs, the device sends a jam signal (32 bits) to notify others.
- Then it waits a random time before retrying (back-off).
- The random wait time increases exponentially with each collision, up to 16 retries.
- After 16 failed attempts, the transmission is aborted and higher layers are notified.


### 10. ⏱ Slot Time and Its Importance

**Slot Time** is the time needed to detect collisions reliably. It is based on the round-trip propagation delay of the physical medium plus the time to send a jam signal.

- For 10/100 Mbps Ethernet, slot time is 512 bit times (about 51.2 µs for 10 Mbps).
- This corresponds to a maximum cable length (e.g., 2800m for coaxial cable at 10 Mbps).
- For Gigabit Ethernet, the slot time is extended to 4096 bits due to faster signaling and shorter maximum cable lengths.
- Slot time ensures that collisions are detected before the transmission ends.


### 11. 🚀 Gigabit Ethernet and Full Duplex Operation

#### Gigabit Ethernet:
- Operates at 1 Gbps.
- Uses the same CSMA/CD principles in half-duplex mode but with shorter slot times.
- To accommodate longer distances, slot time is extended to 4096 bits.
- Uses **carrier extension** to pad short frames to minimum length.

#### Full Duplex Ethernet:
- Allows simultaneous transmission and reception on separate channels.
- Requires point-to-point links (e.g., twisted pair or fiber optic).
- No collisions occur, so CSMA/CD is not needed.
- Doubles effective bandwidth (e.g., 100 Mbps full duplex = 200 Mbps total).
- Specified by IEEE 802.3x.


### 12. 🔖 VLANs (Virtual LANs)

#### Concept:
- VLANs allow grouping of switch ports into separate logical networks, acting like independent hubs.
- VLANs improve security and traffic management by isolating groups of devices.
- VLANs can span multiple switches using **frame tagging**.

#### IEEE 802.1Q Standard:
- Defines a vendor-independent VLAN tagging method.
- Adds a 4-byte VLAN tag to Ethernet frames, increasing max frame size to 1522 bytes.
- VLAN tag includes:
  - **TPID (Tag Protocol Identifier):** Identifies the frame as VLAN tagged (0x8100).
  - **TCI (Tag Control Information):** Contains priority bits and VLAN ID.
- VLAN management requires network software to handle configurations and traffic rules.


### 13. 📡 Other Related Topics

- **Wireless LANs (WLANs):** IEEE 802.11 standards (e.g., 802.11a, 802.11b) define wireless networking.
- **Metropolitan Area Networks (MANs):** Larger than LANs but smaller than WANs.
- **Ethernet in the First Mile (EFM):** IEEE 802.3ah standard for Ethernet access networks.


### Summary

This study note covers the essentials of Local Area Networks, including their characteristics, IEEE standards, media access methods like CSMA/CD and token passing, Ethernet frame structure, collision handling, Gigabit Ethernet enhancements, full duplex operation, and VLANs. Understanding these concepts provides a solid foundation for studying network design and operation in modern computer networks.