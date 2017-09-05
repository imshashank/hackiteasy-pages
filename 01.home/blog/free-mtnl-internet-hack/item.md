---
# http://learn.getgrav.org/content/headers
title: Free Mtnl Internet hack..
slug: free-mtnl-internet-hack
# menu: Free Mtnl Internet hack..
date: 19-08-2008
published: true
publish_date: 19-08-2008
# unpublish_date: 19-08-2008
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
        - BSNL hack
        - free
        - internet
        - mtnl
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [BSNL hack,free,internet,mtnl]
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

Beware this trick is only for educational purpose and is only used to reveal weak security measures used by India’s top Company..  
Reflecting unprofessional structure…and has no intentions to harm anyone at all..

Here is a general procedure to hack any dsl/cable account.I have already hacked MTNL triband and spectra net cable net using this.  
The actual procedure specifically for mtnl is damn simpler but this is the general method.Not for noobs.  
As they say,no pain no gain.  
I am not responsible for any harm caused to you using this method.Though the method is damn simple,the detection is simpler.

This tutorial will explain to you how to hack someone’s internet account through his router.

This hack is based on a security exploit of the router’s default password and the stupidity of the user.

Explanation: when somebody buy’s a xDSL/Cable router, the router is set to manufacture defaults like IP range, user accounts, router table, and most important the security level.  
The last one we will exploit.  
Most routers will have a user friendly setup menu running on port 23 (telnet) and sometimes port 80 (HTTP) or both.  
  
This is what we are looking for.

Step 1.

Get a multie IP range scanner like superscanner  
Or use Nettools 5 the ultimate tool i recommend.  
Get a xDSL/Cabel user IP range. This is a single user IP 212.129.169.196 so the ip range of this Internet provider is 212.129.xxx.xxx most likely it will be from 212.129.1.1 to 212.129.255.255 .

To keep your scanning range not to big it’s smart to scan from 212.129.1.1 to 212.129.1.255 it also depends of your bandwidth how fast the scan will be finished.

The IP address above is just a example any IP range from a xDSL/Cable provider can be used for this hack.  
before you start scanning specify the TCP/IP ports. You know that we are looking for TCP port 23 (telnet) and TCP port 80 (HTTP) so edit the list and select only port 23 and port 80.

Now start scanning and wait for the results.

When finished scanning look for a IP that has a open port 23 and 80. Write them down or remember them.

Step 2.

Way 1

This is important: Most routers have connection log capability so the last thing you want to do is making a connection with your own broadband connection so use a anonymous proxy server or dial-up connection with a fake name and address (56.9 modem for example) when connection to the victim’s router.  
Now get a telnet program. Windows has a standard telnet program just go to start,  
select run and type down “telnet” without the “, click or enter OK.  
Select “connect” than “Remote system” enter IP adres of the victim in the “host name” field press OK.  
wait for your computer to make a connection. This way only works when the router has a open telnet port service running.

Way 2

This is important: Most routers have connection log capability so the last thing you want to do is making a connection with your own broadband connection so use a anonymous proxy server or dial-up connection with a fake name and address (56.9 modem for example) when connection to the victim’s router.  
Open a Internet explorer windows enter the IP address of the victim after the http:// in the address bar.  
This way only works when the router has a open hyper text transfer protocol (http) service running.

Step 3

Entering the user friendly setup menu. 9 out of 10 times the menu is protected by a login name and password. When the user doesn’t change any security value’s the default password stay’s usable.  
So the only thing you have to do is find out what type of router the victim uses. I use this tool: GFILanguard Network Security Scanner is good. When you find out the type of router that’s been used get the right login name and password from this list (not every router is on the list)

Step 4

When you have a connection in telnet or internet explorer you need to look for user accounts.  
PPP, PPtP, PPeP, PPoP, or such connection protocol. If this is not correct look for anything that maybe contains any info about the ISP account of the user.  
go to this option and open it. Most likely you will see a overview of user setup options.  
Now look for the user name and password.  
In most case the user name will be freely displayed so just write it down or what ever….  
The password is a different story. All most always the password is protected by \*\*\*\*\*\*\*\*\* (stars) in the telnet way there is noway around it (go to another victim) but when you have a port 80 connection (http). Internet connection way open click right mouse key and select “View source” now look for the field where the star are at. most likely you can read it because in the source code the star are converted to normal ASCII text.  
If not get a “\*\*\*\*\*\*\*\* to text” converter like sandboy’s revelation V.2 move the cursor over the \*\*\*\*\*\* and….  
Also there is a built in tool in Nettools that lest you know passwords in Internet Explorer Behind asterisks.

It’s a miracle you can read the password.  
Now you have the username and password.  
There a million fun thing to do with that but more about that next time.

Tips.

Beware on most routers only one person can be login on simultaneous in the router setup menu.  
Don’t change anything in the router if you don’t know what you are doing.

Don’t cause any unintentional harm. Don’t overuse any connection as the sufferer may complain.

Go to our new site- shankee.com
