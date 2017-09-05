---
# http://learn.getgrav.org/content/headers
title: Learn how to Hack Wifi Password
slug: learn-how-to-hack-wifi-password
# menu: Learn how to Hack Wifi Password
date: 23-10-2012
published: true
publish_date: 23-10-2012
# unpublish_date: 23-10-2012
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
        - free
        - hack wifi password
        - hacking
        - internet
        - password
        - tutorial
        - wifi
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [free,hack wifi password,hacking,internet,password,tutorial,wifi]
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

This tutorial teaches you how to hack wifi passowrd in just 10 to 15 minutes. This tutorial explains How to Hack or Crack Wifi Password. This hack will work on hacking WEP encryption password.  
So guys tighten your belts for new hack and lets start hack wifi. STEPS TO HACK WIFI OR WIRELESS PASSWORD

1. Get the Backtrack-Linux CD. Backtrack Linux Live CD(best Linux available for hackers with more than 2000 hacking tools inbuilt). (FREE !!)  
Download Backtrack Linux Live CD from here: http://http://www.backtrack-linux.org/downloads/

2. SCAN TO GET THE VICTIM

Get the victim to attack that is whose password you want to hack or crack.  
Now Enter the Backtrack Linux CD into your CD drive and start it. Once its started click on the black box in the lower left corner to load up a “CONSOLE” . Now you should start your Wifi card. To do it so type

**airmon-ng**

You will see the name of your wireless card. (mine is named “ath0”) From here on out, replace “ath0” with the name of your card. Now type

**airmon-ng stop ath0**

then type:

**ifconfig wifi0 down**

then type:

**macchanger –mac 00:11:22:33:44:55 wifi0**

then type:

**airmon-ng start wifi0**

The above steps i have explained is to spoof yourself from being traced. In above step we are spoofing our MAC address, this will keep us undiscovered.

Now type:

**airodump-ng ath0**

Now you will see a list of wireless networks in the Console. Some will have a better signal than others and its always a good idea to pick one that has a best signal strength otherwise it will take huge time to crack or hack the password or you may not be able to crack it at all.  
Once you see the networks list, now select the network you want to hack. To freeze the airodump screen HOLD the CNTRL key and Press C.

3. SELECTING NETWORK FOR HACKING

Now find the network that you want to crack and MAKE SURE that it says the encryption for that network is WEP. If it says WPA or any variation of WPA then move on…you can still crack WPA with backtrack and some other tools but it is a whole other ball game and you need to master WEP first.

Once you’ve decided on a network, take note of its channel number and bssid. The bssid will look something like this —

**00:23:69:bb:2d:of**

The Channel number will be under a heading that says “CH”.

Now in the same CONSOLE window type:

**airodump-ng -c (channel) -w (file name) –bssid (bssid) ath0**

The file name can be whatever you want. This file is the place where airodump is going to store the packets of info that you receive to later crack. You don’t even put in an extension…just pick a random word that you will remember.

Note: If you want to crack more than one network in the same session, you must have different file names for each one or it won’t work. I usually name them as ben1, ben2 etc.

Once you typed in that last command, the screen of airodump will change and start to show your computer gathering packets. You will also see a heading marked “IV” with a number underneath it. This stands for “Initialization Vector” but in general terms all this means is “packets of info that contain characters of the password.” Once you gain a minimum of 5,000 of these IV’s, you can try to crack the password. I’ve cracked some right at 5,000 and others have taken over 60,000. It just depends on how long and difficult they made the password. More difficult is password more packets you will need to crack it.

4. Cracking the WEP password

Now leave this Console window up and running and open up a 2nd console window.  
In this window type:

**aireplay-ng -1 0 -a (bssid) -h 00:11:22:33:44:55 ath0**

This will send some commands to the router that basically it is to associate your computer even though you are not officially connected with the password. If this command is successful, you should see about 4 lines of text print out with the last one saying something similar to “Association Successful :-)”

If this happens, then good! You are almost there.

Now type:  
**aireplay-ng -3 -b (bssid) -h 00:11:22:33:44:55 ath0**

This will generate a bunch of text and then you will see a line where your computer is gathering a bunch of packets and waiting on ARP and ACK. Don’t worry about what these mean…just know that these are your meal tickets. Now you just sit and wait. Once your computer finally gathers an ARP request, it will send it back to the router and begin to generate hundreds of ARP and ACK per second. Sometimes this starts to happen within seconds…sometimes you have to wait up to a few minutes. Just be patient. When it finally does happen, switch back to your first Console window and you should see the number underneath the IV starting to rise rapidly. This is great! It means you are almost finished! When this number reaches AT LEAST 5,000 then you can start your password crack. It will probably take more than this but I always start my password cracking at 5,000 just in case they have a really weak password.

Now you need to open up a 3rd and final console window. This will be where we actually crack the password.   
Now type:  
**aircrack-ng -b (bssid) (filename)-01.cap**

Remember the file name you made up earlier? Mine was “Ben”. Don’t put a space in between it and -01.cap here. Type it as you see it. So for me, I would type wepkey-01.cap  
Once you have done this you will see aircrack fire up and begin to crack the password. typically you have to wait for more like 10,000 to 20,000 IV’s before it will crack. If this is the case, aircrack will test what you’ve got so far and then it will say something like “not enough IV’s. Retry at 10,000.”   
DON’T DO ANYTHING! It will stay running…it is just letting you know that it is on pause until more IV’s are gathered. Once you pass the 10,000 mark it will automatically fire up again and try to crack it. If this fails it will say “not enough IV’s. Retry at 15,000.” and so on until it finally gets it.

If you do everything correctly up to this point, before too long you will have the password! now if the password looks goofy, dont worry, it will still work. some passwords are saved in ASCII format, in which case, aircrack will show you exactly what characters they typed in for their password. Sometimes, though, the password is saved in HEX format in which case the computer will show you the HEX encryption of the password. It doesn’t matter either way, because you can type in either one and it will connect you to the network.

Take note, though, that the password will always be displayed in aircrack with a colon after every 2 characters. So for instance if the password was “secret”, it would be displayed as:  
**se:cr:et**

This would obviously be the ASCII format. If it was a HEX encrypted password that was something like “0FKW9427VF” then it would still display as:  
**0F:KW:94:27:VF**

Just omit the colons from the password, boot back into whatever operating system you use, try to connect to the network and type in the password without the colons and presto! You are in!

It may seem like a lot to deal with if you have never done it, but after a few successful attempts, you will get very quick with it. If I am near a WEP encrypted router with a good signal, I can often crack the password in just a couple of minutes.

I am not responsible for what you do with this information. Any malicious/illegal activity that you do, falls completely on you because…technically…this is just for you to test the security of your own network.

 

Go to our new site- shankee.com
