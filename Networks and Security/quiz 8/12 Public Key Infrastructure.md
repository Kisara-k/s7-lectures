## 12 Public Key Infrastructure

## Questions

#### 1. Which of the following statements correctly describe symmetric cryptosystems?  
A) They use the same key for both encryption and decryption.  
B) They provide confidentiality, authentication, and nonrepudiation.  
C) The number of keys required grows quadratically with the number of users.  
D) They are generally slower than asymmetric cryptosystems.

#### 2. What are the key differences between symmetric and asymmetric cryptosystems?  
A) Symmetric cryptosystems require a shared secret key, while asymmetric cryptosystems use a public-private key pair.  
B) Asymmetric cryptosystems provide better scalability and key distribution than symmetric ones.  
C) Symmetric cryptosystems can provide nonrepudiation, but asymmetric cannot.  
D) Asymmetric cryptosystems are typically slower than symmetric cryptosystems.

#### 3. Which of the following are true about digital certificates in a Public Key Infrastructure (PKI)?  
A) They contain the public key and identifying information of an individual.  
B) They are issued and digitally signed by a Registration Authority (RA).  
C) They follow the X.509 standard format.  
D) They enable authentication between parties who have never met before.

#### 4. What roles do Certificate Authorities (CAs) and Registration Authorities (RAs) play in PKI?  
A) CAs verify the identity of individuals requesting certificates.  
B) RAs issue digital certificates after verifying identities.  
C) CAs sign and maintain digital certificates over their lifetime.  
D) RAs act as intermediaries between users and CAs but do not issue certificates themselves.

#### 5. Which of the following scenarios would likely cause a Certificate Authority to revoke a digital certificate?  
A) The certificate holder’s private key is compromised.  
B) The certificate was issued based on false credentials.  
C) The certificate holder changes their email address.  
D) The certificate holder no longer needs to use the certificate.

#### 6. Regarding PKI security services, which of the following are provided by PKI frameworks?  
A) Confidentiality and access control.  
B) Integrity and authentication.  
C) Nonrepudiation and anonymity.  
D) Nonrepudiation and authentication.

#### 7. Why is it important to verify the authenticity of a public key in asymmetric cryptography?  
A) Because anyone can generate a public key and claim it belongs to someone else.  
B) To prevent Man-in-the-Middle attacks during key exchange.  
C) Because the private key can be derived from the public key if not verified.  
D) To ensure that the public key has not been revoked by the Certificate Authority.

#### 8. Which of the following statements about PKI components and terminology are correct?  
A) The Issuer is the entity that issues a digital certificate.  
B) The Subject is the entity that verifies the certificate chain.  
C) The Verifier evaluates the validity of a certificate chain.  
D) The Principal is any entity possessing a public key.



<br>

## Answers

#### 1. Which of the following statements correctly describe symmetric cryptosystems?  
A) ✓ Symmetric cryptosystems use the same key for encryption and decryption.  
B) ✗ They provide confidentiality but not authentication or nonrepudiation.  
C) ✓ The number of keys required grows as N(N-1)/2 with N users, which is quadratic.  
D) ✗ Symmetric cryptosystems are generally faster, not slower, than asymmetric ones.

**Correct:** A, C


#### 2. What are the key differences between symmetric and asymmetric cryptosystems?  
A) ✓ Symmetric uses a shared secret key; asymmetric uses a public-private key pair.  
B) ✓ Asymmetric cryptosystems offer better scalability and key distribution.  
C) ✗ Symmetric cryptosystems do not provide nonrepudiation; asymmetric can.  
D) ✓ Asymmetric cryptosystems are slower than symmetric ones.

**Correct:** A, B, D


#### 3. Which of the following are true about digital certificates in a Public Key Infrastructure (PKI)?  
A) ✓ Digital certificates contain the public key and identifying information.  
B) ✗ Certificates are issued and signed by Certificate Authorities (CAs), not RAs.  
C) ✓ Digital certificates follow the X.509 standard.  
D) ✓ Certificates enable authentication between parties who have never met, based on trust in the CA.

**Correct:** A, C, D


#### 4. What roles do Certificate Authorities (CAs) and Registration Authorities (RAs) play in PKI?  
A) ✗ Identity verification is performed by RAs, not CAs.  
B) ✗ RAs do not issue certificates; only CAs issue and sign certificates.  
C) ✓ CAs sign and maintain certificates over their lifetime.  
D) ✓ RAs act as intermediaries between users and CAs but cannot issue certificates themselves.

**Correct:** C, D


#### 5. Which of the following scenarios would likely cause a Certificate Authority to revoke a digital certificate?  
A) ✓ Compromise of the private key is a valid reason for revocation.  
B) ✓ Issuance based on false credentials is a valid reason for revocation.  
C) ✗ Changing an email address is not a reason for revocation; certificate renewal may be needed instead.  
D) ✗ Simply no longer needing the certificate does not cause revocation; it may expire or be replaced.

**Correct:** A, B


#### 6. Regarding PKI security services, which of the following are provided by PKI frameworks?  
A) ✓ PKI provides confidentiality and access control.  
B) ✓ PKI provides integrity and authentication.  
C) ✗ PKI does not provide anonymity; nonrepudiation is provided, but anonymity is not.  
D) ✓ PKI provides nonrepudiation and authentication.

**Correct:** A, B, D


#### 7. Why is it important to verify the authenticity of a public key in asymmetric cryptography?  
A) ✓ Anyone can generate a public key and falsely claim ownership, so verification is needed.  
B) ✓ Verification prevents Man-in-the-Middle attacks during key exchange.  
C) ✗ The private key cannot be derived from the public key if the system is secure; verification is for trust, not key derivation.  
D) ✓ Verification ensures the public key has not been revoked by the CA.

**Correct:** A, B, D


#### 8. Which of the following statements about PKI components and terminology are correct?  
A) ✓ The Issuer is the entity that issues a digital certificate.  
B) ✗ The Subject is the entity that obtains the certificate, not the verifier.  
C) ✓ The Verifier evaluates the validity of a certificate chain.  
D) ✓ The Principal is any entity possessing a public key.

**Correct:** A, C, D