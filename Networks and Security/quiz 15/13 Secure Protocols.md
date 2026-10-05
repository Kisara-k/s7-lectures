## 13 Secure Protocols

## Questions

#### 1. Which of the following are primary security requirements motivated by network security threats?  
A) Non-repudiation  
B) Integrity  
C) Privacy  
D) Scalability  

#### 2. In a man-in-the-middle attack, which security requirements are most critically violated?  
A) Non-repudiation  
B) Availability  
C) Integrity  
D) Authentication  

#### 3. What are common countermeasures used to protect communication channels against eavesdropping and message tampering?  
A) Cryptographic checksums and hashes  
B) Firewalls  
C) Encryption  
D) Intrusion detection systems  

#### 4. Which of the following statements about substitution and transposition ciphers are true?  
A) Transposition ciphers rearrange the order of letters without changing the letters themselves.  
B) Frequency analysis can be used to break substitution ciphers.  
C) Both substitution and transposition ciphers are considered very secure against modern attacks.  
D) Substitution ciphers replace each letter with another letter or numeral.  

#### 5. Regarding secret key cryptography, which conditions contribute to making a cipher difficult to break?  
A) Large key space with many possible keys  
B) Algorithm complexity that prevents exhaustive key search  
C) Use of public keys for encryption  
D) Easy derivation of the secret key from intercepted messages  

#### 6. Which of the following are true about cryptographic checksums and hashes in network security?  
A) They replace the need for encryption in all cases.  
B) They always provide message confidentiality.  
C) They can be keyed with a secret key to provide authentication.  
D) They provide message integrity by detecting alterations.  

#### 7. What are the key differences between public key cryptography and secret key cryptography?  
A) Secret key cryptography requires secure key distribution between parties.  
B) Secret key cryptography uses the same key for encryption and decryption.  
C) Public key cryptography uses two different keys: one public and one private.  
D) Public key cryptography is generally faster than secret key cryptography.  

#### 8. Which of the following are valid security services provided by IPsec?  
A) Integrity  
B) Virus scanning  
C) Confidentiality (Privacy)  
D) Authentication  

#### 9. In IPsec, what is the role of a Security Association (SA)?  
A) It is used to negotiate firewall rules.  
B) It is a physical connection between two routers.  
C) It specifies cryptographic algorithms and keys to be used.  
D) It defines a logical simplex connection between two network-layer entities.  

#### 10. Which of the following statements about the IPsec Authentication Header (AH) are correct?  
A) AH includes a sequence number to protect against replay attacks.  
B) AH encrypts the entire IP packet including headers.  
C) AH provides integrity and authentication but does not encrypt the payload.  
D) AH is inserted between the IP header and the payload.  

#### 11. What are the characteristics of the Encapsulating Security Payload (ESP) in IPsec?  
A) ESP provides encryption of the payload for privacy.  
B) ESP encrypts the IP header to hide routing information.  
C) ESP can provide both integrity and confidentiality services.  
D) ESP always includes authentication data at the end of the packet.  

#### 12. Which of the following are true about firewalls and their operation?  
A) IP-layer filtering firewalls can inspect and filter packet payloads.  
B) Application-level gateways can perform authentication and filter application-specific commands.  
C) Circuit-level gateways relay TCP segments between clients and servers without allowing direct connections.  
D) Firewalls can prevent denial of service attacks by themselves without additional measures.  

#### 13. Regarding TLS (Transport Layer Security), which statements are accurate?  
A) TLS encrypts IP headers to provide network layer security.  
B) TLS operates directly on top of TCP.  
C) TLS provides privacy through secret key encryption negotiated during the handshake.  
D) TLS handshake protocol can authenticate both client and server using public key cryptography.  

#### 14. Which of the following are challenges in setting up a Security Association (SA) for IPsec?  
A) Agreeing on cryptographic algorithms and security services.  
B) Authenticating each other’s identity.  
C) Automatically detecting and blocking all malware on the network.  
D) Establishing a shared secret key securely.  

#### 15. Which of the following statements about replay attacks and their prevention are correct?  
A) Replay attacks involve resending captured valid messages to gain unauthorized access.  
B) Sequence numbers included in packets and covered by cryptographic hashes help prevent replay attacks.  
C) Replay attacks can be prevented by encrypting only the packet headers.  
D) Receivers maintain a window of acceptable sequence numbers to detect and reject replayed packets.  



<br>

## Answers

#### 1. Which of the following are primary security requirements motivated by network security threats?  
A) ✓ Non-repudiation prevents senders from denying message transmission.  
B) ✓ Integrity ensures messages are not altered during transmission.  
C) ✓ Privacy is a fundamental requirement to keep information readable only by intended recipients.  
D) ✗ Scalability is not a core security requirement; it relates to system performance.  

**Correct:** A, B, C


#### 2. In a man-in-the-middle attack, which security requirements are most critically violated?  
A) ✗ Non-repudiation is not directly violated by this attack type.  
B) ✗ Availability is not the primary concern in man-in-the-middle attacks.  
C) ✓ Integrity is violated because the attacker can alter messages.  
D) ✓ Authentication is violated as the attacker impersonates both parties.  

**Correct:** C, D


#### 3. What are common countermeasures used to protect communication channels against eavesdropping and message tampering?  
A) ✓ Cryptographic checksums and hashes provide integrity and detect tampering.  
B) ✗ Firewalls protect network borders but do not secure communication channels directly.  
C) ✓ Encryption protects privacy by making messages unreadable to eavesdroppers.  
D) ✗ Intrusion detection systems monitor for attacks but do not secure the channel itself.  

**Correct:** A, C


#### 4. Which of the following statements about substitution and transposition ciphers are true?  
A) ✓ Transposition ciphers rearrange the order of letters without changing them.  
B) ✓ Frequency analysis is effective against substitution ciphers.  
C) ✗ Both are easy to break with known plaintext or frequency analysis.  
D) ✓ Substitution ciphers replace each letter or numeral with another.  

**Correct:** A, B, D


#### 5. Regarding secret key cryptography, which conditions contribute to making a cipher difficult to break?  
A) ✓ Large key space prevents exhaustive key search.  
B) ✓ Algorithm complexity and large key space make brute force impractical.  
C) ✗ Public keys are part of public key cryptography, not secret key cryptography.  
D) ✗ Easy derivation of the key makes the cipher weak, not strong.  

**Correct:** A, B


#### 6. Which of the following are true about cryptographic checksums and hashes in network security?  
A) ✗ They do not replace encryption when privacy is required.  
B) ✗ They do not provide confidentiality; encryption is needed for that.  
C) ✓ Keyed hashes can authenticate the sender by using a secret key.  
D) ✓ They detect message alterations, providing integrity.  

**Correct:** C, D


#### 7. What are the key differences between public key cryptography and secret key cryptography?  
A) ✓ Secret key cryptography requires secure key distribution between parties.  
B) ✓ Secret key cryptography uses the same key for encryption and decryption.  
C) ✓ Public key cryptography uses a public/private key pair.  
D) ✗ Public key cryptography is generally slower than secret key cryptography.  

**Correct:** A, B, C


#### 8. Which of the following are valid security services provided by IPsec?  
A) ✓ Integrity to ensure message is unaltered.  
B) ✗ Virus scanning is not a function of IPsec.  
C) ✓ Confidentiality by encrypting payloads.  
D) ✓ Authentication to verify sender identity.  

**Correct:** A, C, D


#### 9. In IPsec, what is the role of a Security Association (SA)?  
A) ✗ SA does not negotiate firewall rules.  
B) ✗ SA is a logical, not physical, connection.  
C) ✓ SA specifies cryptographic algorithms and keys.  
D) ✓ SA defines a logical simplex connection between two network entities.  

**Correct:** C, D


#### 10. Which of the following statements about the IPsec Authentication Header (AH) are correct?  
A) ✓ AH includes a sequence number to prevent replay attacks.  
B) ✗ AH does not encrypt the entire IP packet or headers.  
C) ✓ AH provides integrity and authentication but does not encrypt payload.  
D) ✓ AH is inserted between the IP header and the payload.  

**Correct:** A, C, D


#### 11. What are the characteristics of the Encapsulating Security Payload (ESP) in IPsec?  
A) ✓ ESP encrypts the payload to provide privacy.  
B) ✗ ESP does not encrypt the IP header; only the payload is encrypted.  
C) ✓ ESP can provide both integrity and confidentiality.  
D) ✗ Authentication data is optional, not always included.  

**Correct:** A, C


#### 12. Which of the following are true about firewalls and their operation?  
A) ✗ IP-layer filtering cannot inspect or filter packet payloads, only headers.  
B) ✓ Application-level gateways perform authentication and filter application commands.  
C) ✓ Circuit-level gateways relay TCP segments without allowing direct client-server connections.  
D) ✗ Firewalls alone cannot fully prevent DoS attacks; additional measures are needed.  

**Correct:** B, C


#### 13. Regarding TLS (Transport Layer Security), which statements are accurate?  
A) ✗ TLS does not encrypt IP headers; it operates above the transport layer.  
B) ✓ TLS operates on top of TCP.  
C) ✓ TLS provides privacy through secret key encryption negotiated during handshake.  
D) ✓ TLS handshake can authenticate both client and server using public key cryptography.  

**Correct:** B, C, D


#### 14. Which of the following are challenges in setting up a Security Association (SA) for IPsec?  
A) ✓ Agreeing on cryptographic algorithms and security services is essential.  
B) ✓ Authenticating each other’s identity is required.  
C) ✗ Detecting and blocking malware is outside the scope of SA setup.  
D) ✓ Establishing a shared secret key securely is difficult but necessary.  

**Correct:** A, B, D


#### 15. Which of the following statements about replay attacks and their prevention are correct?  
A) ✓ Replay attacks involve resending captured valid messages to gain unauthorized access.  
B) ✓ Sequence numbers covered by cryptographic hashes help prevent replay attacks.  
C) ✗ Encrypting only packet headers does not prevent replay attacks.  
D) ✓ Receivers maintain a window of acceptable sequence numbers to detect replays.  

**Correct:** A, B, D