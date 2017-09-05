---
# http://learn.getgrav.org/content/headers
title: BSNL GPRS TRICK(NOT SURE ABOUT ITS WORKING)
slug: bsnl-gprs-tricknot-sure-about-its-working
# menu: BSNL GPRS TRICK(NOT SURE ABOUT ITS WORKING)
date: 31-05-2008
published: true
publish_date: 31-05-2008
# unpublish_date: 31-05-2008
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
        - hacking
        - mobile
        - mobile phones
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hacking,mobile,mobile phones]
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

BSNL GPRS TRICK(NOT SURE ABOUT ITS WORKING)

server has a major bug in it, by which it fails to block two simultaneous connections from the phone and establishes a connection with full internet working,Supported devices: all phones with multichannel gprs support For connection on your mobile phone.

1) Make two connections like BSNL111 and BSNL222

2) Select the application you got to have the full connection working on. Surpassingly “web” now just select “BSNL111” profile and select a link like wap.cellone.in the page will get open, just press the red button such that the “web” application goes in the background. Make sure that the gprs connection is still established with the web app.Two parallel lines on the top left of the screen will confirm this

3) Now open any other app that requires web connection like opera. Select BSNL222 and open any other link like wap.google.com, u will get AN error.the aim of using the other app is to perform multi-channel gprs,this is verified by seeing some dots on the pre-existing connection established by “web” ACCESS DENIED.Technical description: 403 Forbidden – You are not allowed to communicate with the requested resource.”

4) close opera and open web and open a site like esato.com

 5) if everything is done as said here then esato will load and THTS IT! We have the whole internet! For connection on pc.

 1)create a connection and enter the number to be dialed as \*99\*\*\*1#

2) enter the string as extra initialization command

3)now dial from pc, the connection will be established

4)pick the phone and open “web” open “wap.cellone.in” the phone shows error .

5) close “web” and then from the browser open and thts it !

The whole intenet is here .settings for profiles apn: celloneportal ip: 192.168.51.163 port : 8080 leave other fields blank as they are of the least concern! the browser settings on pc 2 go the same as mentioned above!

Go to our new site- shankee.com
