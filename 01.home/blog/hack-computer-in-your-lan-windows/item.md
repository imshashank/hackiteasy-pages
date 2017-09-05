---
# http://learn.getgrav.org/content/headers
title: Hack computer in your LAN (Windows)
slug: hack-computer-in-your-lan-windows
# menu: Hack computer in your LAN (Windows)
date: 12-01-2011
published: true
publish_date: 12-01-2011
# unpublish_date: 12-01-2011
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
        - computers tricks
        - hack
        - hacker
        - lan
        - network
        - tech
        - windows
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [computers tricks,hack,hacker,lan,network,tech,windows]
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

[Easily Hack A Windows password.. Click Here!](http://80fcb0h10nxcnrvoa7w2251kac.hop.clickbank.net/)Here we hack a PC somwhere in our LAN. This is a simple trick that uses open port to gain access to the target computer.The Lan hacking technique uses port 139 for the hack. On a LAN mostly the port 139 would remain open. Today,I will write about hacking computer inside the LAN network.

This technique will be taking advantage of Port 139.

Most of the time,Port 139 will be opened.

First of all,I will do a port scanning at the target computer which is 192.168.40.128.

This computer is inside my LAN network.

I will scan it using Nmap.

[![[Image: 1_13.jpg]](http://h.imagehost.org/0744/1_13.jpg)](http://h.imagehost.org/view/0744/1_13)

I get the result and it shows Port 139 is opened up for me.

Now you will need both of these tools:  
\*\* USER2SID & SID2USER  
\*\* NetBios Auditing Tool

You can get both of them on the Internet.

After you get both of them,put them in the C: directory.

[![[Image: 2_1.jpg]](http://h.imagehost.org/0447/2_1.jpg)](http://h.imagehost.org/view/0447/2_1)  
[Easily Hack A Windows password.. Click Here!](http://80fcb0h10nxcnrvoa7w2251kac.hop.clickbank.net/)   
   
You now need to create a null session to the target computer.  
  
  
[![[Image: 3_3.jpg]](http://h.imagehost.org/0848/3_3.jpg)](http://h.imagehost.org/view/0848/3_3)

Now open the Command Prompt and browse to the USER2SID & SID2USER folder.There will be 2 tools inside it,one will be USER2SID and another one will be SID2USER.

We will first using USER2SID to get the ID.

[![[Image: 4_10.jpg]](http://h.imagehost.org/0770/4_10.jpg)](http://h.imagehost.org/view/0770/4_10)

We will test against the Guest account because Guest account is a built in account.

After we get the ID,we need to do some modification on the ID.

We take the ID we get from the guest account and modified it become   
“5 21 861567501 1383384898 839522115 500”.

Please leave out the S-1-,leave out all the – too.

[![[Image: 5_8.jpg]](http://h.imagehost.org/0672/5_8.jpg)](http://h.imagehost.org/view/0672/5_8)

Now you will see that you get the username of the Administrator account.

In this case,the Administrator account is Administrator.

Create a text file called user.txt and the content will be the username of the Admin account.

[![[Image: 6.jpg]](http://h.imagehost.org/0571/6.jpg)](http://h.imagehost.org/view/0571/6)

Prepare yourself a good wordlist.

[![[Image: 7.jpg]](http://h.imagehost.org/0358/7.jpg)](http://h.imagehost.org/view/0358/7)

Now put both of them in the same directory with the NetBios Auditing Tool.

[![[Image: 8.jpg]](http://h.imagehost.org/0827/8.jpg)](http://h.imagehost.org/view/0827/8)

Now we are going to crack the Admin account for the password in order to access to the target computer.

Browse to the NetBios Auditing Tool directory.

[![[Image: 9_1.jpg]](http://h.imagehost.org/0231/9_1.jpg)](http://h.imagehost.org/view/0231/9_1)

Press on enter and the tool will run through the passlist.

[![[Image: 10.jpg]](http://h.imagehost.org/0494/10.jpg)](http://h.imagehost.org/view/0494/10)

In this case,I have get the password.

In order to proof that I can get access to the target computer using this password.

[![[Image: 11.jpg]](http://h.imagehost.org/0103/11.jpg)](http://h.imagehost.org/view/0103/11)

After you press enter,it will prompt you for the username and password.

[![[Image: 12_6.jpg]](http://h.imagehost.org/0857/12_6.jpg)](http://h.imagehost.org/view/0857/12_6)

Therefore,just input them inside the prompt and continue.

[![[Image: 13.jpg]](http://h.imagehost.org/0631/13.jpg)](http://h.imagehost.org/view/0631/13)

Target C drive will be on your screen.

[![[Image: 14.jpg]](http://h.imagehost.org/0589/14.jpg)](http://h.imagehost.org/view/0589/14)

In order to prevent from this attack,close down port that you do not want to use such as Port 135,Port 136,Port 137,Port 138 and Port 139.

The download link of the tools will be:  
[Download Tools.rar](http://www.megaupload.com/?d=0ITWD0FD)

We check for open 139 port by using Zenmap, you can use any other port scanners as well.

For this you need to know the IP of computers in your network which would most probably look like 192.168.xx where only ‘xx’ changes in range 0 to 255 and shows different IPs.

Once we get the IP of the target machine we scan it using Nmap.

[![[Image: 1_13.jpg]](http://h.imagehost.org/0744/1_13.jpg)](http://h.imagehost.org/view/0744/1_13)

Here we see that port 139 is open and ready to be hacked.

We need these two hack tools-  
\*\* USER2SID & SID2USER  
\*\* NetBios Auditing Tool

Google them on the net.

After you get both of them,put them in the C: directory.

[![[Image: 2_1.jpg]](http://h.imagehost.org/0447/2_1.jpg)](http://h.imagehost.org/view/0447/2_1)

Create a null session on your computer do this as follows:-

[![[Image: 3_3.jpg]](http://h.imagehost.org/0848/3_3.jpg)](http://h.imagehost.org/view/0848/3_3)

Now open the Command Prompt and browse to the USER2SID & SID2USER folders .There will be 2 tools inside it,one would be USER2SID and another one be SID2USER.

We use USER2SID to get the ID of the user on target machine.

[![[Image: 4_10.jpg]](http://h.imagehost.org/0770/4_10.jpg)](http://h.imagehost.org/view/0770/4_10)

We will test against the Guest account because Guest account is a built in account.

After we get the ID,we need to do some modification on the ID.

We use the ID which we got from the guest account and modify it-

“5 21 861567501 1383384898 839522115 500”.

Please leave out the S-1-,leave out all the – too.

[![[Image: 5_8.jpg]](http://h.imagehost.org/0672/5_8.jpg)](http://h.imagehost.org/view/0672/5_8)

Now you will see that you get the username of the Administrator account.

In this case,the Administrator account is “Administrator”.

Create a text file called user.txt and the content will be the username of the Admin account.

[![[Image: 6.jpg]](http://h.imagehost.org/0571/6.jpg)](http://h.imagehost.org/view/0571/6)

Prepare yourself a good wordlist. Or get the list of most common password on the internet.

[![[Image: 7.jpg]](http://h.imagehost.org/0358/7.jpg)](http://h.imagehost.org/view/0358/7)

Now put both of them in the same directory with the NetBios Auditing Tool.

[![[Image: 8.jpg]](http://h.imagehost.org/0827/8.jpg)](http://h.imagehost.org/view/0827/8)

Now we are going to crack the Admin account for the password in order to access to the target computer.

Browse to the NetBios Auditing Tool directory.

[![[Image: 9_1.jpg]](http://h.imagehost.org/0231/9_1.jpg)](http://h.imagehost.org/view/0231/9_1)

Press on enter and the tool will run through the passlist.

[![[Image: 10.jpg]](http://h.imagehost.org/0494/10.jpg)](http://h.imagehost.org/view/0494/10)

In this case,we have the password.

In order to proof that we can get access to the target computer using this password.

[![[Image: 11.jpg]](http://h.imagehost.org/0103/11.jpg)](http://h.imagehost.org/view/0103/11)

After you press enter,it will prompt you for the username and password.

[![[Image: 12_6.jpg]](http://h.imagehost.org/0857/12_6.jpg)](http://h.imagehost.org/view/0857/12_6)

Therefore,just input them inside the prompt and continue.

[![[Image: 13.jpg]](http://h.imagehost.org/0631/13.jpg)](http://h.imagehost.org/view/0631/13)

Target C drive will be pop on your screen.

[![[Image: 14.jpg]](http://h.imagehost.org/0589/14.jpg)](http://h.imagehost.org/view/0589/14)

In order to prevent from this attack,close down port that you do not want to use such as Port 135,Port 136,Port 137,Port 138 and Port 139.  
  
  
  
  
  
  
WE recommend using the tool->  
[To Easily Hack A Windows password.. Click Here to download the tool!](http://80fcb0h10nxcnrvoa7w2251kac.hop.clickbank.net/)    
  
The download link of the tools will be:  
[Download Tools.rar](http://www.megaupload.com/?d=0ITWD0FD)

 

 

Go to our new site- shankee.com
