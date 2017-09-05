---
# http://learn.getgrav.org/content/headers
title: Make Firefox Fast
slug: make-firefox-fast
# menu: Make Firefox Fast
date: 05-07-2008
published: true
publish_date: 05-07-2008
# unpublish_date: 05-07-2008
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
        - firefox
        - mozilla speedup
        - speed up
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [firefox,mozilla speedup,speed up]
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

Before i came up with a tweak/hack to speed up firefox.. Here i present a modified version of the previous hack..

Hack it easy with step by step guide to do….

Here we start.. open your Firefox web browser. In the address/location bar type “about:config” and then press your Enter key. (NOTE: DON’T TYPE THE COMMAS.)

[![](http://bp0.blogger.com/_hIBd5aAMVaI/SEDWDGPWAiI/AAAAAAAAAII/gfLcb8yKyaY/s200/firefoxtricks1.jpg)](http://bp0.blogger.com/_hIBd5aAMVaI/SEDWDGPWAiI/AAAAAAAAAII/gfLcb8yKyaY/s1600-h/firefoxtricks1.jpg)

  
Step #1:  
In the bar below the address bar type “network.http.pipelining”. Then, right click on it and select Toggle.That cjanges its value from False to True

[![](http://bp3.blogger.com/_hIBd5aAMVaI/SEDWZ82qSJI/AAAAAAAAAIQ/y1QdZYOjwR4/s200/firefoxtricks2.jpg)](http://bp3.blogger.com/_hIBd5aAMVaI/SEDWZ82qSJI/AAAAAAAAAIQ/y1QdZYOjwR4/s1600-h/firefoxtricks2.jpg)

Step #2:  
Now in the Filter bar write “network.http.pipelining.maxrequests”. Right click on that and select modify and select and value more than 4 .I selected 30.Some says that a high no. but that works well for me.

[![](http://bp2.blogger.com/_hIBd5aAMVaI/SEDWl_CpX-I/AAAAAAAAAIY/Vg-mfmn5dOQ/s200/firefoxtricks3.jpg)](http://bp2.blogger.com/_hIBd5aAMVaI/SEDWl_CpX-I/AAAAAAAAAIY/Vg-mfmn5dOQ/s1600-h/firefoxtricks3.jpg)

Step #3:  
Now go to “network.http.proxy.pipelining”. Then right click on it and select toggle. Thats sets it to True from False.  
[![](http://bp0.blogger.com/_hIBd5aAMVaI/SEDWy2Xf3-I/AAAAAAAAAIg/kxWBlLP8Kh8/s200/firefoxtricks4.jpg)](http://bp0.blogger.com/_hIBd5aAMVaI/SEDWy2Xf3-I/AAAAAAAAAIg/kxWBlLP8Kh8/s1600-h/firefoxtricks4.jpg)

Step #4:  
Now go to “network.dns.disableIPv6”. And toggle its value from False to True.  
[![](http://bp0.blogger.com/_hIBd5aAMVaI/SEDXdcIVVUI/AAAAAAAAAIw/Pjsj33vwh7Q/s200/firefoxtricks5.jpg)](http://bp0.blogger.com/_hIBd5aAMVaI/SEDXdcIVVUI/AAAAAAAAAIw/Pjsj33vwh7Q/s1600-h/firefoxtricks5.jpg)

Step #5:  
Now in the Filter bar write “plugin.expose\_full\_path”. Then, right click on it and select Toggle.That cjanges its value from False to True.  
[![](http://bp2.blogger.com/_hIBd5aAMVaI/SEDXIKw84II/AAAAAAAAAIo/9_Wkq9uE2Xk/s200/firefoxtricks6.jpg)](http://bp2.blogger.com/_hIBd5aAMVaI/SEDXIKw84II/AAAAAAAAAIo/9_Wkq9uE2Xk/s1600-h/firefoxtricks6.jpg)

Step #6:  
Now write this in the Filter Bar “network.protocol-handler.external.ms-help”. Now, you are going to create a new Preference Name with an Integer Value. To do this, right-click on this line under Preference Name and select New, then Integer.  
[![](http://bp2.blogger.com/_hIBd5aAMVaI/SEDXnWlbUtI/AAAAAAAAAI4/bkhBFNrWb3s/s200/firefoxtricks7.jpg)](http://bp2.blogger.com/_hIBd5aAMVaI/SEDXnWlbUtI/AAAAAAAAAI4/bkhBFNrWb3s/s1600-h/firefoxtricks7.jpg)

In the New Integer value box type in “nglayout.initialpaint.delay” and click OK. Then in the Enter Integer value box type “0” (that’s a zero) and click OK.  
[![](http://bp2.blogger.com/_hIBd5aAMVaI/SEDXt89hs8I/AAAAAAAAAJA/tD3ykR5qZwM/s200/firefoxtricks8.jpg)](http://bp2.blogger.com/_hIBd5aAMVaI/SEDXt89hs8I/AAAAAAAAAJA/tD3ykR5qZwM/s1600-h/firefoxtricks8.jpg)

Step #7:  
In the Filter bar again type “network.protocol-handler.external.ms-help”. Now, create another new Preference Name with an Integer Value. To do this, right-click on this line under Preference Name and select New, then Integer. In the New Integer value box type in “content.notify.backoffcount” and click OK. Then in the Enter Integer value box type “5” and click OK.  
[![](http://bp1.blogger.com/_hIBd5aAMVaI/SEDYDl9Z16I/AAAAAAAAAJI/ySS_87OYDLI/s200/firefoxtricks9.jpg)](http://bp1.blogger.com/_hIBd5aAMVaI/SEDYDl9Z16I/AAAAAAAAAJI/ySS_87OYDLI/s1600-h/firefoxtricks9.jpg)

Step #8:  
In the Filter bar again type “network.protocol-handler.external.ms-help”. Now, you are going to create another new Preference Name with an Integer Value. To do this, right-click on this line under Preference Name and select New, then Integer. In the New Integer value box type in “ui.submenuDelay” and click OK. Then in the Enter Integer value box type “0” (that’s a zero) and click OK.  
[![](http://bp0.blogger.com/_hIBd5aAMVaI/SEDYRqIwoYI/AAAAAAAAAJQ/IFuJqsExybk/s200/firefoxtricks10.jpg)](http://bp0.blogger.com/_hIBd5aAMVaI/SEDYRqIwoYI/AAAAAAAAAJQ/IFuJqsExybk/s1600-h/firefoxtricks10.jpg)

Now, close your web browser and restart it.  
You would certainly notice the change in speed of your browser. The pages get loaded faster

Do let me know any improvement that could be made.

Do comment if it worked for you too..

Regard  
[HackItEasy](http://hackiteasy.blogspot.com/)

Go to our new site- shankee.com
