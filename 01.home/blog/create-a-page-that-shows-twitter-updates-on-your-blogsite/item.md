---
# http://learn.getgrav.org/content/headers
title: Create a Page that shows twitter updates on your blog/site
slug: create-a-page-that-shows-twitter-updates-on-your-blogsite
# menu: Create a Page that shows twitter updates on your blog/site
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
        - hack
        - internet
        - site
        - social
        - tech
        - twitter
        - wordpress
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hack,internet,site,social,tech,twitter,wordpress]
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

Twitter is the best way to publicize and advertise your blog or site and to stay in touch with followers. We already showed you how to display your latest tweet on your blog, in your sidebar for example. Another good way to introduce readers to your Twitter updates is to create a dedicated page for displaying your tweets, using the powerful “Page template” WordPress option.  
To perform this hack, you need to know how to create and use page templates. If you’re not familiar with this, [this article](http://www.wprecipes.com/how-to-create-and-use-wordpress-page-templates) will tell you all you need to know.  
Here’s the code to create a Twitter page template. Paste it in a new file, name the file something like *twitter-page.php*, for example, and then add it to your blog.

[view source](http://www.smashingmagazine.com/2009/03/04/15-useful-twitter-plugins-and-hacks-for-wordpress/#viewSource "view source")

[print](http://www.smashingmagazine.com/2009/03/04/15-useful-twitter-plugins-and-hacks-for-wordpress/#printSource "print")[?](http://www.smashingmagazine.com/2009/03/04/15-useful-twitter-plugins-and-hacks-for-wordpress/#about "?")



 

 `01` `` 

 `02`  

 `03` `/*` 

 `04` `Template Name: Twitter page` 

 `05` `*/` 

 `06`  

 `07` `get_header(); ` 

 `08`  

 `09` `include_once``(ABSPATH.WPINC.``'/rss.php'``);` 

 `10` `wp_rss(``'<a href="http://twitter.com/statuses/user_timeline/15985955.rss">http://twitter.com/statuses/user_timeline/15985955.rss</a>'``, 20); ` 

 `11`  

 `12` `get_sidebar();` 

 `13` `get_footer();` 

 `14` `?>` 

 

 

This code uses the *wp\_rss()* function from WordPress core, which is an RSS reader. In the first argument I pass my Twitter RSS feed, and in the second argument I determine the number of entries to display.

Go to our new site- shankee.com
