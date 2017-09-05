---
# http://learn.getgrav.org/content/headers
title: Increase your internet speed
slug: increase-your-internet-speed
# menu: Increase your internet speed
date: 04-06-2009
published: true
publish_date: 04-06-2009
# unpublish_date: 04-06-2009
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
        - internet
        - make xp faster
        - tech
        - vista
        - windows 7
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [internet,make xp faster,tech,vista,windows 7]
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

This is not just one trick but a series of simple trick that lets you significantly increase you internet speed and i guarantee you an increase in your internet speed. This trick works on all windows machine including XP, Vista and windows 7.

1] go to desktop->My computer-(right click on)->properties->then go HARDWARE tab-> Devicemanager-> now u see a window of Device manager  
then go to Ports->Communication Port(double click on it and Open).  
after open u can see a Communication Port properties.  
go the Port Setting:—-  
and now increase ur “Bits per second” to 128000.  
and “Flow control” change 2 Hardware

2]type this coding in notepad and save as .reg and then execute this file….this will increase ur surfing n downloading speed…..

REGEDIT4  
[HKEY\_LOCAL\_MACHINESYSTEMCurrentControlSetServic esTcpipParameters]  
“SackOpts”=dword:00000001  
“TcpWindowSize”=dword:0005ae4c  
“Tcp1323Opts”=dword:00000003  
“DefaultTTL”=dword:00000040  
“EnablePMTUBHDetect”=dword:00000000  
“EnablePMTUDiscovery”=dword:00000001  
“GlobalMaxTcpWindowSize”=dword:0005ae4c

3]Xp reserves 20% bandwith,  
to unreserve it,follow following steps:

a)Click Start

b)Run:”gpedit.msc”

c)Goto:>Local Computer Policy  
——-–>Computer Configuration  
——-–>Administrative Templates  
——-–>Network–>QOS Packet Scheduler  
——-–>Limit Reservable Bandwidth

d) Double click on Limit Reservable bandwidth

e)Select Enable

f) Change 20% to 0%

g)Click Apply

Enjoy!

Go to our new site- shankee.com
