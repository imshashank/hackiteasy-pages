---
# http://learn.getgrav.org/content/headers
title: Top 10 Password Crackers
slug: top-10-password-crackers
# menu: Top 10 Password Crackers
date: 21-01-2010
published: true
publish_date: 21-01-2010
# unpublish_date: 21-01-2010
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
        - Hack Tools
        - hacking
        - internet
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hack,Hack Tools,hacking,internet]
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

After the tremendously successful [2000](http://sectools.org/tools2000.html) and [2003](http://sectools.org/tools2003.html) security tools surveys, [Insecure.Org](http://www.insecure.org/) is delighted to release this 2006 survey. I ([Fyodor](http://insecure.org/fyodor/)) asked users from the [nmap-hackers](http://seclists.org/#nmap-hackers) mailing list to share their favorite tools, and 3,243 people responded. This allowed me to expand the list to 100 tools, and even subdivide them into categories. **This is the category page for password crackers** — the full network security list is [available here](http://sectools.org/index.html). Anyone in the security field would be well advised to go over the list and investigate tools they are unfamiliar with. I discovered several powerful new tools this way. I also point newbies to this site whenever they write me saying “I don’t know where to start”.   
Respondents were allowed to list open source or commercial tools on any platform. Commercial tools are noted as such in the list below. No votes for the [Nmap Security Scanner](http://insecure.org/nmap/) were counted because the survey was taken on a Nmap mailing list. This audience also biases the list slightly toward “attack” hacking tools rather than defensive ones.   
Each tool is described by one ore more attributes:

 ![new](http://mirror.sectools.org/flags/new_28x11.gif "New") Did not appear on the [2003 list](http://sectools.org/tools2003.html) ![  TITLE=](http://mirror.sectools.org/flags/dollarlogo_20x30.gif) Generally costs money. A free limited/demo/trial version may be available. ![Linux](http://mirror.sectools.org/flags/linuxpenguinlogo_30x30.gif "Runs on Linux") Works natively on Linux ![*BSD](http://mirror.sectools.org/flags/openbsdheadlogo_30x30.gif "Runs on *BSD") Works natively on OpenBSD, FreeBSD, Solaris, and/or other UNIX variants ![OS X](http://mirror.sectools.org/flags/osx-30x30.png "Runs on Mac OS X") Works natively on Apple Mac OS X ![Windows](http://mirror.sectools.org/flags/winlogo_30x30.gif "Runs on Windows") Works natively on Microsoft Windows ![Command-line interface](http://mirror.sectools.org/flags/term-30x30.png "Command-line interface") Features a command-line interface ![GUI Interface](http://mirror.sectools.org/flags/mouse-30x30.png "GUI Interface") Offers a GUI (point and click) interface ![Source code](http://mirror.sectools.org/flags/magnifying-glass-30x19.png "Source code available") Source code available for inspection.Please send updates and suggestions (or better tool logos) to [Fyodor](mailto:fyodor@insecure.org). If your tool is featured or you think your site visitors might enjoy this list, you are welcome to use our [link banners](http://sectools.org/banners.html). Here is the list, starting with the most popular:

[ ](http://www.blogger.com/post-edit.g?blogID=6229390536840976879&postID=4577409274841113222)

 \#1  
![Windows](http://mirror.sectools.org/flags/winlogo_30x30.gif "Runs on Windows")  
![GUI Interface](http://mirror.sectools.org/flags/mouse-30x30.png "GUI Interface") [![](http://mirror.sectools.org/logos/cain-80x32.png)](http://www.oxid.it/cain.html) [Cain and Abel](http://www.oxid.it/cain.html) : The top password recovery tool for Windows  
UNIX users often smugly assert that the best free security tools support their platform first, and Windows ports are often an afterthought. They are usually right, but Cain & Abel is a glaring exception. This Windows-only password recovery tool handles an enormous variety of tasks. It can recover passwords by sniffing the network, cracking encrypted passwords using Dictionary, Brute-Force and Cryptanalysis attacks, recording VoIP conversations, decoding scrambled passwords, revealing password boxes, uncovering cached passwords and analyzing routing protocols. It is also [well documented](http://www.oxid.it/ca_um/). Also categorized as: [packet sniffers](http://sectools.org/sniffers.html) - - - - - -

[ ](http://www.blogger.com/post-edit.g?blogID=6229390536840976879&postID=4577409274841113222) \#2  
![Linux](http://mirror.sectools.org/flags/linuxpenguinlogo_30x30.gif "Runs on Linux")  
![*BSD](http://mirror.sectools.org/flags/openbsdheadlogo_30x30.gif "Runs on *BSD")  
![OS X](http://mirror.sectools.org/flags/osx-30x30.png "Runs on Mac OS X")  
![Windows](http://mirror.sectools.org/flags/winlogo_30x30.gif "Runs on Windows")  
![Command-line interface](http://mirror.sectools.org/flags/term-30x30.png "Command-line interface")  
![Source code](http://mirror.sectools.org/flags/magnifying-glass-30x19.png "Source code available") [![](http://mirror.sectools.org/logos/john-80x163.png)](http://www.openwall.com/john/) [John the Ripper](http://www.openwall.com/john/) : A powerful, flexible, and *fast* multi-platform password hash cracker  
John the Ripper is a fast password cracker, currently available for many flavors of Unix (11 are officially supported, not counting different architectures), DOS, Win32, BeOS, and OpenVMS. Its primary purpose is to detect weak Unix passwords. It supports several crypt(3) password hash types which are most commonly found on various Unix flavors, as well as Kerberos AFS and Windows NT/2000/XP LM hashes. Several other hash types are added with contributed patches. You will want to start with some wordlists, which you can find [here](ftp://ftp.mirrorgeek.com/openwall/wordlists), [here](ftp://ftp.ox.ac.uk/pub/wordlists/), or [here](http://www.outpost9.com/files/WordLists.html). - - - - - -

[ ](http://www.blogger.com/post-edit.g?blogID=6229390536840976879&postID=4577409274841113222) \#3  
![Linux](http://mirror.sectools.org/flags/linuxpenguinlogo_30x30.gif "Runs on Linux")  
![*BSD](http://mirror.sectools.org/flags/openbsdheadlogo_30x30.gif "Runs on *BSD")  
![OS X](http://mirror.sectools.org/flags/osx-30x30.png "Runs on Mac OS X")  
![Windows](http://mirror.sectools.org/flags/winlogo_30x30.gif "Runs on Windows")  
![Command-line interface](http://mirror.sectools.org/flags/term-30x30.png "Command-line interface")  
![GUI Interface](http://mirror.sectools.org/flags/mouse-30x30.png "GUI Interface")  
![Source code](http://mirror.sectools.org/flags/magnifying-glass-30x19.png "Source code available") [![](http://mirror.sectools.org/logos/hydra-80x79.png)](http://www.thc.org/thc-hydra/) [THC Hydra](http://www.thc.org/thc-hydra/) : A Fast network authentication cracker which supports many different services  
When you need to brute force crack a remote authentication service, Hydra is often the tool of choice. It can perform rapid dictionary attacks against more then 30 protocols, including telnet, ftp, http, https, smb, several databases, and much more. Like [THC Amap](http://sectools.org/index.html#amap) this release is from the fine folks at [THC](http://www.thc.org/). - - - - - -

[ ](http://www.blogger.com/post-edit.g?blogID=6229390536840976879&postID=4577409274841113222) \#4  
![new](http://mirror.sectools.org/flags/new_28x11.gif)  
![Linux](http://mirror.sectools.org/flags/linuxpenguinlogo_30x30.gif "Runs on Linux")  
![*BSD](http://mirror.sectools.org/flags/openbsdheadlogo_30x30.gif "Runs on *BSD")  
![OS X](http://mirror.sectools.org/flags/osx-30x30.png "Runs on Mac OS X")  
![Windows](http://mirror.sectools.org/flags/winlogo_30x30.gif "Runs on Windows")  
![Command-line interface](http://mirror.sectools.org/flags/term-30x30.png "Command-line interface")  
![Source code](http://mirror.sectools.org/flags/magnifying-glass-30x19.png "Source code available") [![](http://mirror.sectools.org/logos/aircrack-80x63.png)](http://www.aircrack-ng.org/) [Aircrack](http://www.aircrack-ng.org/) : The fastest available WEP/WPA cracking tool  
Aircrack is a suite of tools for 802.11a/b/g WEP and WPA cracking. It can recover a 40 through 512-bit WEP key once enough encrypted packets have been gathered. It can also attack WPA 1 or 2 networks using advanced cryptographic methods or by brute force. The suite includes airodump (an 802.11 packet capture program), aireplay (an 802.11 packet injection program), aircrack (static WEP and WPA-PSK cracking), and airdecap (decrypts WEP/WPA capture files). Also categorized as: [wireless tools](http://sectools.org/wireless.html) - - - - - -

[ ](http://www.blogger.com/post-edit.g?blogID=6229390536840976879&postID=4577409274841113222) \#5  
![  TITLE=](http://mirror.sectools.org/flags/dollarlogo_20x30.gif)  
![Windows](http://mirror.sectools.org/flags/winlogo_30x30.gif "Runs on Windows")  
![GUI Interface](http://mirror.sectools.org/flags/mouse-30x30.png "GUI Interface") [![](http://mirror.sectools.org/logos/l0phtcrack-64x64.gif)](http://www.l0phtcrack.com/) [L0phtcrack](http://www.l0phtcrack.com/) : Windows password auditing and recovery application  
L0phtCrack attempts to crack Windows passwords from hashes which it can obtain (given proper access) from stand-alone Windows workstations, networked servers, primary domain controllers, or Active Directory. In some cases it can sniff the hashes off the wire. It also has numerous methods of generating password guesses (dictionary, brute force, etc). LC5 was discontinued by Symantec in 2006, then re-acquired by the original L0pht guys and [reborn as LC6 in 2009](http://www.l0phtcrack.com/). For free alternatives, consider [Ophcrack](http://ophcrack.sourceforge.net/), [Cain and Abel](http://sectools.org/crackers.html#cain), or [John the Ripper](http://sectools.org/crackers.html#john). - - - - - -

[ ](http://www.blogger.com/post-edit.g?blogID=6229390536840976879&postID=4577409274841113222) \#6  
![Linux](http://mirror.sectools.org/flags/linuxpenguinlogo_30x30.gif "Runs on Linux")  
![*BSD](http://mirror.sectools.org/flags/openbsdheadlogo_30x30.gif "Runs on *BSD")  
![OS X](http://mirror.sectools.org/flags/osx-30x30.png "Runs on Mac OS X")  
![Windows](http://mirror.sectools.org/flags/winlogo_30x30.gif "Runs on Windows")  
![Command-line interface](http://mirror.sectools.org/flags/term-30x30.png "Command-line interface")  
![Source code](http://mirror.sectools.org/flags/magnifying-glass-30x19.png "Source code available") [![](http://mirror.sectools.org/logos/airsnort-80x41.png)](http://airsnort.shmoo.com/) [Airsnort](http://airsnort.shmoo.com/) : 802.11 WEP Encryption Cracking Tool  
AirSnort is a wireless LAN (WLAN) tool that recovers encryption keys. It was developed by the [Shmoo Group](http://www.shmoo.com/) and operates by passively monitoring transmissions, computing the encryption key when enough packets have been gathered. You may also be interested in the similar [Aircrack](http://sectools.org/crackers.html#aircrack). Also categorized as: [wireless tools](http://sectools.org/wireless.html) - - - - - -

[ ](http://www.blogger.com/post-edit.g?blogID=6229390536840976879&postID=4577409274841113222) \#7  
![  TITLE=](http://mirror.sectools.org/flags/dollarlogo_20x30.gif)  
![Windows](http://mirror.sectools.org/flags/winlogo_30x30.gif "Runs on Windows")  
![GUI Interface](http://mirror.sectools.org/flags/mouse-30x30.png "GUI Interface") [![](http://mirror.sectools.org/logos/solarwinds-80x47.png)](http://www.solarwinds.net/) [SolarWinds](http://www.solarwinds.net/) : A plethora of network discovery/monitoring/attack tools  
SolarWinds has created and sells dozens of special-purpose tools targeted at systems administrators. Security-related tools include many network discovery scanners, an SNMP brute-force cracker, router password decryption, a TCP connection reset program, one of the fastest and easiest router config download/upload applications available and more. Also categorized as: [traffic monitoring tools](http://sectools.org/traffic-monitors.html) - - - - - -

[ ](http://www.blogger.com/post-edit.g?blogID=6229390536840976879&postID=4577409274841113222) \#8  
![Windows](http://mirror.sectools.org/flags/winlogo_30x30.gif "Runs on Windows")  
![Command-line interface](http://mirror.sectools.org/flags/term-30x30.png "Command-line interface")  
![Source code](http://mirror.sectools.org/flags/magnifying-glass-30x19.png "Source code available") [Pwdump](http://www.foofus.net/fizzgig/pwdump/) : A window password recovery tool  
Pwdump is able to extract NTLM and LanMan hashes from a Windows target, regardless of whether Syskey is enabled. It is also capable of displaying password histories if they are available. It outputs the data in L0phtcrack-compatible form, and can write to an output file. - - - - - -

[ ](http://www.blogger.com/post-edit.g?blogID=6229390536840976879&postID=4577409274841113222) \#9  
![new](http://mirror.sectools.org/flags/new_28x11.gif)  
![Linux](http://mirror.sectools.org/flags/linuxpenguinlogo_30x30.gif "Runs on Linux")  
![*BSD](http://mirror.sectools.org/flags/openbsdheadlogo_30x30.gif "Runs on *BSD")  
![OS X](http://mirror.sectools.org/flags/osx-30x30.png "Runs on Mac OS X")  
![Windows](http://mirror.sectools.org/flags/winlogo_30x30.gif "Runs on Windows")  
![Command-line interface](http://mirror.sectools.org/flags/term-30x30.png "Command-line interface")  
![Source code](http://mirror.sectools.org/flags/magnifying-glass-30x19.png "Source code available") [RainbowCrack](http://www.antsight.com/zsl/rainbowcrack/) : An Innovative Password Hash Cracker  
The RainbowCrack tool is a hash cracker that makes use of a large-scale time-memory trade-off. A traditional brute force cracker tries all possible plaintexts one by one, which can be time consuming for complex passwords. RainbowCrack uses a time-memory trade-off to do all the cracking-time computation in advance and store the results in so-called “rainbow tables”. It does take a long time to precompute the tables but RainbowCrack can be hundreds of times faster than a brute force cracker once the precomputation is finished. - - - - - -

[ ](http://www.blogger.com/post-edit.g?blogID=6229390536840976879&postID=4577409274841113222) \#10  
![Windows](http://mirror.sectools.org/flags/winlogo_30x30.gif "Runs on Windows")  
![GUI Interface](http://mirror.sectools.org/flags/mouse-30x30.png "GUI Interface") [Brutus](http://www.hoobie.net/brutus/) : A network brute-force authentication cracker  
This Windows-only cracker bangs against network services of remote systems trying to guess passwords by using a dictionary and permutations thereof. It supports HTTP, POP3, FTP, SMB, TELNET, IMAP, NTP, and more. No source code is available. UNIX users should take a look at [THC Hydra](http://sectools.org/crackers.html#hydra) Go to our new site- shankee.com
