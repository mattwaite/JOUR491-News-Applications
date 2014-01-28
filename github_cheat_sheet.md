#GitHub cheat sheet#

Make sure you're in your project root directory -- the folder that contains your project. Hint: type ls and look and see if your files are in that directory. If you don't see them, you're not there.

###Step 1: Check to see what you did.

<code>git status</code>

###Step 2: If you created new files, add them to version control.###

<code>git add [filename or . for all]</code>

###Step 3: Bundle files to be committed to version control.###

To just commit everything, do this:   

<code>git commit -a -m "A message that tells whoever what you've done"</code>

If you want to just commit a single file: 

<code>git commit filenamehere -m "Message to whoever here saying what you've done"</code>

###Step 4: Kick the kiddies out the door.###

<code>git push</code>

###Step 5. Celebrate.###

If all worked well, you should see a message telling you how many files were sent to GitHub.