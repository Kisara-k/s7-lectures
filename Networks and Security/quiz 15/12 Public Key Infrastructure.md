## 12 Public Key Infrastructure

## Questions

#### 1. Which of the following statements correctly describe symmetric cryptosystems?  
A) Key management becomes complex as the number of users increases.  
B) They use a pair of mathematically related public and private keys.  
C) The same key is used for both encryption and decryption.  
D) They provide confidentiality, authentication, and nonrepudiation.  

#### 2. What are the main disadvantages of symmetric cryptosystems?  
A) They are slower than asymmetric cryptosystems.  
B) They cannot provide confidentiality.  
C) Each pair of users requires a unique key, leading to scalability issues.  
D) They require a secure mechanism to deliver and store keys.  

#### 3. Which of the following algorithms are examples of symmetric key cryptosystems?  
A) AES  
B) RSA  
C) Elliptic Curve Cryptosystem (ECC)  
D) DES  

#### 4. In asymmetric cryptosystems, which of the following are true?  
A) The private key is mathematically related to the public key but cannot be derived from it.  
B) The public key is kept secret by the owner.  
C) Encryption and decryption use the same key.  
D) The private key must be kept confidential to maintain security.  

#### 5. What are the advantages of asymmetric cryptosystems over symmetric ones?  
A) Faster encryption and decryption processes.  
B) Better key distribution and scalability.  
C) Ability to provide authentication and nonrepudiation.  
D) Requires fewer keys as the number of users increases.  

#### 6. Which of the following are examples of asymmetric cryptosystems?  
A) Diffie-Hellman  
B) RSA  
C) RC4  
D) Triple-DES (3DES)  

#### 7. What is the primary purpose of a Public Key Infrastructure (PKI)?  
A) To replace symmetric cryptosystems entirely.  
B) To store private keys for users.  
C) To provide a framework of policies, protocols, and cryptographic mechanisms for secure communication.  
D) To securely distribute and verify the authenticity of public keys.  

#### 8. Which of the following security services are provided by PKI?  
A) Integrity  
B) Nonrepudiation  
C) Confidentiality  
D) Access control  

#### 9. Which components are essential for the effective operation of a PKI?  
A) Certificate Authorities (CAs)  
B) Registration Authorities (RAs)  
C) Symmetric keys  
D) Digital Certificates  

#### 10. What information does a digital certificate typically contain?  
A) The public key of the individual.  
B) The private key of the individual.  
C) Identifying information about the certificate holder.  
D) The digital signature of a trusted Certificate Authority.  

#### 11. What role does a Certificate Authority (CA) play in PKI?  
A) Acts as a broker between users and Registration Authorities.  
B) Maintains and updates the Certificate Revocation List (CRL).  
C) Verifies the identity of individuals requesting certificates.  
D) Issues and digitally signs digital certificates.  

#### 12. Under which circumstances might a Certificate Authority revoke a digital certificate?  
A) The certificate was issued based on false credentials.  
B) The certificate has expired.  
C) The certificate holder requests a new certificate.  
D) The private key associated with the certificate has been compromised.  

#### 13. What is the function of a Registration Authority (RA) in PKI?  
A) Maintains the Certificate Revocation List (CRL).  
B) Issues digital certificates directly to users.  
C) Confirms the identity of individuals requesting certificates.  
D) Initiates the certification process with the CA on behalf of users.  

#### 14. Which of the following terms correctly match their PKI definitions?  
A) Principal – Any entity possessing a public key.  
B) Subject – The entity that verifies a digital certificate.  
C) Verifier – The entity evaluating a chain of certificates.  
D) Issuer – The entity that issues a digital certificate.  

#### 15. How do web browsers typically handle digital certificates?  
A) They accept any digital certificate regardless of the issuer.  
B) They are pre-configured to trust certificates signed by a list of known Certificate Authorities.  
C) They verify certificates by contacting the Registration Authority directly.  
D) They use the Certificate Revocation List (CRL) to check if a certificate is still valid.  



<br>

## Answers

#### 1. Which of the following statements correctly describe symmetric cryptosystems?  
A) ✓ Key management becomes complex as the number of users increases.  
B) ✗ They use a pair of mathematically related public and private keys. (This describes asymmetric cryptosystems.)  
C) ✓ The same key is used for both encryption and decryption.  
D) ✗ They provide confidentiality, authentication, and nonrepudiation. (Only confidentiality is provided, not authentication or nonrepudiation.)  

**Correct:** A, C


#### 2. What are the main disadvantages of symmetric cryptosystems?  
A) ✗ They are slower than asymmetric cryptosystems. (Symmetric systems are faster.)  
B) ✗ They cannot provide confidentiality. (They do provide confidentiality.)  
C) ✓ Each pair of users requires a unique key, leading to scalability issues.  
D) ✓ They require a secure mechanism to deliver and store keys.  

**Correct:** C, D


#### 3. Which of the following algorithms are examples of symmetric key cryptosystems?  
A) ✓ AES is a symmetric key algorithm.  
B) ✗ RSA is an asymmetric algorithm.  
C) ✗ ECC is an asymmetric algorithm.  
D) ✓ DES is a symmetric key algorithm.  

**Correct:** A, D


#### 4. In asymmetric cryptosystems, which of the following are true?  
A) ✓ The private key is mathematically related to the public key but cannot be derived from it.  
B) ✗ The public key is kept secret by the owner. (Public key is known to everyone.)  
C) ✗ Encryption and decryption use the same key. (Different keys are used.)  
D) ✓ The private key must be kept confidential to maintain security.  

**Correct:** A, D


#### 5. What are the advantages of asymmetric cryptosystems over symmetric ones?  
A) ✗ Faster encryption and decryption processes. (They are slower.)  
B) ✓ Better key distribution and scalability.  
C) ✓ Ability to provide authentication and nonrepudiation.  
D) ✗ Requires fewer keys as the number of users increases. (Key management is easier but not necessarily fewer keys.)  

**Correct:** B, C


#### 6. Which of the following are examples of asymmetric cryptosystems?  
A) ✓ Diffie-Hellman is asymmetric.  
B) ✓ RSA is asymmetric.  
C) ✗ RC4 is symmetric.  
D) ✗ Triple-DES (3DES) is symmetric.  

**Correct:** A, B


#### 7. What is the primary purpose of a Public Key Infrastructure (PKI)?  
A) ✗ To replace symmetric cryptosystems entirely. (PKI complements symmetric systems.)  
B) ✗ To store private keys for users. (Private keys are kept by users, not PKI.)  
C) ✓ To provide a framework of policies, protocols, and cryptographic mechanisms for secure communication.  
D) ✓ To securely distribute and verify the authenticity of public keys.  

**Correct:** C, D


#### 8. Which of the following security services are provided by PKI?  
A) ✓ Integrity  
B) ✓ Nonrepudiation  
C) ✓ Confidentiality  
D) ✓ Access control  

**Correct:** A, B, C, D


#### 9. Which components are essential for the effective operation of a PKI?  
A) ✓ Certificate Authorities (CAs)  
B) ✓ Registration Authorities (RAs)  
C) ✗ Symmetric keys (Not a PKI component)  
D) ✓ Digital Certificates  

**Correct:** A, B, D


#### 10. What information does a digital certificate typically contain?  
A) ✓ The public key of the individual.  
B) ✗ The private key of the individual. (Private key is never included.)  
C) ✓ Identifying information about the certificate holder.  
D) ✓ The digital signature of a trusted Certificate Authority.  

**Correct:** A, C, D


#### 11. What role does a Certificate Authority (CA) play in PKI?  
A) ✗ Acts as a broker between users and Registration Authorities. (RA acts as broker.)  
B) ✓ Maintains and updates the Certificate Revocation List (CRL).  
C) ✗ Verifies the identity of individuals requesting certificates. (This is the RA’s role.)  
D) ✓ Issues and digitally signs digital certificates.  

**Correct:** B, D


#### 12. Under which circumstances might a Certificate Authority revoke a digital certificate?  
A) ✓ The certificate was issued based on false credentials.  
B) ✗ The certificate has expired. (Expiration is natural, not revocation.)  
C) ✗ The certificate holder requests a new certificate. (Requesting a new certificate is not a revocation reason.)  
D) ✓ The private key associated with the certificate has been compromised.  

**Correct:** A, D


#### 13. What is the function of a Registration Authority (RA) in PKI?  
A) ✗ Maintains the Certificate Revocation List (CRL). (CA maintains CRL.)  
B) ✗ Issues digital certificates directly to users. (Only CA issues certificates.)  
C) ✓ Confirms the identity of individuals requesting certificates.  
D) ✓ Initiates the certification process with the CA on behalf of users.  

**Correct:** C, D


#### 14. Which of the following terms correctly match their PKI definitions?  
A) ✓ Principal – Any entity possessing a public key.  
B) ✗ Subject – The entity that verifies a digital certificate. (Subject is the certificate holder.)  
C) ✓ Verifier – The entity evaluating a chain of certificates.  
D) ✓ Issuer – The entity that issues a digital certificate.  

**Correct:** A, C, D


#### 15. How do web browsers typically handle digital certificates?  
A) ✗ They accept any digital certificate regardless of the issuer. (Browsers trust only known CAs.)  
B) ✓ They are pre-configured to trust certificates signed by a list of known Certificate Authorities.  
C) ✗ They verify certificates by contacting the Registration Authority directly. (Verification is via CA and CRL, not RA.)  
D) ✓ They use the Certificate Revocation List (CRL) to check if a certificate is still valid.  

**Correct:** B, D