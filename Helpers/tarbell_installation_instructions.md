#Tarbell#

For each of you, this will be slightly different. 

**MAC USERS**

I highly recommend you use a virtual environment. My preferred virtual environment manager is Anaconda. You can [download it here](https://www.continuum.io/downloads). Download the Python 3.5 graphical installer. 

Once you have installed Anaconda (or for those of you who already have it installed), you need to set up a Python 2.7 environment. Open a terminal and type this:

`conda create --name tarbell python=2.7` 

Before proceeding to Installing Tarbell below, make sure you activate your tarbell environment by typing `source activate tarbell`.

**PC USERS**

Tarbell does not work on Windows. Period. And there's other glitches with Windows and open source software (unless you're using the absolute latest version of Windows) that we're just going to avoid by creating a virtual machine. To install a virtual machine, [first download VirtualBox](https://www.virtualbox.org/wiki/Downloads) for Windows hosts and install it. 

Now you'll need a Linux Distribution. I strongly encourage Ubuntu, which you can [download here](https://www.ubuntu.com/download). When you click through the downloads, you do not have to donate. Look for the not now link below the stuff. WARNING: The file you're downloading is quite large. It will take some time. 

To install the virtual machine, click New in VirtualBox. Under Name, just call it Ubuntu. That should make the next two drop downs autopopulate (if not, they should be Linux and Ubuntu (64-bit)). 

For memory size, 1024 MB should be the default. Then check to make sure Create a virtual hard disk is checked in the next area. Click Create, then click Create again. The windows should close. 

Click Start (the big green arrow). A window will pop up asking you for a drive. Click the folder icon on the right and find the Ubuntu file you downloaded. For most of you, that will be in Downloads. Click it, click open, then click Start. Some alerts will pop up at the top. You can click the X to close them. 

When you get a desktop, a window will appear. Click Install Ubuntu. Then click Download updates while installing Ubuntu and then hit continue. 

The next window sounds scary, but isn't. You want to Erase disk and install Ubuntu. To be very clear -- it's just the VIRTUAL disk that's being erased. Not your computer. The virtual machine cannot affect the host machine like that. So click Install Now, then Continue.

During the installation, you should fill out the forms, setting the time zone, the keyboard. Fill in your name, computer name and a password you will remember. To save you some trouble, click Log in automatically (you'll still need the password for other things, so pick one you'll remember). After you click continue, the installation should proceed. When it's done, it'll ask you to restart your machine. 

After the virtual machine boots up, you can delete the file you downloaded to free up that space.

As soon as it boots up, click on Devices in the menu bar at the top and click Insert Guest Additions CD image ... and then click Run when the window pops up. You'll be prompted for your password that you created during the installation. Let it install.

The guest additions will make things like expanding the screen size easier. When it is done installing, click the Power button in the top right corner and go to shut down. Click restart your machine to make the guest additions take effect.

With guest additions, you should be able to stretch the window to be as wide as you need. 

Your first task in Linux is to pull up a terminal. Click the purple icon in the top left to search your new computer type terminal and click the terminal icon. 

With a terminal open, type:

* `sudo apt-get update`
* `sudo apt-get upgrade`
* `sudo apt-get install libncurses5-dev libffi-dev`
* `sudo apt-get install python-pip`
* `sudo pip install --upgrade pip`

You're now (finally) ready to install Tarbell.


##Installing Tarbell

Step 1: Install Tarbell. You will have to run this command as root (sudo)

    sudo pip install tarbell
    
Step 2: Configure Tarbell

    tarbell configure
    
Step 3: Answer question one with a y.

Step 4: Go here [https://cloud.google.com/console/project](https://cloud.google.com/console/project)

Step 5: Create a new project.

Step 6: Click on APIs and Auth in the left navigation area. (click on APIs below that if it doesn't open up by default). Find the Drive API and turn it on. Accept the terms of service. There should be four other APIs on by default (BigQuery, Google Cloud SQL, Google Cloud Storage, Google Cloud Storage JSON API). If they are not on, you will get an error message. 

Step 7: Click on Credentials. Click Create New Client ID under the OAuth 2.0 area. In the pop-up window, change the type to Installed Application and the Installed Application Type to 'other'. Click create client ID.

Step 8: In the new client ID area, click download JSON. 

Step 9: Rename it client_secrets.json (it will have some weirdly crufty file name)

Step 10: Return to your console and accept the default on where the file is (because it should be there now).

Step 11: Say yes to wanting to authenticate. Hold down control and click the big url in the terminal and enter in the verification code. Click Allow Access and copy the verification code from your browser and paste it into your terminal.

Step 12: Enter your google account email address where it asks which account should have access. 

Step 13: SAY NO to setting up S3. We'll do this later when we're ready to publish.

Step 14: Accept the default for where your projects will be stored. 

Step 15: Look on in terror for you have installed Tarbell and can now rule the world. Or make news apps. One or the other. Your call.





