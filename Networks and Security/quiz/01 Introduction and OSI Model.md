## 1 Introduction and OSI Model

## Questions

#### 1. What are the main strategies for coping with the complexity and rapid change in communications systems?  
A) Modularization  
B) Layering  
C) Standardization of interfaces  
D) Increasing hardware speed  

#### 2. Which of the following statements about the OSI Reference Model are true?  
A) It was developed by ISO in 1974 to provide a basis for network standardization  
B) It consists of five layers that each perform multiple unrelated functions  
C) Each layer provides services to the layer above and relies on the layer below  
D) Peer layers communicate directly without involving lower layers  

#### 3. In the OSI model, what is the role of protocols?  
A) Define how adjacent layers access each other  
B) Define the rules for communication between peer layers on different nodes  
C) Provide the physical transmission of bits  
D) Manage the interface between hardware and software  

#### 4. Which of the following are true about the layering principle in the OSI model?  
A) Layers should be large enough to group unrelated functions for efficiency  
B) Layers should minimize information flow across boundaries  
C) Each layer has exactly one interface to the layer above and one to the layer below  
D) Layer boundaries are chosen arbitrarily without regard to function  

#### 5. Which OSI layer is primarily responsible for establishing, maintaining, and terminating sessions between applications?  
A) Transport  
B) Session  
C) Presentation  
D) Network  

#### 6. What functions are typically handled by the Presentation layer?  
A) Data formatting and encryption  
B) Routing and addressing  
C) Error detection and correction  
D) Dialog control between applications  

#### 7. Which of the following are key functions of the Data Link layer?  
A) Framing  
B) Error detection and correction  
C) End-to-end delivery  
D) Flow control  

#### 8. The Network layer is responsible for which of the following?  
A) Delivery of packets from source to destination across multiple networks  
B) Error-free transmission across a single link  
C) Establishing and terminating connections between hosts  
D) Routing and congestion control  

#### 9. How does the Transport layer differ from the Data Link layer?  
A) Transport layer provides end-to-end delivery across networks, Data Link layer only across a single link  
B) Transport layer handles framing and error detection, Data Link layer does not  
C) Transport layer manages flow control and multiplexing, Data Link layer does not  
D) Transport layer operates only on physical connections, Data Link layer operates on logical connections  

#### 10. Which of the following are true about the Session layer?  
A) It manages dialog control such as half- and full-duplex communication  
B) It is widely used in most modern network implementations  
C) It handles synchronization and recovery management  
D) It formats data for transmission  

#### 11. Why is the TCP/IP model considered less complex than the OSI model?  
A) It excludes the physical, session, and presentation layers explicitly  
B) It combines session and presentation functions into other layers  
C) It uses fewer layers but provides the same functionality  
D) It does not require standardization of interfaces  

#### 12. Which of the following are reasons for TCP/IP’s widespread adoption?  
A) Runs on a wide variety of hardware platforms  
B) Has consistent APIs across implementations  
C) Is more complex and feature-rich than OSI  
D) Has a strong track record and supports the Internet and WWW  

#### 13. In the OSI model, what is the primary purpose of the Physical layer?  
A) Encoding and transmitting raw bits across a physical medium  
B) Providing error-free transmission across a link  
C) Routing packets between hosts  
D) Managing end-to-end delivery  

#### 14. Which of the following statements about the OSI model’s interfaces and services are correct?  
A) Services describe what a layer does, not how it is accessed  
B) Interfaces define how adjacent layers access each other’s services  
C) Each layer has multiple interfaces to the layer above and below  
D) Peer layers communicate directly through their interfaces  

#### 15. What are some challenges addressed by the Network layer?  
A) Addressing the destination machine  
B) Routing packets through the best path  
C) Managing congestion at intermediate nodes  
D) Encrypting data for secure transmission



<br>

## Answers

#### 1. What are the main strategies for coping with the complexity and rapid change in communications systems?  
A) ✓ Modularization helps break down complex systems into manageable parts.  
B) ✓ Layering organizes functions into separate levels to manage complexity.  
C) ✓ Standardization of interfaces ensures interoperability between components.  
D) ✗ Increasing hardware speed does not address architectural complexity or change.  

**Correct:** A, B, C


#### 2. Which of the following statements about the OSI Reference Model are true?  
A) ✓ ISO developed the OSI model in 1974 for standardization purposes.  
B) ✗ The OSI model has seven layers, each with well-defined, related functions.  
C) ✓ Each layer provides services to the layer above and relies on the layer below.  
D) ✗ Peer layers communicate logically via lower layers, not directly.  

**Correct:** A, C


#### 3. In the OSI model, what is the role of protocols?  
A) ✗ Defining how adjacent layers access each other is the role of interfaces, not protocols.  
B) ✓ Protocols define rules for communication between peer layers on different nodes.  
C) ✗ Physical transmission of bits is handled by the Physical layer, not protocols.  
D) ✗ Managing hardware-software interface is not the role of protocols.  

**Correct:** B


#### 4. Which of the following are true about the layering principle in the OSI model?  
A) ✗ Layers should avoid grouping unrelated functions to maintain clarity.  
B) ✓ Minimizing information flow across boundaries reduces complexity and dependencies.  
C) ✓ Each layer has one interface to the layer above and one to the layer below.  
D) ✗ Layer boundaries are chosen carefully based on function, not arbitrarily.  

**Correct:** B, C


#### 5. Which OSI layer is primarily responsible for establishing, maintaining, and terminating sessions between applications?  
A) ✗ Transport layer handles end-to-end delivery, not session management.  
B) ✓ Session layer manages dialog control and session establishment.  
C) ✗ Presentation layer handles data formatting, not session control.  
D) ✗ Network layer handles routing and addressing, not sessions.  

**Correct:** B


#### 6. What functions are typically handled by the Presentation layer?  
A) ✓ Data formatting and encryption are key Presentation layer functions.  
B) ✗ Routing and addressing are Network layer functions.  
C) ✗ Error detection and correction belong to Data Link and Transport layers.  
D) ✗ Dialog control is a Session layer function.  

**Correct:** A


#### 7. Which of the following are key functions of the Data Link layer?  
A) ✓ Framing is a core Data Link layer function.  
B) ✓ Error detection and correction are handled at this layer.  
C) ✗ End-to-end delivery is a Transport layer responsibility.  
D) ✓ Flow control is managed to prevent overwhelming the receiver.  

**Correct:** A, B, D


#### 8. The Network layer is responsible for which of the following?  
A) ✓ Delivering packets across multiple networks is the Network layer’s main role.  
B) ✗ Error-free transmission across a single link is Data Link layer’s job.  
C) ✗ Connection establishment is handled by Transport layer.  
D) ✓ Routing and congestion control are key Network layer issues.  

**Correct:** A, D


#### 9. How does the Transport layer differ from the Data Link layer?  
A) ✓ Transport provides end-to-end delivery across networks; Data Link is link-to-link.  
B) ✗ Framing and error detection are primarily Data Link functions.  
C) ✓ Transport manages flow control and multiplexing across multiple connections.  
D) ✗ Transport operates on logical connections, not just physical ones.  

**Correct:** A, C


#### 10. Which of the following are true about the Session layer?  
A) ✓ It manages dialog control such as half- and full-duplex communication.  
B) ✗ It is not widely used in many modern systems.  
C) ✓ It handles synchronization and recovery management.  
D) ✗ Data formatting is a Presentation layer function.  

**Correct:** A, C


#### 11. Why is the TCP/IP model considered less complex than the OSI model?  
A) ✓ TCP/IP excludes physical, session, and presentation layers explicitly.  
B) ✓ Session and Presentation functions are combined into other layers in TCP/IP.  
C) ✗ TCP/IP does not have fewer layers but merges some functions.  
D) ✗ TCP/IP still requires standardization of interfaces.  

**Correct:** A, B


#### 12. Which of the following are reasons for TCP/IP’s widespread adoption?  
A) ✓ Runs on a wide variety of hardware platforms.  
B) ✓ Has consistent APIs across implementations.  
C) ✗ TCP/IP is less complex, not more complex than OSI.  
D) ✓ Has a strong track record and supports the Internet and WWW.  

**Correct:** A, B, D


#### 13. In the OSI model, what is the primary purpose of the Physical layer?  
A) ✓ Encoding and transmitting raw bits across a physical medium.  
B) ✗ Error-free transmission is Data Link layer’s responsibility.  
C) ✗ Routing packets is a Network layer function.  
D) ✗ End-to-end delivery is handled by Transport layer.  

**Correct:** A


#### 14. Which of the following statements about the OSI model’s interfaces and services are correct?  
A) ✓ Services describe what a layer does, not how it is accessed.  
B) ✓ Interfaces define how adjacent layers access each other’s services.  
C) ✗ Each layer has exactly one interface to the layer above and one to the layer below, not multiple.  
D) ✗ Peer layers communicate logically via protocols, not directly through interfaces.  

**Correct:** A, B


#### 15. What are some challenges addressed by the Network layer?  
A) ✓ Addressing the destination machine is a Network layer function.  
B) ✓ Routing packets through the best path is handled here.  
C) ✓ Managing congestion at intermediate nodes is a Network layer issue.  
D) ✗ Encrypting data is typically handled by Presentation or Application layers.  

**Correct:** A, B, C