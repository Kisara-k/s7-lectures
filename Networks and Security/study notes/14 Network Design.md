## 14 Network Design

## Study Notes

### 1. 🌐 Introduction to Network Design

Network design is the process of planning and structuring a computer network to meet the specific needs of an organization. It involves making decisions about how to connect devices, what technologies to use, and how to ensure the network supports business goals efficiently and securely. A well-designed network balances performance, cost, security, and future growth, ensuring that the organization’s communication and data needs are met both now and in the future.

Network design is not just about technology; it must align with business requirements, existing infrastructure, and security policies. It also involves choosing the right architecture and design strategies to create a network that is reliable, scalable, and manageable.


### 2. 📝 Key Design Considerations

When designing a network, several important factors must be considered to ensure the network supports the organization effectively:

#### Business Needs
The network must align with the organization’s goals and provide value. This means understanding what services and applications the business requires, where resources should be placed, and how the network can give a competitive advantage. Cost is also a factor—investments in network infrastructure should be justified by the benefits they bring.

#### Future Growth
Networks should be designed with expansion in mind. This includes anticipating increases in users, applications, services, and servers. For example, if the business plans to add wireless hotspots, expand to new locations, or connect subsidiaries, the network must be able to support these changes without major redesign.

#### Existing Infrastructure
Often, organizations already have some network components in place. It’s important to evaluate what can be reused rather than discarded, as throwing away equipment can be costly and unnecessary. Existing cabling, switches, or routers might still be useful if restructured properly. Physical factors like building locations and security also influence network design.

#### Internet & Intranet Requirements
Decisions must be made about how branches connect to the internet—whether each branch has its own connection or if all traffic routes through a central office. This affects control, security, and reliability. The network must also balance public-facing services with internal services, ensuring appropriate access and security.

#### Security vs. Accessibility
A critical balance in network design is between protecting resources and allowing users to access what they need. Organizational policies define who can access what, how authentication is handled (e.g., single sign-on vs. distributed authentication), and how mobile employees connect securely. Servers with sensitive data require higher protection.

#### Appropriate Network Architecture
The architecture should be as simple as possible while meeting current needs. Overly complex designs can be costly and difficult to manage. Consider traffic loads, server workloads, and application types. While equipment may become outdated in a few years, structured cabling can last longer and make future upgrades easier and more cost-effective.


### 3. 🛠️ Network Design Strategies

There are several approaches to designing a network, each focusing on different priorities:

#### Function (Application) Based Design
Also known as business-IT alignment, this strategy designs the network around the specific applications and data needs of the organization. Different types of businesses require different network forms depending on their applications, data sensitivity, and user needs. This approach ensures the network supports business processes effectively.

#### Security Based Design
Security is a major concern in network design. This strategy focuses on protecting the network from physical and network-based threats. It involves setting policies for access control, office setups, and third-party connections. Techniques include:

- Limited access using proxies and Network Address Translation (NAT) to control who can connect.
- Privileged access for managers or collaborators using VPNs and role-based permissions.
- Protecting critical nodes like server farms and VLANs.
- Using firewalls, Intrusion Detection Systems (IDS), and Intrusion Prevention Systems (IPS).
- Multi-tier architectures to isolate sensitive applications.
- Ensuring secure communication with SSL and cryptography.
- Creating isolated subnets with multiple firewall interfaces to limit exposure.

#### Topology (Technology/Protocol) Based Design
This strategy focuses on the physical and logical layout of the network, considering different technologies such as LANs, WLANs, and WANs. It accounts for:

- Speed and technology differences between network segments.
- Budget and environmental constraints.
- Use of VPNs and tunnels (e.g., PPTP, L2TP) to extend networks securely.
- Security considerations over wide-area networks.
- How to extend LANs effectively.

#### Traffic Based Design
This approach designs the network based on traffic patterns and performance requirements. Key considerations include:

- Queuing and prioritizing traffic to avoid congestion.
- Whether applications can tolerate delays.
- Switching capabilities and whether the network can operate at wire-speed (maximum speed without delay).
- Load balancing to distribute traffic evenly.
- Ensuring reliability and availability through redundant paths.
- Quality of Service (QoS) parameters like latency and throughput.
- Choosing appropriate transmission media, such as satellite or fiber optics, based on performance needs.


### 4. 💼 Business Needs in Network Design

Understanding business needs is fundamental to network design. The network must support business goals such as improving customer service, gaining competitive advantage, and ensuring a good return on investment. This involves deciding:

- What services and resources to provide.
- Where to place servers and network devices.
- How to balance cost against the added value the network brings.

The network should be designed to enhance business operations, not just to implement the latest technology.


### 5. 📈 Planning for Future Growth

Networks must be scalable to accommodate future changes. This includes:

- Anticipating growth in applications, services, and servers.
- Planning for new technologies like wireless hotspots or island-wide coverage.
- Considering connections to subsidiaries or third-party providers.
- Preparing for diversification of business activities.
- Ensuring the network can adapt to new requirements without costly overhauls.


### 6. 🏗️ Leveraging Existing Infrastructure

Before building a new network, evaluate what existing infrastructure can be reused. This saves costs and reduces waste. Consider:

- Which equipment must be replaced and which can be restructured.
- Physical factors like building locations and security.
- Centralizing core network components, such as placing a core switch in a central location for a campus network.
- The longevity of cabling, which often lasts longer than active equipment.


### 7. 🔐 Balancing Security and Accessibility

Security policies must define who can access what resources and how. This includes:

- Organizational and IT security policies.
- Computer use policies.
- Access for mobile employees.
- Authentication methods, such as single sign-on or distributed authentication.
- Protecting critical servers and sensitive data.

The goal is to protect the network without unnecessarily restricting legitimate access.


### 8. 🏛️ Choosing Appropriate Network Architecture

The network architecture should be practical and based on current needs. Avoid overly complex designs that are expensive and hard to maintain. Consider:

- Traffic loads and server workloads.
- Types of applications used.
- The fact that most equipment will become outdated within a few years.
- The benefits of structured cabling for easier management and upgrades.


### 9. 🔄 Summary of Design Strategies

- **Function-based design** aligns the network with business applications and data.
- **Security-based design** focuses on protecting the network from threats and controlling access.
- **Topology-based design** considers the physical and logical layout, technology choices, and protocols.
- **Traffic-based design** manages network performance, prioritization, and reliability.

Each strategy addresses different aspects of network design, and often a combination is used to create an effective network.


### Final Thoughts

Network design is a complex but essential task that requires balancing many factors: business goals, future growth, existing resources, security, accessibility, and technical constraints. By carefully considering these elements and choosing appropriate design strategies, organizations can build networks that are efficient, secure, scalable, and aligned with their needs.