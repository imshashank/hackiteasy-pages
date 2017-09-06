---
# http://learn.getgrav.org/content/headers
title: New simple Windows hacks
slug: new-simple-windows-hacks
# menu: New simple Windows hacks
date: 07-06-2009
published: true
publish_date: 07-06-2009
# unpublish_date: 07-06-2009
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
        - tech
        - windows
        - windows 7
        - XP
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hack,hacking,tech,windows,windows 7,XP]
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

I have some secret Windows tips and tricks here. Many are problems which you may encounter, but for which Windows does not provide a ready made solution.

Registry  
Display a banner each time Windows boots

 1. Start -> Run  
 2. Type regedit  
 3. Go to the key HKEY\_LOCAL\_MACHINESOFTWAREMicrosoftWindowsCurrentVersionWinLogon  
 4. Create a new string value in the right pane named LegalNoticeCaption and enter the value that you want to see in the menubar  
 5. Create a new string value and name it LegalNoticeText. Modify it and insert the message you want to display each time Windows boots.

Windows  
Shutting down Windows the fastest way

 1. Start -> Run  
 2. Type rundll.exe user.exe,exitwindows

Internet Explorer  
Your browser logo shows something other than the IE logo. Maybe you have installed your ISP software and you have a different logo on the top right. How do you remove it?

 1. Close all browser windows  
 2. Start -> Run  
 3. Type RunDLL32.EXE IEdkcs32.dll,Clear  
 4. Click on OK, and start Internet Explorer. You should find the old spinning IE logo.

Go to our new site- shankee.com
