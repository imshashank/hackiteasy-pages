---
# http://learn.getgrav.org/content/headers
title: Renaming the Windows Logon Box
slug: renaming-the-windows-logon-box
# menu: Renaming the Windows Logon Box
date: 11-06-2009
published: true
publish_date: 11-06-2009
# unpublish_date: 11-06-2009
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
        - computers tricks
        - hacking
        - tech
        - windows
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [computers tricks,hacking,tech,windows]
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

Rename the Windows Logon box, just follow the simple steps. Mail me if any problem!!

Run regedit and go to HKEY\_Local\_MachineSoftwareMicrosoft WindowsCurrentVersionWinlogon  
Then add or change the key:  
LegalNoticeCaption REG\_SZ=”(Title for Box)”

And the same for this key:  
LegalNoticeText REG\_SZ=”(Message to be displayed in the box)”

Go to our new site- shankee.com
