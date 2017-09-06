---
# http://learn.getgrav.org/content/headers
title: Auto End Tasks to Enable a Proper Shutdown
slug: auto-end-tasks-to-enable-a-proper-shutdown
# menu: Auto End Tasks to Enable a Proper Shutdown
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
        - tech
        - XP
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hack,tech,XP]
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

This reg file automatically ends tasks and timeouts that prevent programs from shutting down and clears the Paging File on Exit.

1. Copy the following (everything in the box) into notepad.

QUOTE  
Windows Registry Editor Version 5.00

[HKEY\_LOCAL\_MACHINESYSTEMCurrentControlSetControlSession ManagerMemory Management]  
“ClearPageFileAtShutdown”=dword:00000001

[HKEY\_USERS.DEFAULTControl PanelDesktop]  
“AutoEndTasks”=”1”

[HKEY\_LOCAL\_MACHINESYSTEMCurrentControlSetControl]  
“WaitToKillServiceTimeout”=”1000”

2. Save the file as shutdown.reg

3. Double click the file to import into your registry.

NOTE: If your anti-virus software warns you of a “malicious” script, this is normal if you have “Script Safe” or similar [technology](http://www.tricksystem.com/2008/08/auto-end-tasks-to-enable-proper.html#) enabled.

Go to our new site- shankee.com
