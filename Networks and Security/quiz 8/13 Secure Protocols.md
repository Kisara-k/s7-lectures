## 13 Secure Protocols

## Questions

#### 1. Which of the following are primary security requirements motivated by network security threats?  
A) Non-repudiation  
B) Availability  
C) Integrity  
D) Privacy  
E) Scalability  

#### 2. In a man-in-the-middle attack, which security requirements are most directly compromised?  
A) Integrity and Authentication  
B) Non-repudiation and Privacy  
C) Availability and Integrity  
D) Privacy and Availability  

#### 3. Which of the following statements about secret key cryptography are true?  
A) Cryptographic checksums can provide message integrity with less processing than full encryption.  
B) The same key is used for both encryption and decryption.  
C) Secret keys are typically distributed publicly to ensure scalability.  
D) It inherently provides non-repudiation without additional mechanisms.  

#### 4. Regarding IPsec, which of the following are correct descriptions of its features or components?  
A) It operates only in transport mode, encrypting only the payload of IP packets.  
B) Encapsulating Security Payload (ESP) can provide both encryption and optional authentication data.  
C) Authentication Header (AH) provides integrity and authentication but does not encrypt the payload.  
D) Security Associations (SAs) are simplex connections and two are needed for bidirectional communication.  

#### 5. Which of the following are true about firewalls and their operation in network security?  
A) Firewalls eliminate the need for encryption in secure communication channels.  
B) Circuit-level gateways relay TCP segments without allowing direct client-to-server connections.  
C) Application-level gateways can perform authentication and filter messages between client and server.  
D) IP-layer filtering firewalls can inspect and filter packet payload contents.  

#### 6. Which of the following statements about cryptographic hash functions and message authentication codes (MACs) are accurate?  
A) Keyed hashes (MACs) provide both integrity and authentication of messages.  
B) Hashes can protect against replay attacks if combined with sequence numbers.  
C) Hash functions always require a secret key to compute the hash value.  
D) MD5 and SHA-1 are examples of keyed hash algorithms used in network security.  

#### 7. In the TLS handshake protocol, which of the following occur during session setup?  
A) Establishment of a shared secret between client and server.  
B) Transmission of the entire plaintext message for verification.  
C) Negotiation of encryption algorithm and key generation method.  
D) Authentication of peers using public key algorithms.  

#### 8. Which of the following statements about denial of service (DoS) attacks and their countermeasures are correct?  
A) DoS attacks aim to overload server resources, denying service to legitimate clients.  
B) Firewalls and intrusion detection systems can be effective countermeasures against DoS attacks.  
C) Distributed DoS attacks involve a single attacker using one compromised machine.  
D) Availability is the primary security requirement targeted by DoS attacks.  



<br>

## Answers

#### 1. Which of the following are primary security requirements motivated by network security threats?  
A) ✓ Non-repudiation prevents senders from denying message transmission.  
B) ✓ Availability ensures information and services are accessible when needed.  
C) ✓ Integrity ensures messages are not altered during transmission.  
D) ✓ Privacy is a fundamental requirement to keep information readable only by intended recipients.  
E) ✗ Scalability is not a core security requirement; it relates to system performance.  

**Correct:** A, B, C, D


#### 2. In a man-in-the-middle attack, which security requirements are most directly compromised?  
A) ✓ Integrity is compromised because messages can be altered; Authentication is broken as attacker impersonates parties.  
B) ✗ Non-repudiation and Privacy are important but not the main targets in man-in-the-middle.  
C) ✗ Availability is not the main concern in this attack type.  
D) ✗ Privacy and Availability are affected in other attacks but not the primary focus here.  

**Correct:** A


#### 3. Which of the following statements about secret key cryptography are true?  
A) ✓ Cryptographic checksums (hashes) provide integrity with less processing than full encryption.  
B) ✓ Secret key cryptography uses the same key for encryption and decryption.  
C) ✗ Secret keys must be kept secret; public distribution defeats their purpose.  
D) ✗ Non-repudiation requires asymmetric cryptography or additional mechanisms, not inherent in secret key methods.  

**Correct:** A, B


#### 4. Regarding IPsec, which of the following are correct descriptions of its features or components?  
A) ✗ IPsec operates in both transport and tunnel modes; tunnel mode encrypts entire packets.  
B) ✓ ESP provides encryption and optional authentication data.  
C) ✓ Authentication Header provides integrity and authentication but does not encrypt payload.  
D) ✓ Security Associations are simplex; two SAs are needed for bidirectional communication.  

**Correct:** B, C, D


#### 5. Which of the following are true about firewalls and their operation in network security?  
A) ✗ Firewalls do not replace encryption; they complement secure communication channels.  
B) ✓ Circuit-level gateways relay TCP segments and prevent direct client-server connections.  
C) ✓ Application-level gateways perform authentication and filter messages between client and server.  
D) ✗ IP-layer filtering cannot inspect payload contents; it filters based on header fields only.  

**Correct:** B, C


#### 6. Which of the following statements about cryptographic hash functions and message authentication codes (MACs) are accurate?  
A) ✓ Keyed hashes (MACs) provide both integrity and authentication.  
B) ✓ Sequence numbers combined with hashes can protect against replay attacks.  
C) ✗ Hash functions do not always require a secret key; plain hashes are keyless, but MACs are keyed.  
D) ✗ MD5 and SHA-1 are standard hash algorithms; keyed versions exist but MD5 and SHA-1 themselves are not keyed hashes.  

**Correct:** A, B


#### 7. In the TLS handshake protocol, which of the following occur during session setup?  
A) ✓ Client and server establish a shared secret.  
B) ✗ Plaintext messages are not transmitted for verification; handshake uses encrypted exchanges.  
C) ✓ Encryption algorithm and key generation method are negotiated.  
D) ✓ Peers can authenticate each other using public key algorithms.  

**Correct:** A, C, D


#### 8. Which of the following statements about denial of service (DoS) attacks and their countermeasures are correct?  
A) ✓ DoS attacks overload server resources to deny service to legitimate users.  
B) ✓ Firewalls and intrusion detection systems can help mitigate DoS attacks.  
C) ✗ Distributed DoS attacks involve multiple compromised machines, not a single one.  
D) ✓ Availability is the primary security requirement targeted by DoS attacks.  

**Correct:** A, B, D