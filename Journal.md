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
