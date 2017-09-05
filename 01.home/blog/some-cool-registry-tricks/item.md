---
# http://learn.getgrav.org/content/headers
title: Some Cool registry tricks&#8230;
slug: some-cool-registry-tricks
# menu: Some Cool registry tricks&#8230;
date: 06-06-2009
published: true
publish_date: 06-06-2009
# unpublish_date: 06-06-2009
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
        - registry
        - tech
        - windows
        - XP
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hack,hacking,registry,tech,windows,XP]
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

Here is a list of the coolest registry tricks i came across all these years, packed all in one. Do try these and discover amazing stuff. They are simple and explained in simple steps. But be careful because playing with registry is not a joke  
..

Display Your Quick Launch Toolbar Tip:

Is your Quick Launch toolbar missing from the taskbar?  
To display your familiar Quick Launch toolbar:  
Right-click an empty area on the taskbar, click Toolbars, and then click Quick Launch.

Easy as that your Quick Launch bar appears. To add items to your Quick Launch toolbar, click the icon for the program you want to add, and drag it to the Quick Launch portion of the taskbar.

====================================================================================  
How to remove recycle bin from your desktop Tip:

Open Regedit by going to START – RUN and type Regedit and hit enter. Then you should navigate to following entry in registry HKEY\_LOCAL\_MACHINESOFTWAREMicrosoftWindowsCurrentVersionExplorer  
DesktopNameSpace{645FF040-5081-101B-9F08-00AA002F954E} and delete it. This action should remove recycle bin from your desktop.  
=====================================================================================  
How to stop new programs installed balloon from coming up tip:

Right click on START button and select properties. Click on Customize and go to Advanced tab and deselect check box saying “Highlight newly installed programs”. This would help you stop this annoying feature from popping up every now and then.  
=====================================================================================

Unlock Toolbars to Customize Them Tip:

The new Windows XP now features locking toolbars, and you can adjust them. You may customize a lot of the Windows XP features such as the Taskbar, Start Menu, and even toolbar icons in Internet Explorer and Outlook Express. Remember your right-click:  
\* Right-click on a toolbar, and then click Lock the Toolbars to remove the check mark.  
\* Right-click on the toolbar again, and then click Customize.

You may add or remove toolbar buttons, change text options and icon options. When you’ve got the toolbar customized, click Close. Now right-click on the toolbar and then click Lock the Toolbars to lock them in place. com

=====================================================================================

Want to remove shared documents folder from My Computer window tip:

Some don’t like my shared documents folder option. If you are one of that, here is a trick to remove it.Open registry editor by going to START-RUN and entering regedit.  
Once in registry, navigate to key HKEY\_LOCAL\_MACHINE SOFTWARE Microsoft Windows CurrentVersion Explorer My Computer NameSpace DelegateFolders You must see a sub-key named {59031a47-3f72-44a7-89c5-5595fe6b30ee}. If you delete this key, you have effectively removed the my shared documents folder.

=====================================================================================  
How to improve on shutdown time ? Close apps automatically & quickly at shutdown tip:

Open Registry by going to START-RUN and typing REGEDIT. Navigate to HKEY\_CURRENT\_USERCONTROL PANELDESKTOP and look for AutoEndTasks. On my computer default value is 0. Change it to 1. Thats all. Further more you can reduce the time it takes for Windows to issue kill directive to all active/hung applications.  
In doing this only constraint that you should make sure exists is that HungAppTimeout is greater than WaitToKillAppTimeout. Change the values of WaitToKillAppTimeout to say 3500 (since default value for HungAppTimeout 5000 and for WaitToKillAppTimeout is 20000)

=====================================================================================

Are you missing icons Tip:

Are you missing icons? You may be wondering where all the icons from your desktop are in Windows XP? Well if you’re like me, you like to have at least My Computer, My Network Places, and My Documents on the your desktop.  
You need to:  
\* Right-click on the desktop, and then click Properties.  
\* Click the Desktop tab and then click on Customize Desktop.  
\* Put a check mark in the box next to My Document, My Computer, My Network Places, or Internet Explorer, to add those familiar icons to your desktop. Easy yes!  
=====================================================================================  
How to login as administrator if you don’t see it available tip:

Unless and until you have run into issues and fixing XP (under which case you have to go to Safe Mode to login as Administrator), you can get to administrator screen by simply pressing CTRL+ALT+DELETE twice at the main screen.  
=====================================================================================

Speedup boot up sequence by defragmenting all key boot files tip:

Open Registry by going to START-RUN and typing REGEDIT. Navigate to HKEY\_LOCAL\_MACHINESOFTWAREMicrosoftDfrgBootOptimizeFunction. In right hand panel look for Enable. Right click on it and set it ‘Y’ for enable. This is the way I have it set on my computer. This will help speedup boot time.

Use a Shortcut to Local Area Network Connection Information:

=====================================================================================

Use a Shortcut to Local Area Network Connection Information Tip:

Here’s something new in Windows XP, instead of using the command line program and typing ipconfig to get local area network information, you can try using the following shortcut:  
\* Click on Start, point to Connect to, and then click Show All Connections.  
\* Right–click the connection you want information about, and then click Status.  
\* In the connection Properties dialog box, click the Support tab.  
\* For more information, click on the Advanced tab.

To automatically enable the status monitor each time the connection is active, in the connection Properties dialog box, select the Show icon in taskbar notification area when connected check box.

=====================================================================================

Do you know you can have Virtual Desktops (like in Linux) with PowerToys ?

If you have powertoys installed on Windows XP Its available for free at Microsoft download webpage. It is very easy to enable Microsoft Virtual Desktop Feature. Simply right click on the Start Panel Bar also called TaskBar, Click on Tool Bar and select Desktop manager.  
You would see a set of 5 icons placed on the right portion of the TAskBar. Click on number 1 to 4 to go to any of the desktops. Now you have have four different Active Desktops.  
IMPORTANT NOTE: You may see a little degradation in performance.

=====================================================================================

Customize Internet. Explorer Title bar tip:

This tip won’t make your computer any faster but may help personalize your computer experience. Open Registry by going to START-RUN and typing REGEDIT. Navigate to HKEY\_CURRENT\_USERSoftwareMicrosoftInternet. ExplorerMain. In right hand panel look for string “Window Title” and change its value to whatever custom text you want to see.

Easy Text Size Change in Help & IE Tip:  
I mentioned a way that you can change the size of the text that is display in the Help file and in Internet Explorer. As it turns out if you have a “wheel mouse,” there is an even easier way to change the text size. In Internet Explorer or when viewing a Help file, simply hold the ctrl key while you spin the mouse wheel up to increase text size, or down to decrease text size.  
Java VM: Java applets run in Internet Explorer 6 (a component of Windows XP) just as they run in older versions of Internet Explorer. The Java VM is not installed as part of the typical installation, but is installed on demand when a user encounters a page that uses a Java Applet. For more information see the Microsoft Technologies for Java Web site.

=====================================================================================

Windows XP Shutdown and Power Off Tip:

On some computers, by default, Windows XP doesn’t power off the computer when you tell it to shut down. However, if your computer is relatively new, it can probably by shut completely off by WinXP. To configure your computer for this behavior, simply open the Control Panel, open Performance and Maintenance, then Power Options. On the APM tab, check next to “Enable Advanced Power Management support,” then click OK. The next time you choose “Shut Down” from the Start Menu, your computer should shut down completely and then power off.

=====================================================================================

Customize Explorer Toolbar Tip:

In Windows Explorer, you can customize the toolbar to make Explorer even more handy. The Toolbar is the bar of icons directly underneath the menu bar. It contains icons for going back, up one level, displaying folders or search, etc. You can right-click an open area of this Toolbar and choose Customize to change the order of these icons, and even to add new icons to it. For instance, I like to add the Map Drive and Disconnect buttons. In Windows XP, you may have to unlock the Taskbar before you can make changes in Windows Explorer.  
Lock the Taskba – If you find that your Windows XP Taskbar keeps being changed, or moved to one side or the top of your screen, and you didn’t mean to have it do that, this tip is for you. Once you have your Task Bar arranged the way you like it, in the right location on the screen, and with all the right toolbars and icons, you can lock it, so that it won’t get changed accidentally. To lock the Taskbar, simply right click it and choose Properties. In the window that appears, check the box (click) next to “Lock the Taskbar.” Now you won’t accidentally bump the mouse and have your Task bar end up on another side of the screen.

=====================================================================================

Check Personal Firewall Status Tip:

In the previous tip, I mention how to turn on Windows XP’s Personal Firewall feature. But once you turn it on, your connection looks just the same as it did before. How can you check the status of the connection and the firewall? Simply open Control Panel from the Start Menu, open Internet and Network Connections, then Network Connections. By default the view is of large icons.  
Click the View Menu, and choose “details” in order to reveal several more columns of information about the connections that your computer has. Check the Status column to see if your connection is currently connected, and whether or not it is “firewalled.” You can even drag the column headings around (I like to slide the Status column right next to the Name column. You can even remove entire columns by right-clicking the column heading and unchecking it.

Where does Window’s Product Id get stored Tip:

There are two places at least where ProductId gets stored. To see the first place, open Registry by going to START-RUN and entering REGEDIT and Navigate to [HKEY\_LOCAL\_MACHINESOFTWAREMicrosoftWindows NTCurrentVersion]. In right pane, look for key by the name “ProductId”. This is your Windows Product Id. Alternatively you can navigate to [HKEY\_LOCAL\_MACHINESOFTWAREMicrosoftWindowsCurrentVersion] and still find same field with the name ProductId.

=====================================================================================

You can Keep Your Favorite Programs on Top of the Start Menu tip:

Do you have a favorite program that you frequently use? Elevate its priority on the Start menu by putting it at the top of the list. This ensures that the program will remain on the Start menu and cannot be bumped by other programs, even if you use the others more frequently.  
Right-click the link to your favorite program on the Start menu and select Pin to Start Menu.  
Your program will be moved permanently to the top part of the list, just below your browser and e-mail programs.

=====================================================================================

Having problems with Outlook Express ? Does it ask for password every time you connect tip:

If this is problem for you. Sometimes no matter what you do, Outlook Express forgets your password and asks you to enter it again each and every time you connect to your mail server.I have a solution that may work for you. Open Registry by going to START-RUN and entering REGEDIT and Navigate to HKEY\_CURRRENT USERSoftwareMicrosoft and look for “Protected Storage System Provider”. There is a good chance that you will see this folder. If you have it. Simply delete it. More than likely, you have solved your problem.

=====================================================================================

How to avoid auto play of CD ? Way I like best tip.

Hey this time no registry trick even though there are ways in registry to do it. In earlier operating systems only those CD that had autorun.inf file in their root directory were able to execute on its own but with advent of WINDOWS XP it has become possible with just about anything. Well sometimes it is good but there are other times when you want to avoid this part of automation. What would I do. Simply press SHIFT key when you enter a CD in your CD drive. It won’t Auto play. For those of you, who do want a registry hack. Here it is:  
Open Registry and navigate to [HKEY\_LOCAL\_MACHINESOFTWAREMicrosoftWindowsCurrentVersionpoliciesExplorer] and look for key “NoDriveTypeAutoRun” and set its value to 185 (decimal). This would stop autoplay.

=====================================================================================

This tip to speed up the Start Menu in Windows XP.  
Did you know you can customize the speed of the Start Menu by editing a Registry Key.

\* Click Start, and then click Run.  
\* Type Regedit in the box, and then click OK.  
\* Expand the menu in the left panel and select the HKEY\_CURRENT\_USERControl PanelDesktop folder.  
\* Scroll down in the right panel and double click on the MenuShowDelay file.  
\* In the Value Data box, change to default value for the menu speed from 400 to a lesser number, such as 1.  
\*Click OK.  
Caution: Incorrectly editing the registry may severely damage your system. Before making changes to the registry, you may want to back up any valued data on your computer.

=====================================================================================

Customizing Windows Explorer Context menu (right click menu in windows explorer)

Ever wondered how does the right click menu (which is actually a context menu) work ? For example, when I right click in windows explorer, I see an option which says “open command window here”. Do You know why I see this ? Well I see this because I have following entries in my registry.

[HKEY\_CLASSES\_ROOTDriveshellcmd]  
@=”Open Command Window Here”  
[HKEY\_CLASSES\_ROOTDriveshellcmdcommand]  
@=”C:WINDOWSSystem32cmd.exe /k cd “%1″”  
If You have never used a tweaking utility and have newly installed Windows XP, You would not see this option. You would have to navigate to [[HKEY\_CLASSES\_ROOTDrive] go and create two subkeys (“cmd” and within that “command” and would have to put the text “Open Command Window Here” without quotes in default string value of “cmd” key and the text “C:WINDOWSSystem32cmd.exe /k CD”%1″” without quotes in default string value of command key). After this You need to REBOOT for these changes to take effect.  
Trick is in adding similar entries for other applications as well even though its much harder to come with ideas about what to put in the context menu!!!! .

Go to our new site- shankee.com
