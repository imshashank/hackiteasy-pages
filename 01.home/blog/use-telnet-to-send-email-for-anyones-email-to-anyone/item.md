---
# http://learn.getgrav.org/content/headers
title: Use telnet to send email for anyone&#8217;s email to anyone
slug: use-telnet-to-send-email-for-anyones-email-to-anyone
# menu: Use telnet to send email for anyone&#8217;s email to anyone
date: 05-06-2010
published: true
publish_date: 05-06-2010
# unpublish_date: 05-06-2010
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
        - email
        - hack
        - internet
        - tech
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [email,hack,internet,tech]
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

Send anonymous email from anyone to anyone. You hear it right from any email ID to any email ID. You can send any email to your friend from their email ID. Or you might even send someone an email from Steve Jobs’s email. Here is the simple hack that let’s you do just that using the most common feature available in all computers. Just follow the simple procedure. And so comment for any help.

1** Open the cmd prompt**. (Start -> Run or press win key + R, then type cmd and presss OK )

 

 



 

   
2** Type **telnet server**.com 25** (where “server.com” is the name of the smtp (outgoing) server of your email provider, such as smtp-server.austin.rr.com). This can be found by checking your account info in the program you normally use for email.

   
3** Type **HELO server**.com**. (Or “EHLO server.com”)

   
4**Type **MAIL FROM**:**you@server.com.

   
5You may get a message saying “250 ok”

****

   
6**Type **RCPT TO**:**Friend1@anotherserver.com, friend\_two@someotherserver.org, friend.3three@Someserver.com, etc.

   
7 again, You may get a message saying “250 ok”

****

   
8** To write the message, type **DATA** and press Enter**. 

1. On the first line type **SUBJECT:yoursubject** and press Enter **twice**.
2. Continue typing your message.
3. Put a single period (.) on a line by itself and press Enter to send your message. The server should say ‘Message accepted for delivery’. (Or it says 250 OK id=`a long id`)
 


9**Type **QUIT** to exit Telnet**. This will not work if your ISP uses dynamic IP to give you internet access. If you could try using some botnet server that is quite easy. If you would request would post a tutorial for that as well.

Well use the hack at your own risk as you can easily be traced back, as each email also sends your IP. You might use some IP re-routing software like anonymizer. But still use it cautiously. And this post was only for educational purpose.



Go to our new site- shankee.com
