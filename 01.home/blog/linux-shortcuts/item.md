---
# http://learn.getgrav.org/content/headers
title: Linux Shortcuts..
slug: linux-shortcuts
# menu: Linux Shortcuts..
date: 28-08-2008
published: true
publish_date: 28-08-2008
# unpublish_date: 28-08-2008
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
        - linux
        - software
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [linux,software]
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

## Here is a list of Linux Shortcuts..most of these can be easily used o WIndows machine as well

## Virtual terminals >

`Ctrl + Alt + F1`  
Switch to the first virtual terminal. In Linux, you can have several virtual terminals at the same time. The default is 6.

`Ctrl + Alt + Fn`  
Switch to the nth virtual terminal. Because the number of virtual terminals is 6 by default, n = 1…6.

`tty`  
Typing the `tty` command tells you what virtual terminal you’re currently working in.

`Ctrl + Alt + F7`  
Switch to the GUI. If you have X Window System running, it runs in the seventh virtual terminal by default. If X isn’t running, this terminal is empty.

 

 

## X Window System >

`Ctrl + Alt + +`  
Switch to the next resolution in the X Window System. This works if you’ve configured more than one resolution for your X server. Note that you must use the + in your numpad.

`Ctrl + Alt + -`  
 Switch to the previous X resolution. Use the – in your numpad.

`MiddleMouseButton`  
Paste the highlighted text. You can highlight the text with your left mouse button (or with some other highlighting method, depending on the application you’re using), and then press the middle mouse button to paste. This is the traditional way of copying and pasting in the X Window System, but it may not work in some X applications.

If you have a two-button mouse, pressing both of the buttons at the same time has the same effect as pressing the middle one. If it doesn’t, you must enable 3-mouse-button emulation.

This works also in text terminals if you enable the `gpm` service.

`Ctrl + Alt + Backspace`  
Kill the X server. Use this if X crashes and you can’t exit it normally. If you’ve configured your X Window System to start automatically at bootup, this restarts the server and throws you back to the graphical login screen.

 

 

## Command line – input >

`Home or Ctrl + a`  
 Move the cursor to the beginning of the current line.

`End or Ctrl + e`  
 Move the cursor to the end of the current line.

`Alt + b`  
Move the cursor to the beginning of the current or previous word. Note that while this works in virtual terminals, it may not work in all graphical terminal emulators, because many graphical applications already use this as a menu shortcut by default.

`Alt + f`  
Move the cursor to the end of the next word. Again, like with all shortcuts that use Alt as the modifier, this may not work in all graphical terminal emulators.

`Tab`  
 Autocomplete commands and file names. Type the first letter(s) of a command, directory or file name, press `Tab` and the rest is completed automatically! If there are more commands starting with the same letters, the shell completes as much as it can and beeps. If you then press `Tab` again, it shows you all the alternatives.

This shortcut is really helpful and saves a lot of typing! It even works at the lilo prompt and in some X applications.

`Ctrl + u`  
 Erase the current line.

`Ctrl + k`  
 Delete the line from the position of the cursor to the end of the line.

`Ctrl + w`  
 Delete the word before the cursor.

 

 

## Command line – output >

`Shift + PageUp`  
 Scroll terminal output up.

`Shift + PageDown`  
 Scroll terminal output down.

`clear`  
 The `clear` command clears all previously executed commands and their output from the current terminal.

`Ctrl + l`  
 Does exactly the same as typing the `clear` command.

`reset`  
 If you mess up your terminal, use the `reset` command. For example, if you try to cat a binary file, the terminal starts showing weird characters. Note that you may not be able to see the command when you’re typing it.

 

 

## Command line – history >

`history`  
 When you type the `history` command, you’ll see a list of the commands you executed previously.

`ArrowUp or Ctrl + p`  
 Scroll up in the history and edit the previously executed commands. To execute them, press `Enter` like you normally do.

`ArrowDown or Ctrl + n`  
 Scroll down in the history and edit the next commands.

`Ctrl + r`  
Find the last command that contained the letters you’re typing. For example, if you want to find out the last action you did to a file called “`file42.txt`“, you’ll press Ctrl + r and start typing the file name. Or, if you want to find out the last parameters you gave to the “`cp`” command, you’ll press Ctrl + r and type in “`cp`“.

 

 

## Command line – misc >

`Ctrl + c`  
 Kill the current process.

`Ctrl + z`  
Send the current process to background. This is useful if you have a program running, and you need the terminal for awhile but don’t want to exit the program completely. Then just send it to background with `Ctrl+z`, do whatever you want, and type the command `fg` to get the process back.

`Ctrl + d`  
Log out from the current terminal. If you use this in a terminal emulator under X, this usually shuts down the terminal emulator after logging you out.

`Ctrl + Alt + Del`  
 Reboot the system. You can change this behavior by editing `/etc/inittab` if you want the system to shut down instead of rebooting.

 

 

Go to our new site- shankee.com
