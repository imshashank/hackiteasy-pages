---
# http://learn.getgrav.org/content/headers
title: Display your latest tweet without a plug-in
slug: display-your-latest-tweet-without-a-plug-in
# menu: Display your latest tweet without a plug-in
date: 29-07-2010
published: true
publish_date: 29-07-2010
# unpublish_date: 29-07-2010
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
        - blogger
        - internet
        - plug-in
        - social
        - twitter
        - wordpress
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [blogger,internet,plug-in,social,twitter,wordpress]
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

#### 

[![8 in 15 Useful Twitter Hacks and Plug-Ins For WordPress](http://media.smashingmagazine.com/cdn_smash/images/twitter-tips-wordpress/8.png)](http://media.smashingmagazine.com/cdn_smash/images/twitter-tips-wordpress/8.png)If people like your blog, they would probably also enjoy your tweets. Displaying your latest tweets on your WordPress blog is a good way to gain new subscribers. A plug-in can do that, but for such a simple task, I prefer a hack. This one grabs your latest tweet and displays it on your blog.  
This ready-to-use code can be pasted anywhere in your theme files. Just don’t forget to change the value of the $username on line 4. The $prefix and $suffix variable can be used to insert a title, and the div element can be used for further CSS styling.

 
    // Your twitter username.<br></br>$username = "TwitterUsername";<br></br><br></br>// Prefix - some text you want displayed before your latest tweet.<br></br>// (HTML is OK, but be sure to escape quotes with backslashes: for example href="link.html")<br></br>$prefix = "<h2>My last Tweet</h2>";<br></br><br></br>// Suffix - some text you want display after your latest tweet. (Same rules as the prefix.)<br></br>$suffix = "";<br></br><br></br>$feed = "http://search.twitter.com/search.atom?q=from:" . $username . "&rpp=1";<br></br><br></br>function parse_feed($feed) {<br></br>    $stepOne = explode("<content type=""html"">", $feed);<br></br>    $stepTwo = explode("</content>", $stepOne[1]);<br></br>    $tweet = $stepTwo[0];<br></br>    $tweet = str_replace("<", "<", $tweet);<br></br>    $tweet = str_replace(">", ">", $tweet);<br></br>    return $tweet;<br></br>}<br></br><br></br>$twitterFeed = file_get_contents($feed);<br></br>echo stripslashes($prefix) . parse_feed($twitterFeed) . stripslashes($suffix);<br></br>?>

Save the file, and your latest tweet is displayed on your blog. Nice, huh?

Go to our new site- shankee.com
