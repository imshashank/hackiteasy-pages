---
# http://learn.getgrav.org/content/headers
title: Start networking in BackTrack 4
slug: start-networking-in-backtrack-4
# menu: Start networking in BackTrack 4
date: 28-12-2011
published: true
publish_date: 28-12-2011
# unpublish_date: 28-12-2011
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
        - backtrack
        - hacking
        - linux
        - tutorial
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [backtrack,hacking,linux,tutorial]
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

So you have installed BackTrack 4 and are ready for hacking, but you can’t connect to the internet.  
Well, Backtrack won’t start the networking automatically to maintain stealth boot.  
So, to initiate networking and enabling internet enter the following command:  
    <pre style="-webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; background-color: black; border-bottom-color: rgb(133, 133, 133); border-bottom-style: solid; border-bottom-width: 1px; border-color: initial; border-left-color: rgb(133, 133, 133); border-left-style: solid; border-left-width: 1px; border-right-color: rgb(133, 133, 133); border-right-style: solid; border-right-width: 1px; border-style: initial; border-top-color: rgb(133, 133, 133); border-top-style: solid; border-top-width: 1px; color: #858585; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: 1.1em; orphans: 2; padding-bottom: 1em; padding-left: 1em; padding-right: 1em; padding-top: 1em; text-align: -webkit-auto; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px;">root@bt:~# <span style="color: red;">/etc/init.d/networking start</span><br></br>

This command will start networking/internet in backtrack.

have fun 🙂



Go to our new site- shankee.com
