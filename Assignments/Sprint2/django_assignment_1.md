#Django assignment 1

To start this, you should cd ~ to your home directory. 

Then run the following commands:

```
django-admin.py startproject homework

cd homework

python manage.py startapp enrollment
```

You need to edit settings.py to add your enrollment app to the installed apps (see the tutorials for help with this).

You should then be good to go.

1. Create a model to store data on [undergraduate enrollment by year since 1967](http://irads.unl.edu/dmdocuments/050_fall_enrl_level_history.pdf). This model will be very simple, but it must store a year and a number. What type of field should your two fields be?
2. Create an admin for your model. [The official Django tutorial will show you how to do this](https://docs.djangoproject.com/en/1.10/intro/tutorial02/). In your admin, add three years of data from the above link.
3. Create a URL, a view and a template to show your three years of data that you entered. You do not need complex HTML, but some basic markup to show the three years would be good.

Due Tuesday. I'm available Friday afternoon and Monday and available via Slack. 