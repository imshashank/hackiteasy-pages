---
# http://learn.getgrav.org/content/headers
title: Make XP faster as never before
slug: make-xp-faster-as-never-before
# menu: Make XP faster as never before
date: 05-06-2009
published: true
publish_date: 05-06-2009
# unpublish_date: 05-06-2009
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
        - microsoft
        - vista
        - windows
        - XP
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hack,microsoft,vista,windows,XP]
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

Yet another series of tricks to significantly increase your windows XP’s speed. This include removing uselessly enabled options that do nothing but just slow down the PC. Just follow these simple steps and boost up your PC to a new level.

Disable CD Autorun  
( WinXP PRO Only)

1) Click Start, Run and enter GPEDIT.MSC

2) Go to Computer Configuration, Administrative Templates, System.

3) Locate the entry for Turn autoplay off and modify it as you desire.

Speed Up Browsing  
When you connect to a web site your computer sends information back and forth. Some of this information deals with resolving the site name to an IP address, the stuff that TCP/IP really deals with, not words. This is DNS information and is used so that you will not need to ask for the site location each and every time you visit the site. Although Windows XP and Windows XP have a pretty efficient DNS cache, you can increase its overall performance by increasing its size. You can do this with the registry entries below:

Windows Registry Editor Version 5.00  
[HKEY\_LOCAL\_MACHINESYSTEMCurrentControlSetServicesDnscacheParameters]  
“CacheHashTableBucketSize”=dword:00000001  
“CacheHashTableSize”=dword:00000180  
“MaxCacheEntryTtlLimit”=dword:0000fa00  
“MaxSOACacheEntryTtlLimit”=dword:0000012d

Make a new text file and rename it to dnscache.reg. Then copy and paste the above into it and save it. Merge it into the registry.

 DISABLE INDEXING SERVICES

Indexing Services is a small little program that uses large amounts of RAM and can often make a computer endlessly loud and noisy. This system process indexes and updates lists of all the files that are on your computer. It does this so that when you do a search for something on your computer, it will search faster by scanning the index lists. If you don’t search your computer often, or even if you do search often, this system service is completely unnecessary. To disable do the following:

1. Go to Start  
2. Click Settings  
3. Click Control Panel  
4. Double-click Add/Remove Programs  
5. Click the Add/Remove Window Components  
6. Uncheck the Indexing services  
7. Click Next

OPTIMISE DISPLAY SETTINGS

Windows XP can look sexy but displaying all the visual items can waste system resources. To optimize:

1.Go to Start  
2. Click Settings  
3. Click Control Panel  
4. Click System  
5. Click Advanced tab  
6. In the Performance tab click Settings  
7. Leave only the following ticked:  
– Show shadows under menus  
– Show shadows under mouse pointer  
– Show translucent selection rectangle  
– Use drop shadows for icons labels on the desktop  
– Use visual styles on windows and buttons

 SPEEDUP FOLDER BROWSING

You may have noticed that everytime you open my computer to browse folders that there is a slight delay. This is because Windows XP automatically searches for network files and printers everytime you open Windows Explorer. To fix this and to increase browsing significantly:

1. Open My Computer  
2. Click on Tools menu  
3. Click on Folder Options  
4. Click on the View tab.  
5. Uncheck the Automatically search for network folders and printers check box  
6. Click Apply  
7. Click Ok  
8. Reboot your computer  
 REMOVE THE DESKTOP PICTURE

Your desktop background consumes a fair amount of memory and can slow the loading time of your system. Removing it will improve performance.

1. Right click on Desktop and select Properties  
2. Select the Desktop tab  
3. In the Background window select None  
4. Click Ok

DISABLE UNNECESSARY SERVICES

Because Windows XP has to be all things to all people it has many services running that take up system resources that you will never need. Below is a list of services that can be disabled on most machines:

Alerter  
Clipbook  
Computer Browser  
Distributed Link Tracking Client  
Fast User Switching  
Help and Support – (If you use Windows Help and Support leave this enabled)  
Human Interface Access Devices  
Indexing Service  
IPSEC Services  
Messenger  
Netmeeting Remote Desktop Sharing (disabled for extra security)  
Portable Media Serial Number  
Remote Desktop Help Session Manager (disabled for extra security)  
Remote Procedure Call Locator  
Remote Registry (disabled for extra security)  
Remote Registry Service  
Secondary Logon  
Routing & Remote Access (disabled for extra security)  
Server  
SSDP Discovery Service – (Unplug n’ Pray will disable this)  
Telnet  
TCP/IP NetBIOS Helper  
Upload Manager  
Universal Plug and Play Device Host  
Windows Time  
Wireless Zero Configuration (Do not disable if you use a wireless network)  
Workstation  
To disable these services:

Go to Start and then Run and type “services.msc”  
Doubleclick on the service you want to change  
Change the startup type to ‘Disable”

 REMOVE ANNOYING DELETE CONFIRMATION MESSAGES

Although not strictly a performance tweak I love this fix as it makes my machine ‘feel’ faster. I hate the annoying ‘are you sure?’ messages that XP displays, especially if I have to use a laptop touchpad to close them. To remove these messages:

1. Right-click on the ‘Recycle Bin’ on the desktop and then click ‘Properties’

2. Clear the ‘Display Delete Confirmation Dialog’ check box and click ‘Ok’

If you do accidently delete a file don’t worry as all is not lost. Just go to your Recycle Bin and ‘Restore’ the file.

Go to our new site- shankee.com
