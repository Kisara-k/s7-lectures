## 13 Secure Protocols

## Questions

#### 1. Which of the following are primary security requirements motivated by network security threats?  
A) Privacy  
B) Integrity  
C) Scalability  
D) Non-repudiation  

#### 2. In a man-in-the-middle attack, which security requirements are most critically violated?  
A) Integrity  
B) Authentication  
C) Availability  
D) Non-repudiation  

#### 3. What are common countermeasures used to protect communication channels against eavesdropping and message tampering?  
A) Encryption  
B) Firewalls  
C) Cryptographic checksums and hashes  
D) Intrusion detection systems  

#### 4. Which of the following statements about substitution and transposition ciphers are true?  
A) Substitution ciphers replace each letter with another letter or numeral.  
B) Transposition ciphers rearrange the order of letters without changing the letters themselves.  
C) Both substitution and transposition ciphers are considered very secure against modern attacks.  
D) Frequency analysis can be used to break substitution ciphers.  

#### 5. Regarding secret key cryptography, which conditions contribute to making a cipher difficult to break?  
A) Large key space with many possible keys  
B) Easy derivation of the secret key from intercepted messages  
C) Algorithm complexity that prevents exhaustive key search  
D) Use of public keys for encryption  

#### 6. Which of the following are true about cryptographic checksums and hashes in network security?  
A) They provide message integrity by detecting alterations.  
B) They always provide message confidentiality.  
C) They can be keyed with a secret key to provide authentication.  
D) They replace the need for encryption in all cases.  

#### 7. What are the key differences between public key cryptography and secret key cryptography?  
A) Public key cryptography uses two different keys: one public and one private.  
B) Secret key cryptography uses the same key for encryption and decryption.  
C) Public key cryptography is generally faster than secret key cryptography.  
D) Secret key cryptography requires secure key distribution between parties.  

#### 8. Which of the following are valid security services provided by IPsec?  
A) Authentication  
B) Integrity  
C) Confidentiality (Privacy)  
D) Virus scanning  

#### 9. In IPsec, what is the role of a Security Association (SA)?  
A) It defines a logical simplex connection between two network-layer entities.  
B) It is used to negotiate firewall rules.  
C) It specifies cryptographic algorithms and keys to be used.  
D) It is a physical connection between two routers.  

#### 10. Which of the following statements about the IPsec Authentication Header (AH) are correct?  
A) AH provides integrity and authentication but does not encrypt the payload.  
B) AH is inserted between the IP header and the payload.  
C) AH encrypts the entire IP packet including headers.  
D) AH includes a sequence number to protect against replay attacks.  

#### 11. What are the characteristics of the Encapsulating Security Payload (ESP) in IPsec?  
A) ESP provides encryption of the payload for privacy.  
B) ESP always includes authentication data at the end of the packet.  
C) ESP can provide both integrity and confidentiality services.  
D) ESP encrypts the IP header to hide routing information.  

#### 12. Which of the following are true about firewalls and their operation?  
A) IP-layer filtering firewalls can inspect and filter packet payloads.  
B) Circuit-level gateways relay TCP segments between clients and servers without allowing direct connections.  
C) Application-level gateways can perform authentication and filter application-specific commands.  
D) Firewalls can prevent denial of service attacks by themselves without additional measures.  

#### 13. Regarding TLS (Transport Layer Security), which statements are accurate?  
A) TLS operates directly on top of TCP.  
B) TLS provides privacy through secret key encryption negotiated during the handshake.  
C) TLS handshake protocol can authenticate both client and server using public key cryptography.  
D) TLS encrypts IP headers to provide network layer security.  

#### 14. Which of the following are challenges in setting up a Security Association (SA) for IPsec?  
A) Agreeing on cryptographic algorithms and security services.  
B) Authenticating each other’s identity.  
C) Establishing a shared secret key securely.  
D) Automatically detecting and blocking all malware on the network.  

#### 15. Which of the following statements about replay attacks and their prevention are correct?  
A) Replay attacks involve resending captured valid messages to gain unauthorized access.  
B) Sequence numbers included in packets and covered by cryptographic hashes help prevent replay attacks.  
C) Replay attacks can be prevented by encrypting only the packet headers.  
D) Receivers maintain a window of acceptable sequence numbers to detect and reject replayed packets.



<br>

## Answers

#### 1. Which of the following are primary security requirements motivated by network security threats?  
A) ✓ Privacy is a fundamental requirement to keep information readable only by intended recipients.  
B) ✓ Integrity ensures messages are not altered during transmission.  
C) ✗ Scalability is not a core security requirement; it relates to system performance.  
D) ✓ Non-repudiation prevents senders from denying message transmission.  

**Correct:** A, B, D


#### 2. In a man-in-the-middle attack, which security requirements are most critically violated?  
A) ✓ Integrity is violated because the attacker can alter messages.  
B) ✓ Authentication is violated as the attacker impersonates both parties.  
C) ✗ Availability is not the primary concern in man-in-the-middle attacks.  
D) ✗ Non-repudiation is not directly violated by this attack type.  

**Correct:** A, B


#### 3. What are common countermeasures used to protect communication channels against eavesdropping and message tampering?  
A) ✓ Encryption protects privacy by making messages unreadable to eavesdroppers.  
B) ✗ Firewalls protect network borders but do not secure communication channels directly.  
C) ✓ Cryptographic checksums and hashes provide integrity and detect tampering.  
D) ✗ Intrusion detection systems monitor for attacks but do not secure the channel itself.  

**Correct:** A, C


#### 4. Which of the following statements about substitution and transposition ciphers are true?  
A) ✓ Substitution ciphers replace each letter or numeral with another.  
B) ✓ Transposition ciphers rearrange the order of letters without changing them.  
C) ✗ Both are easy to break with known plaintext or frequency analysis.  
D) ✓ Frequency analysis is effective against substitution ciphers.  

**Correct:** A, B, D


#### 5. Regarding secret key cryptography, which conditions contribute to making a cipher difficult to break?  
A) ✓ Large key space prevents exhaustive key search.  
B) ✗ Easy derivation of the key makes the cipher weak, not strong.  
C) ✓ Algorithm complexity and large key space make brute force impractical.  
D) ✗ Public keys are part of public key cryptography, not secret key cryptography.  

**Correct:** A, C


#### 6. Which of the following are true about cryptographic checksums and hashes in network security?  
A) ✓ They detect message alterations, providing integrity.  
B) ✗ They do not provide confidentiality; encryption is needed for that.  
C) ✓ Keyed hashes can authenticate the sender by using a secret key.  
D) ✗ They do not replace encryption when privacy is required.  

**Correct:** A, C


#### 7. What are the key differences between public key cryptography and secret key cryptography?  
A) ✓ Public key cryptography uses a public/private key pair.  
B) ✓ Secret key cryptography uses the same key for encryption and decryption.  
C) ✗ Public key cryptography is generally slower than secret key cryptography.  
D) ✓ Secret key cryptography requires secure key distribution between parties.  

**Correct:** A, B, D


#### 8. Which of the following are valid security services provided by IPsec?  
A) ✓ Authentication to verify sender identity.  
B) ✓ Integrity to ensure message is unaltered.  
C) ✓ Confidentiality by encrypting payloads.  
D) ✗ Virus scanning is not a function of IPsec.  

**Correct:** A, B, C


#### 9. In IPsec, what is the role of a Security Association (SA)?  
A) ✓ SA defines a logical simplex connection between two network entities.  
B) ✗ SA does not negotiate firewall rules.  
C) ✓ SA specifies cryptographic algorithms and keys.  
D) ✗ SA is a logical, not physical, connection.  

**Correct:** A, C


#### 10. Which of the following statements about the IPsec Authentication Header (AH) are correct?  
A) ✓ AH provides integrity and authentication but does not encrypt payload.  
B) ✓ AH is inserted between the IP header and the payload.  
C) ✗ AH does not encrypt the entire IP packet or headers.  
D) ✓ AH includes a sequence number to prevent replay attacks.  

**Correct:** A, B, D


#### 11. What are the characteristics of the Encapsulating Security Payload (ESP) in IPsec?  
A) ✓ ESP encrypts the payload to provide privacy.  
B) ✗ Authentication data is optional, not always included.  
C) ✓ ESP can provide both integrity and confidentiality.  
D) ✗ ESP does not encrypt the IP header; only the payload is encrypted.  

**Correct:** A, C


#### 12. Which of the following are true about firewalls and their operation?  
A) ✗ IP-layer filtering cannot inspect or filter packet payloads, only headers.  
B) ✓ Circuit-level gateways relay TCP segments without allowing direct client-server connections.  
C) ✓ Application-level gateways perform authentication and filter application commands.  
D) ✗ Firewalls alone cannot fully prevent DoS attacks; additional measures are needed.  

**Correct:** B, C


#### 13. Regarding TLS (Transport Layer Security), which statements are accurate?  
A) ✓ TLS operates on top of TCP.  
B) ✓ TLS provides privacy through secret key encryption negotiated during handshake.  
C) ✓ TLS handshake can authenticate both client and server using public key cryptography.  
D) ✗ TLS does not encrypt IP headers; it operates above the transport layer.  

**Correct:** A, B, C


#### 14. Which of the following are challenges in setting up a Security Association (SA) for IPsec?  
A) ✓ Agreeing on cryptographic algorithms and security services is essential.  
B) ✓ Authenticating each other’s identity is required.  
C) ✓ Establishing a shared secret key securely is difficult but necessary.  
D) ✗ Detecting and blocking malware is outside the scope of SA setup.  

**Correct:** A, B, C


#### 15. Which of the following statements about replay attacks and their prevention are correct?  
A) ✓ Replay attacks involve resending captured valid messages to gain unauthorized access.  
B) ✓ Sequence numbers covered by cryptographic hashes help prevent replay attacks.  
C) ✗ Encrypting only packet headers does not prevent replay attacks.  
D) ✓ Receivers maintain a window of acceptable sequence numbers to detect replays.  

**Correct:** A, B, D