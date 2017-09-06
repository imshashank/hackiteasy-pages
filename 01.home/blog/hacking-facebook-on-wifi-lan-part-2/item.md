---
# http://learn.getgrav.org/content/headers
title: Hacking facebook on wifi LAN part 2
slug: hacking-facebook-on-wifi-lan-part-2
# menu: Hacking facebook on wifi LAN part 2
date: 02-02-2014
published: true
publish_date: 02-02-2014
# unpublish_date: 02-02-2014
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
        - facebook
        - hack wifi password
        - hacking
        - internet
        - lan
        - learn to hack
        - wifi
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [cookies,facebook,hack wifi password,hacking,internet,lan,learn to hack,wifi]
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

Im back with the second part of the post. At the end of the last post, we successfully re-routed all the traffic from the victim’s computer to the router through our computer.Next, we have to capture their facebook cookies through wireshark. So How do you go about doing that? It’s very simple actually.

- Open up wireshark
- Goto capture – > Interfaces in the top menu and select your interface. It’s usually the one which has an IP address and  a certain number of packets flowing through it.
- Next goto capture and click on start.. It should look something like this

[![](http://35.160.74.13/wp-content/uploads/2014/02/wire.png?w=640&h=338 "wire")](http://35.160.74.13/wp-content/uploads/2014/02/wire.png)

This window has all the packets sent from the victim’s/victims’ computer to the router and all the packets sent from the router to the victim.

Next in the filter type  “http.cookie contains datr”.  You ask why? Because, when a user logs in to facebook, he is given some cookies which is unique to him. If we replace our cookies with the victim’s cookies, we can login to his account as then facebook wont know the difference.

![](http://35.160.74.13/wp-content/uploads/2014/02/wire8-300x60.png "wire8")

You now have the cookies. To get the information stored in the cookies,  right-click on any one of the cookie and click on Follow TCP stream.

[![](http://35.160.74.13/wp-content/uploads/2014/02/wire3.png?w=640&h=341 "wire3")](http://35.160.74.13/wp-content/uploads/2014/02/wire3.png)

In the TCP stream look for the line  Cookie: ( and all cookie names). If it doesn’t come, select some other packet in wireshark and click on follow tcp stream for that. You can see the source IP and destination IP in wireshark. So if you have more than one source IP , then you know you have the cookies of more than one account on your LAN. This is what I got when I did it.

[![](http://35.160.74.13/wp-content/uploads/2014/02/wire4.png?w=640&h=394 "wire4")](http://35.160.74.13/wp-content/uploads/2014/02/wire4.png)

So now you have it :D. The datr cookie, c\_user cookie, lu cookie, sct cookie, w cookie and xs cookie. These are the main cookies you need.

Now open firefox and goto [http://www.facebook.com](http://www.facebook.com/). Once there, click on cookies in the web developer add on which you had installed in the last post. Then do the following

- ·         Clear session cookies

- ·         Delete domain cookies

- ·         Delete path cookies.

[![](http://35.160.74.13/wp-content/uploads/2014/02/wire5.png?w=640&h=255 "wire5")](http://35.160.74.13/wp-content/uploads/2014/02/wire5.png)

IMPORTANT: Once you do this, again type [http://www.facebook.com](http://www.facebook.com/) in the URL and click enter. Basically you are reloading facebook after deleting all cookies.

Now login to your account with your username and password. After logging in , click on cookies in web developer add-on and click on “view cookie information”.

And there you have all your cookies :p. Now what to do?! I guess you know it by now. !

Click on “edit cookie” for each cookie there and replace the cookie value with the value you got through wireshark.

If you did not get all the  cookies in wireshark its OK! But mainly, you should look to replace the datr cookie, c\_user cookie, lu cookie, sct cookie, w cookie and xs cookie.

[![](http://35.160.74.13/wp-content/uploads/2014/02/wire6.png?w=640&h=359 "wire6")](http://35.160.74.13/wp-content/uploads/2014/02/wire6.png)  


After replacing all the  cookie values with the ones you got in wireshark, just refresh the facebook page. And thats it! You are in to the victim’s account! You have HACKED a facebook account on LAN.:D



 

Go to our new site- shankee.com
