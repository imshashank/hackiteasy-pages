---
# http://learn.getgrav.org/content/headers
title: Top 12 Windows 7 Hacks You Must Know
slug: top-12-windows-7-hacks-you-must-know
# menu: Top 12 Windows 7 Hacks You Must Know
date: 07-06-2009
published: true
publish_date: 07-06-2009
# unpublish_date: 07-06-2009
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
        - microsoft
        - tech
        - windows
        - windows 7
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hack,microsoft,tech,windows,windows 7]
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

If you are looking for Windows 7 hacks, I am sure you can finds loads of them on web. What matters is, how many of them are really important. Do you think unlocking the Taskbar in Windows 7 is something very exciting? Obviously, not for the majority of users its nothing cool. Instead if you are interested in Windows 7 Hack that can help you to get rid of expiry date, remove watermark, or disable send feedback link then my article can surely help you out. I organized a set Top 12 Windows 7 Hack You Must Know. This list includes some of the handy posts on Windows 7 hacks in our blog. I have also provided the sources where you can find the hacks.![windows-7-hack](http://blog.taragana.com/wp-content/uploads/2009/03/windows-7-hack.jpg)

## 1. How to Get Windows Vista-Style Taskbar in Windows 7

It’s hard to deny that Windows Vista scores high on appearance. Here’s your chance to give the Windows 7 a Vista look. Just follow the steps mentioned below

Step 1: Right-click on the taskbar and choose the properties dialog. Select the small icons checkbox  
Step 2: Under the taskbar buttons setting, choose combine when taskbar is full. Although it’s not pixel-perfect in accuracy, but, it’s close from a functionality point.

[Source ](http://blog.taragana.com/index.php/archive/how-to-achieve-windows-vista-style-taskbar-in-windows-7-in-two-simple-steps/)

## 2. How to Change Windows 7 Log On Screen

If you don’t want the same old blue log on screen for your Windows Vista, here’s what you gotta do. Go ahead with the steps below.

Step 1: Download the file – http://www.mediafire.com/?e9y3j3vme0w  
Step 2: Click on Save and save the .zip file to the desktop  
Step 3: Open the .zip file and extract the .reg file to the desktop  
Step 4: Right click the .reg file (On Desktop) and click on Merge.  
Step 5: Click on Run, and press Yes, Yes, and OK when prompted  
Step 6: Save the custom .jpg image you want to use to the desktop with the name backgroundDefault.jpg  
Step 7: Check to see what your primary display screen resolution is. (You can do it by right clicking on any empty space on your desktop and choose screen resolution and then actuate it with your monitor’s specification.)  
*[NOTE: For example, mine is 1920 x 1280.]*  
Step 8: Open Paint, and click on the File icon (top left corner), Open, and navigate to and select the .jpg image from step 6.  
*[NOTE: You can open Paint by typing mspaint.exe in the Start menu search line]*  
Step 9: In Paint, click on Resize, dot Pixels, uncheck Maintain aspect ratio, then resize the .jpg image to the screen resolution size in step 7 (whatever be yours)  
Step 10:Save the .jpg file to the desktop with the exact file name below with the screen resolution size of the image. When completed, close Paint  
Step 11: In Windows Explorer, navigate to  
C:Windowssystem32oobeinfobackgrounds  
Step 12: Copy and Paste the .jpg files from step 10, and from step 6 into the C:Windowssystem32oobeinfobackgrounds folder, then close the window  
Step 13: You’re logon screen is now changed. You can press Ctrl+Alt+Del to test it. Click on Cancel to return to the desktop.  
[NOTE: You can now delete the .reg and .zip files on the desktop if you like.]

[Source](http://blog.taragana.com/index.php/archive/hack-to-change-windows-7-log-on-screen/)

## 3. How to Unlock the Windows 7 Hidden Themes

The Windows 7 beta has a pack of hidden and locked themes. Let’s see how you can unlock the hidden themes.

Step 1: Open the Explorer (Windows + E) and go to C:Windowswinsxs  
Step 2: Enter \*.theme into the search field. Alternately you can use the \* sign on the number block.  
Step 3: You’ll get the Click me prompt  
Step 4: Double-click the themes ZA, US, GB, CA, AU to install them.

[Source](http://blog.taragana.com/index.php/archive/windows-7-hidden-themes-in-4-simple-steps/)

## 4. How to Enable the Windows Aero in Windows 7

If you were looking for the best designed and most transparent Microsoft user interface then you can’t escape Windpws Aero. Here’s a hack to enable Windows Aero in Windows 7. But before you proceed with the steps keep a backup of your registry.

Step 1. Click on the Start Menu and type “regedit” into the search box. When the program appears click to open the regedit.exe icon.  
Step 2. Locate the Key below  
HKEY\_CURRENT\_USERSoftwareMicrosoftWindowsDWM

Step 3. Look to the pane on the right of the key hierarchy. Right click on the white area and select New > DWORD (32 bit) Value.  
Step 4. As the value appears name it UseMachineCheck.  
Step 5. Repeat and create 2 more DWORD Values, Blur and Animations  
Step 6. First double-click the value just created with the UseMachineCheck and enter 0 in the Value Data box. Do the same for Values Blur and Animations. Then click OK.  
Step 7. Now close the Registry Editor.  
Step 8. Open the Start Menu and type “cmd” into the search box, right-click on cmd.exe when the program appears in the search results. Now, select Run as Administrator from the drop-down.  
Step 9. As the Command Prompt opens type the commands below

i) Net Stop uxsms – this command will stop the Desktop Windows Manager Session Manager

ii) Net Start uxsms– this command will restart it

Step 10. Once you close the Command Prompt. Right click on the desktop and click on Personalize from the menu.  
Step 11. Click on the Window Color and Appearance in the Personalization Windows Aero the Color Scheme menu.

[Source](http://laptoplogic.com/resources/9-amazing-yet-simple-windows7-hacks)

## 5. How to Enable the Quick Launch Bar in Windows 7

It is a surprising to see that the Quick Launch Bar has not been enlisted in the easy to enable list. Here’s what you gotta to do to enable the Quick Launch Bar.

Step 1:Right-click on the Taskbar and select Toolbars > New Toolbar from the menu.  
Step 2: Copy and paste the address provided below into the Address bar

%SystemDrive%Users%username%AppDataRoamingMicrosoftInternet Explorer

then click the arrow to the right of the Address bar to navigate to the folder.

Step 3: Select the Quick Launch folder listed and click the Select Folder button

[Source](http://laptoplogic.com/resources/9-amazing-yet-simple-windows7-hacks)

## 6. How to Remove Send Feedback link in Windows 7

The bug that troubles the window in Windows 7 is the send feedback link. This is a simple fix to get rid of this pique. Make sure you have a backup of the registry before you proceed.

Step 1: Click on the Start Menu and type “regedit” into the search box, click to open the regedit.exe icon when the program appears.  
Step 2: Look for the following Key HKEY\_CURRENT\_USERControl PanelDesktop  
Step 3: Right-click on the white space in the In the pane to the right of the key hierarchy and select New > DWORD (32 bit) Value.  
Step 4: Now as the value appears name it FeedbackToolEnabled  
Step 5: Double-click the value that was created with FeedbackToolEnabled and enter 0 in the Value Data box, and then click OK.  
Step 6: To effect the changes Log off the computer and log on to the system.

[Source](http://laptoplogic.com/resources/9-amazing-yet-simple-windows7-hacks)

## 7. How to Start Windows Explorer from ‘My Computer’

For those who are in the habit of customizing the Windows for convenience and fun can try this out on Windows 7. With this hack you can set the indows Explorer to start from My Computer instead. This will help you to access the different hard disk drives or removable disks easily. Let’s go through the steps

Step 1: navigate to Windows Explorer in the Start Menu (it’s in the Accessories folder). Then edit the properties and change the target to read:  
%SystemRoot%explorer.exe /root,::{20D04FE0-3AEA-1069-A2D8-08002B30309D}

This will make the explorer open folders/drives in new Windows. To fix this see the next step

Step 2: Set the target to

%SystemRoot%explorer.exe /e,::{20d04fe0-3aea-1069-a2d8-08002b30309d}

[Source ](http://blog.taragana.com/index.php/archive/windows-7-hack-remove-1st-july-expiry-date-disable-send-feedback-button-and-remove-watermark-3-in-1-patch/)

## 8. Remove Watermark from Windows 7 beta 1 Desktop

WIndows 7 is in its beta version and you can realize it well with the lapses in the operating system. One such annoying feature with the OS is the water mark embedded in the desktop. To remove the watermark you can follow the steps below. Before beginning with the steps you need to ensure that the User Account Control is disabled.

Step 1: Click on the Start Menu> Control Panel  
Step 2: Click on User Accounts. Change User Account Control Settings and adjust the slider so that it is at the bottom of the screen (Never Notify).  
Step 3: Next restart the computer  
Step 4: After the rebooting browse to the following directory

C:WindowsSystem32en-US  
Step 5: Once you’re in the directory locate and right-click the following file  
user32.dll.mui  
Step 6: From the drop down menu select the properties. Click on the Security tab and click on the Advanced button at the buttom.  
Step 7: In the Advanced Security Settings window click on the Owner tab and click Edit.  
Step 8: Click OK to effect the changes and return to the original file Properties window.  
Step 9: Under the security tab, Click Edit.  
Step 10:Select Users and a checkmark to the all the checkboxes giving you full control of the file  
Step 11: Rename user32.dll.mui to user32-backup.dll.mui  
Step 12: Download the patched version of the files – 32 bit Download or 64 bit Download  
Step 13: After the files have been downloaded extract it from the original directory  
C:WindowsSystem32en-US  
Step 14: Restart the computer

[Source](http://laptoplogic.com/resources/9-amazing-yet-simple-windows7-hacks)

## 9. How to Unibstall Internet Explorer for Good

This is for those users who never need to use the Internet Explorer. Just follow the steps below to uninstall IE

Step 1: Click on the Start Menu and move to the Control Panel  
Step 2: Select the Programs and Features  
Step 3: Click on Turn Windows features on or off link located on the left pane  
Step 4: The Turn Windows features on or off window appears. Uncheck the Internet Explorer 8 and click OK  
Step 5: After a couple of restarts Internet Explorer should be gone for good

[Source](http://laptoplogic.com/resources/9-amazing-yet-simple-windows7-hacks)

## 10. How to Enable Recording in Windows 7

In windows 7 the WaveMix and SterioMix are disabled by default. I’ll let you the hack to activate the recording device. Here are the steps

Step 1: Right click on the speaker icon. Now look for the Recording Devices and select it.  
Step 2: Now right click and select the option Show Disabled Devices  
Step 3:Select the Wave Out Mix device and Enable it. Click on Set as Default Device and open up the Audacity.

[Source](http://blog.taragana.com/index.php/archive/how-to-enable-recording-in-windows-vista-and-windows-7/)

## 11. How to Get Rid of Windows 7 Expiry Date

Install the TimerNuke patch to remove the files associated with activation. It will disable the related services. So you can continue with the Windows 7 even after the activation timeline is over. Just download the patch and install.

[Download](http://www.google.com/url?sa=U&start=1&q=http://www.mydigitallife.info/2008/12/30/timernuke-crack-free-download-to-disable-activation-of-windows-7-and-server-2008/&ei=kbnASbmmHMPQkAWhsZ0x&usg=AFQjCNFmHNSfFsruE5UfLXqi5RHXFMkIxw)  
Source

## 12. Windows 7 Installed on a Macbook Pro

This is for the MacBook Pro users who are yet to install the Windows 7. From the sites below you can get the instructions to install the latest windows OS on MacBook Pro.

[Windows 7 installation on Macbook Pro ](http://www.engadget.com/2009/01/11/windows-7-gets-installed-on-macbook-pro-explained/)  
[Source](http://laptoplogic.com/resources/9-amazing-yet-simple-windows7-hacks)

Enjoy the hacks. Let me know if you have some more tips to share.

 

Go to our new site- shankee.com
