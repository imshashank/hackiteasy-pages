---
# http://learn.getgrav.org/content/headers
title: Auto Complete passwords
slug: auto-complete-passwords
# menu: Auto Complete passwords
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
        - hacking
        - internet
        - passwords
        - tech
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hacking,internet,passwords,tech]
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

Hi Techies!!  
Remember the Windows “Password Remember” prompt, each time you login to a new website?? Here’s some freaking information about the magic box.

For some sites, we don’t require the auto login , and so might choose “No” in the dialog box. This may end with the dialog box not being displayed ever. So just follow the steps below if you want the prompt back.

\* Enter the site and double click the login field

\* This displays a list of usernames that are Auto saved.

\* Highlight the Username and click “Delete”.

Now try logging in and you are again with the same dialog box.

This can also be acheived with a simple registry setting, if the above isn’t working for you….

\* Start ==> Run ==> Enter *“Regedit”*

\* *HKEY\_CURRENT\_USERSoftwareMicrosoftInternet ExplorerIntelliFormsSPW*

\* You can see a list of encrypted passwords.

\* Now select the SPW key and click *“Delete”*.

Every password that you enter is saved with a unique SPW key, whether you select “YES” or “NO”.

But the Auto complete data is saved in a different storage:

**  
***HKEY\_CURRENT\_USERSoftwareMicrosoftProtected Storage System Provider*****

Each of the passwords can be decrypted with various tools available.

Go to our new site- shankee.com
