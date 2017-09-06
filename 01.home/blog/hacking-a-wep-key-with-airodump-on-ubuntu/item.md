---
# http://learn.getgrav.org/content/headers
title: Hacking a WEP key with airodump on Ubuntu
slug: hacking-a-wep-key-with-airodump-on-ubuntu
# menu: Hacking a WEP key with airodump on Ubuntu
date: 10-01-2011
published: true
publish_date: 10-01-2011
# unpublish_date: 10-01-2011
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
        - linux
        - trick
        - wep
        - wifi
        - wireless
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hack,hacking,linux,trick,wep,wifi,wireless]
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

[![](http://www.instructables.com/image/F5T0XHAF04FMXU0/Wi-Fi-hack-mod.jpg)](http://www.instructables.com/image/F5T0XHAF04FMXU0/Wi-Fi-hack-mod.jpg)

WEP key can easily be cracked with a simple combination of tools on Linux machine. The WEP cracking is made easier by the flaws in the design of the WEP encryption that makes it so vulnerable.

These tools are already inbuilt in the Backtrack linux about which I posted recently. But you can install these hacking tools separately as well on any linux distro.

These steps are made for an Ubuntu machine and uses Debian version which is the format for Ubuntu. Specific version for each each hack tool are available for almost all leading linux versions.

The hack starts-

Install [aircrack-ng](http://dl.aircrack-ng.org/aircrack-ng-svn-win.zip) – on Debian Etch by:

sudo apt-get install aircrack-ng

Then start aircrack-ng to look for wireless networks:

> sudo airodump-ng eth1

   
Then notice the channel number of the wireless network you want to crack.

Quit aircrack-ng and start it again with med specific channel number to collect packages faster:

> sudo airodump-ng -c 4 -w dump eth1

   
Then wait and let it collect about 500K IVS and the try the do the actual crack:

> sudo aircrack-ng -b 0a:0b:0c:0d:0e:0f dump-01.cap

   
The MAC after the -b option is the BSSID of the target and dump-01.cap the file containing the captured packets.

A new project called Pyrit is currently under it’s way. “Pyrit takes a step ahead in attacking WPA-PSK and WPA2-PSK, the protocol that today de-facto protects public WIFI-airspace. The project’s goal is to estimate the real-world security provided by these protocols. Pyrit does not provide binary files or wordlists and does not encourage anyone to participate or engage in any harmful activity. This is a research project, not a cracking tool.

Pyrit’s implementation allows to create massive databases, pre-computing part of the WPA/WPA2-PSK authentication phase in a space-time-tradeoff. The performance gain for real-world-attacks is in the range of three orders of magnitude which urges for re-consideration of the protocol’s security. Exploiting the computational power of GPUs, this is currently by far the most powerful attack against one of the world’s most used security-protocols.”

Go to our new site- shankee.com
