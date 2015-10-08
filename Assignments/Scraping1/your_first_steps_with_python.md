#Your first steps with Python#

We're going to take our first steps into programming today with some of the basics: variables, lists, loops, conditionals and functions.


###First things first###

We need an environment. Fortunately for us, Python runs in the browser quite well, so long as we only need the standard library. To avoid the need to install Python on everyone's computer and all the fun that brings, we'll stick to the standard library and we'll use a browser based Python editor. 

####[Go here](http://www.tutorialspoint.com/execute_python_online.php)####

###Hello World###

Every tutorial begins with Hello World and so I suppose we have to do this. So let's get it out of the way. 

type this

`print "Hello world"`

Now press the execute button.

Wow. 

###Variables###

So let's riff off this and dip into variables. Remember: A variable is just a bucket to store something. That something can be words, numbers, lists and all kinds of other stuff. 

Let's make a variable called message and print that:

	message="Informatics is the Bees Knees!"

	print message

So this is a more complicated version of Hello World. Still not exciting. But we can create as many variables as we need and use them. 

	message="My professor is old. He's at least "
	age = 40
	
	print message, age

We can go on for days like this. But what if we want to play Mad Libs? Remember playing Mad Libs as a kid? Let's do that.

	name = "Matt"
	adverb = "wildly"
	verb = "flew"
	adjective = "fat"
    noun = "strawberry patch"
	pronoun = "he"
	
	print "%s %s %s over the %s %s, just like %s dreamed." % (name, adverb, verb, adjective, noun, pronoun)

This method uses substitition to replace the placeholder (%s) with the corresponding item from the list. Note: They must match.

---
*Write your own Mad Lib.*

---

The types of variables we can use are:

* Strings ex. "words here"
* Integers ex. 15
* Floats ex. 1.5
* Booleans ex. True

Note: Quote marks matter. `winner = True` is a boolean meaning what it says. `winner = "True"` is a string that says True and is not a boolean. Also, "15" is a string and 15 is an integer. Numbers do not have quote marks around them. To see the effect of this, try to add them.

	number = 15
	not_a_number = "15"
	
	print number+not_a_number 

What happens if you try to add two strings? Any guesses why?

###Conditionals and comparisons###

Conditionals in Python are very simple. You can get a simple boolean answer by comparing things:

	number1 = 15
	number2 = 20

	print number1 > number2
	
Or `<` or `<=` or `!=` for does not equal. If you want equal to, then you need two equal signs, not one. One equal sign makes it a variable. Two equal signs it the comparison.

Now you can use conditional logic:

	number1 = 15
	number2 = 20

	if number1 > number2:
		print "bigger!"
	elif number1 < number2:
		print "smaller!"
	else:
		print "equal!"
		
If there are only two possibilities, then you want if, else. If there's more than two possibilities, then the elif comes in handy.

###Lists###

Lists are what you think they are: They're a list of objects that you can do stuff with. Lists are very powerful and you can do a lot with them. For our purposes, we're going to deal with indexing and looping.

Your first list:

	people = ["Matt", "Steve", "Sally", "Jane"]
	
	print people
	
Not too exciting, eh?

We can find the first item in the list, or the last one, by using indexing. Indexing is assigning a number to each item in a list. NOTE: In Python and a lot of other programming lanugages, the index starts with 0. 

So to get the first item in the list, do this:

	people = ["Matt", "Steve", "Sally", "Jane"]
	
	print people[0]

Or to get the last, use `print people[-1]`

*Why negative 1?*

###Loops###

The real power of list is in loops. A loop is where Python goes to each item in your list and does something until it gets to the end of the list. We can make a sentence about each person in our list with a loop.

	people = ["Matt", "Steve", "Sally", "Jane"]
	
	for person in people:
		print person + "is a gigantic tool"
		
What happened? Got a spacing problem, eh? Python is doing literally what you told it to do: print the name, then print the phrase immediately next. If you want a space, you have to add a space.

Now this loop takes some unpacking. What it says is for each thing in a list of things, do a thing. What you call that individual thing is up to you -- there's no magic to it. You're creating a variable on the fly called whatever you put there. So for person in people or for zebras in people, you can put whatever you want after the for. The in part is less forgiving. The second part of that is your list. There's better be a list matching your list there. So for person in people COLON (remember the colon -- if you get a syntax error, a safe bet is you forgot it). Then you drop down a line and indent four spaces. In Python, indents are four spaces. An on that indented line, you do something. Or for the next series of lines, you do a thing, until you're done. 

###Functions###

A function is a collection of instructions you can call over and over again and it will give you an answer back. Your function may take something into it -- an input -- and it will almost always provide an output. They're a good way to take code out of your main area to simplify things.

So let's make a function:

	import random

	people = ["Matt", "Steve", "Sally", "Jane"]

	def hookupizer(person):
    	target = random.choice(people)
    	hookup = "%s likes them some %s" % (person, target)
    	return hookup

	for person in people:
    	print hookupizer(person)
    	
In this example, there's two new things: first we imported a library called random so we can get a random choice from a list. We defined a function called hookupizer, which creates a variable from a random choice from the list of people. And then the rest you have done before -- loop through a list, print out a result. 

###Assignment###

I want you to write a simple Python script where the computer plays Rock, Paper Scissors against itself using random choices. You will need to define a function that makes a choice. You will need to define a function that determines a winner. And you'll need to play the game. Bonus points: How would you set it up to determine a winner of two out of three?