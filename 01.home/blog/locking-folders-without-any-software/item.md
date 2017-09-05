---
# http://learn.getgrav.org/content/headers
title: Locking Folders without any software
slug: locking-folders-without-any-software
# menu: Locking Folders without any software
date: 08-06-2009
published: true
publish_date: 08-06-2009
# unpublish_date: 08-06-2009
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
        - fol
        - hacking
        - lock
        - tech
        - XP
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [fol,hacking,lock,tech,XP]
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

Though there are various softwares to lock up folders on your windows, but what if we can just do same thing without help of any software. Today here I am writing how to lock up a folder in windows without help of any software. Hope you all will enjoy this trick.

Just follow some intructions :

Type the following code in a note pad and save the note pad in your pc with the name ‘ NOMANs Lock Up.bat ‘ (that is with the extension of .bat). You can replace the ‘NOMAN’s Lock Up ‘ portion with anything u want to use.  
A batch file will be created where you have saved. Now double click on it, it will make a folder with the name ‘ Locker ‘ at the same place where the batch file is save.  
Now add the files you want to lock in that folder named “Locker”.  
Double click on the batch file. It will ask for locking the folder. Type ‘ Y ‘ OR ‘ y ‘ to lock the items. The folder will be locked and hidden.  
[NB: This is a very strong process. Even if you choose Tools – Folder Options… – View – Show hidden files and folders, the ‘ Locker ‘ folder will remain hidden. Only a correct password can unlock it.

To unlock the items, just double click on the batch file again and enter the password unlock in the new opened window. Then hit ‘ Enter ‘ ( iff u wanna create othr passwrd. thn u have to make change in the code….( I mark \* there for you)

> cls  
> @ECHO OFF  
> title Folder Locker  
> if EXIST “Control Panel.{21EC2020-3AEA-1069-A2DD-08002B303  
> 09D}” goto UNLOCK  
> if NOT EXIST Locker goto MDLOCKER  
> :CONFIRM  
> echo This is created by SAKET,Hey Dude,Are you sure u want to Lock the folder(Y/N)  
> set/p “cho=>”  
> if %cho%==Y goto LOCK  
> if %cho%==y goto LOCK  
> if %cho%==n goto END  
> if %cho%==N goto END  
> echo Invalid choice.  
> goto CONFIRM  
> :LOCK  
> ren Locker “Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}”  
> attrib +h +s “Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}”  
> echo Folder locked  
> goto End  
> :UNLOCK  
> echo Enter password to Unlock folder  
> set/p “pass=>”  
> if NOT %pass%==unlock goto FAIL  
> attrib -h -s “Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}”  
> ren “Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}” Locker  
> echo Folder Unlocked successfully  
> goto End  
> :FAIL  
> echo Invalid password  
> goto end  
> :MDLOCKER  
> md Locker  
> echo NOMAN created successfully  
> goto End  
> :End

Code ends ( need not to copy this line)  
Now if u want to change the password just find if NOT %pass%==unlock goto FAIL line and change word ” open” to somethng else and enjoy

 **  
**

Go to our new site- shankee.com
