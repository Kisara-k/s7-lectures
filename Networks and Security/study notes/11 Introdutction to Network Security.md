## 11 Introdutction to Network Security

## Study Notes

### 1. 🔐 What is Network Security and Why Does It Matter?

Network security is about protecting computers, networks, and the data that flows through them from unauthorized access, misuse, or damage. In today’s world, the Internet is a vital part of business and daily life, but connecting to it also exposes us to many risks. Understanding these risks and how to control them is essential to keep our information safe and systems reliable.

When we talk about security in this context, it’s not just about technology but also about trust and assurance—knowing that the systems behave as expected and that our data and resources are protected.


### 2. 🖥️ Understanding Computer Security

#### What is Computer Security?

Computer security means that a computer system behaves as you expect it to, without being compromised by unauthorized users or malicious software. It’s about protecting the computer’s resources, which include:

- **Physical assets** (hardware like hard drives, processors)
- **Data and software** (files, applications)
- **Personnel** (people who use or manage the system)
- **Trust** (confidence that the system is reliable and secure)

#### Where Do Security Threats Come From?

Threats can come from many sources:

- **Insiders:** People within the organization, such as employees or system administrators, who might misuse their access.
- **Users:** Regular users who might accidentally or intentionally cause harm.
- **Outsiders:** Hackers, competitors, or anyone outside the organization.
- **Associates:** Customers, contractors, or partners who have some access.
- **Former employees:** People who once had access but may still try to exploit it.

Interestingly, most security incidents happen because of insiders, which highlights the importance of internal controls.


### 3. 🌐 Network Security Challenges

Network security is more complicated than securing a single computer because:

- Networks are **dispersed**—they spread across many locations.
- Not all devices (nodes) on the network are visible or controlled.
- Networks consist of many **heterogeneous parts**—different hardware and software.
- There is often a **lack of central control**, making it harder to enforce security policies.
- There are **many avenues of attack**, such as intercepting data, impersonating users, or exploiting vulnerabilities.

When you connect your system to the Internet, these risks multiply because millions of people can potentially access your system, and vulnerabilities can be exploited very quickly.


### 4. 💼 Internet and Electronic Commerce Security

#### Why Internet Security is Crucial

The Internet is a two-way network: you can access it, but it can also access you. This openness means:

- Your system is exposed to millions of unknown users.
- You have no control over who tries to connect.
- Vulnerabilities can be discovered and exploited almost instantly.

#### Electronic Commerce (E-commerce) Security Issues

When doing business online, you face unique challenges:

- **Authentication:** Verifying the identity of the parties involved.
- **Confidentiality and Integrity:** Ensuring data is private and unaltered.
- **Accountability:** Tracking actions so users can be held responsible.
- **Non-repudiation:** Preventing parties from denying their actions.

These issues are critical because you often deal with unseen parties and sensitive information.


### 5. 🛡️ Computer System Security Basics

#### Types of Computer Systems

Security applies to various systems, including:

- **Hosts:** Unix systems, mainframes, PCs.
- **Networks:** Servers, workstations, routers, switches.

#### How Can Systems Be Attacked?

Systems can be compromised by:

- **Impersonation:** Pretending to be a valid user.
- **Human engineering:** Tricking people into revealing information.
- **Wiretapping:** Intercepting communications.
- **Exploiting bugs:** Taking advantage of flaws in hardware, operating systems, or applications.

#### Achieving System Security

Key methods include:

- **Access control:** The “front door” of the system, allowing only authorized users.
- **File and data control:** Setting permissions on who can read, write, modify, or delete files.

Complete security by denying all access is useless because the system would then serve no purpose. Instead, the goal is to balance security with usability.

#### User Privileges

The **principle of minimum privilege** means users get only the access they need to do their job—no more. This limits damage if an account is compromised.


### 6. 🔑 Authentication and Data Security

#### Authentication

Authentication is proving you are who you say you are. Common methods include:

- **Something you have:** A physical token or smart card.
- **Something you know:** A password or PIN.
- **Something you are:** Biometrics like fingerprints.

#### Data Security

Two main goals:

- **Integrity:** Data remains unchanged and the identity of who created or modified it is known.
- **Confidentiality:** Data is not disclosed to unauthorized people.

#### File Security

Access rights are set per user or group and specify what actions are allowed on files or directories (read, write, modify, delete).


### 7. 🐞 Bugs and Protecting Yourself

All systems have bugs, and some bugs can be exploited to breach security. Sometimes, what looks like a security hole is actually a “feature” designed for usability, showing the trade-off between security and convenience.

#### How to Protect Yourself from Bugs

- Use only the minimum necessary components to reduce complexity.
- Choose reliable components designed with security in mind.
- Keep your system updated with the latest security patches.
- Monitor security advisories (e.g., www.cert.org).
- Remember, no system is 100% safe.


### 8. 🌍 Network Security in Detail

#### Types of Networks

- **Departmental:** Within a room.
- **Local:** Within a building.
- **Corporate:** Worldwide company network.
- **Public:** The Internet.

Security problems increase as networks grow larger and more complex.

#### Host Security on a Network

Hosts provide services. To secure them:

- Provide only necessary services.
- Ensure those services are secure.
- Avoid providing no services at all, or the system becomes useless.

#### Access Control Over Networks

Passwords sent in plaintext can be intercepted (wiretapped). To prevent this, use cryptographic methods like:

- **Secure Shell (SSH):** Encrypts communication.
- **Challenge-response mechanisms:** Verify identity without sending passwords directly.
- **Smart cards and time-based tokens** for stronger authentication.


### 9. 🖥️ Server and Client Security

#### Server Security

- Use secure operating systems.
- Enable security features.
- Ensure competent system administrators.
- Disable unnecessary features.
- Keep all software updated.

#### Client Security Problems

- Some operating systems (e.g., Windows 9x) and applications (e.g., MS Office) are not designed with strong security.
- Users control clients and often prioritize features over security.
- Viruses spread due to lack of security and careless behavior.

#### Implementing Client Security

- Use more secure operating systems (e.g., Windows 2000, Linux).
- Use client management systems to control software.
- Educate users about security risks.


### 10. 🦠 Viruses and Network Infrastructure Security

#### Viruses

- Caused by weak security on PCs.
- Spread mainly through carelessness and poor policies.
- Use virus scanners and guards to reduce risk.

#### Network Infrastructure Security

- Network devices (hubs, switches, routers) have vulnerabilities.
- Physical security of network cabling and outlets is important.
- Wide-area networks may be outside your control, increasing risk.


### 11. 🔒 Data Transfer Security and Encryption

#### Goals of Data Transfer Security

- **Confidentiality:** Data is not revealed during transmission.
- **Integrity:** Data is not altered in transit.
- **Authentication:** Confirm you are communicating with the intended party.

#### Encryption Types

- **Single-key (symmetric) encryption:** Same key for sender and receiver; provides privacy and integrity.
- **Dual-key (public key) encryption:** Each user has a public and private key.
  - Privacy: Encrypt with recipient’s public key; only they can decrypt with private key.
  - Integrity: Encrypt with sender’s private key; anyone can verify with sender’s public key.

#### Export Restrictions and Key Length

- Historically, only 40-bit encryption was allowed for export from the U.S., which is weak.
- Now, 128-bit encryption is generally available and considered secure.
- Always question if you trust your software vendor.


### 12. 🌐 Security on the Internet and Firewalls

#### Types of Internet Connections

- Dial-up (single computer or network)
- Dedicated network connections

#### Risks When Connecting to the Internet

- The Internet can access your system.
- Many unknown people may try to attack.
- Privacy, commerce, and reputation are at risk.

#### Implementing Internet Security

- Secure servers, clients, and networks.
- Use firewalls to separate secure internal networks from the Internet.

#### Firewalls

- Easier to secure a network by controlling access at a single point.
- Functions include:
  - Denying unauthorized access (both inbound and outbound).
  - Controlling access to authorized services.
  - Logging access attempts.
  - Raising alarms on suspicious activity.

#### Types of Firewalls

- **Packet filters:** Work at the network layer, filtering packets based on rules.
- **Application gateways:** Filter traffic at the application level.

Configuring firewalls is complex and requires regular updates.


### 13. 🌐 Web Security

#### Web Security Problems

- Securing the web server and its interface to databases.
- Securing the web client (browser).
- Securing data traveling between server and client.

#### Web Server Security

- Secure the operating system and applications.
- Protect the interface between the web server and databases.
- Use scripting languages carefully (e.g., Perl, ASP).
- Implement encrypted protocols like SSL (Secure Sockets Layer).

#### Web Client Security

- Browsers are complex software with many features, each a potential security hole.
- Risks include:
  - Downloaded files that may contain viruses or trojans.
  - Helper applications and plug-ins that can run harmful code.
  - JavaScript and Java security models.
  - ActiveX controls with many known vulnerabilities.
  - Cookies that track user behavior.
  - Browser bugs that may never be fully fixed.

#### Securing Data Transfer on the Web

- SSL encrypts data between browser and server.
- SSL also identifies the server (and optionally the user).
- SSL does not protect data once it reaches the server or client.


### 14. ✅ Conclusion: Best Practices for Security

- Secure all your machines—servers, clients, and network devices.
- Keep software and systems up-to-date with patches and updates.
- Have a recovery plan in case of security breaches.
- Understand that no system is perfectly safe, but good practices reduce risks significantly.


### Summary

Network security is a broad and complex field that covers protecting computers, networks, and data from threats. It involves understanding risks from insiders and outsiders, securing systems and networks, authenticating users, encrypting data, and managing vulnerabilities. With the Internet and web technologies, security challenges multiply, requiring careful planning, use of firewalls, secure protocols like SSL, and ongoing vigilance. The goal is to balance usability with security to protect privacy, business interests, and reputation.