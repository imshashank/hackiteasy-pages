---
# http://learn.getgrav.org/content/headers
title: How to Disable or Remove ‘Send Feedback’ Button in Windows 7
slug: how-to-disable-or-remove-send-feedback-button-in-windows-7
# menu: How to Disable or Remove ‘Send Feedback’ Button in Windows 7
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
        - microsoft
        - tech
        - windows
        - windows 7
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hack,microsoft,tech,windows,windows 7]
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

In Windows 7 beta version, there is a **send feedback** button on the right side of the title bar on each and every window opened on desktop. Well there are two reasons for which one can feel bothered.

1. There are so many times you can accidentally click on that button and then every damn internet options will try and start themselves as if you have done a terrible mistake.

2. Even if you try and send feedback, believe me nothing will happen unless your issue is the commonest one

So why don’t we get rid of that service which either annoys or remains inactive when needed?

Here is how to hack it

1. Go to **Run**
2. Type **regedit **(Registry Editor), press ENTER.
3. Now navigate to the following registry key:  
**HKEY\_CURRENT\_USERControl PanelDesktop**
4. ****Add in a new **DWORD (32-bit) Value** named **FeedbackToolEnabled**, and then set its value data as **0**.
5. Log on again for the change to take effect.

 

Go to our new site- shankee.com
