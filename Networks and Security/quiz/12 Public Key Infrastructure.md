## 12 Public Key Infrastructure

## Questions

#### 1. Which of the following statements correctly describe symmetric cryptosystems?  
A) The same key is used for both encryption and decryption.  
B) They provide confidentiality, authentication, and nonrepudiation.  
C) Key management becomes complex as the number of users increases.  
D) They use a pair of mathematically related public and private keys.  

#### 2. What are the main disadvantages of symmetric cryptosystems?  
A) They require a secure mechanism to deliver and store keys.  
B) They are slower than asymmetric cryptosystems.  
C) Each pair of users requires a unique key, leading to scalability issues.  
D) They cannot provide confidentiality.  

#### 3. Which of the following algorithms are examples of symmetric key cryptosystems?  
A) AES  
B) RSA  
C) DES  
D) Elliptic Curve Cryptosystem (ECC)  

#### 4. In asymmetric cryptosystems, which of the following are true?  
A) The public key is kept secret by the owner.  
B) The private key is mathematically related to the public key but cannot be derived from it.  
C) Encryption and decryption use the same key.  
D) The private key must be kept confidential to maintain security.  

#### 5. What are the advantages of asymmetric cryptosystems over symmetric ones?  
A) Faster encryption and decryption processes.  
B) Better key distribution and scalability.  
C) Ability to provide authentication and nonrepudiation.  
D) Requires fewer keys as the number of users increases.  

#### 6. Which of the following are examples of asymmetric cryptosystems?  
A) Diffie-Hellman  
B) Triple-DES (3DES)  
C) RSA  
D) RC4  

#### 7. What is the primary purpose of a Public Key Infrastructure (PKI)?  
A) To securely distribute and verify the authenticity of public keys.  
B) To replace symmetric cryptosystems entirely.  
C) To provide a framework of policies, protocols, and cryptographic mechanisms for secure communication.  
D) To store private keys for users.  

#### 8. Which of the following security services are provided by PKI?  
A) Confidentiality  
B) Access control  
C) Integrity  
D) Nonrepudiation  

#### 9. Which components are essential for the effective operation of a PKI?  
A) Digital Certificates  
B) Certificate Authorities (CAs)  
C) Registration Authorities (RAs)  
D) Symmetric keys  

#### 10. What information does a digital certificate typically contain?  
A) The public key of the individual.  
B) The private key of the individual.  
C) Identifying information about the certificate holder.  
D) The digital signature of a trusted Certificate Authority.  

#### 11. What role does a Certificate Authority (CA) play in PKI?  
A) Verifies the identity of individuals requesting certificates.  
B) Issues and digitally signs digital certificates.  
C) Maintains and updates the Certificate Revocation List (CRL).  
D) Acts as a broker between users and Registration Authorities.  

#### 12. Under which circumstances might a Certificate Authority revoke a digital certificate?  
A) The certificate was issued based on false credentials.  
B) The private key associated with the certificate has been compromised.  
C) The certificate holder requests a new certificate.  
D) The certificate has expired.  

#### 13. What is the function of a Registration Authority (RA) in PKI?  
A) Issues digital certificates directly to users.  
B) Confirms the identity of individuals requesting certificates.  
C) Initiates the certification process with the CA on behalf of users.  
D) Maintains the Certificate Revocation List (CRL).  

#### 14. Which of the following terms correctly match their PKI definitions?  
A) Issuer – The entity that issues a digital certificate.  
B) Subject – The entity that verifies a digital certificate.  
C) Principal – Any entity possessing a public key.  
D) Verifier – The entity evaluating a chain of certificates.  

#### 15. How do web browsers typically handle digital certificates?  
A) They accept any digital certificate regardless of the issuer.  
B) They are pre-configured to trust certificates signed by a list of known Certificate Authorities.  
C) They verify certificates by contacting the Registration Authority directly.  
D) They use the Certificate Revocation List (CRL) to check if a certificate is still valid.



<br>

## Answers

#### 1. Which of the following statements correctly describe symmetric cryptosystems?  
A) ✓ The same key is used for both encryption and decryption.  
B) ✗ They provide confidentiality, authentication, and nonrepudiation. (Only confidentiality is provided, not authentication or nonrepudiation.)  
C) ✓ Key management becomes complex as the number of users increases.  
D) ✗ They use a pair of mathematically related public and private keys. (This describes asymmetric cryptosystems.)  

**Correct:** A, C


#### 2. What are the main disadvantages of symmetric cryptosystems?  
A) ✓ They require a secure mechanism to deliver and store keys.  
B) ✗ They are slower than asymmetric cryptosystems. (Symmetric systems are faster.)  
C) ✓ Each pair of users requires a unique key, leading to scalability issues.  
D) ✗ They cannot provide confidentiality. (They do provide confidentiality.)  

**Correct:** A, C


#### 3. Which of the following algorithms are examples of symmetric key cryptosystems?  
A) ✓ AES is a symmetric key algorithm.  
B) ✗ RSA is an asymmetric algorithm.  
C) ✓ DES is a symmetric key algorithm.  
D) ✗ ECC is an asymmetric algorithm.  

**Correct:** A, C


#### 4. In asymmetric cryptosystems, which of the following are true?  
A) ✗ The public key is kept secret by the owner. (Public key is known to everyone.)  
B) ✓ The private key is mathematically related to the public key but cannot be derived from it.  
C) ✗ Encryption and decryption use the same key. (Different keys are used.)  
D) ✓ The private key must be kept confidential to maintain security.  

**Correct:** B, D


#### 5. What are the advantages of asymmetric cryptosystems over symmetric ones?  
A) ✗ Faster encryption and decryption processes. (They are slower.)  
B) ✓ Better key distribution and scalability.  
C) ✓ Ability to provide authentication and nonrepudiation.  
D) ✗ Requires fewer keys as the number of users increases. (Key management is easier but not necessarily fewer keys.)  

**Correct:** B, C


#### 6. Which of the following are examples of asymmetric cryptosystems?  
A) ✓ Diffie-Hellman is asymmetric.  
B) ✗ Triple-DES (3DES) is symmetric.  
C) ✓ RSA is asymmetric.  
D) ✗ RC4 is symmetric.  

**Correct:** A, C


#### 7. What is the primary purpose of a Public Key Infrastructure (PKI)?  
A) ✓ To securely distribute and verify the authenticity of public keys.  
B) ✗ To replace symmetric cryptosystems entirely. (PKI complements symmetric systems.)  
C) ✓ To provide a framework of policies, protocols, and cryptographic mechanisms for secure communication.  
D) ✗ To store private keys for users. (Private keys are kept by users, not PKI.)  

**Correct:** A, C


#### 8. Which of the following security services are provided by PKI?  
A) ✓ Confidentiality  
B) ✓ Access control  
C) ✓ Integrity  
D) ✓ Nonrepudiation  

**Correct:** A, B, C, D


#### 9. Which components are essential for the effective operation of a PKI?  
A) ✓ Digital Certificates  
B) ✓ Certificate Authorities (CAs)  
C) ✓ Registration Authorities (RAs)  
D) ✗ Symmetric keys (Not a PKI component)  

**Correct:** A, B, C


#### 10. What information does a digital certificate typically contain?  
A) ✓ The public key of the individual.  
B) ✗ The private key of the individual. (Private key is never included.)  
C) ✓ Identifying information about the certificate holder.  
D) ✓ The digital signature of a trusted Certificate Authority.  

**Correct:** A, C, D


#### 11. What role does a Certificate Authority (CA) play in PKI?  
A) ✗ Verifies the identity of individuals requesting certificates. (This is the RA’s role.)  
B) ✓ Issues and digitally signs digital certificates.  
C) ✓ Maintains and updates the Certificate Revocation List (CRL).  
D) ✗ Acts as a broker between users and Registration Authorities. (RA acts as broker.)  

**Correct:** B, C


#### 12. Under which circumstances might a Certificate Authority revoke a digital certificate?  
A) ✓ The certificate was issued based on false credentials.  
B) ✓ The private key associated with the certificate has been compromised.  
C) ✗ The certificate holder requests a new certificate. (Requesting a new certificate is not a revocation reason.)  
D) ✗ The certificate has expired. (Expiration is natural, not revocation.)  

**Correct:** A, B


#### 13. What is the function of a Registration Authority (RA) in PKI?  
A) ✗ Issues digital certificates directly to users. (Only CA issues certificates.)  
B) ✓ Confirms the identity of individuals requesting certificates.  
C) ✓ Initiates the certification process with the CA on behalf of users.  
D) ✗ Maintains the Certificate Revocation List (CRL). (CA maintains CRL.)  

**Correct:** B, C


#### 14. Which of the following terms correctly match their PKI definitions?  
A) ✓ Issuer – The entity that issues a digital certificate.  
B) ✗ Subject – The entity that verifies a digital certificate. (Subject is the certificate holder.)  
C) ✓ Principal – Any entity possessing a public key.  
D) ✓ Verifier – The entity evaluating a chain of certificates.  

**Correct:** A, C, D


#### 15. How do web browsers typically handle digital certificates?  
A) ✗ They accept any digital certificate regardless of the issuer. (Browsers trust only known CAs.)  
B) ✓ They are pre-configured to trust certificates signed by a list of known Certificate Authorities.  
C) ✗ They verify certificates by contacting the Registration Authority directly. (Verification is via CA and CRL, not RA.)  
D) ✓ They use the Certificate Revocation List (CRL) to check if a certificate is still valid.  

**Correct:** B, D