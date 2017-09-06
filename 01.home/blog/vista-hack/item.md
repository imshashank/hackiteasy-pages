---
# http://learn.getgrav.org/content/headers
title: Vista hack
slug: vista-hack
# menu: Vista hack
date: 08-05-2008
published: true
publish_date: 08-05-2008
# unpublish_date: 08-05-2008
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
        - vista
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [vista]
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

This worked for me…and i have an fully activated system..previous one just increases the time u cud use vista …but this activates it..But for this u need a Vista business OS

Install Windows Vista Business Edition (the KMS server is meant for corporate users so it can activate Windows Vista Business or Enterprise edition) by using default volume license (VL) product key for Vista Business retail edition  
(i.e. YFKBB-PQJJV-G996G-VWGXY-2V3X8),  
do not leave the field without using any serial key or skip input of volume license product key.  
When Windows installation and setup complete,  
setup Internet access.  
Right click on Command Prompt icon and select &#147;Run as Admin&#148; to launch the Command Prompt with Administrative privilege.  
In the Command Prompt window, type the following commands:  
cscript C:windowssystem32slmgr.vbs -skms kms.vbs.net.cn

You will see:

Microsoft (R) Windows Script Host Version 5.7  
Copyright (C) Microsoft Corporation. All rights reserved.

Key Management Service machine name set to kms.vbs.net.cn successfully

cscript C:windowssystem32slmgr.vbs -ato

The commands will activate Windows Vista Edition against kms.vbs.net.cn KMS server (setup by individual user which availability and reliability are not certain, another alternative KMS host is vbs.net.cn). It&#146;s a private KMS server for Volume License 2.0a activation but have been setup by individual and released to public Internet usage.

If there is error, disable the Windows Vista&#146;s firewall, or check out this page for possible resolution.  
To check the activation status, use the following command:  
cscript C:windowssystem32slmgr.vbs -dlv

If successful activation, you will see screen like this:

Microsoft (R) Windows Script Host Version 5.7  
Copyright (C) Microsoft Corporation. All rights reserved.

Software licensing service version: 6.0.6000.16386

Name: Windows(TM) Vista, Business edition  
Description: Windows Operating System – Vista, VOLUME\_KMSCLIENT channel  
Activation ID: xxxxxxxxxxxxxx  
Application ID: xxxxxxxxxxxx  
Extended PID: xxxxxxxxxxxxx  
Installation ID: xxxxxxxxxx  
Partial Product Key: 2V3X8  
License Status: Licensed

Volume activation expiration: 259193 minute(s) (179 day(s))

Key Management Service client information

Client Machine ID (CMID): xxxxxxxxxxx  
Registered KMS machine name: kms.vbs.net.cn:1688  
KMS machine extended PID: xxxxxxxxx  
Activation interval: 120 minutes  
Renewal interval: 10080 minutes

After the VLK is verified in KMS host, the Windows Vista client will be activated and can be used for 180 days, and requires re-activation once every 180 days. If after the activation expires, and the client doesn&#146;t activate again in 30 days grace period, Windows Vista will go into reduced functionality mode. Beside, Windows Vista Ultimate edition is unable to activated by this way.

Another problem is whether there is any open public KMS servers around on the Internet for activation, as using KMS server in the public domain is illegal. As most public KMS servers are setup by individual users who may need 25 clients to activate his or her own copy of Vista, so the availability of the public Internet KMS host is very uncertain. The fact is that many KMS servers have came and taken down such as peterpwq.vicp.net:1688, sito.kmip.net, binbin.xicp.net:1688, 220.133.135.222 and 59.39.163.239:1688 (1688 is the default port for KMS activation, and can be skipped). However, you can setup and create your own KMS server (if you don&#146;t have extra computer, VMWare or Virtual PC virtual machine can be used) and invite others to activate the Windows Vista together by using that KMS host, as KMS server requires at least 25 computers in order to start activating any of the Vista machines.

Go to our new site- shankee.com
