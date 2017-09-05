---
# http://learn.getgrav.org/content/headers
title: Fasttrack &#8211; an automated penetration tool for linux
slug: fasttrack-an-automated-penetration-tool-for-linux
# menu: Fasttrack &#8211; an automated penetration tool for linux
date: 19-01-2011
published: true
publish_date: 19-01-2011
# unpublish_date: 19-01-2011
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
        - dos
        - hack tool
        - hacking
        - internet
        - linux
        - penetration
        - software
        - website
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [dos,hack tool,hacking,internet,linux,penetration,software,website]
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

Fast-Track is a python based open-source project aimed at helping Penetration Testers in an effort to identify, exploit, and further penetrate a network. Fast-Track was originally conceived when a h4cker was on a penetration test and found that there was generally a lack of tools or automation in certain attacks that were normally extremely advanced and time consuming.

In an effort to reproduce some advanced attacks and propagate it down , he ended up writing Fast-Track for the public. Many of the issues Fast-Track exploits are due to improper sanitizing of client-side data within web applications, patch management, or lack of hardening techniques. All of these are relatively simple to fix if you know what to look for, but as penetration testers are extremely common findings for us. Fast-Track arms the penetration tester with advanced attacks that in most cases have never been performed before. Sit back relax, crank open a can of jolt cola and enjoy the ride.

**Installing Fast-Track:**  
make sure you have the latest version of Subversion

Open a terminal and type the following command (In Linux offcourse) :

> svn co http://svn.thepentest.com/fasttrack /path-to-install/

The svn co simply means “check out” the latest version of Fast-Track, the /path-to-install/ is the directory you want to install Fast-Track.

If you want to update Fast-Track after you check out the files, simply type svn update, or use the Fast-Track menu to update.

When you first check out Fast-Track, there are a few modules that need to be installed, fortunately, Fast-Track comes with a setup file that helps you install the files needed. From the command line and in the Fast-Track menu, simply type:

> python setup.py install

Follow the guide for installing Fast-Track, note that the setup does NOT install Metasploit for you. If you don’t have Metasploit installed, some applications will not work properly. Ensure that you enter the right path to Metasploit.

Once installation has finished, run Fast-Track, if it errors out saying you do not have the proper requirements, type yes to try a different type of install. If this still doesn’t work you will need to manually install the requirements.

now to run Fast-Track type:

 
    <pre style="border-style: inset; border-width: 1px; height: 34px; margin: 0px; overflow: auto; padding: 6px; text-align: left; width: 480px;">./fast-track.py

 

  
to run the web GUI mod: 
    <pre style="border-style: inset; border-width: 1px; height: 34px; margin: 0px; overflow: auto; padding: 6px; text-align: left; width: 480px;">./ftgui

Open a browser and go to http://127.0.0.1:44444

Fast-Track HomePage: [http://www.thepentest.com](http://www.thepentest.com/)

  
  
[hackiteasy](http://www.blogger.com/) 

Go to our new site- shankee.com
