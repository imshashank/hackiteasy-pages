---
# http://learn.getgrav.org/content/headers
title: Make Mozilla Firefox 10x Faster!!!
slug: make-mozilla-firefox-10x-faster
# menu: Make Mozilla Firefox 10x Faster!!!
date: 08-05-2008
published: true
publish_date: 08-05-2008
# unpublish_date: 08-05-2008
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
        - mozilla speedup
        - speed up
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [mozilla speedup,speed up]
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

New Modified Trick to speed up your firefox….  
See that here….[  
http://www.shankee.com](http://www.shankee.com/)

THIS IS A VERY SIMPLE TRICK. NO SOFTWARE REQUIRED.

1. Type “about:config” into the address bar and hit enter. Scroll down and look for the following entries:

2. Alter the entries as follows:

Set “network.http.pipelining” to “true”  
Set “network.http.proxy.pipelining” to “true”

set “network.http.pipelining.maxrequests” to some number like 30. This means it will make 30 requests at once.

3. Lastly right-click anywhere and select New-> Integer. Name it “nglayout.initialpaint.delay” and set its value to “0”. This value is the amount of time the browser waits before it acts on information it recieves.

NOTE: this trick only works for broadband users not for dialup.

Go to our new site- shankee.com
