---
# http://learn.getgrav.org/content/headers
title: Denial of Service (DOS) attacl :Tutorial
slug: denial-of-service-dos-attacl-tutorial
# menu: Denial of Service (DOS) attacl :Tutorial
date: 05-02-2011
published: true
publish_date: 05-02-2011
# unpublish_date: 05-02-2011
# template: false
# theme: false
visible: true
summary:
    enabled: true
    format: short
    size: 128

taxonomy:
    category:
        - Blog
    tag:
        - hack
        - hacking
        - internet
        - server
        - tutorial
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hack,hacking,internet,server,tutorial]
    tag: []
author: 'Shashank Agarwal'
metadata:
    author: 'Shashank Agarwal'
#      description: Your page description goes here
#      keywords: HTML, CSS, XML, JavaScript
#      robots: noindex, nofollow
#      og:
#          title: The Rock
#          type: video.movie
#          url: http://www.imdb.com/title/tt0117500/
#          image: http://ia.media-imdb.com/images/rock.jpg
#  cache_enable: false
#  last_modified: true

---

A denial-of-service attack (DoS attack) or distributed denial-of-service attack (DDoS attack) is an attempt to make a computer resource unavailable to its intended users. Although the means to carry out, motives for, and targets of a DoS attack may vary, it generally consists of the concerted efforts of a person or people to prevent an Internet site or service from functioning efficiently or at all, temporarily or indefinitely. Perpetrators of DoS attacks typically target sites or services hosted on high-profile web servers such as banks, credit card payment gateways, and even root nameservers. One common method of attack involves saturating the target machine with external communications requests, such that it cannot respond to legitimate traffic, or responds so slowly as to be rendered effectively unavailable. In general terms, DoS attacks are implemented by either forcing the targeted computer(s) to reset, or consuming its resources so that it can no longer provide its intended service or obstructing the communication media between the intended users and the victim so that they can no longer communicate adequately.

**Methods of attack**

A “denial-of-service” attack is characterized by an explicit attempt by attackers to prevent legitimate users of a service from using that service. There are two general forms of DoS attacks: those that crash services and those that flood services.Attacks can be directed at any network device, including attacks on routing devices and web, electronic mail, or Domain Name System servers.

A DoS attack can be perpetrated in a number of ways. The five basic types of attack are:

1. Consumption of computational resources, such as bandwidth, disk space, or processor time.  
2. Disruption of configuration information, such as routing information.  
3. Disruption of state information, such as unsolicited resetting of TCP sessions.  
4. Disruption of physical network components.  
5. Obstructing the communication media between the intended users and the victim so that they can no longer communicate adequately.

**ICMP flood**

A smurf attack is one particular variant of a flooding DoS attack on the public Internet. It relies on misconfigured network devices that allow packets to be sent to all computer hosts on a particular network via the broadcast address of the network, rather than a specific machine. The network then serves as a smurf amplifier. In such an attack, the perpetrators will send large numbers of IP packets with the source address faked to appear to be the address of the victim. The network’s bandwidth is quickly used up, preventing legitimate packets from getting through to their destination. To combat Denial of Service attacks on the Internet, services like the Smurf Amplifier Registry have given network service providers the ability to identify misconfigured networks and to take appropriate action such as filtering.

Ping flood is based on sending the victim an overwhelming number of ping packets, usually using the “ping” command from unix-like hosts (the -t flag on Windows systems has a far less malignant function). It is very simple to launch, the primary requirement being access to greater bandwidth than the victim.

SYN flood sends a flood of TCP/SYN packets, often with a forged sender address. Each of these packets is handled like a connection request, causing the server to spawn a half-open connection, by sending back a TCP/SYN-ACK packet, and waiting for a packet in response from the sender address. However, because the sender address is forged, the response never comes. These half-open connections saturate the number of available connections the server is able to make, keeping it from responding to legitimate requests until after the attack ends.

** Teardrop attacks**

A Teardrop attack involves sending mangled IP fragments with overlapping, over-sized payloads to the target machine. This can crash various operating systems due to a bug in their TCP/IP fragmentation re-assembly code. Windows 3.1x, Windows 95 and Windows NT operating systems, as well as versions of Linux prior to versions 2.0.32 and 2.1.63 are vulnerable to this attack.

Around September 2009, a vulnerability in Vista was referred to as a “teardrop attack”, but the attack targeted SMB2 which is a higher layer than the TCP packets that teardrop used.

**Peer-to-peer attacks**

Attackers have found a way to exploit a number of bugs in peer-to-peer servers to initiate DDoS attacks. The most aggressive of these peer-to-peer-DDoS attacks exploits DC++. Peer-to-peer attacks are different from regular botnet-based attacks. With peer-to-peer there is no botnet and the attacker does not have to communicate with the clients it subverts. Instead, the attacker acts as a “puppet master,” instructing clients of large peer-to-peer file sharing hubs to disconnect from their peer-to-peer network and to connect to the victim’s website instead. As a result, several thousand computers may aggressively try to connect to a target website. While a typical web server can handle a few hundred connections per second before performance begins to degrade, most web servers fail almost instantly under five or six thousand connections per second. With a moderately large peer-to-peer attack, a site could potentially be hit with up to 750,000 connections in short order. The targeted web server will be plugged up by the incoming connections.

While peer-to-peer attacks are easy to identify with signatures, the large number of IP addresses that need to be blocked (often over 250,000 during the course of a large-scale attack) means that this type of attack can overwhelm mitigation defenses. Even if a mitigation device can keep blocking IP addresses, there are other problems to consider. For instance, there is a brief moment where the connection is opened on the server side before the signature itself comes through. Only once the connection is opened to the server can the identifying signature be sent and detected, and the connection torn down. Even tearing down connections takes server resources and can harm the server.

This method of attack can be prevented by specifying in the peer-to-peer protocol which ports are allowed or not. If port 80 is not allowed, the possibilities for attack on websites can be very limited.

**Asymmetry of resource utilization in starvation attacks**

An attack which is successful in consuming resources on the victim computer must be either:

\* carried out by an attacker with great resources, by either:  
o controlling a computer with great computation power or, more commonly, large network bandwidth  
o controlling a large number of computers and directing them to attack as a group. A DDOS attack is the primary example of this.  
\* taking advantage of a property of the operating system or applications on the victim system which enables an attack consuming vastly more of the victim’s resources and the attackers (an asymmetric attack). Smurf attack, SYN flood, and NAPTHA are all asymmetric attacks.

**Permanent denial-of-service attacks**

A permanent denial-of-service (PDoS), also known loosely as phlashing, is an attack that damages a system so badly that it requires replacement or reinstallation of hardware. Unlike the distributed denial-of-service attack, a PDoS attack exploits security flaws which allow remote administration on the management interfaces of the victim’s hardware, such as routers, printers, or other networking hardware. The attacker uses these vulnerabilities to replace a device’s firmware with a modified, corrupt, or defective firmware image—a process which when done legitimately is known as flashing. This therefore “bricks” the device, rendering it unusable for its original purpose until it can be repaired or replaced.

The PDoS is a pure hardware targeted attack which can be much faster and requires fewer resources than using a botnet in a DDoS attack. Because of these features, and the potential and high probability of security exploits on Network Enabled Embedded Devices (NEEDs), this technique has come to the attention of numerous hacker communities. PhlashDance is a tool created by Rich Smith (an employee of Hewlett-Packard’s Systems Security Lab) used to detect and demonstrate

**Application-level floods**

On IRC, IRC floods are a common electronic warfare weapon.

Various DoS-causing exploits such as buffer overflow can cause server-running software to get confused and fill the disk space or consume all available memory or CPU time.

Other kinds of DoS rely primarily on brute force, flooding the target with an overwhelming flux of packets, oversaturating its connection bandwidth or depleting the target’s system resources. Bandwidth-saturating floods rely on the attacker having higher bandwidth available than the victim; a common way of achieving this today is via Distributed Denial of Service, employing a botnet. Other floods may use specific packet types or connection requests to saturate finite resources by, for example, occupying the maximum number of open connections or filling the victim’s disk space with logs.

A “banana attack” is another particular type of DoS. It involves redirecting outgoing messages from the client back onto the client, preventing outside access, as well as flooding the client with the sent packets.

An attacker with access to a victim’s computer may slow it until it is unusable or crash it by using a fork bomb.

**Nuke**

A Nuke is an old denial-of-service attack against computer networks consisting of fragmented or otherwise invalid ICMP packets sent to the target, achieved by using a modified ping utility to repeatedly send this corrupt data, thus slowing down the affected computer until it comes to a complete stop.

A specific example of a nuke attack that gained some prominence is the WinNuke, which exploited the vulnerability in the NetBIOS handler in Windows 95. A string of out-of-band data was sent to TCP port 139 of the victim’s machine, causing it to lock up and display a Blue Screen of Death (BSOD).

**Distributed attack**

A distributed denial of service attack (DDoS) occurs when multiple systems flood the bandwidth or resources of a targeted system, usually one or more web servers. These systems are compromised by attackers using a variety of methods.

Malware can carry DDoS attack mechanisms; one of the better-known examples of this was MyDoom. Its DoS mechanism was triggered on a specific date and time. This type of DDoS involved hardcoding the target IP address prior to release of the malware and no further interaction was necessary to launch the attack.

A system may also be compromised with a trojan, allowing the attacker to download a zombie agent (or the trojan may contain one). Attackers can also break into systems using automated tools that exploit flaws in programs that listen for connections from remote hosts. This scenario primarily concerns systems acting as servers on the web.

Stacheldraht is a classic example of a DDoS tool. It utilizes a layered structure where the attacker uses a client program to connect to handlers, which are compromised systems that issue commands to the zombie agents, which in turn facilitate the DDoS attack. Agents are compromised via the handlers by the attacker, using automated routines to exploit vulnerabilities in programs that accept remote connections running on the targeted remote hosts. Each handler can control up to a thousand agents.

These collections of systems compromisers are known as botnets. DDoS tools like stacheldraht still use classic DoS attack methods centered on IP spoofing and amplification like smurf attacks and fraggle attacks (these are also known as bandwidth consumption attacks). SYN floods (also known as resource starvation attacks) may also be used. Newer tools can use DNS servers for DoS purposes. See next section.

Simple attacks such as SYN floods may appear with a wide range of source IP addresses, giving the appearance of a well distributed DDoS. These flood attacks do not require completion of the TCP three way handshake and attempt to exhaust the destination SYN queue or the server bandwidth. Because the source IP addresses can be trivially spoofed, an attack could come from a limited set of sources, or may even originate from a single host. Stack enhancements such as syn cookies may be effective mitigation against SYN queue flooding, however complete bandwidth exhaustion may require involvement

Unlike MyDoom’s DDoS mechanism, botnets can be turned against any IP address. Script kiddies use them to deny the availability of well known websites to legitimate users. More sophisticated attackers use DDoS tools for the purposes of extortion — even against their business rivals.

It is important to note the difference between a DDoS and DoS attack. If an attacker mounts an attack from a single host it would be classified as a DoS attack. In fact, any attack against availability would be classed as a Denial of Service attack. On the other hand, if an attacker uses a thousand systems to simultaneously launch smurf attacks against a remote host, this would be classified as a DDoS attack.

The major advantages to an attacker of using a distributed denial-of-service attack are that multiple machines can generate more attack traffic than one machine, multiple attack machines are harder to turn off than one attack machine, and that the behavior of each attack machine can be stealthier, making it harder to track down and shut down. These attacker advantages cause challenges for defense mechanisms. For example, merely purchasing more incoming bandwidth than the current volume of the attack might not help, because the attacker might be able to simply add more attack machines.

It should be noted that in some cases a machine may become part of a DDoS attack with the owner’s consent. An example of this is the 2010 DDoS attack against major credit card companies by supporters of WikiLeaks. In cases such as this, supporters of a movement (in this case, those opposing the arrest of WikiLeaks founder Julian Assange) choose to download and run DDoS software.

**Reflected attack**

A distributed reflected denial of service attack (DRDoS) involves sending forged requests of some type to a very large number of computers that will reply to the requests. Using Internet protocol spoofing, the source address is set to that of the targeted victim, which means all the replies will go to (and flood) the target.

ICMP Echo Request attacks (Smurf Attack) can be considered one form of reflected attack, as the flooding host(s) send Echo Requests to the broadcast addresses of mis-configured networks, thereby enticing many hosts to send Echo Reply packets to the victim. Some early DDoS programs implemented a distributed form of this attack.

Many services can be exploited to act as reflectors, some harder to block than others.DNS amplification attacks involve a new mechanism that increased the amplification effect, using a much larger list of DNS servers than seen earlier.

**Degradation-of-service attacks**

“Pulsing” zombies are compromised computers that are directed to launch intermittent and short-lived floodings of victim websites with the intent of merely slowing it rather than crashing it. This type of attack, referred to as “degradation-of-service” rather than “denial-of-service”, can be more difficult to detect than regular zombie invasions and can disrupt and hamper connection to websites for prolonged periods of time, potentially causing more damage than concentrated floods. Exposure of degradation-of-service attacks is complicated further by the matter of discerning whether the attacks

**Unintentional denial of service**

This describes a situation where a website ends up denied, not due to a deliberate attack by a single individual or group of individuals, but simply due to a sudden enormous spike in popularity. This can happen when an extremely popular website posts a prominent link to a second, less well-prepared site, for example, as part of a news story. The result is that a significant proportion of the primary site’s regular users — potentially hundreds of thousands of people — click that link in the space of a few hours, having the same effect on the target website as a DDoS attack. A VIPDoS is the same, but specifically when the link was posted by a celebrity.

An example of this occurred when Michael Jackson died in 2009. Websites such as Google and Twitter slowed down or even crashed. Many sites’ servers thought the requests were from a virus or spyware trying to cause a Denial of Service attack, warning users that their queries looked like “automated requests from a computer virus or spyware application”.

News sites and link sites — sites whose primary function is to provide links to interesting content elsewhere on the Internet — are most likely to cause this phenomenon. The canonical example is the Slashdot effect. Sites such as Digg, the Drudge Report, Fark, Something Awful, and the webcomic Penny Arcade have their own corresponding “effects”, known as “the Digg effect”, being “drudged”, “farking”, “goonrushing” and “wanging”; respectively.

**Denial-of-Service Level II**

The goal of DoS L2 (possibly DDoS) attack is to cause a launching of a defense mechanism which blocks the network segment from which the attack originated. In case of distributed attack or IP header modification (that depends on the kind of security behavior) it will fully block the attacked network from Internet, but without system crash.

**Blind denial of service**

In a blind denial of service attack, the attacker has a significant advantage. The attacker must be able to receive traffic from the victim, then the attacker must either subvert the routing fabric or use the attacker’s own IP address. Either provides an opportunity for the victim to track the attacker and/or filter out his traffic. With a blind attack the attacker uses one or more forged IP addresses, making it extremely difficult for the victim to filter out those packets. The TCP SYN flood attack is an example of a blind attack.

Source-[ http://en.wikipedia.org/wiki/Denial-of-service\_attack](http://en.wikipedia.org/wiki/Denial-of-service_attack)   
By hackiteasy.com 



Go to our new site- shankee.com
