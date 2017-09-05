---
# http://learn.getgrav.org/content/headers
title: Easy trick to convert FAT partitions to  NTFS
slug: easy-trick-to-convert-fat-partitions-to-ntfs
# menu: Easy trick to convert FAT partitions to  NTFS
date: 05-06-2009
published: true
publish_date: 05-06-2009
# unpublish_date: 05-06-2009
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
        - disk
        - hack
        - hardware
        - tech
        - XP
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [disk,hack,hardware,tech,XP]
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

If you are still stuck with FAT or FAT32 file system then its time to move on. Here is an easy trick lets you convert the FAT partitions to NTFS very easily.

Click Start, click Programs, and then click Command Prompt. In Windows XP, click Start, click Run, type cmd and then click OK.

At the command prompt, type CONVERT [driveletter]: /FS:NTFS. Convert.exe will attempt to convert the partition to NTFS.

NOTE:=  
Although the chance of corruption or data loss during the conversion from FAT to NTFS is minimal, it is best to perform a full backup of the data on the drive that it is to be converted prior to executing the convert command.

Go to our new site- shankee.com
