#Scraping, part 2#

Understand this: Scraping is a giant puzzle. Often it's puzzles within puzzles. It's loops within loops, and searches for very specific words. If you like problem solving, you'll love scraping. 

Let's start with a simple example. It's about to get cold in these parts, so let's look at the record low for every month going back to 1887. [You can get that here](http://snr.unl.edu/lincolnweather/data/monthly-coldest.asp).

####Page source, web inspectors, looking under the hood####

First: Let's be clear. This is a simple HTML table. You can copy and paste it into Excel easily without ever having to write any code. So why wouldn't you do this? 

What if we had this same table for every weather reporting station in the United States? Tens of thousands of pages, just like this? Who wants to copy and paste that over and over again? No one. That's a human rights violation. 

So we're going to write code that does this. 

The first step is knowing what's under the hood. 

Control U is your first step.


**Sometimes the data is hidden**

[Look at this page from the FAA](https://www.faa.gov/uas/legislative_programs/section_333/333_authorizations/)

See how data is paginated? Look at the source code underneath. Notice something?

**Back to the weather**

So let's break this problem down step by step determining what we need to accomplish the task.

1. We need Python to fetch a web page.
2. We need Python to read that page.
3. We need Python to break out the HTML into stuff we can use.
4. We need to find the table in the data.
5. We need to traverse the table and do stuff with it. 

So first things first:

We need a library to parse HTML. So from your command line, you're going to run this command: 

`sudo apt-get install python-bs4`

There are several ways to fetch pages with Python. The standard way is to use urllib2

    import urllib2
    from bs4 import BeautifulSoup

    url = "http://snr.unl.edu/lincolnweather/data/monthly-coldest.asp"  
    page = urllib2.urlopen(url).read()
    
    soup = BeautifulSoup(page)
    
    print soup
    
Whee!

Now what? 

Let's look at the code again. Where does our data reside? If these were lists, what would our code look like?

    for tr in soup.find_all('tr')[1:]:
        tds = tr.find_all('td')
        print tds[0].text
    
    
    
####Assignment: Scrape the FAA's 333 list####

What I want to see printed to the screen: The date issued, the petitioner, and a link to the grant of exemption (the link). 

Use what you've learned. It's very similar. 

[Here is your target.](https://www.faa.gov/uas/legislative_programs/section_333/333_authorizations/)

It's dangerous out there. [Take this](http://www.crummy.com/software/BeautifulSoup/bs4/doc/). 



