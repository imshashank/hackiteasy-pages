---
# http://learn.getgrav.org/content/headers
title: How to Recover and Reset Password in windows 7/Vista/XP/2003/2K/NT
slug: how-to-recover-and-reset-password-in-windows-7vistaxp20032knt
# menu: How to Recover and Reset Password in windows 7/Vista/XP/2003/2K/NT
date: 25-04-2010
published: true
publish_date: 25-04-2010
# unpublish_date: 25-04-2010
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
        - hacking
        - windows
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hacking,windows]
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

Forgetting your Windows administrator login password. With no way to get into the system, you can’t even perform basic maintenance, let alone a thorough tune-up. Formatting is always an option, but we consider that a last resort. (Plus, guess who’s going to have to help reinstall all the programs lost after a wipe?) But all hope is not lost. There are a few ways to actually retrieve a lost Windows account password. Read on, and we’ll show you the light.

The first thing which you check if you forget login password. When we install Windows, it automatically creates an account “Administrator” and sets its password to blank. So if you have forget your user account password then try this:  
Start system and when you see Windows Welcome screen / Login screen, press ctrl+alt+del keys twice and it’ll show Classic Login box. Now type “Administrator” (without quotes) in Username and leave Password field blank. Now press Enter and you should be able to log in Windows.  
Now you can reset your account password from “Control Panel -> User Accounts”.  
Same thing can be done using Safe Mode. In Safe Mode Windows will show this in-built Administrator account in Login screen.

If you sure that you had completely no idea what your password is, then keep trying these methods.

Method 1: Take a rest

Sometimes, human being is a little weird. You won’t get the thing that you urgently need. So have a coffee, take a snap or even come back after a few days, you may found that you suddenly ‘remember’ your Windows password.

Method 2: Reset password with RESET DISK if you made before.

Windows XP and further versions also provide another method to recover forgotten password by using “Reset Disk”. If you created a Password Reset Disk in past, you can use that disk to reset the password. To know more about it, please visit following links:  
http://support.microsoft.com/kb/305478

Method 3: Reset password from another administrator account

If you cannot log on to Windows by using a particular user account, but you can log on to another account that has administrative credentials, follow these steps on how to do the trick:

1. Log on to Windows by using an administrator account that has a password that you remember. You may need to start WinXP in safe mode.

2. Click Start, and then click Run.

3. In the Open box, type “control userpasswords2?, and then click OK.

4. Click the user account that you forgot the password for, and then click Reset Password.

5. Type a new password in both the New password and the Confirm new password boxes, and then click OK.

Method 4: TRY command prompt about password reset trick

1. Log in with any valid account.

2. Bring up the command prompt.

Type: net user

You get a list of accounts

Type: net user Administrator \*

Type: net user (any account on that list) \*

3. It prompts for a password. Enter one, then enter it again when prompted to confirm.

Now, try to log on as ‘Administrator’ with your new password.

\* Please note that this might not work on a LIMITED account

.

Method 5: Make third party recovery tool yourself

There are a lot of tools and utilities that can be downloaded and used to recover, reset, retrieve or reveal existing password. These windows password recovery utilities, free or paid, are usually a Linux boot disk or CD that able to comes with NT file system (NTFS) drivers and software that will read the registry and rewrite the password hashes, or can brute force crack the password for any user account including the Administrators. The advantage is that there is no fear of leaking your password to outsiders, while the process requires physical access to the console and a floppy or CD drive, depending on which tool you choose. And it’s not easy, although it always work!

Below is the most famous recovery tool I found:

Windows Password Recovery Tool 3.0 – it is the most popular Windows password cracker . It is a very efficient implementation of windows any versions. It comes with a Graphical User Interface and runs on multiple platforms.

For more information:

http://www.windowspasswordsrecovery.com

Password Recovery Bundle –This is a utility to reset the password of any user that has a valid (local) account on your windows system. You do not need to know the old password to set a new one. It works offline, that is, you have to shutdown your computer and boot off a floppydisk or CD. It’ll detect and offer to unlock locked or disabled out user accounts. It is also an almost fully functional registry editor.

For more information:

http://www.recoverlostpassword.com

Windows Password Key 8.0 -It is considered as the best tool to reset local administrator and user passwords on any Windows system. It creates a password recovery CD/DVD, USB Flash Drive for home, business and enterprise. And most of all, it’s the most popular and safe solution for removing your Windows password until now.

For more information:

http://www.lostwindowspassword.com

Method 6: Make a Wish!

If it doesn’t work above, I hope that you have some hacker friends.

Go to our new site- shankee.com
