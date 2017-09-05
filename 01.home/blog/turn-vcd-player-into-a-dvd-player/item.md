---
# http://learn.getgrav.org/content/headers
title: Turn Vcd player into a DVD player..
slug: turn-vcd-player-into-a-dvd-player
# menu: Turn Vcd player into a DVD player..
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
        - convert VCD into DVD palyer
        - DVD
    author:
        - 'Shashank Agarwal'
    migration-status: review
    category: [convert VCD into DVD palyer,DVD]
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

Well i dont guarantee that it works…….  
But it might work..  
Their isn’t anythin wrong in tryin this if u are goin for a cange and think of throwing ur old VDD rom……….  
There are two types of CD-ROM drives we can mod:  
24x to 40x  
40x or higher  
Drives slower than 24x are too old to be modded.  
24x to 40x CD ROMs

Laser Head Adjustments:  
The track pitch of CDs is 1.6 microns, and the track pitch of DVDs is only 0.8 microns. The minimum length of track pits of CDs is 0.843mm, and the minimum length of track pits of DVDs is 0.293mm. That’s why DVD discs can store much more data in the size of a CD.  
Pinpointing this situation, we need to adjust the laser head so it can read discs with smaller track pitchs and shorter track pits. Open up the CD-ROM drive, do you see a lens on the rail? That’s the laser head. On the side of the laser head, there’s a screw you can adjust.This is the key of this mod.This screw can adjust the size of the laser beam that lands on the disc. Referring to the above, after adjusting, the laser beam should be less than 0.293mm, to suit the needs of DVD discs. So turn that screw 2-3 times. I got this number through trial and error. Mark with a pencil, in case you forget how many times you turned that screw.

Speed adjustments:  
DVD-ROM drives can play DVD movies smoothly at 4x speed. If we’re modding a 32x CD-ROM drive, the rotation speed is obviously too high, increasing heat, and shortening the life of the drive.  
So we need to decrease the speed of it.  
Most people know that power supplies can provide 5V (red wire) and 12V (yellow wire) electricity output for Molex connectors. Find the Molex connector you’ll plug into the modded CD-ROM drive, cut the yellow wire or insulate it with tape, so only 5V of electricity is transferred to the CD-ROM drive. The speed of the drive is now 32 \* 5/17 = 9.41x and can now fulfill our requirements.

40x or higher CD ROMs  
When 40x CD-ROM drives are released, most manufacturers are already producing DVD-ROM drives. To lower cost, they use the same core as DVD-ROM drives with DVD functions disabled. What we need to do here is to re-enable the DVD function.  
Open up the CD-ROM, behind the circuit board, look for a jumper that says DVD JUMP. Find a jumper to connect this jumper. Thin metal wire also works fine.  
OK, so the DVD function is unlocked, but we still need to decrease the speed. Use the instructions above on how to decrase the speed of the drive.  
  
Notes:  
Modded drives cannot be detected in POST, that means you cannot use it in DOS. But once you get into Windows, the drive works fine.  
Modded drives have no region code problems.  
Modded drives MIGHT NOT read DVD9 discs, that’s why I said you can watch most retail DVDs in the beginning.

Go to our new site- shankee.com
