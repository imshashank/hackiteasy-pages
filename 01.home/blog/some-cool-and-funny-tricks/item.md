---
# http://learn.getgrav.org/content/headers
title: Some cool and funny tricks&#8230;
slug: some-cool-and-funny-tricks
# menu: Some cool and funny tricks&#8230;
date: 14-06-2009
published: true
publish_date: 14-06-2009
# unpublish_date: 14-06-2009
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
        - tech
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [computers tricks,tech]
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

Funny Computer Tricks: Check out these tips and funny tricks  
(1)Fun With Browswer :  
Copy and paste the java script code in the following red lines to the address bar of your browser

javascript:function Shw(n) {if (self.moveBy) {for (i = 35; i > 0; i–) {for (j = n; j > 0; j–) {self.moveBy(1,i);self.moveBy(i,0);self.moveBy(0,-i);self.moveBy(-i,0); } } }} Shw(6)  
Press enter and watch your window’s |shaking it” You can change the value of i if you wish 🙂  
(2)Cool DOS Commands  
Command #1: By typing in ‘tree’ into Dos, you can view all of the folders (not files) on the computer or User. Pretty cool but then again pretty worthless. Just a cool thing to know.

Command #2: By typing in ‘ipconfig’ you can view your default gateway ip adress for your router. This is really only useful if you are good with the computer and are trying to fix your internet connection, you can look at what’s wrong.

Command #3: By typing in ‘format c:’ you can delete all the information on your hard drive, if you want to start new or something, but dont do that just to be an idiot.

Command #4: By typing in ‘netstat’ or ‘nbtstat’ (both similar) you can view the TCP/IP network of your computer.

Command #5: By typing in ‘title whatever’ the blue bar at the top where it is command prompt will be replaced with whatever you typed after title.

(3)Renaming the Recycle Bin  
Ever wanted to rename your recycle bin? Who wouldn’t?  
Well, it’s pretty simple, the bare bones of it are just typing in commands to the registry.  
Ok, what you do is, copy this information (in bold) to notepad or something similar. (Start–>All Programs–>Accessories–>Notepad).

REGEDIT4

[HKEY\_CLASSES\_ROOTCLSID{645FF040-5081-101B-9F08-00AA002F954E}ShellFolder]  
“Attributes”=hex:50,01,00,20

“CallForAttributes”=dword:00000000

Once you have that copied into NotePad, save it as something like “Recyclebin.reg” (without the quotations).  
Then, find whereever you saved it, click on it, say yes, and BAM!

Go to our new site- shankee.com
