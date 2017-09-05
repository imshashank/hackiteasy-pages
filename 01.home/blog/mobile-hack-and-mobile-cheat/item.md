---
# http://learn.getgrav.org/content/headers
title: Mobile hack and mobile cheat
slug: mobile-hack-and-mobile-cheat
# menu: Mobile hack and mobile cheat
date: 27-05-2008
published: true
publish_date: 27-05-2008
# unpublish_date: 27-05-2008
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
        - mobile
        - mobile phones
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [mobile,mobile phones]
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

**Nokia 31xx  
\_\_\_\_\_\_\_\_\_\_\_\_**

Firmware version  
\*#0000# or \*#3110#  
IMEI Code  
\*# 06 #  
Restores Factory Settings  
\*#7780#  
Warranty Codes  
\*#92702689# (= \*#war0anty#)

Just scroll down through the information. If entering the above code requires a  
further warranty code try entering the following:

6232 (OK) : Month and year of manufacture  
7332 (OK) : Last repair date  
7832 (OK) : Purchase date (if previously set)  
9268 (OK) : Serial number  
37832 (OK) : Set purchase date (this can only be done once)  
87267 (OK) : Confirm transfer

Nokia 5110  
\_\_\_\_\_\_\_\_\_\_\_\_\_

IMEI Number \*#06#  
For checking the IMEI (International Mobile Equipment Identity).  
———————————————————  
Security Code 12345  
Default security code is 12345. If you forgot your security code, there s so many program on the net which allowed you to know the security code likes Security ID Generator, Nokia IMEI Changer, etc.

update:  
Security ID Generator (SID.EXE) and IMEI Generator (NOKIAIMEI.EXE) doesn t works with Nokia 5110  
Resetting Security Code

If you accidentally lock the phone or forgot the security code, the best thing to do is check it with your local Nokia dealer. For advanced user, you can use WinTesla, PCLocals or LogoManager program to read the security code or resetting the code (You will need an FBUS/MBUS (or compatible) cable to do this.  
———————————————————  
Software Version \*#0000#  
For checking the phones software (SW) – called firmware revision information.  
e.q : Version V. 4.51 (26-03-98) will display  
V 04.51  
26-03-98  
NSE-1

first line:  
The Software Version (my guess is that this software has been used in previously Nokia-phones, what do you say?!).

second line:  
The Date of the SW release.

third line:  
NHE-8 has something to do with the type of phone you are dealing with. Is it GSM 900 (standard), GSM 1800 (DCS1800) or GSM 1900 (PCS1900)?  
Nokia 2110, 3110, 8110(i) are all NHE types. The only thing that vary is the code after NHE- (“8”).  
NHE = GSM 900, NHK =GSM 1800 – The number in the end = the model (2110i = 4 etc.)  
The 5110 and 6110 is called NSE-1 and NSE-3…this may be because it supports EFR (?)

update:  
Newest Software Version was V5.22 (xx-xx-99)  
V 05.22  
01-07-99  
NSE-1

If your software version is V4.00, upgrade your software version to latest version. V4.00 contains bugs that sometimes will show message,  
“SIM Card Not Ready” even the card is already inside the phone.  
———————————————————

Software Update  
The only thing to do (for you and me) is for us to go to the nearest Nokia dealer and make him do it for you. Just remember that it is supposed to be free (a receipt is required) so don t let him tell you anything else!  
———————————————————

SIM clock \*#746025625# [\*#sim0clock#]  
to check if the Sim-Clock can be Stopped. This option is depen on your service provider network. (Sim-clock-stop is a kind of standby mode which will save battery time)

update:  
This code doesn t work on phone with software version 4.59.  
———————————————————

Waranty Code \*#92702689# [\*#war0anty#]  
Menu:  
Displays Serial Number.  
Displays the Month and Year of Manufacture (0698)  
Displays (if there) the date where the phone was purchased (MMYY) you can here set the Purchasing Date  
(Warning: You can only do this once – so be careful what you write)  
Displays the date of the last repairment – if found (0000)  
The next screen has Transfer User Data? (the same option as the 8110)  
To exit turn the phone off and then back on.  
———————————————————

SP Lock The Service provider (SP) lock  
Is used to lock the cell phone to the SP s SIM card. Once the cell phone is locked to a specific operator, if one inserts a SIM card from a different operator the phone will refuse to accept it!  
The cell phone will however accept another SIM card from the same operator.

All Nokia phones (2110 and newer) have four different SIM locks which can be used to lock the phone for up to 4 different providers. But most phones with restriction only have one lock activated. ( lock 1)  
The main code used in Nokia phones is:

\#pw+(master code)+Y#

This code is able to check, activate or remove Sim card restriction (SP-lock).  
Use the \* key to get the p, + and w chars.  
Y has to be 1,2,3 or 4 – depending of what lock you what to deal with.

\#pw+1234567890+1# for Provider-Lock status  
\#pw+1234567890+2# for Network-Lock status  
\#pw+1234567890+3# for Provider(???)-Lock status  
\#pw+1234567890+4# for SimCard-Lock status

(master code) is a 10 digit code, based on the phones IMEI number.  
(I can NOT give you the master code SO DON T ASK ME FOR IT! )

Please click here to learn more about how to obtain mastercode and find out the lock status of your phone  
eq. To remove restriction on lock 1 type following code:

\#pw+(master code)+1#

If you just want to check your phone use 10 random numbers Eg. 1234567890 as the (master code)  
eq. To check if phone if restricted on lock 1 type the following code:

\#pw+1234567890+1#

Please NOTE that these codes could be used with care!  
A user told me that it s only possible to type in about 3 different codes on each lock! Then something bad will happen ..therefore be careful!  
———————————————————

How can I check what locks have my phone closed?

There is 2 methods:  
Use winlock to see the state of the locks, pressing Read Info.The Counter is the number of times that you have tried unlock your phone using an incorrect master code.  
You can check it entering an imaginary mastercode on your phone but, it s not recommended because if you try enter a code 5 times your phone will not work anymore. By example, if you press at your phone #pw+1234567890+2# (note that # , p , w and + characters must be selected from \* key) and your phone give you Code Error then your phone have lock 2 closed, if you get the message SIM Restriction Off your phone have lock 2 opened.  
Look the table above to see how can check all locks:

Lock number Description Sequence to Check  
1 Provider Lock #pw+1234567890+1#  
2 Network-Lock #pw+1234567890+2#  
3 Another Provider Lock #pw+1234567890+3#  
4 SIM Card Lock #pw+1234567890+4#  
———————————————————  
Unlock SP-Lock  
Here is a way to Unlock your phone which is Service Provider locked, without to know SPLock code. With a Nokia 16xx/21xx/31xx/51xx/81xx that are SIMlocked to one privider you can bypass the SP lock like this:

First of all, PIN CODE MUST BE ON, then press:

C

C and hold until it clears display  
\* and hold until start to blink  
\* and hold until start to blink  
04\*\*\*your pin>#

Each time you turn your phone OFF it resets the lock, so this need to be done each time you ll turn your phone ON

The phone now says: PIN CODE CHANGED (or ACCEPTED)  
and the SIM card is accepted until you restart the phone again.

NOTE: On vesion 5.04 Nokia has removed this option !

update:  
There s another Nokia service provider lock generator for DOS (somehere on the net) called 5161un.zip (for Nokia 51xx-61xx models) This program uses the #pw+(master code)+1# code to unlock the phone. With this software you need to have a access to the eeprom.. ![Sad](http://foolzparadize.org/images/smiles/icon_sad.gif "Sad")  
———————————————————

Bypass the SP-lock

With a Nokia 16xx/21xx/31xx/51xx/81xx that are SIM locked to one privider you can bypass the SP lock like this:

Insert sim card of diferent provider.

Turn on the phone and press the UP VOLUME key for 3 sec. then release it and the phone says PIN CODE ?

Press the “C” key.

Then Press \* and wait until it desapear and apear again, then press \* one more time and 04\*PIN\*PIN\*PIN#

The phone now says: PIN CODE CHANGED (or ACCEPTED)  
and the SIM card is accepted until you restart the phone again.

update:  
On version 5.04 Nokia has removed this option !  
———————————————————

How to open lock 1 and 4?  
You will need Winlock software and MBUS cable to do this. Winlock is a Nokia service program that you can use to open lock 1 and 4, really you are closing locks when you do that, but when you write ????? at MCC+MNC and MSIN text box, the phone don t understand it and consider that it s open.

That trick only works for lock 1 and 4, but not for lock 2 and 3. If you did not know your lock type, please read our miscellaneous tips page first. or read at above section in this page.

Install winlock 1.10  
Connect your MBUS nokia data cable  
Run Winlock  
Push Read Phone, if you have Lock 2 or Lock 3 closed you can not open your phone, but you can try change Lock 2.  
Select State Close in Lock 1 and Lock 4, fill out MCC+MNC and MSIN text boxes with ??????? and Push Close Locks.  
Now you can use any operator card in your phone. If you get any error when you do that do the following steps:  
Select State Automatic in Lock 1 and Lock 4 and change type to User in Lock 1 and Lock 4, fill out MCC+MNC and MSIN text boxes with ?????????? and Push Close Locks.  
Select State Automatic in Lock 1 and Lock 4 and change type to Factory in Lock 1 and Lock 4, fill out MCC+MNC and MSIN text boxes with ?????????? and Push Close Locks.  
If you continue getting errors you must turn off your phone and reset computer and try again.  
———————————————————

How to open lock 2?

When operators companies close lock2 you can only use the contract or prepaid card for this operator, but you can use another operator company prepaid card if you know what GID1 must write.

Install Winlock  
Run Winlock  
Configure Winlock. Select menu Winlock->Defaults and change GID byte count to 2.  
Push Read Phone, and write down GID1 info that appear in lock 2.  
Insert the prepaid card from a different operator company.  
We must find out a the GID1 info adecuate for our new prepaid or contract card, take a look at our GID1 list and check if your operator and SIM card type is included, if not try to get a phone that have lock 2 closed and have the SIM card type that you want to use in your phone, and read GID1 info with winlock. You can try to write the most used GID1 codes like 0000,10FF,01FF, or FFFF, etc.  
Change Lock 2 Type from User To Factory or from Factory to User.  
Push Close Locks  
Your phone will be reset every time you push Close Locks, if your card is not acepted the GID1 is not correct, repeat from step 4 until you find the correct GID1.  
If you get error you must turn off your phone and reset computer and try again.  
If you want your phone accept your original prepaid card write in GID1 the code you read at step 2 and close locks.  
Exist a GID1 list?

In addition to the official way to open locks that Nokia service centers use with TDB4 or TDF-4(for WinTesla) security boxes, there is two secrets methods:

Opening the phone and adding a chip inside phone motherboard. But you will loose any warranty of your phone.  
Using a special software with a MBUS Nokia cable. I don t have this software. Please don t bother me asking me about that. The only thing i know about that is that a friend is removing lock 2 using a special software. He don t make this for money, only for fun.  
——————————————————–

Main Code #pw+(master code)+Y#  
This code is able to check, activate or remove Sim card restriction (SP-lock).

Use the \* key to get the p, + and w chars.  
Y has to be 1,2,3 or 4 – depending of what lock you what to deal with.

\#pw+1234567890+1# for Provider-Lock status  
\#pw+1234567890+2# for Network-Lock status  
\#pw+1234567890+3# for Provider(???)-Lock status  
\#pw+1234567890+4# for SimCard-Lock status

(master code) is a 10 digit code, based on the phones IMEI number.

update:  
I get report that told me the code didn t works for Optimus Card  
———————————————————  
Enhanced Full Rate Codec (EFR)  
Enhanced Full Rate will give you much better sound quality when you enable it. The new Enhanced Full Rate CODEC adopted by GSM uses the ASELP (AlgebraicCode Excitation Linear Prediction) compression technology. This technology allows for much great voice quality in the same number of bits as the older Full Rate CODEC. The older technology was called LPC-RPE (Linear Prediction Coding with Regular Pulse Excitation). Both operate at 13 kilobits.(but you take up more space on the network, so they can charge you more)

\*3370# and EFR will be activated after a reboot of the phone ( consumes more power )

\#3370#  
and EFR will be switched off after a reboot of the phone.  
———————————————————

Half Rate Codec (HR)  
Half Rate will give you bad sound quality, which gives the service provider the opportunity to have more calls on the network; and you might get a lower charge from them. (Will give you 30% longer talk-time)  
\*4720# Half Rate coded will be activated after a reboot of the phone ( better standby time )

\#4720# Half Rate coded will be de-activated after a reboot of the phone  
———————————————————

Unblocking Code  
Unblock PIN1 : \*\*05\*PUK\*newPIN1\*newPIN1#@  
UnBlock PIN2 : \*\*052\*PUK2\*newPIN2\*newPIN2#@  
———————————————————

Hiding your phone number  
Dial 141 then the number you want to call eg. 141#######  
This should stop your number been sent to the caller. (\*)  
(\*) This only works on UK phones, if anybody has tried this and works, please let me know.  
———————————————————

Unlocking PIN2 for software version  
V 05.07  
20.11.98  
NSE-1

If your SimCard is locked by your SP, you can check it and if it is, you will get the “wrong code” message on the display (for use 1234567890)  
If your SimCard is locked by your SP, you can t unlock PIN2 !  
———————————————————

Blocking phone number at Cantel AT&T

If you have one of those cantel at&t phones if you press #0000# you can block your number  
at no extra charge.  
———————————————————

New Menu on Emergency Calls \*3001#12345#

Brings a new menu that gives you access to the emergency calls ( 911 Etc. ). It will give you FREE calls! (only the ones you put in the emergency!! )

This option will depend on your GSM operator  
———————————————————

Your number in your display  
Goto menu 3-7 Call cost settings.  
Turn ON the Call costs limit 3-7-1. PIN2 code Required.  
Put in the limit with the phone number.  
eg. my phone # is 019 2184697  
Enter the limit as 2184697  
Goto menu 3-7-2 Show costs in. PIN2 code Required.  
Select Currency.  
Enter Unit price : 1  
Enter Currency name as 019 (per my phone # eg. above)  
Now the phone number 019 2184697 will remains on the 4th row of the display.  
Secondly, if you press the # key, it prompt which line to be used; Line 1 or 2.  
———————————————————  
Free Call Tip

The tips needs Net Monitor enabled. Be aware that the trick will remove Netmonitor in some sw versions like v4.73 and v5.04.  
Launch the Net Monitor in your Nokia 51xx / 61xx  
Execute the test number 497  
Free calling for about 90 sec should now have been activated.  
———————————————————

Nokia 5110 PIN-Out

Pin-Outs: Bottom view, keyboard up, counting from the left

V V 1 2 3 4 5 6 V  
(o) | | [= = = = = =] | |  
7 8 9 10 11 12

1 – VIN CHARGER INPUT VOLTAGE 8.4V 0.8A  
2 – CHRG CTRL CHARGER CONTROL PWM 32Khz  
3 – XMIC MIC INPUT 60mV – 1V  
4 – SGND SIGNAL GROUND  
5 – XEAR EAR OUTPUT 80mV – 1V  
6 – MBUS 9600 B/S  
7 – FBUS\_RX 9.6 – 230.4 KB/S  
8 – FBUS\_TX 9.6 – 230.4 KB/S  
9 – L\_GND CHARGER / LOGIC GND

Nokia 61xx  
\_\_\_\_\_\_\_\_\_\_

Firmware version  
\*#0000# or \*#61×0#  
IMEI Code  
\* # 06 #  
Warranty Codes  
\*#92702689# (= \*#war0anty#)

Just scroll down through the information. If entering the above code requires a  
further warranty code try entering the following:

6232 (OK) : Month and year of manufacture  
7332 (OK) : Last repair date  
7832 (OK) : Purchase date (if previously set)  
9268 (OK) : Serial number  
37832 (OK) : Set purchase date (this can only be done once)  
87267 (OK) : Confirm transfer

Enhanced Full Rate (EFR) and Half Rate Mode (HFR)

\*3370# to activate Enhanced Full Rate – Makes calls sound better, but  
decreases the battery life by about 5%.(I recommend this one)  
\#3370# to deactivate Enhanced Full Rate  
\*4720# to activate Half Rate Mode – Drops call quality, but increases battery  
life by about 30%.  
\#4720# to deactivate Half Rate Mode

Nokia 81xx  
\_\_\_\_\_\_\_\_\_\_\_\_\_

Show IMEI code  
\* # 06 #  
Software Version  
\* # 8110 #  
This code shows you software version, date of manufacture and hardware number of your phone.

Warranty Codes  
\*#92702689# (= \*#war0anty#)

Just scroll down through the information. If entering the above code requires a  
further warranty code try entering the following:

6232 (OK) : Month and year of manufacture  
7332 (OK) : Last repair date  
7832 (OK) : Purchase date (if previously set)  
9268 (OK) : Serial number  
37832 (OK) : Set purchase date (this can only be done once)  
87267 (OK) : Confirm transfer

Sim Clock information

To check if the Sim-Clock can be stopped type: \*#746025625# (= \*#sim0clock#)

Nokia 8810  
\_\_\_\_\_\_\_\_\_\_\_\_  
Firmware version  
\*#0000# or \*#8810#  
IMEI Code  
\* # 06 #  
Warranty Codes  
\*#92702689# (= \*#war0anty#)

Just scroll down through the information. If entering the above code requires a  
further warranty code try entering the following:

6232 (OK) : Month and year of manufacture  
7332 (OK) : Last repair date  
7832 (OK) : Purchase date (if previously set)  
9268 (OK) : Serial number  
37832 (OK) : Set purchase date (this can only be done once)  
87267 (OK) : Confirm transfer

Enhanced Full Rate (EFR) and Half Rate Mode (HFR)

\*3370# to activate Enhanced Full Rate – Makes calls sound better, but  
decreases the battery life by about 5%.(I recommend this one)  
\#3370# to deactivate Enhanced Full Rate  
\*4720# to activate Half Rate Mode – Drops call quality, but increases battery  
life by about 30%.  
\#4720# to deactivate Half Rate Mode

Go to our new site- shankee.com
