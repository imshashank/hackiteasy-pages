---
# http://learn.getgrav.org/content/headers
title: SAVE DOS OUTPUT IN A FILE
slug: save-dos-output-in-a-file
# menu: SAVE DOS OUTPUT IN A FILE
date: 12-06-2009
published: true
publish_date: 12-06-2009
# unpublish_date: 12-06-2009
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
        - computers tricks
        - dos
        - hacking
        - tech
        - windows
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [computers tricks,dos,hacking,tech,windows]
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

This is a small trick that many Dos might already know. The trick just shows you how to run a Dos command and instead of displaying the outputs on the screen, it saves the outputs into a file.

This trick is very helpful when you want to save the result of a dos command to a file to email it or read/print it later. For example, you can print out your network configuration data and email it to a technical support.

Here’s how

simply put a “>” and the destination file at the end of the dos command. Examples:

This command outputs the IP configurations to the file “ipdata.txt” in “C” drive:  
ipconfig /all > C:ipdata.txt

This command outputs the “Path” configurations to the file “pathdata.txt” in the floppy drive “A“:  
path > A:pathdata.txt

This command outputs help text of the command “copy” to the file “copyhelp.txt” in “C” drive:  
copy /? > C:copyhelp.txt

Go to our new site- shankee.com
