#Installing Django on your computer

###Mac users

If you haven't already, install [Anaconda for Mac](https://www.continuum.io/downloads). After installation, open a Terminal and type these commands.

```
conda create --name django python=3    
source activate django  
pip install Django==1.10.5

```


###PC users

If you haven't already, install [Anaconda for Windows](https://www.continuum.io/downloads). After installation, open a Command Prompt and type these commands.

```
conda create --name django python=3    
activate django  
conda install django

```

##Your first Django project

The first thing you need is the [Django documentation](https://docs.djangoproject.com/en/1.10/). You'll use this a lot. 

Using a dataset of parking tickets, we're going to create an app that will tell show you the top 25 places on campus where parking tickets are written. We'll have a page that lists where those tickets are issued, and when.


```
django-admin startproject demo1

cd demo1

python manage.py runserver
```

Now take your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

It worked!

Okay, slow down trigger. You didn't do anything yet. So let's do that. 

##Models and data

First, hit control c and quit the server you just started.

```
python manage.py startapp tickets

```

Now go into the folder tickets and open models.py.

Models are how we are going to represent our database tables in code. We'll describe those database tables using Python classes, telling Django what our fields will be. 

The general rule on database models is this: Try to represent real life. If there's only one of a thing, store that thing as a table and refer to it. What does that look like? 

```
from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    def __str__(self):
        return name
    
class Violation(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    def __str__(self):
        return name
    
class Ticket(models.Model):
    ticket_number = models.CharField(max_length=255)
    issued = models.DateTimeField()
    location = models.ForeignKey(Location)
    violation = models.ForeignKey(Violation)
    def __str__(self):
        return self.ticket_number
```

Note a few things: Class names are capitalized. Where things can be normalized -- i.e. the same thing is stored only once, we store it in a separate table -- we do that. Lastly, the order of things matters. We can't ForeignKey -- relate one record to a record in another database -- to a table that doesn't already exist. So we have to create the related table before we can relate to it. 

Now we need to create those database tables. 

Open settings.py inside your demo1 folder (which is in your demo1 folder, of course). Add tickets to installed apps, like this:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tickets',
]
```

Then, from the command line, run this:
```
python manage.py migrate
```

That will create some database tables that you need regardless of what we've done. These are installed by default. Then run this:

```
python manage.py makemigrations tickets  
python manage.py migrate 
```

That will make database migrations for our tickets apps and then migrate those to the database. This is the steps you will take every time you change your database models. You create a migration file first, then you migrate it. 

We have data already. We'll talk about how this works in a later lesson. We need to do a few things. First, install pytz

`pip install pytz`

Download [this file](https://unl.box.com/s/mdpwobqys1i193dq07v5yyf4w6qrsnrv) and move it into the same folder as your manage.py file. Now create a file called loader.py and add this code.

```
import os, sys, string, csv, datetime, time, django, pytz
from pytz import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo1.settings") 

django.setup()

from tickets.models import Location, Violation, Ticket

from django.template.defaultfilters import slugify, urlize
from django.core.exceptions import ObjectDoesNotExist

central = timezone('US/Central')

reader = csv.reader(open("tickets.csv", "rU"), dialect=csv.excel)
next(reader)
for row in reader:
    loc = row[2]
    loc_slug = slugify(loc)
    locate, locadded = Location.objects.get_or_create(name=loc, name_slug=loc_slug)
    vio = row[3]
    vio_slug = slugify(vio)
    violate, vioadded = Violation.objects.get_or_create(name=vio, name_slug=vio_slug)
    idate = time.strptime(row[1], "%Y-%m-%d %H:%M:%S")
    incdate = central.localize(datetime.datetime(idate.tm_year, idate.tm_mon, idate.tm_mday, idate.tm_hour, idate.tm_min, idate.tm_sec))
    tic = Ticket(ticket_number=row[0], issued=incdate, location=locate, violation=violate)
    print(tic)
    tic.save()
```
Now run that loader.py file.

```
python loader.py
```

Get comfortable, it'll take a few minutes. You're loading 161,000 parking tickets.

##URLs, views, templates

So with our data loaded and our models made, we now move to the workflow part of Django.

1. Create a URL.
2. Point it to a view.
3. Create the view to provide needed elements to a template.
4. Create and edit the template.
5. Look at it on your server. 

Rinse. Repeat.

So to start, let's do something simple. Open `tickets/views.py` and add this code to what's already there:

```
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the homepage.")
```

Now replace `urls.py` in the demo1 folder with this:

```
from django.conf.urls import url
from django.contrib import admin

from tickets import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
]
```

So let's review urls.py. The imports at the top aren't important (for now). What is important is that first url line. What that says is "Create a url, and have it match the regular expression of ... nothing. Just the root domain and nothing after it. So www.mysite.com and nothing else after it." Then point that to views.index, giving it the name of index. 

Note, in views, we created a view called index. So they point to each other now. Run `python manage.py runserver` and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/). You should see Hello World.

So let's make this a little more involved. Go back to `views.py` and let's edit it to be a little more complicated.

```
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count

from tickets.models import Ticket, Violation, Location

def index(request):
    top_location = Location.objects.annotate(num_tickets=Count('ticket')).order_by('-num_tickets')[:10]
    top_violation = Violation.objects.annotate(num_tickets=Count('ticket')).order_by('-num_tickets')[:10]
    context = {'top_location': top_location, 'top_violation': top_violation}
    return render(request, 'tickets/index.html', context)
```

What we've done here is created two querysets -- a term you'll hear a lot -- that query data from oure models. It sounds backwards when you say it, but the queries are simple. Model.objects is the same way as saying "Give me all the objects in the model called Model that fit this following criteria." We can do basic things like filter (name = "Abel Hall") or exclude (same, but instead of Abel Hall we'll get everything BUT Abel Hall). In our case, we annotated the queryset with an aggregate. In our case, it was count. Count the number of tickets at this place, order it by that count, and then only give me the top 10. 

Then, below, we said the page context was going to be our two querysets -- meaning make that data available to the template -- and then render the template with the context. 

If you go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) you'll get ... an error message. But what's the error? Template not found. Why? Because we haven't made it yet. So that's an error we expect.

So from the command line, hit control c to exit out of the server. Then type `cd tickets` then `mkdir templates` then `cd templates` then mkdir `tickets` then `cd tickets` then `touch index.html`. That will create a folder called templates, which Django is looking for in our tickets app, and then creates a file called index.html in that folder. 

If you were to type `cd ../../..` and then rerun your server with `python manage.py runserver` you'll see your error page is now gone. It's replaced with ... nothing. Why? Because your template is blank. Let's replace it with this:

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Parking tickets</title>
</head>
<body>
<h1>Parking tickets are bad</h1>

<h3>Top locations for tickets</h3>
<ul>
{% for object in top_location %}
<li>{{ object.name }} | {{ object.num_tickets }}</li>
{% endfor %}</ul>

<h3>Top violations on tickets</h3>
<ul>
{% for object in top_violation %}
<li>{{ object.name }} | {{ object.num_tickets }}</li>
{% endfor %}</ul>

</body>
</html>
```

##Going further

So we've made a page now that shows some things, but our site doesn't allow us to explore very much. What if we wanted to be able to click on a location and be shown what the most frequent tickets are at that location? Or click on a violation and find out what locations those tickets most frequently get written? The steps for this are pretty simple, though there are several of them. But refer back to our workflow: Define a url, create a view, create a template. 

In this case, we're going to add one thing: We're going to add to our models. We can add the url to each object in our models by adding a method to them to do so. It's called `get_absolute_url` and it's pretty simple: 

```
class Location(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "/locations/%s/" % self.name_slug

class Violation(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "/violations/%s/" % self.name_slug
```

All we have added to our models is a function called `get_absolute_url` that returns a url pattern. In this case, it does a simple python text substitution, swapping out the %s for self.name_slug, meaning the name_slug field from this class. We created the name_slug field to be in a url, so here it is. To see this in action, we can change our template. 

```
<h3>Top locations for tickets</h3>
<ul>
{% for object in top_location %}
<li><a href="{{ object.get_absolute_url }}">{{ object.name }}</a> | {{ object.num_tickets }}</li>
{% endfor %}</ul>

<h3>Top violations on tickets</h3>
<ul>
{% for object in top_violation %}
<li><a href="{{ object.get_absolute_url }}">{{ object.name }}</a> | {{ object.num_tickets }}</li>
{% endfor %}</ul>
```

See how we added an a tag around name, and populated the href for that with `{{ object.get_absolute_url }}`. That's all we have to do to add a link. If you don't have a server runnning, start it and go to your page. You'll see links galore. But if you click on one, you'll get ... a 404 error. Page not found. Why? Because we haven't made the url yet. So lets do that. 

Add this to demo1/urls.py between your homepage and the admin.

```
    url(r'^locations/(?P<location_slug>\w+)', views.location, name='location'),
```

And now add this to tickets/views.py:

```
def location(request, location_slug):
    location = Location.objects.get(name_slug=location_slug)
    top_violation = Violation.objects.filter(ticket__location__name_slug=location_slug).annotate(num_tickets=Count('ticket')).order_by('-num_tickets')[:10]
    context = {'location': location, 'top_violation': top_violation}
    return render(request, 'tickets/location.html', context)
```

And add this template to tickets/templates/tickets/location.html

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Parking tickets at {{ location }}</title>
</head>
<body>
<h1>Parking tickets are bad at {{ location }}</h1>

<h3>Top tickets</h3>
<ul>
{% for object in top_violation %}
<li>{{ object.name }} | {{ object.num_tickets }}</li>
{% endfor %}</ul>

</body>
</html>
```

##Stretch goal: How do we do this for violations?