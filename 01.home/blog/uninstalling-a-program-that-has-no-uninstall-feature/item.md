---
# http://learn.getgrav.org/content/headers
title: uninstalling a program that has no uninstall feature
slug: uninstalling-a-program-that-has-no-uninstall-feature
# menu: uninstalling a program that has no uninstall feature
date: 04-06-2009
published: true
publish_date: 04-06-2009
# unpublish_date: 04-06-2009
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
        - microsoft
        - tech
        - vista
        - windows 7
        - XP
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hack,microsoft,tech,vista,windows 7,XP]
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

This trick lets you uninstall any program in windows XP/Vista/Windows 7 that doesn’t feature an uninstall command or does not get deleted by simple removing it from the add/remove software option. Just follow the simple steps.

1. Make a backup of the registry
2. Shutdown the application, if it is running (If WinNT+ check also for services)
3. Search the registry for any references to the directory where the application resides, and remove them
4. Search the registry for any references to the name of the application, and remove them
5. Start Regedit and drill down to :
 

[HKEY\_CURRENT\_USER Software ]   
[HKEY\_LOCAL\_MACHINE Software ]   
[HKEY\_LOCAL\_MACHINE Software Microsoft Windows CurrentVersion SharedDLLs]

1. Rename the directory in which the application was installed in the first place
2. Reboot and if everything goes well, then delete the renamed directory
Use Explorer to to remove the entries from the Start Menu in either

*C:Documents and FoldersAll UsersStart MenuPrograms and/or   
C:Documents and Folders(your username)Start MenuPrograms *

If there is an entry in the Add/Remove list, start regedit go to:

*HKEY\_LOCAL\_MACHINESOFTWAREMicrosoftWindowsCurrentVersionUninstall*

Locate the entry and delete it. If the app has a service, edit:

*HKEY\_LOCAL\_MACHINESystemCurrentControlSetServices *

and scroll down till you locate it. Then delete it. If this app starts automatically and there is no entry in the StartUp folder(s), then use Regedt32 to edit:

*HKEY\_CURRENT\_USERSoftwareMicrosoftWindowsNTCurrentVersionWindows*

Aaron Stebner discribes another method in his [Aaron Stebner’s WebLog](http://blogs.msdn.com/astebner/archive/2005/10/30/487096.aspx "http://blogs.msdn.com/astebner/archive/2005/10/30/487096.aspx")

Also worth to check : [http://support.microsoft.com/kb/314481](http://support.microsoft.com/kb/314481 "http://support.microsoft.com/kb/314481") [http://support.microsoft.com/kb/Q247501](http://support.microsoft.com/kb/Q247501 "http://support.microsoft.com/kb/Q247501") [http://support.microsoft.com/kb/Q247515](http://support.microsoft.com/kb/Q247515 "http://support.microsoft.com/kb/Q247515") [http://support.microsoft.com/kb/Q290301](http://support.microsoft.com/kb/Q290301 "http://support.microsoft.com/kb/Q290301")

**Add Remove Program Cleaner 2** :This program allows you to clean up the Add/Remove programs list in the control panel. It should only be used to remove entries that are broken and cannot be removed by running the uninstall program.

[![SparksSpace023](http://lh5.ggpht.com/spaaark/SF5A8QS5jqI/AAAAAAAAETA/cUxoNHBPX1E/SparksSpace023_thumb%5B2%5D.png?imgmax=800 "SparksSpace023")](http://lh3.ggpht.com/spaaark/SF5A42R5vII/AAAAAAAAES8/c06j0shOhhM/s1600-h/SparksSpace023%5B4%5D.png)

[**Add-Remove-Program-Cleaner**](http://www.download.com/Add-Remove-Program-Cleaner/3000-2096_4-10572853.html "http://www.download.com/Add-Remove-Program-Cleaner/3000-2096_4-10572853.html") |Sys Req:Windows NT/2000/XP/2003 Server/Vista | Freeware | 940KB

 

Go to our new site- shankee.com
