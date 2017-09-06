---
# http://learn.getgrav.org/content/headers
title: Guide to easiest hacking
slug: guide-to-easiest-hacking
# menu: Guide to easiest hacking
date: 10-09-2008
published: true
publish_date: 10-09-2008
# unpublish_date: 10-09-2008
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
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hacking]
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

OK, this is my mini guide to the easiest ‘hacking’ there is ( I think ) if any  
one knows different then mail me and tell me 🙂 .  
Most FTP servers have the directory /pub which stores all the ‘public’ information  
for you to download. But along side /pub you will probably find other directorys  
such as /bin and /etc its the /etc directory which is important. In this directory  
  
there is normally a file called passwd. . This looks something like this :-  
root:7GHgfHgfhG:1127:20:Superuser  
jgibson:7fOsTXF2pA1W2:1128:20:Jim Gibson,,,,,,,:/usr/people/jgibson:/bin/csh  
tvr:EUyd5XAAtv2dA:1129:20:Tovar:/usr/people/tvr:/bin/csh  
mcn:t3e.QVzvUC1T.:1130:20:Greatbear,,,,,,,:/usr/people/mcn:/bin/csh  
mouse:EUyd5XAAtv2dA:1131:20:Melissa P.:/usr/people/mouse:/bin/csh  
This is where all the user names and passwords are kept. For example, root is  
the superuser and the rest are normal users on the site. The bit after the word  
root or mcn such as in this example (EUyd5XAAtv2dA) is the password BUT it is  
encrypted. So you use a password cracker….which you can d/l from numerous sites  
which I will give some URL’s to at the end of this document. With these password  
crackers you will be asked to supply a passwd. file which you download from the  
etc directory of the FTP server and a dictionary file which the crackers progam  
will go through and try to see if it can make any match. And as many people use  
simple passwords you can use a ‘normal’ dictionary file. But when ppl REALLY don’t  
want you to break their machines they set their passwords to things such as GHTiCk45  
which Random Word Generator will create (eventually ). Which is where programs such  
as Random Word Generator come in. ( Sorry just pluging my software )  
BTW the bad news is that new sites NORMALLY have password files which look like this :-  
root:x:0:1:0000-Admin(0000):/:/sbin/sh  
The x signifies shadowed – you can’t use a cracker to crack it because there’s nothing  
there to crack, its hidden somewhere else that you can’t get to. x is also represented  
as a \* or sometimes a . Ones like the top example are known as un-shadowed password  
files normally found at places with .org domain or .net and prehaps even .edu sites.  
(Also cough .nasa.gov cough sites).  
If you want a normal dictionary file i recommend you go to  
http://www.globalkos.org and download kOS Krack which  
has a 3 MEG dictionary file. Then run a .passwd cracking program  
such as jack the ripper or hades or killer crack ( I recommend ) against the  
.passwd file and dictionary file. Depending upon the amount of passwords in  
the .passwd file, the size of the dictionary file and the speed of the processor  
it could be a lengthy process.  
Eventually once you have cracked a password you need a basic knowledge of unix.  
I have included the necassary commands to upload a different index.html file to  
a server :-  
Connect to a server through ftp prefably going through a few shells to hide your  
host and login using the hacked account at the Login: Password: part.  
Then once connected type  
dir or list  
If there’s a directory called public\_html@ or something similar change directory  
using the Simple dos cd command ( cd public\_html )  
Then type binary to set the mode to binary transfer ( so you can send images if  
necassary )  
Then type put index.html or whatever the index file is called.  
It will then ask which transfer you wish to use, Z-Modem is the best.  
Select the file at your end you wish to upload and send it.  
Thats it !  
If you have root delete any log files too.  
Please note that this process varys machine to machine.  
To change the password file for the account ( very mean ) login in through telnet  
and simply type passwd at the prompt and set the password for the account to anything  
you wish.  
Thats it….if ya don’t understand it read it about 10x if ya still don’t ask someone  
else i am too busy with errrr stuff..  
Links :-  
Where you got this I hope.  
Stay cool and be somebodys fool everyone

Go to our new site- shankee.com
