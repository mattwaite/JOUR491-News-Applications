#Tarbell#

Installing Tarbell on our Ubuntu virtual machines.

Step 1: Install Tarbell. You will have to run this command as root (sudo)

    sudo pip install tarbell==0.9b4
    
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





