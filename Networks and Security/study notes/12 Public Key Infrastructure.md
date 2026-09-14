## 12 Public Key Infrastructure

## Study Notes

### 1. 🔐 Introduction to Cryptosystems

Cryptosystems are methods used to secure communication by transforming readable data (plaintext) into an unreadable format (ciphertext) and vice versa. There are two main types of cryptosystems:

- **Symmetric Cryptosystems (Private Key Cryptography)**
- **Asymmetric Cryptosystems (Public Key Cryptography)**

Understanding these two types is fundamental to grasping how secure communication works in modern digital systems.


### 2. 🔑 Symmetric Cryptosystems (Private Key)

Symmetric cryptosystems use the **same key** for both encryption (locking the message) and decryption (unlocking the message). This key is called the **secret key** or **shared secret** because both the sender and receiver must have it and keep it confidential.

#### How It Works:
- Both parties share the same secret key.
- The sender encrypts the message using this key.
- The receiver decrypts the message using the same key.

#### Advantages:
- **Speed:** Symmetric encryption and decryption are very fast, making them suitable for encrypting large amounts of data.
- **Security with Large Key Space:** If the key is long and complex enough, it becomes very difficult for attackers to guess or break the key.

#### Disadvantages:
- **Key Management Problem:** Every pair of users needs a unique secret key. For example, if there are N users, the number of keys required is N(N-1)/2. This grows very quickly and becomes hard to manage.
- **Secure Key Distribution:** The secret key must be shared securely before communication, which can be challenging.
- **Limited Security Services:** Symmetric cryptosystems provide **confidentiality** (keeping data secret) but do **not** provide **authentication** (verifying who sent the message) or **nonrepudiation** (preventing denial of sending).

#### Examples of Symmetric Algorithms:
- **Data Encryption Standard (DES)**
- **Triple-DES (3DES)**
- **RC4, RC5, RC6**
- **Advanced Encryption Standard (AES)**


### 3. 🗝️ Asymmetric Cryptosystems (Public Key)

Asymmetric cryptosystems use **two different keys**: a **public key** and a **private key**. These keys are mathematically linked but not identical.

#### How It Works:
- The **public key** is shared openly and can be known by anyone.
- The **private key** is kept secret by the owner.
- If a message is encrypted with the public key, only the private key can decrypt it.
- Conversely, if a message is encrypted with the private key (used in digital signatures), anyone with the public key can verify it.

#### Key Properties:
- The private key **cannot** be derived from the public key, ensuring security.
- If the private key is leaked, the entire system’s security is compromised.

#### Advantages:
- **Better Key Distribution:** No need to share secret keys securely beforehand.
- **Scalability:** Easier to manage keys as the number of users grows.
- **Provides Authentication and Nonrepudiation:** Because private keys are unique and secret, they can be used to prove identity and prevent denial of actions.

#### Disadvantages:
- **Slower Performance:** Asymmetric encryption is computationally intensive and slower than symmetric encryption.

#### Examples of Asymmetric Algorithms:
- **RSA**
- **Elliptic Curve Cryptosystem (ECC)**
- **Diffie-Hellman (key exchange)**
- **El Gamal**


### 4. 🏛️ Public Key Infrastructure (PKI) Overview

While asymmetric cryptography solves many problems, it introduces a new challenge: **How do you verify that a public key actually belongs to the person it claims to?** This is crucial because if an attacker can trick you into using their public key, they can intercept or alter your communication (a Man-in-the-Middle attack).

#### What is PKI?

PKI is a **framework** (not a single technology) designed to securely distribute and verify public keys. It combines software, hardware, policies, and procedures to enable secure communication among many users who may never have met.

#### PKI Provides:
- **Confidentiality:** Ensuring data is only accessible to authorized parties.
- **Access Control:** Restricting who can access certain information.
- **Integrity:** Ensuring data is not altered during transmission.
- **Authentication:** Verifying the identity of users.
- **Nonrepudiation:** Preventing users from denying their actions.


### 5. 🧾 Components of PKI

For PKI to work effectively, several components must work together:

#### Digital Certificates
- A **digital certificate** is like an electronic ID card.
- It contains the public key of an individual or entity along with identifying information (like a name or organization).
- It is **digitally signed** by a trusted third party called a **Certificate Authority (CA)**.
- This signature allows others to trust that the public key belongs to the person named in the certificate.

#### Certificate Authority (CA)
- A CA is a trusted organization or server that issues and manages digital certificates.
- When someone requests a certificate, the CA verifies their identity (often through a Registration Authority) and then issues the certificate.
- The CA also maintains the certificate during its lifetime and can revoke it if necessary.

#### Registration Authority (RA)
- The RA acts as a verifier for the CA.
- It confirms the identity of individuals requesting certificates.
- It cannot issue certificates itself but facilitates the process between the user and the CA.
- It also manages the lifecycle of certificates (renewal, revocation requests).

#### Directories
- PKI uses directories to store and distribute certificates and revocation lists so that users and systems can access them when needed.


### 6. 📜 Digital Certificates and Standards

Digital certificates follow a standard called **X.509**, which defines the format and fields of a certificate. These fields typically include:

- The public key
- The identity of the certificate holder (subject)
- The identity of the issuer (CA)
- Validity period (start and expiry dates)
- Digital signature of the CA


### 7. 🚫 Certificate Revocation and CRL

Sometimes certificates need to be revoked before they expire. Reasons include:

- The certificate was issued based on false information.
- The private key has been compromised or lost.

The CA maintains a **Certificate Revocation List (CRL)**, which is a regularly updated list of revoked certificates. Systems check this list to ensure they do not trust revoked certificates.


### 8. 🔄 PKI Terminology

Understanding PKI requires knowing some key terms:

- **Issuer:** The CA or entity that issues a digital certificate.
- **Subject:** The person or entity to whom the certificate is issued.
- **Target:** The person or entity whose certificate is being verified.
- **Principal:** Any entity (person, device, or system) that has a public key.
- **Verifier:** The entity that checks the validity of a certificate or certificate chain.


### 9. 🌐 Web Browsers and Digital Certificates

Web browsers come pre-configured with a list of trusted CAs. When you visit a secure website (HTTPS), the browser checks the website’s digital certificate against this list. If the certificate is valid and signed by a trusted CA, the browser establishes a secure connection.


### Summary

- **Symmetric cryptosystems** use one shared secret key, are fast but have key management challenges.
- **Asymmetric cryptosystems** use a public/private key pair, solve key distribution problems, and provide authentication but are slower.
- **PKI** is a comprehensive system that manages public keys and certificates to ensure secure communication.
- **Digital certificates** and **Certificate Authorities** are central to PKI, enabling trust in public keys.
- **Registration Authorities** verify identities before certificates are issued.
- **Certificate Revocation Lists** help maintain trust by listing invalid certificates.
- Web browsers rely on PKI to secure internet communications.