#Scraping bounty: Department of Environmental Quality#

NET News reported on a broad story this morning about the visible signs of climate change in Nebraska. [One of those signs is a steady increase in toxic algal blooms in Nebraska lakes](http://netnebraska.org/article/news/994707/climate-change-seen-risk-nebraskas-health-well-being). 

That's interesting because that data is tracked. [And it's online](http://deq.ne.gov/Beaches.nsf/LakeSampling15). You can check if your lake is fouled up before you go there, thanks to the Nebraska Department of Environmental Quality. 

The problem: It's in Nebraska State Government Style Website, which is to say straight out of 1996 and awful. And the data formatting does not promote any kind of analysis. It just gives you the current situation, and then lets you look at past data with another click. You *could* get this data by clicking over and over and over and copying and pasting each time, but why? 

We can scrape it.

**Your mission, should you choose to accept it...**

1. [Go to the DEQ's reporting site and inspect the data](http://deq.ne.gov/Beaches.nsf/LakeSampling15).
2. Write a script that grabs all of the data in this page.
3. Now write a script that loops through the links, goes to that page, and gets the data out of that.
4. Now write a script that will get previous years (which are linked at the bottom of the page).
5. Bonus: Write it out to a CSV file. There's a ton of ways to do this.

Hint: Everything you need to do this -- with the exception of writing a CSV file out -- you've done with Python before. It's about applying concepts. Think procedureally and linearly. What do I need first? What do I need second? What do I need to happen now?