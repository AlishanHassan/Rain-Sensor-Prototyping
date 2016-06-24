# Journal
***

### June 7, 2016
1. Decided to log stuff everyday, mostly as a way to keep notes. 
2. Ran the Photon overnight. Stability is questionable since it seems to lose the cloud connection from time to time. It did reconnect automatically, but we need to make sure any problems can be solved remotely, to reduce maintenance. 
3. SPI program written yesterday resulted in strange behavior that prevented it from connecting to the cloud. Hitting reset or power cycling reconnected it, but it only lasted for a few seconds before losing the connection. Had to go into safe mode and load older version of program to fix it. SPI works on an Arduino, though. 
4. 17:34 EDT: Finally got SPI working on the Photon. Hooked it up to the scope and compared it with the Arduino, found out it was only the SI pin on the MCP41100 that had issues. It was merely supposed to be hooked up to D2 (MOSI), not D3 (MISO). -_- With one pin on the wiper and the other on PB0, I'm able to vary the resistance from ~600 Ω to just over 36 kΩ.  
5. Have not seen any stability issues all day. Perhaps the power supply that was used last night isn't perfect (I found it in a box, after all). 

***

### June 8, 2016
1. Need to find a way to hook up the piezoelectric in a way that doesn't damage it. Durability isn't its strong suit. (I had to solder a new wire on the old one a few days back, maybe thicker wires are a meaningful upgrade?).  
2. Potential Milestone: Can we indicate that rain has begun falling 10 seconds after it starts?
3. Bought a few parts. Two PVC pipes, one 3/4", one 1" at 5 feet long each. Carriage bolt as a potential cap  (by cutting off the head of the bolt), PVC cement, and a sprinkler.
4. The 3/4" pipe is basically perfect for the piezo element, which slides right in. Just needs a little bit of adhesive on the edges. The 1" tube could possibly be used for added insulation around the 3/4" tube (needs a bit of sanding). 
5. Carriage bolt's acoustics are questionable. Need to look into machining a custom aluminum cap ASAP. 
6. Oscillating sprinkler was cheap and, per reviews, breaks easily. That said, we don't need oscaillation, so this should be fine. 

***

### June 9, 2016
1. Cut the PVC tubing down to size. Will lengthen the wires on the piezo element tomorrow when I bring my heat gun. 
2. Went to Lacy, but nobody was there. Need to get a few tips on how to machine stainless steel. 
3. Considering using 316 Stainless Steel (if that's not available, 440 Stainless Steel) for the cap. Decent corrosion resistance, but cutting it might be annoying. 
4. Look into cutting a Stainless Steel ball in half to make a dome. See [here](https://www.onlinemetals.com/merchant.cfm?id=1425&step=2&top_cat=1) for a bag of them. Need to get a 1" dimater to fit over the 3/4" PVC tube. 
5. Vaisala used stainless steel for the cap, the master's thesis used PVC for the final revision, noting better acoustic capabilities than aluminum. So look into PVC as well (if that's easier to find). 

***

### June 10, 2016
1. Brought the sheetmetal from the first prototype. It's developing rust, so it's probbably not the one we want to keep, but it's something to work with while I figure out how to design the final cap. 
2. Talked to Lewis about how to machine a dome. Would have to use a lathe with the cutting tool. Not ideal, but it can work. 
3. He can provide the material (considering it isn't much). He has aluminum, nylon, acrylic, and brass stock (all solid tubes). Stainless steel can be used, but it's pretty hard to machine.
4. Impacts on the side of PVC tube aren't too bad (no amplifier). 
5. A single tap actually produces a reasonable signal. Sampling rate is more than enough. 
6. Need to waterproof the electronics. One of my project boxes is the perfect size for the breadboard. Just need to dremel two holes, one for the USB cable, the other for the sensor wires. (Ah, "dremel", another proper noun used regularly as a verb...)
7. Taking the sprinkler home to see how it fares as a rain machine. Don't think it's wise to get the sensor wet until it's all sealed off. 
8. Also need to find an adhesive to smoothly attached the piezo element to the metal cap. PVC cement and hot glue are probably a no go. 

***

### June 21, 2016
1. Finally back -_-
2. Superglued the piezo element to the metal cap and the metal cap to the PVC tube.
3. Seems to work fine, and the data picked up is reasonable (just need to play around with amplification settings, current data has no amplificiation). 
4. I tried to use a thin layer of glue, but we'll have to make sure there's some consistency in this step when we manufacture a lot of them. 
5. New set of parts should arrive tomorrow. 
6. Also tested the sprinkler a few days back. Seems to hit 12 feet. Goal is 15 feet, so placing it on a 3 foot high table, or something, should do the job. 

***

### June 22, 2016
1. Cleaned up the breadboard, so now it's much nicer and can be stashed in the project box. 
![Cleaned Breadboard](Photos/breadboard_cleaned.jpg?raw=true "Cleaned Breadboard")
2. Need to dremel the project box for the USB port, holes for piezo wiring and tipping bucket wiring and possibly an LED hole.
3. So, this is odd, the new breadboard, without the amp hooked up, doesn't seem to sit near 0 when there's no tapping. It's around 60-70, which is what I used to get when the amp was hooked up. The only change I made was reducing the delay from 5ms to 0ms. Let's see if reverting that makes a difference. 
4. Yeah, dropping it to a 5ms delay brought the numbers back down. Without a delay, the base values are much larger, but it does dip to zero after a tap, before returning back to 60-70 stable. Hmm, odd. It doesn't seem like a zero delay is necessary anyway, since it isn't polling any more useful data compared to 5ms. So, I'll be sticking to 5ms. 
5. I brought a metal lid to attach the PVC tube to, but I don't know if that's the best idea because it's lacking in sound insultation. Need to find some plastic or wood.

***

### June 23, 2016
1. Next revision needs to ditch the AD623 in favor of some op-amp. I don't think it's fast enough. I tried a second AD623, and the results were the same. Only need very mild amplifification as it is, and it should only be necessary for drizzles. 
2. The acoustics of that metal lid aren't perfect, but without the amp I'm getting a reading of, at most ~70, from the piezo element. So, that shouldn't be a big deal, but definitely use something better for the next revision. 
3. Went ahead and hot glued the PVC tube to the lid. Took it outside, since it's raining, to see how it did. Seems perfectly fine. Well sealed and stable. 

![Prototype just after the rain](Photos/prototype_after_rain.jpg?raw=true "Prototype just after the rain")
4. Finished putting the electronics in a project box. Slightly tight on the USB port, but does the job. 
![Black Box](Photos/black_box.jpg?raw=true "Black Box")
5. AccuWeather said it was about to rain - it didn't. Spent some time outside waiting for the rain to begin, but gave up. Rain is in the forecast tomorrow, though. 
![Waiting for rain](Photos/waiting_for_rain.jpg?raw=true "Waiting for rain")
