---
# http://learn.getgrav.org/content/headers
title: Hiding the blogger nav bar or the blogger bar
slug: hiding-the-blogger-nav-bar-or-the-blogger-bar
# menu: Hiding the blogger nav bar or the blogger bar
date: 16-09-2008
published: true
publish_date: 16-09-2008
# unpublish_date: 16-09-2008
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
        - hackiteasy
        - internet
        - sites
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [computers tricks,hackiteasy,internet,sites]
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

Here’s a simple trick to hide the blogger nav bar or the blogger bar that appears at the top when you create a new blog at blogger.com,  
Follow the simple steps and it would be gone..

Go to Edit Layout  
The to Edit Html..  
Go to

]]>  
And paste this right after it…

\#navbar-iframe {  
 height:0px;  
 visibility:hidden;  
 display:none;  
 }

Also enclose the above in tabs..  
( thats is a tab at brginning and a tab at end)  
that’s it .  
It’s that simple…

I still got no idea if removing a blogger bar violates Blogger’s Terms and conditions or not  
..

Go to our new site- shankee.com
