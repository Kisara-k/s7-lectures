## 13 Secure Protocols

## Questions

#### 1. Which of the following are primary security requirements motivated by network security threats?  
A) Privacy  
B) Integrity  
C) Scalability  
D) Non-repudiation  
E) Availability  

#### 2. In a man-in-the-middle attack, which security requirements are most directly compromised?  
A) Privacy and Availability  
B) Integrity and Authentication  
C) Non-repudiation and Privacy  
D) Availability and Integrity  

#### 3. Which of the following statements about secret key cryptography are true?  
A) The same key is used for both encryption and decryption.  
B) It inherently provides non-repudiation without additional mechanisms.  
C) Cryptographic checksums can provide message integrity with less processing than full encryption.  
D) Secret keys are typically distributed publicly to ensure scalability.  

#### 4. Regarding IPsec, which of the following are correct descriptions of its features or components?  
A) It operates only in transport mode, encrypting only the payload of IP packets.  
B) Security Associations (SAs) are simplex connections and two are needed for bidirectional communication.  
C) Authentication Header (AH) provides integrity and authentication but does not encrypt the payload.  
D) Encapsulating Security Payload (ESP) can provide both encryption and optional authentication data.  

#### 5. Which of the following are true about firewalls and their operation in network security?  
A) Circuit-level gateways relay TCP segments without allowing direct client-to-server connections.  
B) IP-layer filtering firewalls can inspect and filter packet payload contents.  
C) Application-level gateways can perform authentication and filter messages between client and server.  
D) Firewalls eliminate the need for encryption in secure communication channels.  

#### 6. Which of the following statements about cryptographic hash functions and message authentication codes (MACs) are accurate?  
A) Hash functions always require a secret key to compute the hash value.  
B) Keyed hashes (MACs) provide both integrity and authentication of messages.  
C) Hashes can protect against replay attacks if combined with sequence numbers.  
D) MD5 and SHA-1 are examples of keyed hash algorithms used in network security.  

#### 7. In the TLS handshake protocol, which of the following occur during session setup?  
A) Negotiation of encryption algorithm and key generation method.  
B) Establishment of a shared secret between client and server.  
C) Transmission of the entire plaintext message for verification.  
D) Authentication of peers using public key algorithms.  

#### 8. Which of the following statements about denial of service (DoS) attacks and their countermeasures are correct?  
A) DoS attacks aim to overload server resources, denying service to legitimate clients.  
B) Distributed DoS attacks involve a single attacker using one compromised machine.  
C) Availability is the primary security requirement targeted by DoS attacks.  
D) Firewalls and intrusion detection systems can be effective countermeasures against DoS attacks.



<br>

## Answers

#### 1. Which of the following are primary security requirements motivated by network security threats?  
A) ✓ Privacy is a fundamental requirement to keep information readable only by intended recipients.  
B) ✓ Integrity ensures messages are not altered during transmission.  
C) ✗ Scalability is not a core security requirement; it relates to system performance.  
D) ✓ Non-repudiation prevents senders from denying message transmission.  
E) ✓ Availability ensures information and services are accessible when needed.  

**Correct:** A, B, D, E


#### 2. In a man-in-the-middle attack, which security requirements are most directly compromised?  
A) ✗ Privacy and Availability are affected in other attacks but not the primary focus here.  
B) ✓ Integrity is compromised because messages can be altered; Authentication is broken as attacker impersonates parties.  
C) ✗ Non-repudiation and Privacy are important but not the main targets in man-in-the-middle.  
D) ✗ Availability is not the main concern in this attack type.  

**Correct:** B


#### 3. Which of the following statements about secret key cryptography are true?  
A) ✓ Secret key cryptography uses the same key for encryption and decryption.  
B) ✗ Non-repudiation requires asymmetric cryptography or additional mechanisms, not inherent in secret key methods.  
C) ✓ Cryptographic checksums (hashes) provide integrity with less processing than full encryption.  
D) ✗ Secret keys must be kept secret; public distribution defeats their purpose.  

**Correct:** A, C


#### 4. Regarding IPsec, which of the following are correct descriptions of its features or components?  
A) ✗ IPsec operates in both transport and tunnel modes; tunnel mode encrypts entire packets.  
B) ✓ Security Associations are simplex; two SAs are needed for bidirectional communication.  
C) ✓ Authentication Header provides integrity and authentication but does not encrypt payload.  
D) ✓ ESP provides encryption and optional authentication data.  

**Correct:** B, C, D


#### 5. Which of the following are true about firewalls and their operation in network security?  
A) ✓ Circuit-level gateways relay TCP segments and prevent direct client-server connections.  
B) ✗ IP-layer filtering cannot inspect payload contents; it filters based on header fields only.  
C) ✓ Application-level gateways perform authentication and filter messages between client and server.  
D) ✗ Firewalls do not replace encryption; they complement secure communication channels.  

**Correct:** A, C


#### 6. Which of the following statements about cryptographic hash functions and message authentication codes (MACs) are accurate?  
A) ✗ Hash functions do not always require a secret key; plain hashes are keyless, but MACs are keyed.  
B) ✓ Keyed hashes (MACs) provide both integrity and authentication.  
C) ✓ Sequence numbers combined with hashes can protect against replay attacks.  
D) ✗ MD5 and SHA-1 are standard hash algorithms; keyed versions exist but MD5 and SHA-1 themselves are not keyed hashes.  

**Correct:** B, C


#### 7. In the TLS handshake protocol, which of the following occur during session setup?  
A) ✓ Encryption algorithm and key generation method are negotiated.  
B) ✓ Client and server establish a shared secret.  
C) ✗ Plaintext messages are not transmitted for verification; handshake uses encrypted exchanges.  
D) ✓ Peers can authenticate each other using public key algorithms.  

**Correct:** A, B, D


#### 8. Which of the following statements about denial of service (DoS) attacks and their countermeasures are correct?  
A) ✓ DoS attacks overload server resources to deny service to legitimate users.  
B) ✗ Distributed DoS attacks involve multiple compromised machines, not a single one.  
C) ✓ Availability is the primary security requirement targeted by DoS attacks.  
D) ✓ Firewalls and intrusion detection systems can help mitigate DoS attacks.  

**Correct:** A, C, D