#YOU NEED THESE TO IMPORT DATA

import os, sys, string, csv, datetime, time, django

# This line imports your settings. You need to change fooproject to the name of your project

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example.settings")

from django.conf import settings

#You need to change the next line to your app.models and import the name of the models in there.

from exampleapp.models import State, County

from django.template.defaultfilters import slugify, urlize

django.setup()

reader = csv.reader(open("countypops1013.csv", "rU"), dialect=csv.excel)
reader.next()
for row in reader:
    statename = row[0]
    stateslug = slugify(row[0])
    st, stcreate = State.objects.get_or_create(state_name=statename, state_slug=stateslug)
    countyname = unicode(row[1], errors='ignore')
    countyslug = slugify(countyname)
    chng = ((float(row[5])-float(row[2]))/float(row[2]))*100
    cty, ctycreated = County.objects.get_or_create(state=st, county_name=countyname, county_slug=countyslug, pop2013=row[5], pop2012=row[4], pop2011=row[3], pop2010=row[2], change=chng)
    print cty