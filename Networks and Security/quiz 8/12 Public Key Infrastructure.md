## 12 Public Key Infrastructure

## Questions

#### 1. Which of the following statements correctly describe symmetric cryptosystems?  
A) They are generally slower than asymmetric cryptosystems.  
B) They provide confidentiality, authentication, and nonrepudiation.  
C) They use the same key for both encryption and decryption.  
D) The number of keys required grows quadratically with the number of users.  

#### 2. What are the key differences between symmetric and asymmetric cryptosystems?  
A) Asymmetric cryptosystems are typically slower than symmetric cryptosystems.  
B) Symmetric cryptosystems can provide nonrepudiation, but asymmetric cannot.  
C) Symmetric cryptosystems require a shared secret key, while asymmetric cryptosystems use a public-private key pair.  
D) Asymmetric cryptosystems provide better scalability and key distribution than symmetric ones.  

#### 3. Which of the following are true about digital certificates in a Public Key Infrastructure (PKI)?  
A) They contain the public key and identifying information of an individual.  
B) They enable authentication between parties who have never met before.  
C) They are issued and digitally signed by a Registration Authority (RA).  
D) They follow the X.509 standard format.  

#### 4. What roles do Certificate Authorities (CAs) and Registration Authorities (RAs) play in PKI?  
A) CAs verify the identity of individuals requesting certificates.  
B) RAs issue digital certificates after verifying identities.  
C) RAs act as intermediaries between users and CAs but do not issue certificates themselves.  
D) CAs sign and maintain digital certificates over their lifetime.  

#### 5. Which of the following scenarios would likely cause a Certificate Authority to revoke a digital certificate?  
A) The certificate holder no longer needs to use the certificate.  
B) The certificate was issued based on false credentials.  
C) The certificate holder changes their email address.  
D) The certificate holder’s private key is compromised.  

#### 6. Regarding PKI security services, which of the following are provided by PKI frameworks?  
A) Integrity and authentication.  
B) Nonrepudiation and anonymity.  
C) Confidentiality and access control.  
D) Nonrepudiation and authentication.  

#### 7. Why is it important to verify the authenticity of a public key in asymmetric cryptography?  
A) Because the private key can be derived from the public key if not verified.  
B) Because anyone can generate a public key and claim it belongs to someone else.  
C) To prevent Man-in-the-Middle attacks during key exchange.  
D) To ensure that the public key has not been revoked by the Certificate Authority.  

#### 8. Which of the following statements about PKI components and terminology are correct?  
A) The Issuer is the entity that issues a digital certificate.  
B) The Principal is any entity possessing a public key.  
C) The Verifier evaluates the validity of a certificate chain.  
D) The Subject is the entity that verifies the certificate chain.  



<br>

## Answers

#### 1. Which of the following statements correctly describe symmetric cryptosystems?  
A) ✗ Symmetric cryptosystems are generally faster, not slower, than asymmetric ones.  
B) ✗ They provide confidentiality but not authentication or nonrepudiation.  
C) ✓ Symmetric cryptosystems use the same key for encryption and decryption.  
D) ✓ The number of keys required grows as N(N-1)/2 with N users, which is quadratic.  

**Correct:** C, D


#### 2. What are the key differences between symmetric and asymmetric cryptosystems?  
A) ✓ Asymmetric cryptosystems are slower than symmetric ones.  
B) ✗ Symmetric cryptosystems do not provide nonrepudiation; asymmetric can.  
C) ✓ Symmetric uses a shared secret key; asymmetric uses a public-private key pair.  
D) ✓ Asymmetric cryptosystems offer better scalability and key distribution.  

**Correct:** A, C, D


#### 3. Which of the following are true about digital certificates in a Public Key Infrastructure (PKI)?  
A) ✓ Digital certificates contain the public key and identifying information.  
B) ✓ Certificates enable authentication between parties who have never met, based on trust in the CA.  
C) ✗ Certificates are issued and signed by Certificate Authorities (CAs), not RAs.  
D) ✓ Digital certificates follow the X.509 standard.  

**Correct:** A, B, D


#### 4. What roles do Certificate Authorities (CAs) and Registration Authorities (RAs) play in PKI?  
A) ✗ Identity verification is performed by RAs, not CAs.  
B) ✗ RAs do not issue certificates; only CAs issue and sign certificates.  
C) ✓ RAs act as intermediaries between users and CAs but cannot issue certificates themselves.  
D) ✓ CAs sign and maintain certificates over their lifetime.  

**Correct:** C, D


#### 5. Which of the following scenarios would likely cause a Certificate Authority to revoke a digital certificate?  
A) ✗ Simply no longer needing the certificate does not cause revocation; it may expire or be replaced.  
B) ✓ Issuance based on false credentials is a valid reason for revocation.  
C) ✗ Changing an email address is not a reason for revocation; certificate renewal may be needed instead.  
D) ✓ Compromise of the private key is a valid reason for revocation.  

**Correct:** B, D


#### 6. Regarding PKI security services, which of the following are provided by PKI frameworks?  
A) ✓ PKI provides integrity and authentication.  
B) ✗ PKI does not provide anonymity; nonrepudiation is provided, but anonymity is not.  
C) ✓ PKI provides confidentiality and access control.  
D) ✓ PKI provides nonrepudiation and authentication.  

**Correct:** A, C, D


#### 7. Why is it important to verify the authenticity of a public key in asymmetric cryptography?  
A) ✗ The private key cannot be derived from the public key if the system is secure; verification is for trust, not key derivation.  
B) ✓ Anyone can generate a public key and falsely claim ownership, so verification is needed.  
C) ✓ Verification prevents Man-in-the-Middle attacks during key exchange.  
D) ✓ Verification ensures the public key has not been revoked by the CA.  

**Correct:** B, C, D


#### 8. Which of the following statements about PKI components and terminology are correct?  
A) ✓ The Issuer is the entity that issues a digital certificate.  
B) ✓ The Principal is any entity possessing a public key.  
C) ✓ The Verifier evaluates the validity of a certificate chain.  
D) ✗ The Subject is the entity that obtains the certificate, not the verifier.  

**Correct:** A, B, C