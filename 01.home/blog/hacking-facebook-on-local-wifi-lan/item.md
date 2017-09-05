---
# http://learn.getgrav.org/content/headers
title: Hacking Facebook on local wifi LAN
slug: hacking-facebook-on-local-wifi-lan
# menu: Hacking Facebook on local wifi LAN
date: 02-02-2014
published: true
publish_date: 02-02-2014
# unpublish_date: 02-02-2014
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
        - cookies
        - facebook
        - hack it easy
        - hack wifi password
        - local
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [cookies,facebook,hack it easy,hack wifi password,local]
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

Hi, A lot of subscribers have been asking me on how to hack Facebook.

Well this is the tutorial that will let you hack not just facebook but any site on your local wifi/LAN.

Ok so in this post I am going to show you a way you can hack the facebook accounts of all the people who are on your network (LAN or wifi ) . I have tried this and believe me it works..This is really the best way to hack facebook accounts. Its much easier than installing RATs, Keyloggers or making phishing sites. Ok so off we go!



You will need 3 programs for this

**Cain and abel** : http://www.oxid.it/cain.html  
**Wireshark** : http://www.wireshark.org/download.html  
**Web developer add-on for firefox** : https://addons.mozilla.org/en-US/firefox/addon/web-developer/

So what exactly happens when you type in http://www.facebook.com and login with your username and password. First download the web developer addon for firefox and then login to facebook. After you log in view the cookies in the web developer toolbar.

![](http://35.160.74.13/wp-content/uploads/2014/02/piccookie-300x156.png "piccookie")

Ok now if you click on view cookie information, you will be able to see all the cookies which facebook has transmitted to your browser.

The main cookies are the c\_user cookie (which identifies a person uniquely) and datr cookie..

So your aim must be to get the cookies of your victim through wireshark and then replace your cookies with the victim’s. So then, facebook will think you are the victim as you have his cookies and you will be logged in as the victim. Simple isn’t it? ![:P](http://35.160.74.13/wp-content/uploads/2014/02/icon_razz.gif)

So how do you do this..

First off install cain and abel.It will ask you whether you want to install the packet driver – WinPCap. Go ahead and install that also.Open up cain.

- Click on configure on top and select your Network card. Mostly its the one with an IP address :p
- Next click on the start/stop sniffer on top as shown below in green square.
- Once you start the sniffer, goto the sniffer tab in cain, right-click and click scan mac address as shown below!

![](http://35.160.74.13/wp-content/uploads/2014/02/cai-300x167.png "cain")

Ok now you should have a list of everyone on the network. It may take some time though. You can right-click on any one computer and find out its name.

Now what we are going to do is the actual shit!We are going to do an ARP poison ! What this means is that you fool the router in thinking that you are the victim, and you fool the victim in thinking that you are the router.

So initially victim -> router -> facebook. Now after ARP poison,  victim->hacker->router. This is called an MITM(Man in the middle) attack.You can google it for more info :p

**Doing the ARP POISON**

- First Click the APR tab below in cain.
- Click the white screen in the top frame
- Click the blue plus on top.

![](http://35.160.74.13/wp-content/uploads/2014/02/ste-300x154.png "ste")

Now you should get a list of all the devices on the left and a blank screen on the right..

In the left screen you should select the router IP. And in the right box, select the computers you want to target. To be safe its better to target one computer. But if you want some real fun then select all the computers on the right frame :D. Press ok.

WARNING: If there is a person at the router, he can know if you have just done an ARP poison. But where is the fun without the risk.:P

You can try googling on other methods to do arp poison safely.

In the top frame all the computer list should have got filled. now select the whole list and click on the nuclear button (top left of cain).

![](http://35.160.74.13/wp-content/uploads/2014/02/ste1-300x154.png "ste")  
 Thats it you are done with the arp poison. Just be careful, if you select too many computers, your computer cant handle the traffic and the network may just crash. I am reminding you, this should be done for ethical reasons !

Now all the data is passing through your computer. All you have to do is sniff the data in wireshark, get the cookie and replace your cookie with victim’s cookie.

Thats what ill be covering in part 2 of this post . Please add my email to you contacts list to avoid this email from going to spam.

Regards,  
Shashank Agarwal  
(Admin: Hack It Easy) 



 

 

Go to our new site- shankee.com
