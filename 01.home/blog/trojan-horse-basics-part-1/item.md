---
# http://learn.getgrav.org/content/headers
title: Trojan Horse (Basics) &#8211; Part 1
slug: trojan-horse-basics-part-1
# menu: Trojan Horse (Basics) &#8211; Part 1
date: 12-05-2013
published: true
publish_date: 12-05-2013
# unpublish_date: 12-05-2013
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
        - learn to hack
        - trojan
        - tutorial
        - virus
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hack,hacking,learn to hack,trojan,tutorial,virus]
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

Have you watched movie **Troy ? **okay lets leave . Have your wallpaper ever changed automatically ? Have the programs ever started without your initiation ? Have the browser opened unexpected websites automatically ? Simply have you ever felt that someone else is controlling your computer ? **NO ?**

Congrats, you probably haven’t been a victim of trojan yet :).



**A trojan horse is a remote administration tool(RAT). This is some thing extremely dangerous.  A trojan gives ****the full control of victim’s PC to the attacker. **

 A trojan has two parts . One is **client part (Control Panel)** and other is **server part** (meant to be sent to victim).



**The basic methodology of using a trojan is as follows:-**



**1.** Attacker creates an executable file of size in kbs. This  is  server part of trojan and mostly called as server.exe

[![](http://3.bp.blogspot.com/_ufGdCaQ3M3k/TRN7W-XmD-I/AAAAAAAAAAo/HIMtDmmq1Rg/s200/trojan+infected.jpg)](http://3.bp.blogspot.com/_ufGdCaQ3M3k/TRN7W-XmD-I/AAAAAAAAAAo/HIMtDmmq1Rg/s1600/trojan+infected.jpg)

****2**.Attacker might hide this server.exe behind any genuine file like a song or image. Attacker gives this file to victim and victim is supposed to double click on it.**

**3**.As victim run that server part , a port on victim’s computer gets opened and attacker can control his PC sitting remotely in any part of the world through the control panel(client part). Attacker can do anything with victim’s computer remotely that victim himself can do on his computer.



*Note: Now I am assuming that you know a little bit about IP addresses that is lan/internal/private and wan/external/public IP.*

Two different methods of working of Trojan.

**1. Direct Connection **: In this method, after the server part has been installed on victim’s machine, the attacker enters the public IP address assigned to victim’s computer for making a connection to it. But limitations of direct connection is that public IP address is most probably dynamic and gets changed everytime one disconnects and reconnects. So attacker needs to find out IP address of victim each time.Moreover the incoming connection like this is usually restricted by firewall. 

**The main limitation of direct connection is that you can not access the victim who is behind a router or a network beacuse victim’s machine is not assigned public/external/wan IP. It is only assigned private/internal/lan IP which is useless or meaningless for computers outside that network.The wan IP belongs to his router.**

**  
**

**It doesnt matter how attacker is connected to internet. Attacker can be connected to internet any of three means.**

[![](http://3.bp.blogspot.com/_ufGdCaQ3M3k/TSbQCusCwsI/AAAAAAAAAF8/G6GFhmHUaGg/s640/direct1.jpg)](http://3.bp.blogspot.com/_ufGdCaQ3M3k/TSbQCusCwsI/AAAAAAAAAF8/G6GFhmHUaGg/s1600/direct1.jpg)

**  
**  
**Victim is behind a router in this case. (havent inserted the picture of victim behind a network, imagine that )**

[![](http://1.bp.blogspot.com/_ufGdCaQ3M3k/TSbVRTp0hCI/AAAAAAAAAGI/ZEy99VwiUYY/s400/direct2.jpg)](http://1.bp.blogspot.com/_ufGdCaQ3M3k/TSbVRTp0hCI/AAAAAAAAAGI/ZEy99VwiUYY/s1600/direct2.jpg)

**2. Reverse Connection:** In this method, attacker enters his own IP address in server part while configuring it .So when the server part is installed on victim’s computer, it automatically makes connection with client part that is attacker. Also the firewall in victim’s machine would not restrict to outgoing connections. Problem in this case is same that attacker’s IP is also dynamic. But this can be over come easily. Attacker actually enters a domain name in server part which always points to his dynamic IP.



**Reverse connection can bypass a router or a network.**

[![](http://1.bp.blogspot.com/_ufGdCaQ3M3k/TSbQI2WanuI/AAAAAAAAAGE/1MgbXifXMPc/s640/reverse.jpg)](http://1.bp.blogspot.com/_ufGdCaQ3M3k/TSbQI2WanuI/AAAAAAAAAGE/1MgbXifXMPc/s1600/reverse.jpg)

**  
**  
**You might be confused at this point. Kindly mention your queries/doubts in comments.**



Go to our new site- shankee.com
