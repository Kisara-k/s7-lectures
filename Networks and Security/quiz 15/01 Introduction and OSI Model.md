## 1 Introduction and OSI Model

## Questions

#### 1. What are the main strategies for coping with the complexity and rapid change in communications systems?  
A) Standardization of interfaces  
B) Increasing hardware speed  
C) Layering  
D) Modularization  

#### 2. Which of the following statements about the OSI Reference Model are true?  
A) It consists of five layers that each perform multiple unrelated functions  
B) It was developed by ISO in 1974 to provide a basis for network standardization  
C) Peer layers communicate directly without involving lower layers  
D) Each layer provides services to the layer above and relies on the layer below  

#### 3. In the OSI model, what is the role of protocols?  
A) Provide the physical transmission of bits  
B) Define how adjacent layers access each other  
C) Define the rules for communication between peer layers on different nodes  
D) Manage the interface between hardware and software  

#### 4. Which of the following are true about the layering principle in the OSI model?  
A) Layers should minimize information flow across boundaries  
B) Layers should be large enough to group unrelated functions for efficiency  
C) Each layer has exactly one interface to the layer above and one to the layer below  
D) Layer boundaries are chosen arbitrarily without regard to function  

#### 5. Which OSI layer is primarily responsible for establishing, maintaining, and terminating sessions between applications?  
A) Network  
B) Session  
C) Presentation  
D) Transport  

#### 6. What functions are typically handled by the Presentation layer?  
A) Data formatting and encryption  
B) Dialog control between applications  
C) Error detection and correction  
D) Routing and addressing  

#### 7. Which of the following are key functions of the Data Link layer?  
A) Framing  
B) End-to-end delivery  
C) Error detection and correction  
D) Flow control  

#### 8. The Network layer is responsible for which of the following?  
A) Establishing and terminating connections between hosts  
B) Error-free transmission across a single link  
C) Routing and congestion control  
D) Delivery of packets from source to destination across multiple networks  

#### 9. How does the Transport layer differ from the Data Link layer?  
A) Transport layer operates only on physical connections, Data Link layer operates on logical connections  
B) Transport layer provides end-to-end delivery across networks, Data Link layer only across a single link  
C) Transport layer manages flow control and multiplexing, Data Link layer does not  
D) Transport layer handles framing and error detection, Data Link layer does not  

#### 10. Which of the following are true about the Session layer?  
A) It is widely used in most modern network implementations  
B) It manages dialog control such as half- and full-duplex communication  
C) It formats data for transmission  
D) It handles synchronization and recovery management  

#### 11. Why is the TCP/IP model considered less complex than the OSI model?  
A) It excludes the physical, session, and presentation layers explicitly  
B) It uses fewer layers but provides the same functionality  
C) It does not require standardization of interfaces  
D) It combines session and presentation functions into other layers  

#### 12. Which of the following are reasons for TCP/IP’s widespread adoption?  
A) Has consistent APIs across implementations  
B) Has a strong track record and supports the Internet and WWW  
C) Is more complex and feature-rich than OSI  
D) Runs on a wide variety of hardware platforms  

#### 13. In the OSI model, what is the primary purpose of the Physical layer?  
A) Managing end-to-end delivery  
B) Routing packets between hosts  
C) Encoding and transmitting raw bits across a physical medium  
D) Providing error-free transmission across a link  

#### 14. Which of the following statements about the OSI model’s interfaces and services are correct?  
A) Peer layers communicate directly through their interfaces  
B) Each layer has multiple interfaces to the layer above and below  
C) Services describe what a layer does, not how it is accessed  
D) Interfaces define how adjacent layers access each other’s services  

#### 15. What are some challenges addressed by the Network layer?  
A) Encrypting data for secure transmission  
B) Addressing the destination machine  
C) Managing congestion at intermediate nodes  
D) Routing packets through the best path  



<br>

## Answers

#### 1. What are the main strategies for coping with the complexity and rapid change in communications systems?  
A) ✓ Standardization of interfaces ensures interoperability between components.  
B) ✗ Increasing hardware speed does not address architectural complexity or change.  
C) ✓ Layering organizes functions into separate levels to manage complexity.  
D) ✓ Modularization helps break down complex systems into manageable parts.  

**Correct:** A, C, D


#### 2. Which of the following statements about the OSI Reference Model are true?  
A) ✗ The OSI model has seven layers, each with well-defined, related functions.  
B) ✓ ISO developed the OSI model in 1974 for standardization purposes.  
C) ✗ Peer layers communicate logically via lower layers, not directly.  
D) ✓ Each layer provides services to the layer above and relies on the layer below.  

**Correct:** B, D


#### 3. In the OSI model, what is the role of protocols?  
A) ✗ Physical transmission of bits is handled by the Physical layer, not protocols.  
B) ✗ Defining how adjacent layers access each other is the role of interfaces, not protocols.  
C) ✓ Protocols define rules for communication between peer layers on different nodes.  
D) ✗ Managing hardware-software interface is not the role of protocols.  

**Correct:** C


#### 4. Which of the following are true about the layering principle in the OSI model?  
A) ✓ Minimizing information flow across boundaries reduces complexity and dependencies.  
B) ✗ Layers should avoid grouping unrelated functions to maintain clarity.  
C) ✓ Each layer has one interface to the layer above and one to the layer below.  
D) ✗ Layer boundaries are chosen carefully based on function, not arbitrarily.  

**Correct:** A, C


#### 5. Which OSI layer is primarily responsible for establishing, maintaining, and terminating sessions between applications?  
A) ✗ Network layer handles routing and addressing, not sessions.  
B) ✓ Session layer manages dialog control and session establishment.  
C) ✗ Presentation layer handles data formatting, not session control.  
D) ✗ Transport layer handles end-to-end delivery, not session management.  

**Correct:** B


#### 6. What functions are typically handled by the Presentation layer?  
A) ✓ Data formatting and encryption are key Presentation layer functions.  
B) ✗ Dialog control is a Session layer function.  
C) ✗ Error detection and correction belong to Data Link and Transport layers.  
D) ✗ Routing and addressing are Network layer functions.  

**Correct:** A


#### 7. Which of the following are key functions of the Data Link layer?  
A) ✓ Framing is a core Data Link layer function.  
B) ✗ End-to-end delivery is a Transport layer responsibility.  
C) ✓ Error detection and correction are handled at this layer.  
D) ✓ Flow control is managed to prevent overwhelming the receiver.  

**Correct:** A, C, D


#### 8. The Network layer is responsible for which of the following?  
A) ✗ Connection establishment is handled by Transport layer.  
B) ✗ Error-free transmission across a single link is Data Link layer’s job.  
C) ✓ Routing and congestion control are key Network layer issues.  
D) ✓ Delivering packets across multiple networks is the Network layer’s main role.  

**Correct:** C, D


#### 9. How does the Transport layer differ from the Data Link layer?  
A) ✗ Transport operates on logical connections, not just physical ones.  
B) ✓ Transport provides end-to-end delivery across networks; Data Link is link-to-link.  
C) ✓ Transport manages flow control and multiplexing across multiple connections.  
D) ✗ Framing and error detection are primarily Data Link functions.  

**Correct:** B, C


#### 10. Which of the following are true about the Session layer?  
A) ✗ It is not widely used in many modern systems.  
B) ✓ It manages dialog control such as half- and full-duplex communication.  
C) ✗ Data formatting is a Presentation layer function.  
D) ✓ It handles synchronization and recovery management.  

**Correct:** B, D


#### 11. Why is the TCP/IP model considered less complex than the OSI model?  
A) ✓ TCP/IP excludes physical, session, and presentation layers explicitly.  
B) ✗ TCP/IP does not have fewer layers but merges some functions.  
C) ✗ TCP/IP still requires standardization of interfaces.  
D) ✓ Session and Presentation functions are combined into other layers in TCP/IP.  

**Correct:** A, D


#### 12. Which of the following are reasons for TCP/IP’s widespread adoption?  
A) ✓ Has consistent APIs across implementations.  
B) ✓ Has a strong track record and supports the Internet and WWW.  
C) ✗ TCP/IP is less complex, not more complex than OSI.  
D) ✓ Runs on a wide variety of hardware platforms.  

**Correct:** A, B, D


#### 13. In the OSI model, what is the primary purpose of the Physical layer?  
A) ✗ End-to-end delivery is handled by Transport layer.  
B) ✗ Routing packets is a Network layer function.  
C) ✓ Encoding and transmitting raw bits across a physical medium.  
D) ✗ Error-free transmission is Data Link layer’s responsibility.  

**Correct:** C


#### 14. Which of the following statements about the OSI model’s interfaces and services are correct?  
A) ✗ Peer layers communicate logically via protocols, not directly through interfaces.  
B) ✗ Each layer has exactly one interface to the layer above and one to the layer below, not multiple.  
C) ✓ Services describe what a layer does, not how it is accessed.  
D) ✓ Interfaces define how adjacent layers access each other’s services.  

**Correct:** C, D


#### 15. What are some challenges addressed by the Network layer?  
A) ✗ Encrypting data is typically handled by Presentation or Application layers.  
B) ✓ Addressing the destination machine is a Network layer function.  
C) ✓ Managing congestion at intermediate nodes is a Network layer issue.  
D) ✓ Routing packets through the best path is handled here.  

**Correct:** B, C, D