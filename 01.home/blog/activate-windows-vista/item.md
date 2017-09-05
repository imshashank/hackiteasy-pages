---
# http://learn.getgrav.org/content/headers
title: Activate WIndows Vista
slug: activate-windows-vista
# menu: Activate WIndows Vista
date: 30-12-2008
published: true
publish_date: 30-12-2008
# unpublish_date: 30-12-2008
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
        - vista
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hacking,vista]
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

### A simple trick that let’s you use Vista infinitely..

###  <a name="Registry_Instructions_for_SkipRearm">Registry Instructions for SkipRearm</a>

1. Preliminary experiment, check the activation expiry date with the command: slmgr -xpr
2. Launch Regedit. Click the Start Orb and write regedit and click on it.
3. Navigate to this path:  
\*\* HKEY\_LOCAL\_MACHINESOFTWARE MicrosoftWindows NTCurrentVersionSL
4. Double-click SkipRearm and change the value to 1.
5. Note: this registry hack does not make any sense on a machine which has already been activated!
6. Now remember to run the 30 day extension command: slmgr -rearm
7. Restart the machine. After it reboots, run slmgr -xpr and check the expiry date.
8. Check the registry setting SkipRearm, slmgr resets the value to zero.

### Screen Shot of SkipRearm

![Vista Activation Hack - SkipRearm](http://www.computerperformance.co.uk/images/Vista/skiprearm.jpg)

Go to our new site- shankee.com
