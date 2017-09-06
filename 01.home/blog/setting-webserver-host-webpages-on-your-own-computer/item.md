---
# http://learn.getgrav.org/content/headers
title: Setting Webserver- Host Webpages on your own computer
slug: setting-webserver-host-webpages-on-your-own-computer
# menu: Setting Webserver- Host Webpages on your own computer
date: 16-05-2013
published: true
publish_date: 16-05-2013
# unpublish_date: 16-05-2013
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
        - hack
        - hacking
        - internet
        - learn to hack
        - tutorial
        - web
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hack,hacking,internet,learn to hack,tutorial,web]
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

Have you ever wondered to setup a website without signing up at any web hosting site ? Learning web site designing and wanna keep testing how your web pages look? Free Web hosting sites removing you phishing     pages ?

 

 



 

So solution to such kinda things is in this post.  Basically we are going to turn our pc to a server.

 



**What is a server  ?**



 

[![](http://4.bp.blogspot.com/_ufGdCaQ3M3k/TSMUBc5RDPI/AAAAAAAAAB8/e7SlmTAJe78/s1600/www.jpg)](http://4.bp.blogspot.com/_ufGdCaQ3M3k/TSMUBc5RDPI/AAAAAAAAAB8/e7SlmTAJe78/s1600/www.jpg)Server is we can say, any computer that is serving something . Like webserver serves webpages, ftp server serves files. Any computer can be turned into a server by simply installing a server software. In this post,

 

I am using XAMPP . **By installing this, contents of a particular directory of  our computer would accessible all over internet . Means one could access those contents from any part of the world through our Public IP address.**

 

You can place your web pages or whatever you wish in that directory.

 

Download XAMPP from [here](http://www.apachefriends.org/en/xampp.html). This package consists of Apache http server (A), MySQL database (M), php (P),Perl (P) and X represents cross platforms.

 



After dowloading it, simply install it . 

[![](http://3.bp.blogspot.com/_ufGdCaQ3M3k/TSMRic6_7rI/AAAAAAAAABg/68igrApVESs/s320/a.JPG)](http://3.bp.blogspot.com/_ufGdCaQ3M3k/TSMRic6_7rI/AAAAAAAAABg/68igrApVESs/s1600/a.JPG)



At last stage on installation you will get this . Press 1 to start XAMPP control panel.

[![](http://1.bp.blogspot.com/_ufGdCaQ3M3k/TSMRlUrpfTI/AAAAAAAAABk/wjC0ZFXk4Us/s320/q.JPG)](http://1.bp.blogspot.com/_ufGdCaQ3M3k/TSMRlUrpfTI/AAAAAAAAABk/wjC0ZFXk4Us/s1600/q.JPG)



The control panel would look like this

[![](http://2.bp.blogspot.com/_ufGdCaQ3M3k/TSMTFFAGSgI/AAAAAAAAAB4/_klcxaOFCRE/s320/xpanel.jpg)](http://2.bp.blogspot.com/_ufGdCaQ3M3k/TSMTFFAGSgI/AAAAAAAAAB4/_klcxaOFCRE/s1600/xpanel.jpg)



Click Start to start apache server. Now lets check whether its working,



Open your web browser and visit your local machine address that is 127.0.0.1 or localhost. Hopefully you must get the XAMPP page as shown.

[![](http://3.bp.blogspot.com/_ufGdCaQ3M3k/TSMRxF-oxoI/AAAAAAAAABs/QT_Dyav5_K8/s320/y.JPG)](http://3.bp.blogspot.com/_ufGdCaQ3M3k/TSMRxF-oxoI/AAAAAAAAABs/QT_Dyav5_K8/s1600/y.JPG)



Now check whether it is accessible on internet. Type your Public/External Ip in your web browser and hit enter. 

If you got a page as shown, follow the instructions :

[![](http://1.bp.blogspot.com/_ufGdCaQ3M3k/TSMRz0qY1iI/AAAAAAAAABw/imhN23jdTtA/s320/z.JPG)](http://1.bp.blogspot.com/_ufGdCaQ3M3k/TSMRz0qY1iI/AAAAAAAAABw/imhN23jdTtA/s1600/z.JPG)





1. Go to file httpd-xampp.conf

2. Remove “deny from all” and save the file.





[![](http://4.bp.blogspot.com/_ufGdCaQ3M3k/TSMR5zxuqKI/AAAAAAAAAB0/hwpO5ewCDIg/s320/x.JPG)](http://4.bp.blogspot.com/_ufGdCaQ3M3k/TSMR5zxuqKI/AAAAAAAAAB0/hwpO5ewCDIg/s1600/x.JPG)



3. Now restart the server and hopefully it would be all right now.



Now what ?



There must be a directory ‘**htdocs**‘ at location C:xampp. The contents of this particular directory will be available to every body. Suppose you place a file **anything.html** in ‘**htdocs**‘ directory. It would be accessible at

**1.http://localhost/anything.html  or http://127.0.0.1/anything.html**

( Obviously above two links gonna work on your own computer only.)

**2.http://xxx.xxx.xxx.xxx/anything.html** (where xxx.xxx.xxx.xxx is your IP address)

You can start/stop this service simply through the control panel.

Thats all. And you have also use Filezilla(ftp server software) and Mysql (database) as per your need. Get a domain name ?  
Now you would want to get a domain name instead of  using the Public IP to check out your contents.  
But how can we get a domain name because our IP is dynamic and to which IP domain name would point ?  
Dont worry, we have a solution.  
1. Log on to www.**no**–**ip**.com and sign up for an account. Choose available domain name.  
2. Download their dynamic DNS update client and run on PC.  
  
  
This client would automatically keep updating your dynamic IP address and that is how the selected domain would always be pointing to your IP address.





*Note: You might need  do port forwarding if you are behind a router. Kindly mention the queries regarding that  in comments*.

 

Go to our new site- shankee.com
