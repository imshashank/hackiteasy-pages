---
# http://learn.getgrav.org/content/headers
title: Some cool tricks i just discovered
slug: some-cool-tricks-i-just-discovered
# menu: Some cool tricks i just discovered
date: 11-06-2009
published: true
publish_date: 11-06-2009
# unpublish_date: 11-06-2009
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
        - hack
        - hacking
        - IP
        - tech
        - windows
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [computers tricks,hack,hacking,IP,tech,windows]
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

### This is a complimation of computer tricks, mainly security and privacy related.

### Getting Ip’s:–

To see the ip all computers you are connected to (web servers, people attempting to \*\*\*\* into your computer). Go to dos (start>run>type command) and run the netstat command. Type netstat /? for details.

### Type netstat -r at the command prompt to see the ip of all computers you are connected to

In MSN (and other programs) when you are chatting to someone everything you type goes through the MSN servers first (they act as a proxy) so you see their ip rather than who you are chatting to. You can get round this by sending them a file as MSN doesn’t send file through its proxy.When you type the netstat -r (or -a for a different view) the ip’s are under the foreign address table. The ports are seperated by a : . Different programs use different ports, so you can work out which ip’s are from which program.

### Connecting to other computers and what ports are:–

Servers send information. Clients retrieve. Simple. Windows comes with a built in program to connect to other computers called telnet. To start Windows telnet Start menu> Run> type Telnet. Click connect> remote system Ports are doors into computers. Hosts are computer names (ip number or a name that is translated into the ip automatically) Different programs open different ports, but they always open the same ports so other computers know which port to connect to. You can get a port list listing all the different ports, but a basic one is: 11 :- Sends info on the computer 21 :- FTP (File transfer program) 23 :- Telnet (Login to the computers command line) 25 :- Smtp (Sends mail) 80 :- Http (Web pages) There are thousands of different programs using different ports. You can get programs called portscanners which check a computer for all ports up to a certain number, looking for ways in. You can portscan a computer looking for ways-in. Anyway, back to telnet. Type www.yahoo.com as the host and port as 80 the click connect. If nothing happens, you’re in. Wow. You are connected to Yahoo’s server. You can now type http commands (you are connected to an http server, so it supports http commands). Ie. on an ftp server you can type open and it will do something. On an http server it will just wonder what the hell you are on about. Type get / http/1.0 then press enter twice to get the file on the server at / (try /index.html) etc.)

### Making undeletable, unreadable folders

Tested on Windows 95/98 By holding down alt, then typing numbers on the number pad (right of the keyboard) you can create special characters. If you hold down alt, then press 1, then let go, you got the ascii character 1. You try some randomn numbers. This goes all the way up to 255. Open a dos prompt, and type md (alt+1+9+4)someword. md is the dos command to make a directoy, now try and open the directory in Windows, you can’t. To open it, type ren (alt+1+9+4)someword someword (ren is the dos command to rename)

### Proxies

Proxies are computers that you connect through, hiding your computer. Most aren’t anonymous, they give away your ip. Some are. Good anonymous proxies: mail.uraltelecom.ru:8080 and 194.247.87.4:8080.Different programs require different ways of using proxies. To do it in internet explorer 5 go to tools, internet options, connections, settings. In the above proxies they are in the format host:port

### Password files

If you lock yourself out of Windows stuff, all passwords are stored in files called \*.pwl in C:windows. In Unix, passwords are normally stored at etc/passwd. This can be viewed using the cat command (prints a file to screen): cat etc/passwd. Make sure you’re passwords are shadowed (not actually in etc/passwd). Also make sure they aren’t in a file called shadow, especically not in a file called etc/shadow.Unix passwords are encrypted far better than Windows one’s (to be fair, Windows 95 isn’t designed for users), but can still be cracked through a program called jon.

Go to our new site- shankee.com
