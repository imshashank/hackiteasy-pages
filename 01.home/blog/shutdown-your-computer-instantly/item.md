---
# http://learn.getgrav.org/content/headers
title: Shutdown your computer instantly
slug: shutdown-your-computer-instantly
# menu: Shutdown your computer instantly
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
        - hack
        - microsoft
        - tech
        - windows
        - XP
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hack,microsoft,tech,windows,XP]
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

You can make your shut down process a bit faster by the following tweak.

Steps: ([download the registry file](http://computerhelper.sitesled.com/RegFiles/FasterShutdown.exe))

1. This step is very important.  
Export (right click > Export) the following keys and save it to a safer place.

HKEY CURRENT USERControl PanelDesktop  
HKEY\_LOCAL\_MACHINESYSTEMCurrentControlSetControl

2. Open [Notepad](http://www.tricksystem.com/2009/01/make-windows-xp-shutdown-faster-than.html#), copy and paste the following to the Notepad.

Windows Registry Editor Version 5.00

[HKEY\_CURRENT\_USERControl PanelDesktop]  
“AutoEndTasks”=”1”  
“HungAppTimeout”=”1000”  
“WaitToKillAppTimeout”=”2000”

[HKEY\_LOCAL\_MACHINESYSTEMCurrentControlSetControl]  
“WaitToKillServiceTimeout”=”2000”

3. Save the file and close Notepad.

4. Change extension of the file from .txt (text file) to .reg (registry file).

5. Double click open this file and click Yes and the OK .

Go to our new site- shankee.com
