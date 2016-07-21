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

***

### June 24, 2016
1. Doesn't look like it's going to rain. There's a hose outside Rice and I need to figure out how to get permission to use it. In the mean time, I'll take the whole setup home this weekend and try to test it with the sprinkler. 
2. Doing a little materials research today for the improved cap. The flat cap is definitely not ideal just based on the quick rain test I did yesterday. Brass seems like it could be OK. I don't have the exact specs of what materials we have to work with, though, which doesn't help. Depending on the grade of nylon we have available, we might be able to get similar performance to the PVC used in the paper. But, again, don't have exact specs. 
3. Maybe what I really need to do is get elasticity data for these materials? 
4. Took a heat gun to the PVC to try and shape it into a cap. Too much smoke - gave up...for now. 
5. FYI: Brass E = 102 - 105 GPa | Nylon-6 E = 2 - 4 GPa | Aluminum E = 69 GPa | Acrylic E = 3.2 GPa 

***

### June 25, 2016
1. Uh oh, looks like we've got some oxidation. 
![Cap Oxidation](Photos/cap_oxidation.jpg?raw=true "Cap Oxidation")
2. This was to be expected, but I was hoping the WD-40 would have helped. You normally apply a thin layer to your tools to prevent oxidation, but I suppose it's not suitable for this application. Guess this means I need to expedite getting the next cap built. 
3. For the record, according to the label this is WELD STL - SHT (22GA).  So, just a 22 gauge sheet of mild weld steel. 
4. OK, taking the whole system home to test it with a sprinkler. Fingers crossed...

***

### June 26, 2016
1. Hooked up the sprinkler and let it rain (also mistyped "sprinkler" in the git commit). 
2. Data, on first inspection, looks semi-promising. I ran the gauge side by side with the tipping bucket. 
3. The main issue is that the oscillating sprinkler is difficult to work it. I'm going to have to break the gears to prevent it from oscillating. 

***

### June 27, 2016
1. It rained today, yay!
2. Hooked up both the piezo guage and the tipping bucket, left them outside with the laptop in the car (to avoid getting it wet) and recorded data for over 25 minutes. 
![June 27 Rain Test](Photos/jun27_rain_test.jpg?raw=true "June 27 Rain Test")
3. The rain was quite light. In fact, in those 25 minutes, the tipping bucket didn't even tip once. I tried to store the amount of water that it collected, but it tipped right when I opened the bucket. I salvaged what I could, first transferring it to a frisbee (the closest thing to a container I had) and then to a water bottle with a funnel. Sadly, some water was lost, some water was introduced, so this is not a reliable measure. We can, however, say we were just barely shy of one tip. 
4. The other issue: with the spinkler's heavy "rain", the readings were relatively usable. Unfortunately, with this light rain (it's considerably heavier than a drizzle), the signal was quite weak. These readings are all done without an amplifier, and this shows that we need an amplifier. Back to the drawing board there.
5. I think I'm going to run to Radio Shack tomorrow and grab the best op-amps they have and see if they fair better. 
6. It does not seem to be affected much by other sounds, considering how weak the signal is without the amp. 
7. Project box is fairing well, no malfunctions with the electronics so far. Keeping the laptop in the car is a great idea. 
8. Hot glue failed after yesterday's sprinkler test, had to tape it down temporarily. Final revision, obviously, will use more permanant adhesive. I just used hot glue because I knew I could take it apart if need be. It was, nevertheless, weaker than expected. 
9. Need to get a graduated cylinder to get more precise rainfall measurements. The tipping bucket is still useful, but the low resolution is going to be problematic. Hopefully I can find one locally by tomorrow. 

***

### June 28, 2016
1. Both Radio Shacks in Charlottesville have closed. :( It really is the end of an era. 
2. The TR-525USW (which is the tipping bucket we're using) measures .01" (8.23 mL) per tip. So we had less than .01" of rain in those 25 minutes?
3. You see this? It's raining in this picture while the sun is out. Sadly, I noticed it too late, so no data was collected. 
![It's sunny and raining](Photos/sunny_rain.jpg?raw=true "It's sunny and raining")
4. Ordered a graduated cylinder, some eye droppers, and an analog rain gauge. "Guaranteed delivery" by July 1.
5. Also purchased some LM741s to test. This amplification problem is becoming really irritating. 
6. Used some actual water drops for testing today. The voltage is tiny and really needs to be amplified cleanly without the weird time shifts I'm seeing.
7. I've reconnected the AD623 and, this time, need to give it more than a ~2x gain. Right now, this thing seems like it's going to do fine with heavier rainfall but, again, light rainfall is a problem. 

***

### June 29, 2016
1. Based on diagrams of how oscillating sprinklers work and how this one is assembled, breaking the oscillation may prevent it from working it all. I think I just need to implement some resistance so that the water pressure is incapable of making it oscillate. 
2. Just an observation...if I had the proper connector for a hose, I could convert one of the PVC pipes to a sprinkler pretty easily. 
3. Ugh, this amplifier is driving me nuts. [This](Serial Data Logger/data_20160629_154858 - towel drops no amp.xlsx) data log shows that the water drops are producing a decentish voltage, even though they're not at terminal velocity (I dropped them from 8-12 inches above the gauage). These are large drops, though. The data with the amplifier is basically useless. 
4. Matlab key expired...even though I have been using it for three years without issue. Need to go to the bookstore tomorrow to get an updated key. 
5. Further droplet testing shows that an easy way for the water to run off is necessary. 
6. Did some rudimentary data analysis in Excel. The one conclusion so far: the relationship between piezo voltage and rainfall totals is not linear (which was expected).
7. Hopefully when the LM741s arrrive, we'll be able to make a better amplifier setup. If those don't do the job, the OPA337 looks promising. 
8. Based on materials properties, I'm going to go ahead and test Nylon and Aluminum. Nylon, because its properties are quite close to PVC (Young's Modulus is nearly identical), and since the master's thesis used PVC, this might be a good option. Aluminum should be a good control (it's the intuitive choice, yes?) and the leap of faith choice. Don't have to worry about oxidation with either of them. I am enticed by brass (mostly because everyone praises how great it is to machine), but I'm not seeing benefits over aluminum. It costs more, too (http://dmsshreddinginc.com/current-prices-2/). Hopefully, tomorrow morning, I can take both to the lathe. 

***

### June 30, 2016
1. Quick note, the ceramic capacitor across pins 5 and 7 on the AD623 is .1 microfarads. 
2. Also, looks like we need to build a dozen or so prototypes. Have to test multiple materials and take thickness into consideration.
3. Purchasing microphones to see how they do as an alternative to the piezo element. Possibly accelerometers as well, though those are active, not passive, and will require a power source. 
4. Built a quick voltage divider. I have a 4 volt input and a .5 volt output. This is how I'm going to test the AD623 and the op-amps.
5. Thinking of buying [this](http://www.mouser.com/search/ProductDetail.aspx?R=0virtualkey0virtualkeyMO095804-1) microphone. 
6. Also holding off on cutting the remaining PVC tubes - I can't find the dust masks. (Seriously, inhaling this stuff is really unpleasant). 
7. Some materials to consider: rubber (like a balloon, but more durable), thin plastic, aluminum foil that doesn't tear (so, somewhat thick aluminum foil?). Also, my cursor disappeared. -_- 

***

### July 1, 2016
1. AD623 seems to working fine with dual supply setup. With a .1 volt input signal, the outputs are as expected (if slightly high).
2. Shipment arrived and I've begun testing the op-amps.
3. Shipment also contained a few other things. FOr starters, eye droppers, which work well enough. It has a graduated cylinder, which will help avoid issues when the tipping bucket's resolution isn't adequate. It also has an analog rain gauge, which isn't realtime, but it's reliable and another metric we can use. (Although, it could become realtime if we hook up a camera, or something. 
4. Nearly done building another prototype with a thin, plastic, cap (the material you would fine in small consumer goods packaging, like a glue stick). Need to grab a couple more tools to finish it, so I should have the finished by tomorrow. 
5. Going to try to make the AD623 work. The fact it works well enough with a positive and negative supply suggests that it is, potentially, a capable chip. Tomorrow, I'll use the dual supply to run the chip and simply run the output to the Photon. Let's see if the graphs are any better. 
6. Also need to buy more super glue. 

***

### July 2, 2016
1. Didn't do anything today, but consider looking into strong metal foils. Does copper foil tear easily? http://www.quickshipmetals.com/foils/crafting-scrapbooking-foil-coil.html

***

### July 3, 2016
1. Manufacturing the plastic cap variant didn't quite go well. In fact, it cracked due to overly liberal use of the heat gun. Going to try and fix it without having to use another piezo element. 
2. A signal generator would be really nice to have, but, regardless, I've been testing the dual supply setup with the AD623, but the results from directly hooking up the piezo element are...well, inconclusive. 
![Testing the dual supply powered AD623](Photos/dual_supply_hack_job.jpg?raw=true "Testing the dual supply powered AD623")
3. As of right now the signal is much too strong, and, honestly, I'm not sure it's detecting the water droplets very well. 

***

### July 4, 2016
1. FYI (from Ashby's "Material Selectrion in Mechanical Design"):
![Acoustic pitch and brightness](Notes/Acoustic_Pitch_and_Brightness.png?raw=true "Acoustic pitch and brightness")
2. We may want to examine the old prototype again. The acoustics are a lot better. But, again, the issue is that drops that land near the edges sound different from drops that land near the center. But perhaps we could still differentiate it? 
![The old prototype](Photos/old_prototype.jpg?raw=true "The old prototype")
3. Found a couple more papers that could be of use. Will read them tonight. 

***

### July 5, 2016
1. Caps made of aluminum, nylon, and acrylic should be ready soon. 
2. ^Scratch that, costs are higher than expected. Need to look into CNC options as well. 

***

### July 7, 2016
1. So the main issue with machining the caps isn't that the prototype is going to cost a lot, it's that when we scale to 100s or 1000s of nodes, we don't want to be spending $50 just for a cap. I figured the plan would have been using some sort of manufacturer, like [ths](http://www.alibaba.com/product-detail/cnc-machining-metal-parts-small-hardware_1972023896.html) one on Alibaba. We'll need to figure this out.
2. If we have to machine all of the parts ourselves, an off the shelf option might very well be the way to go. I bought three different PVC caps and one copper cap from Lowe's to test, and they fit on top of the PVC pipe pretty well. 
3. Also bought some drip pans to harvest the aluminum (which shouldn't tear like plain foil). Acoustics would likely be pretty good. 
4. Also have Plasti Dip as another way to make a cap.
5. It was also suggested to simply palce the piezo element on a board and plasti dipping the whole thing. Will be investigating this. 
6. Microphones should hopefully be here soon. They allow for another way to collect data. Because they are omni-directional, we might be able to set up an array of six of them (six analog inputs on the Photon) and try to calculate where the drop landed. In doing so, we might be able to account for different acoustics on the end of the cap, allowing us to use a larger cap. The greater the surface area, the more flex when a drop lands, which is beneficial.

***

### July 13, 2016
1. You haven't been posting updates. Shame on you. >_< (talking in second person to myself?)
2. So, kind of shifting gears during these last few weeks. The focus is to get one good systematic experiment going, with loops in which I modify just one thing at a time and keep on iterating. 
![Loops](Notes/scaled_loops.jpg?raw=true "Loops") 
3. I had been building more and more prototypes. That's basically halted except for when I iterate. 
4. The machined caps are done and they are AWESOME. 
![Machined Caps](Photos/machined_caps.jpg?raw=true "Machined Caps")
5. There's a perfect storm outside right now but the setup isn't ready for testing. :(
6. Shower head in the basement gave me an idea - why not just have a 15 foot high shower setup outside? 
7. Second loop is fitting a better scaling function (as opposed to linear) to the data (polynomial instead of linear). 
8. Ultiamtely, for the third loop, we need better data, because loop 2 isn't looking great. The old setup was oscillating and I have a feeling that, despite being right next to each other, the piezo device and the tipping bucket were not experiencing the same abount of rain. 
9. Yeah...I don't think the ground truth is really the "truth" at the moment.
10. 10 foot PVC pipe actually fit in the car. :D
11. The new rain machine...inspired by the shower in the basement. Totaly length is about 12 feet. Add the height up to my shoulders and the drops from this should be able to hit terminal velocity. It's game time. 
![Rain Machine](Photos/rain_machine.jpg?raw=true "Rain Machine")

***

### July 14, 2016
1. Got the spigot key and, despite the ferocious mosquitos, the rain machine works. YEAAAAHHH.
![Raining rain machine](Photos/rain_machine_in_action.jpg?raw=true "Raining rain machine")
2. That said, the rain it's capable of is quite heavy (and dramatic, great for filming a epic scene with a burning car in the rain), but if you lower the presure too much, you get a leaking stream. So, this isn't ideal for light rain, but, then again, neither was the sprinkler, and certainly not the shower. 
3. We may just want to test light rain drops with the eye dropper at a later point. 

***

### July 14, 2016
1. Oi, oi, oi. Working so much and not posting anything. Theees good or bad?
2. So, the following are updates from the past few days. 
3. I had wet sanded the PVC cap to smooth it out, and it turned out pretty well. Had to wear a mask, but that's a minor detail. I only had 150 grit, so not as smooth as it can be, but, honestly, my finger flows over it better than the steel cap.
![Wet sanded PVC cap - like a boss](Photos/wet_sanded_pvc_cap.jpg?raw=true "Wet sanded PVC cap before and after.")
4. There isn't a whole lot of time left, so I'm not sure this will materialize, but I set up a rig to test an electret microphone. Basically, now, I just hot swap caps and don't have to worry about soldering wires or glueing (can also be spelled "gluing") things together. 
![Electret microphone testing rig.](Photos/electret_mic_testing_rig.jpg?raw=true "Sing me a song, you're a singer.")
5. Went outside to collect better data, now using the rain gauge instead of the sprinkler. Things are much better, but the Photon requires WiFi to work, and the signal is too weak for the poor little Photon to get online. So I had to set up a hotspot. And guess what, that required two phones...one run the hotspot, one to create an ad-hoc network to configure the Photon. Genius. -_-
6. Also, cut a quick base for the analog rain gauge to confirm that the tipping bucket works (since it didn't seem to be accurate last time when I was using the oscillating sprinkler). 
![Analog rain gauge](Photos/analog_rain_gauge.jpg?raw=true "Rain drops keep fallin' on my head")
7. Luckily managed to confirm that the tipping bucket is correct.
![Ground truth confirmed](Photos/ground_truth_confirmed.jpg?raw=true "Tipping buckets work, who would have thought?")
8. Tried to get rid of the negative voltage with a diode, that didn't actually work. 
9. I think I actually fixed one issue with the amplifier by using a pull down resistor on the positive signal input. It seems to prevent the slow dissipation issue. It still refuses to register very low signals...which is the exact opposite of what it should be doing. 
10. Excel has been a pain. Crashes a lot and using Visual Basic is a nightmare. It was sugested that I switch to NumPy. Glad I did and that's what I'm working on. 
