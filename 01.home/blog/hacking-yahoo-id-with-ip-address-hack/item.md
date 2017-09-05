---
# http://learn.getgrav.org/content/headers
title: hacking yahoo ID with IP address hack
slug: hacking-yahoo-id-with-ip-address-hack
# menu: hacking yahoo ID with IP address hack
date: 09-06-2009
published: true
publish_date: 09-06-2009
# unpublish_date: 09-06-2009
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
        - IP
        - tech
        - yahoo
        - yahoo messenger hack
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hacking,IP,tech,yahoo,yahoo messenger hack]
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

This is only for education purpose.So who ever try this is at his risk.  
I am not sure that this will work 100 %.But yes will work almost 70 percent of the times.But before that you need to know some few things of yahoo chat protocol  
leave a comment here after u see the post lemme know if it does works or not or u havin a problem post here

Following are the features : –  
1) When we chat on yahoo every thing goes through the server.Only when we chat thats messages.  
2) When we send files yahoo has 2 options  
a) Either it uplo— the file and then the other client has to down load it.  
b) Either it connects to the client directly and gets the files  
3) When we use video or audio:-  
a) It either goes thru the server  
b) Or it has client to client connection  
And when we have client to client connection the opponents IP is revealed.On the 5051 port.So how do we exploit the Chat user when he gets a direct connection. And how do we go about it.Remeber i am here to hack a system with out using a TOOL only by simple net commands and yahoo chat techniques.Thats what makes a difference between a real hacker and new bies.  
So lets —-yse  
1) Its impossible to get a Attackers IP address when you only chat.  
2) There are 50 % chances of getting a IP address when you send files  
3) Again 50 % chances of getting IP when you use video or audio.

So why to wait lets exploit those 50 % chances.I will explain only for files here which lies same for Video or audio  
1) Go to dos  
type ->  
netstat -n 3  
You will get the following output.Just do not care and be cool  
Active Connections

Proto Local Address Foreign Address State  
TCP 194.30.209.15:1631 194.30.209.20:5900 ESTABLISHED  
TCP 194.30.209.15:2736 216.136.224.214:5050 ESTABLISHED  
TCP 194.30.209.15:2750 64.4.13.85:1863 ESTABLISHED  
TCP 194.30.209.15:2864 64.4.12.200:1863 ESTABLISHED

Active Connections

Proto Local Address Foreign Address State  
TCP 194.30.209.15:1631 194.30.209.20:5900 ESTABLISHED  
TCP 194.30.209.15:2736 216.136.224.214:5050 ESTABLISHED  
TCP 194.30.209.15:2750 64.4.13.85:1863 ESTABLISHED  
TCP 194.30.209.15:2864 64.4.12.200:1863 ESTABLISHED

Just i will explain what the out put is in general.In left hand side is your IP address.And in right hand side is the IP address of the foreign machine.And the port to which is connected.Ok now so what next ->

2) Try sending a file to the Target .  
if the files comes from server.Thats the file is uploaded leave itYou will not get the ip.But if a direct connection is established  
HMMMM then the first attacker first phase is over  
This is the output in your netstat.The 5101 number port is where the Attacker is connected.  
Active Connections

Proto Local Address Foreign Address State  
TCP 194.30.209.15:1631 194.30.209.20:5900 ESTABLISHED  
TCP 194.30.209.15:2736 216.136.224.214:5050 ESTABLISHED  
TCP 194.30.209.15:2750 64.4.13.85:1863 ESTABLISHED  
TCP 194.30.209.15:2864 64.4.12.200:1863 ESTABLISHED  
TCP 194.30.209.15:5101 194.30.209.14:3290 ESTABLISHED

Thats what is highlighted in RED. So what next  
3) Hmmm Ok so make a DOS attack now  
Go to dos prompt and  
Just do  
nbtstat -A Attackers IPaddress.Can happen that if system is not protected then you can see the whole network.  
C:>nbtstat -A 194.30.209.14

Local Area Connection:  
Node IpAddress: [194.30.209.15] Scope Id: []

NetBIOS Remote Machine Name Table

Name Type Status  
———————————————  
EDP12 UNIQUE Registered  
SHIV GROUP Registered  
SHIV UNIQUE Registered  
SHIVCOMP1 GROUP Registered

MAC Address = 00-C0-W0-D5-EF-9A

Ok so you will ask now what next.No you find what you can do with this network than me explaining everything.

So the conclusion is never exchange files , video or audio till you know that the user with whom you are chatting is not going to harm you.

Go to our new site- shankee.com
