---
# http://learn.getgrav.org/content/headers
title: Find IP of remote computers
slug: find-ip-of-remote-computers
# menu: Find IP of remote computers
date: 04-02-2011
published: true
publish_date: 04-02-2011
# unpublish_date: 04-02-2011
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
        - hacking
        - internet
        - IP
        - tutorial
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hack,hacking,internet,IP,tutorial]
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

Most of you may be curious to know how to find the IP address of your friend’s computer or to find the IP address of the person with whom you are chatting in Yahoo messenger or Gtalk. In this post I’ll show you how to find the IP address of a remote computer in simple steps.

I have created a PHP script to make it easier for you to find the IP address of the remote computer of your choice. Here is a step-by-step process to find out the IP address.

1. [Download](http://www.gohacking.com/downloads/scripts/IP_Finder.zip) the [IP Finder script](http://www.gohacking.com/downloads/scripts/IP_Finder.zip) (IP\_Finder.ZIP) that I have created.

2. Open a new account in [X10Hosting](http://x10hosting.com/) (or any free host that supports PHP).

3. Extract the IP\_Finder.ZIP file and upload the two files **ip.php** and **ip\_log.txt** into the root folder of your hosting account using the File Manager.

4. You can rename the **ip.php** to any name of your choice.

5. Set the permission to **777** on **ip\_log.txt**.

Now you are all set to find the IP address of your friend or any remote computer of your choice. All you have to do is send the link of **ip.php** to your friend or the person with whom you’re chatting. Once the person click’s on the link, his/her IP address is recorded in the file **ip\_log.txt**.

For your better understanding let’s take up the following example.

Suppose you open a new account in X10hosting.com with the subdomain as **abc**, then your IP Finder link would be

**http://abc.x10hosting.com/ip.php**

You have to send the above link to you friend via email or while chatting and ask him to visit that link. Once your friend clicks on the link, his IP address will be recorded along with the Date and Time in the **ip\_log.txt** file. After recording the IP address, the script will redirect the person to google.com so as to avoid any suspicion.

To find the recorded IP address check the logs using the following link.

**http://abc.x10hosting.com/ip\_log.php**

The sample log will be in the following format

79.92.144.237 Thursday 07th of May 2009 05:31:27 PM  
59.45.144.237 Thursday 07th of May 2009 05:31:28 PM  
123.92.144.237 Thursday 07th of May 2009 05:31:31 PM

NOTE: You have to replace **abc** with your subdomain name. 

I hope this helps. Express your opinion and suggestions through comments. by [hackiteasy.com](http://hackiteasy.com/)

 

Go to our new site- shankee.com
