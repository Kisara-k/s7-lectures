## 13 Secure Protocols

## Study Notes

### 1. 🔐 Introduction to Network Security and Secure Protocols

In today’s world, computers and networks are everywhere, enabling powerful services and applications. However, this connectivity also opens the door to many security risks. Network security is about protecting computer systems and data from unauthorized access, attacks, and damage. This involves using various tools and techniques such as firewalls, security protocols, and best practices to defend against threats.

Secure protocols are special sets of rules that ensure communication over networks is safe. They help protect data privacy, verify identities, maintain data integrity, and ensure that services remain available. This study note will guide you through the key concepts of network security threats, requirements, countermeasures, and the cryptographic methods used in secure protocols.


### 2. 🕵️‍♂️ Network Security Threats: What Are We Protecting Against?

Network security threats are the different ways attackers try to compromise systems or data. Understanding these threats helps us design better defenses.

- **Eavesdropping:** Attackers listen in on network traffic to capture sensitive information like passwords or messages. This is often done using tools called packet sniffers.
- **Man-in-the-Middle (MitM) Attacks:** An attacker secretly intercepts and possibly alters communication between two parties, pretending to be each to the other. This can lead to stolen data or hijacked sessions.
- **Imposters:** Attackers pretend to be legitimate users or servers to gain unauthorized access. For example, IP spoofing involves sending packets with fake source addresses.
- **Denial of Service (DoS) Attacks:** Attackers overwhelm a server with excessive requests, making it unavailable to legitimate users. When multiple compromised machines coordinate this, it’s called a Distributed Denial of Service (DDoS) attack.
- **Malicious Code:** Viruses, worms, and other harmful software can infect systems, spread across networks, and cause damage or steal information.

Each threat targets different aspects of security, such as privacy, authentication, integrity, non-repudiation, and availability.


### 3. 🛡️ Security Requirements: What Do We Need to Protect?

To counter these threats, network security focuses on five main requirements:

- **Privacy:** Ensuring that information is only accessible to the intended recipient. This prevents eavesdropping and unauthorized access.
- **Integrity:** Guaranteeing that the data received is exactly what was sent, without any tampering or alteration during transmission.
- **Authentication:** Verifying the identity of the sender or receiver so that parties can trust who they are communicating with.
- **Non-Repudiation:** Preventing a sender from denying that they sent a message. This is important for accountability.
- **Availability:** Ensuring that information and services are accessible when needed, even under attack (e.g., DoS attacks).

These requirements guide the design of security protocols and countermeasures.


### 4. 🔑 Cryptography: The Foundation of Secure Communication

Cryptography is the science of protecting information by transforming it into a secure format. It is the backbone of secure protocols.

- **Encryption:** Converts readable data (plaintext) into an unreadable format (ciphertext) using an algorithm called a cipher and a secret key.
- **Decryption:** The reverse process, turning ciphertext back into plaintext using the same or a related key.
- **Secret Key Cryptography (Symmetric):** The same key is used for both encryption and decryption. Both sender and receiver must keep this key secret.
- **Public Key Cryptography (Asymmetric):** Uses a pair of keys — a public key for encryption (known to everyone) and a private key for decryption (kept secret by the owner).

#### Types of Ciphers

- **Substitution Cipher:** Each letter or number is replaced by another. For example, "security" might be encrypted as "hvxfirgb". These are easy to break by analyzing letter frequency.
- **Transposition Cipher:** The letters are rearranged according to a pattern. For example, "security" becomes "esuciryt". These are also relatively easy to break if the pattern is known.

#### What Makes a Good Cipher?

- Easy to implement and use on a large scale.
- Difficult to break, meaning it has a very large key space.
- The secret key should be hard to guess or derive, even if attackers have many examples of plaintext and ciphertext.

Examples of strong secret key algorithms include DES (Data Encryption Standard), Triple DES, and AES (Advanced Encryption Standard).


### 5. 🔍 Authentication and Integrity with Cryptography

Besides privacy, cryptography also helps with:

- **Integrity:** Ensuring data hasn’t been altered. This is done by creating cryptographic checksums or hashes — fixed-size values calculated from the message content.
- **Authentication:** Verifying identities by using secret keys to encrypt or decrypt challenges (random numbers called nonces). If the correct response is received, the identity is confirmed.

#### Cryptographic Checksums and Hashes

- A hash function takes a message and produces a fixed-length string (hash).
- The hash depends on the message and a secret key.
- The receiver recalculates the hash and compares it to the received one. If they match, the message is authentic and unaltered.

Common hashing algorithms include:

- **MD5:** Produces a 128-bit hash.
- **Keyed MD5:** Adds a secret key to the message before hashing for authentication.
- **SHA-1:** Produces a 160-bit hash and is more secure than MD5.


### 6. 🌐 Secure Protocols in Network Layers

Security can be applied at different layers of the network stack:

- **Data Link Layer:** Security between directly connected devices (e.g., Wi-Fi encryption).
- **IP Layer:** Security between IP addresses, such as IPsec, which provides authentication, integrity, and encryption.
- **Transport Layer:** Security between transport and application layers, such as SSL/TLS, which secures web browsing, email, and other protocols.

#### IPsec (Internet Protocol Security)

IPsec is a suite of protocols that secure IP communications by authenticating and encrypting each IP packet.

- **Security Association (SA):** A logical connection defining security parameters like keys and algorithms.
- **Authentication Header (AH):** Provides integrity and authentication but does not encrypt data.
- **Encapsulating Security Payload (ESP):** Provides encryption (privacy), integrity, and authentication.
- **Transport Mode:** Protects the payload of the IP packet.
- **Tunnel Mode:** Encapsulates the entire IP packet inside a new packet, encrypting the original header and payload, useful for VPNs.

IPsec also includes mechanisms to prevent replay attacks by using sequence numbers and windows of accepted packets.


### 7. 🔥 Firewalls and Border Security

Firewalls act as gatekeepers between internal networks and the Internet, controlling access and filtering traffic based on rules.

- **Packet Filtering:** Blocks or allows packets based on IP addresses, ports, or protocol types.
- **Circuit-Level Gateways:** Relay TCP connections without allowing direct client-server connections.
- **Application-Level Gateways (Proxies):** Intercept and inspect application data, perform authentication, and enforce policies.

Firewalls help prevent unauthorized access and attacks from outside the network.


### 8. 🔒 Secure Sockets Layer (SSL) and Transport Layer Security (TLS)

SSL and TLS are protocols that provide secure communication over the Internet, especially for web browsing, email, and other applications.

- Operate on top of TCP.
- Provide privacy through encryption and integrity through message authentication codes.
- Use a handshake protocol to negotiate encryption algorithms, authenticate parties, and establish shared secret keys.
- TLS is the standardized successor to SSL with improved security.

During the handshake:

- Client and server agree on protocol version and cipher suite.
- They authenticate each other using public key cryptography.
- They establish a shared secret key for encrypting the session.


### 9. 📝 Summary

Network security is essential to protect data and services from a wide range of threats like eavesdropping, impersonation, DoS attacks, and malicious code. To defend against these, security protocols enforce requirements such as privacy, integrity, authentication, non-repudiation, and availability.

Cryptography is the core technology enabling secure communication, using secret key and public key methods to encrypt data, verify identities, and ensure data integrity. Protocols like IPsec and TLS implement these cryptographic techniques at different layers of the network stack to provide secure, reliable communication.

Firewalls and other border security measures complement these protocols by controlling access and monitoring traffic at network boundaries.

Understanding these concepts and how they work together is crucial for building and maintaining secure networks in today’s interconnected world.