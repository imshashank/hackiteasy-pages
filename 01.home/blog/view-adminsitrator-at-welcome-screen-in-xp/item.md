---
# http://learn.getgrav.org/content/headers
title: View adminsitrator at welcome screen in XP
slug: view-adminsitrator-at-welcome-screen-in-xp
# menu: View adminsitrator at welcome screen in XP
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
        - make xp faster
        - tech
        - XP
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hack,make xp faster,tech,XP]
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

By default windows XP doesn’t show the Administrator in the user list at the welcome screen. This simple trick lets you just display admin account at the welcome scree.  
Here’s a way to get around it.Just follow the simple steps.

Now head up to HKEY\_LOCAL\_MACHINESoftwareMicrosoftWindowsNTCurrentVersionWinlogonSpecialAccountsUserlist

create a new DWORD entry and name it as Administrator and change its value to 1.

exit and reboot for the changes to take effect.  
To change it back change its value to 0 or simply delete the key.

Go to our new site- shankee.com
