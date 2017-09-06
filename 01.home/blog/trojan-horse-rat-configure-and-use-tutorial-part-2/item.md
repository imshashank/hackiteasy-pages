---
# http://learn.getgrav.org/content/headers
title: Trojan Horse | RAT | Configure and Use | Tutorial- Part 2
slug: trojan-horse-rat-configure-and-use-tutorial-part-2
# menu: Trojan Horse | RAT | Configure and Use | Tutorial- Part 2
date: 13-05-2013
published: true
publish_date: 13-05-2013
# unpublish_date: 13-05-2013
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
        - learn to hack
        - trojan
        - tutorial
        - virus
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hacking,learn to hack,trojan,tutorial,virus]
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

Just go through the Part 1 which includes the basics of  Trojan Click here. This tutorial is about configuring and using a trojan. There are many trojans available on internet for free. Some popular ones are Beast, Pro Rat, Netbus , Back Orifice, Girlfriend, Sub 7. I will be using Pro Rat in this tutorial. **Requirements**  
**  
**  
**1. Prorat-** Click here to download Trojan Prorat.  
**2. Hostname ** –  Your IP address would probably be dynamic that it keeps changing everytime you disconnect and reconnect. You need a host name which always automatically keep pointing to your changing IP. Follow these steps -:

1. Log On to www.no-ip.com and register for an account.  
2. Go to Hosts/Redirects -> Add Host and choose any free available hostname. Do not change any other option and simply click on Create Host.

![](http://2.bp.blogspot.com/_ufGdCaQ3M3k/TUViknumbVI/AAAAAAAAAJw/wnJQcn98IS0/s400/add.jpg)

3. Downloading and install their DNS update client available here http://www.no-ip.com/downloads.php Run it and enter your credentials. Update your host name and save it.

![](http://1.bp.blogspot.com/_ufGdCaQ3M3k/TUVimDGw9UI/AAAAAAAAAJ0/-ypluGHWw2k/s200/duc.jpg)

4. Lets check whether your IP has been associate with chosen host name or not. Go to command prompt and type ‘ping yourhostname’ (without quotes) , hopefully it should reply with your IP address.

![](http://4.bp.blogspot.com/_ufGdCaQ3M3k/TUVintSwJnI/AAAAAAAAAJ4/VO8ybt5jpwo/s400/ping.jpg)

**Tutorial for configuring Trojan.**  
**  
**  
**1**. Open prorat.exe that you have downloaded.  
**2**. Click on Create  and then Create ProRat Server

![](http://2.bp.blogspot.com/_ufGdCaQ3M3k/TUVcoQQwx0I/AAAAAAAAAJc/2SLQd9ByFzU/s320/pro1.jpg)

 **3.**  Enter your host name in the ProRat Notification field as shown. Uncheck all other options.

![](http://1.bp.blogspot.com/_ufGdCaQ3M3k/TUVct0wRqgI/AAAAAAAAAJg/y6fEpqR-lXY/s400/pro2.jpg)

**4.** Click on general settings Tab and have a look at server port,password, victim name. Remember these things.Check out and configure other options as per your need. You can bind server.exe with any genuine file, change its icon etc.

![](http://4.bp.blogspot.com/_ufGdCaQ3M3k/TUVcxuKpZmI/AAAAAAAAAJk/h0lDZw2GyrQ/s400/pro3.jpg)

**5**. Finally click on create  server and now its ready to be sent to victim.  Once victim installs it, it would automatically disable antivirus/firewall.

**Modes of sending-: **  
You must be thinking of sending this server.exe to victim through an email as an attachment but unfortunately you cant do so. The good option is  to upload it on any uploading site like mediafire.com and give downloading link to victim.

**What after victim has run the server part ?**  
**  
**  
**1.**Click on ProConnective Tab and start listening to connections. Allow firewall if it asks you to open a port.  
**2**.You will start listening to connections, I mean you will get a notification as shown when victim would be online.

![](http://2.bp.blogspot.com/_ufGdCaQ3M3k/TUVj4-htayI/AAAAAAAAAJ8/ffgHKpq_lZg/s1600/pro5.jpg)![](http://2.bp.blogspot.com/_ufGdCaQ3M3k/TUVc0vTaxpI/AAAAAAAAAJo/G_w_WrUSyh4/s320/pro4.jpg)

**Note: **If you know victim is online and still its not listening to any connections. Trace victim’s IP,enter in IP field and hit connect. But its gonna work only if he is not behind any network and directly connected to internet. If you dont know how to trace IP, mention in comments.

**What after successful connection ?**

After you have managed to connect to victim’s machine. There are numberless interesting things to do. I leave this part on you.  Have Fun.



**How to make it undetectable from antivirus ?**  
Though there isn’t any hard and fast way to make it fully undetectable from all antiviruses. The real way to do it is modify the source code of open source trojans available. Its very challenging job. There are many crypters which claim to make it undetectable but unfortunately hardly one out every hundred works. I would try to write next article on the same.  
**  
**  
**Contermeasure against Trojans –**  
The obvious coutermeasure against trojans is that do not accept downloading links blindly. Keep your antivirus up to date.

**Detecting and removing Trojan –**  
Though trojan once installed is very hard to remove . It would hide itself from the **Task Manager . **Install Process Explorer and it would hopefully show you all process running including trojan. Kill the process and remove it. One good thing is to carefully check the open ports and services running through ‘netstat’ command. Anyways , the best option is to reinstall the windows.  
*  
*  
*Feel free to ask  the queries in comments 🙂*



Go to our new site- shankee.com
