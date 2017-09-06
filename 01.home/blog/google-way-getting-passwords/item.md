---
# http://learn.getgrav.org/content/headers
title: google way getting passwords
slug: google-way-getting-passwords
# menu: google way getting passwords
date: 13-05-2008
published: true
publish_date: 13-05-2008
# unpublish_date: 13-05-2008
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
        - google
        - hacking
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [google,hacking]
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

There are many ways to search for vulnerable sites with google. I’ll show you here how to get username and password from sites that use FrontPage extentions. Microsoft FrontPage Extensions creates a service.pwd file inside the \_vti\_pvt directory in the HTTP server’s document root. This file contains user names and passwords that could be remotely retrieved by an attacker. The good news is that Google indexes this kind of files, so they are very easy to search for. The bad news is that the passwords are encrypted, but wait, this is not really a bad news 🙂 because you can crack them if you are patient and you have the will. If you want to become a hacker, you have to be patient and you have to have the will. Please note: I’m not telling you to hack sites, this stuff is just for learning. So if you want to do illegal things, you should know that jail is a possibility.So lets go to the details:<a name="more"></a>1- Some administrators change the name of service.pwd file to authors.pwd or administrators.pwd or users.pwd or some thing else. So to get the biggest chance to retreive this file we will add an “inurl” condition to our search string in Google like this: inurl:(service authors administrators users)2- The file extension is “pwd” and we are not interested to get other extensions, so we will add an “ext” condition to the search string in Google like this: ext:pwd3- The first line in the file service.pwd is “# -FrontPage-“. So we will search for this string with GoogleAnd here is the full search string:(you can click it to go to Google result page)[inurl:(service authors administrators users) ext:pwd “# -FrontPage-“](http://www.google.com/search?hl=en&lr=&c2coff=1&q=inurl%3A%28service+%7C+authors+%7C+administrators+%7C+users%29+ext%3Apwd+%22%23+-FrontPage-%22&btnG=Search)In the Google result page click any link, you should see some thing like this:# -FrontPage-  
ekendall:bYld1Sr73NLKo  
louisa:5zm94d7cdDFiQ  
Here, there are 2 users with their encrypted passwords. The first user is ekendall, his encrypted password is bYld1Sr73NLKo and the second user is louisa, her encrypted password is 5zm94d7cdDFiQ.  
well u still need to see the passwords decryption urself….

Go to our new site- shankee.com
