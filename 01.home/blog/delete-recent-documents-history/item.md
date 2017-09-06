---
# http://learn.getgrav.org/content/headers
title: Delete Recent Documents history
slug: delete-recent-documents-history
# menu: Delete Recent Documents history
date: 14-06-2009
published: true
publish_date: 14-06-2009
# unpublish_date: 14-06-2009
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
        - windows
        - XP
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [computers tricks,windows,XP]
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

Any document that you open in Windows is added to the Recent Documents list. Now with this simple trick you can stop that!!!

\* Start ==> Run ==> Type “Regedit”

\* [HKEY\_CURRENT\_USERSoftwareMicrosoftWindows  
 CurrentVersionPoliciesExplorer]

\* Right Click on the right Pane and create a new DWORD value.

\* Assign Value Name as ***“NoRecentDocsHistory”***

\* Data Type as ***“REG\_DWORD (DWORD Value)”***

\* If Value Data = ***0 : disable restriction  
 1 : enable restriction***

Go to our new site- shankee.com
