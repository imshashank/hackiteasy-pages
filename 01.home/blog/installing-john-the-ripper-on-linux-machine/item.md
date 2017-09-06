---
# http://learn.getgrav.org/content/headers
title: Installing John The ripper on Linux machine
slug: installing-john-the-ripper-on-linux-machine
# menu: Installing John The ripper on Linux machine
date: 15-01-2011
published: true
publish_date: 15-01-2011
# unpublish_date: 15-01-2011
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
        - hack tool
        - hacker
        - hacking
        - linux
        - passwords
        - software
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hack tool,hacker,hacking,linux,passwords,software]
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

John the ripper is undoubtedly one of the best password cracking tool. People have been experiencing some problems with installing it. So here we bring out a tutorial on how to install the famous password cracker on a Linux machine.

This is the method to install and use john the ripper in fedora/ubuntu (and many other linux as well)..

1) Download john the ripper software

[http://www.ziddu.com/download/6365223/jo…ar.gz.html](http://www.ziddu.com/download/6365223/jo...ar.gz.html)

2) Extract it and then copy the text from

<http://www.openwall.com/lists/john-users/2009/09/02/3>

3) Save the copy text in john folder with john.patch.

4) Open terminal and go to john folder

cd Desktop/john-1.7.3.1

5) Now we have to patch our john software with following command

patch -Np1 -i john.patch

6) go to src folder

cd src

7) run this command

make linux-x86-sse2

8) cd .. and goto run folder cd run.

9) Run this commmand

./unshadow /etc/passwd /etc/shadow > filename

10) Finally run this command to crack password

./john filename

and here you have the ripper running.   
by [hackiteasy](http://hackiteasy.com/)

Go to our new site- shankee.com
