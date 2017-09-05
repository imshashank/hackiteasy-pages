---
# http://learn.getgrav.org/content/headers
title: Installing nessus on ubuntu
slug: installing-nessus-on-ubuntu
# menu: Installing nessus on ubuntu
date: 14-01-2011
published: true
publish_date: 14-01-2011
# unpublish_date: 14-01-2011
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
        - Hack Tools
        - hacking
        - internet
        - linux
        - software
        - tutorial
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [Hack Tools,hacking,internet,linux,software,tutorial]
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

[![](http://1.bp.blogspot.com/_V2JZuLkPrjQ/TTHxHtEWcXI/AAAAAAAAI48/P-OAEDciKpA/s200/nessus.jpg)](http://1.bp.blogspot.com/_V2JZuLkPrjQ/TTHxHtEWcXI/AAAAAAAAI48/P-OAEDciKpA/s1600/nessus.jpg)

Installing nessus on an Ubuntu or any other Linux machine can be a difficult task. So here we bring out a tutorial to ease you out to simplify the task of installing Nessus server. Here we have shown the installation on Ubuntu machine this could be used on nay other debian of linux as well.

**The totorial starts here-**

Download Nessus Nessus-4.0.1-ubuntu810\_amd64.deb for Ubuntu 9.04 from http://www.nessus.org.

> dpkg -i Nessus-4.0.1-ubuntu810\_amd64.deb
> 
> Selecting previously deselected package nessus.  
> (Reading database … 128086 files and directories currently installed.)  
> Unpacking nessus (from Nessus-4.0.1-ubuntu810\_amd64.deb) …  
> Setting up nessus (4.0.1) …  
> nessusd (Nessus) 4.0.1. for Linux  
> (C) 1998 – 2009 Tenable Network Security, Inc.
> 
> – Please run /opt/nessus/sbin/nessus-adduser to add a user  
> – Register your Nessus scanner at http://www.nessus.org/register/ to obtain  
> all the newest plugins  
> – You can start nessusd by typing /etc/init.d/nessusd start
> 
> root@testserver:~# /opt/nessus/sbin/nessus-adduser  
> Login : admin  
> Authentication (pass/cert) : [pass]  
> Login password :  
> Login password (again) :  
> Do you want this user to be a Nessus ‘admin’ user ? (can upload plugins, etc…) (y/n) [n]: y  
> User rules  
> ———-  
> nessusd has a rules system which allows you to restrict the hosts  
> that admin has the right to test. For instance, you may want  
> him to be able to scan his own host only.
> 
> Please see the nessus-adduser manual for the rules syntax
> 
> Enter the rules for this user, and enter a BLANK LINE once you are done :  
> (the user can have an empty rules set)
> 
> Login : admin  
> Password : \*\*\*\*\*\*\*\*\*\*\*  
> This user will have ‘admin’ privileges within the Nessus server  
> Rules :  
> Is that ok ? (y/n) [y] y  
> User added

Register for home feed.

> /opt/nessus/bin/nessus-fetch –register xxxx-xxxx-xxxx-xxxx-xxxxx  
> /etc/init.d/nessusd start

To run Nessus from the command line you use an option “q” that is for batch mode. This allows running from a terminal and without the GUI interface to the client. Handy if you would like to script or automate your scans.

Using batch mode the IP’s that are to be scanned are read from a file.

> echo “192.168.0.1″ >> iptoscan.txt
> 
> /opt/nessus/bin/nessus -q 127.0.0.1 1241 admin password iptoscan.txt scanresults2.html -T htm

Replace “admin password” in your command with the login and password you chose when you created the user using nessus-adduser.

> ~$ OpenVAS-Client –help  
> Usage:  
> OpenVAS-Client [OPTION…] – client for the OpenVAS security scanner
> 
> Help Options:  
> -?, –help Show help options  
> –help-all Show all help options  
> –help-gtk Show GTK+ Options
> 
> Application Options:  
> -v, –version Display version information  
> -n, –no-pixmap No pixmaps  
> -q, –batch-mode= Batch-mode scan  
> -c, –config-file=<.rcfile> Configuration file  
> -T, –output-type=[nbe|html|text|xml|tex] Output format  
> -V, –verbose Display status messages in batch mode  
> -p, –list-plugins Obtain list of plugins installed on the server  
> -P, –list-prefs Obtain list of server and plugin preferences  
> -i, –in-report= Input file (report conversion)  
> -o, –out-report= Output file (report conversion)  
> -x, –dont-check-ssl-cert Override SSL “paranoia” question preventing OpenVAS-Client from checking certificates  
> -S, –sqlize-output Issue SQL output for -p and -P (experimental)  
> -s, –list-sessions= List sessions  
> -R, –restore-session= Restore session  
> –display=DISPLAY X display to use

Please do comment if this has been helpful.  
by [hackiteasy](http://www.hackiteasy.com/)

Go to our new site- shankee.com
