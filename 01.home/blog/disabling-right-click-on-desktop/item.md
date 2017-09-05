---
# http://learn.getgrav.org/content/headers
title: Disabling right click on desktop
slug: disabling-right-click-on-desktop
# menu: Disabling right click on desktop
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

Today tip is very useful particularly for home users who want to protect their system default settings against unwanted changes that other users can make. For example changes in system desktop appearance, themes, and screen saver as well as other display settings. Using registry editor, you can disable the right click functionality on desktop to access the “Display Properties” dialog box and this will also prevent users to access windows explorer.

 Follow the given steps to disable the right click functionality on desktop:

 To use this feature, you will need to be logged into your computer with administrative rights.

 Click Start button and type regedit in Run option then press Enter for next.![](http://www.computerfreetips.com/images/regedit.gif)

 Here locate the location to:

 HKEY\_CURRENT\_USERSoftwareMicrosoftWindowsCurrentVersionPoliciesExplorer  
![registry](file:///C:/Users/shashank/AppData/Local/Temp/moz-screenshot.png)![regedit](file:///C:/Users/shashank/AppData/Local/Temp/moz-screenshot-1.png)

 ![](http://www.computerfreetips.com/images/NoViewContextMenu.gif)

 Here in right side panel, right click to create a new DWORD value with the name NoViewContextMenu (it is case sensitive), then assign number 1 in value data box.  
![](http://www.computerfreetips.com/images/NoViewContextMenu-value.gif)

  
 Now close the registry editor and restart your computer after any changes to go into effect.  
 But next time, if you want to enable right click functionality on desktop then simply change the value of data box or delete the NoViewContextMenu DWORD item.

Go to our new site- shankee.com
