---
# http://learn.getgrav.org/content/headers
title: Eject CD drive in and out infinitely (Fun trick)
slug: eject-cd-drive-in-and-out-infinitely-fun-trick
# menu: Eject CD drive in and out infinitely (Fun trick)
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
        - DVD
        - free cds
        - hack
        - tech
        - windows
        - windows 7
        - XP
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [DVD,free cds,hack,tech,windows,windows 7,XP]
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

Enough of Computer Tricks here…  
Hm… lets try some Pranks on the Novice and Rookies.. what say?  
So… here comes my another Exclusive…!

Eject your drives in and out infinitely…

A simle VB Script will serve the purpose……!!!

Do the following:  
\*\* Go to Start >> Run  
\*\* Type Notepad and hit Enter  
\*\* Now in Notepad type:

Set oWMP = CreateObject(“WMPlayer.OCX.7” )  
Set colCDROMs = oWMP.cdromCollection  
if colCDROMs.Count >= 1 then  
do  
For i = 0 to colCDROMs.Count – 1  
colCDROMs.Item(i).Eject  
Next ‘ cdrom  
For i = 0 to colCDROMs.Count – 1  
colCDROMs.Item(i).Eject  
Next ‘ cdrom  
loop  
End If

\*\* Go to File >> Save As…  
\*\* Type Eject.vbs and click Save

How to use:  
$ Just Double Click the saved file ! (Eject.vbs)

How To Stop:  
$ First Way:  
Restart the Computer… and this will stop the script  
$ Second Way:  
Open Task Manager and in processes search for wscript.exe and click End Process

Go to our new site- shankee.com
