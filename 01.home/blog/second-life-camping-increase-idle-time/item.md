---
# http://learn.getgrav.org/content/headers
title: Second life camping increase idle time..
slug: second-life-camping-increase-idle-time
# menu: Second life camping increase idle time..
date: 05-06-2008
published: true
publish_date: 05-06-2008
# unpublish_date: 05-06-2008
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
        - idle time
        - second life hack
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [idle time,second life hack]
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

[![](http://bp3.blogger.com/_V2JZuLkPrjQ/SEkBzFQ4lZI/AAAAAAAAAvQ/EfMibGknrSw/s320/Second+Life.jpg)](http://bp3.blogger.com/_V2JZuLkPrjQ/SEkBzFQ4lZI/AAAAAAAAAvQ/EfMibGknrSw/s1600-h/Second+Life.jpg)  
[![](http://bp1.blogger.com/_V2JZuLkPrjQ/SEkBzSktYSI/AAAAAAAAAvY/M1bnXJk9xVo/s320/secondlife.jpg)](http://bp1.blogger.com/_V2JZuLkPrjQ/SEkBzSktYSI/AAAAAAAAAvY/M1bnXJk9xVo/s1600-h/secondlife.jpg)  
[![](http://bp2.blogger.com/_V2JZuLkPrjQ/SEkBzo59bjI/AAAAAAAAAvg/gj3Gj5_rjLY/s320/secondlife_1.jpg)](http://bp2.blogger.com/_V2JZuLkPrjQ/SEkBzo59bjI/AAAAAAAAAvg/gj3Gj5_rjLY/s1600-h/secondlife_1.jpg)  
[![](http://bp0.blogger.com/_V2JZuLkPrjQ/SEkBz6Tq6KI/AAAAAAAAAvo/iML7WL9Ootc/s320/secondlife-postcard.jpg)](http://bp0.blogger.com/_V2JZuLkPrjQ/SEkBz6Tq6KI/AAAAAAAAAvo/iML7WL9Ootc/s1600-h/secondlife-postcard.jpg)

Hey i wanted to earn more from SL (second life)

So i just used this below trick to con SL,

as they make u logout due to inactivity

While a good number of Second Life’s users spend a large amount of time in the world SL, at times real life presents interruptions which can take attention away from the keys (AFK). By default if one is idle for more than 15 minutes in SL the system will log out an account due to inactivity. While this is beneficial for keeping the asset servers and other key operation handling machines from getting too overloaded, it’s not the most favorable of an occurrence when the users is planning to return shortly. Not to mention the hassle of reconfiguring certain options that fail to save between sessions such as [disabling of lesser used render types](http://www.virtuallytime.com/2007/10/11/how-to-reduce-client-side-lag-in-second-life/) each time after logging in.

Disabling the logout due to inactivity can be disabled or worked around by various ways. Some of the more common are covered below…

**I. Changing the value of the client AFKTimeout ****variable.**

> 1. Enable the Debug Menu, if it isn’t already viewing (you do not see the Client and Server menus in your client). Press Ctrl+Alt+D.  
> 2. From the Client Menu, located at the top middle of your client’s menu bar, go Client > Debug Settings.  
> 3. Using the Debug Settings menu, pick the AFKTimeout variable from the drop down list.  
> 4. Set the value to 9999999, which should change to -2147483.750 after entering.  
> 5. (optional) You can disable the AFK gesture by choosing AllowIdleAFK from the Debug Settings Window. Then change the default value from TRUE to FALSE.

**II. Use a third party macro program to keep from going idle.**

> While you may be AFK or too preoccupied with something else, to set focus directly on the SL client every so often, a continually running macro that performs such an action is not.
> 
> A number of pre-written macro scripts for various applications and freestanding are available. Or you can write your own if so inclined as it’s a simple enough program. Here are a couple scripts for common macro application.

**Anti-AFK Macro using [AutoHotKey](http://www.autohotkey.com/) with Multi-Client Support  
**(get a copy of the [script below](http://www.virtuallytime.com/files/second-life-idle-afk-macro-autohotkey.txt) or download the [compiled executable here](http://www.virtuallytime.com/files/sl-anti-idle-multi.exe))

> SetTitleMatchMode, 3MsgBox, SL Anti-Idle for Multiple Clients is now running.StartingLabel:GroupAdd, clients, Second LifeWinGetActiveTitle, Title<br></br>MouseGetPos, xpos, ypos; MsgBox, The active window is "%active_pid%".<br></br><br></br>If WinExist("Second Life")     ;<br></br>{<br></br>GroupActivate, clients
> 
>  
>     ;WinActivateMouseMove, 20, 30, 50, RMouseMove, -20, -30, 50, R<br></br>GroupActivate, clients;WinActivate<br></br>MouseMove, 20, 30, 50, R<br></br>MouseMove, -20, -30, 50, R<br></br><br></br>GroupActivate, clients<br></br>;WinActivate<br></br>MouseMove, 20, 30, 50, R<br></br>MouseMove, -20, -30, 50, R<br></br><br></br>GroupActivate, clients<br></br>;WinActivate<br></br>MouseMove, 20, 30, 50, R<br></br>MouseMove, -20, -30, 50, R<br></br><br></br>}<br></br><br></br>else<br></br>{<br></br>MsgBox, Unable to find any SL clients.<br></br>ExitApp<br></br>}<br></br><br></br>IfWinExist, %Title%<br></br>{<br></br>WinActivate<br></br>}<br></br><br></br>else<br></br>{<br></br>MsgBox, Unable to find the previous program.<br></br>}<br></br><br></br>MouseMove, %xpos%, %ypos%<br></br>Sleep 900000 ; 15 minutes<br></br>Goto, StartingLabel

**Ultra-simple Script using [Macro Scheduler](http://www.mjtnet.com/)**  
note: The focus (above all other windows and selected) must remain on the Second Life Viewer (client) for this script to work.  
(get a copy of the [script below](http://www.virtuallytime.com/files/second-life-idle-afk-macro-autohotkey.txt))

> Label>StartPress EscWait>600<br></br>Press Enter<br></br>Wait>10<br></br>Goto>Start

**III. Wearing a special attachment on your avatar.**

> This option to longer exists. It used to defeat the anti-idle by triggering the return from AFK gesture, to be acted by your avatar, fooling the system into thinking you have returned. Update to the SL client about half a year ago made this action no longer recognized as actual live user input.

**IV. Continually Keep a Keyboard Key Pressed Using a Penny**

> This is not a highly recommended option but does work in a pinch for most types of keyboards.
> 
> 1. Open up the local chat bar in the SL client by pressing the Enter key.  
> 2. Press and hold a alpha-character key.  
> 3. While continuing to press the key down, take a penny and wedge it between the top of the key your holding down and key above.

While a good number of people use a “stay alive” macro to camp for long periods of time or give their actual land artificially high traffic counts, such an ability can be used for good as well. For me, I always have the idle logout disabled, using the first option listed above, as I find myself using SL but working in PhotoShop and other applications making SL content a good amount of time. Has saved me a good number of headaches. So considered disabling this option by using any of the ways shown above and save yourself some time and hassles.

Go to our new site- shankee.com
