#!/usr/bin/env python
# encoding: utf-8
"""
scraper.py

Created by Matthew Waite on 2011-03-31.

"""
#from django.core.management import setup_environ
import sys

#sys.path.append('/Users/mwaite/Development/django-projects/')
#from unlcrime import settings
#setup_environ(settings)

try:
    from BeautifulSoup import BeautifulSoup
except:
    from bs4 import BeautifulSoup
    
import urllib, urllib2, string, datetime, time, re
#from django.template.defaultfilters import slugify, urlize

#from unlcrime.incidents.models import Clearance, IncidentType, Incident
#from unlcrime.locations.models import Location, LocationType

html = urllib2.urlopen("https://scsapps.unl.edu/policereports/default.aspx")

soup = BeautifulSoup(html)


tables = soup.findAll('table')

reports_container = tables[3]

rows = reports_container.findAll('tr')

for row in rows:
    tds = row.findAll('td')
    reptid = tds[0]
    reported = row.find(id=re.compile('.*_Label2')).string
    occurred = row.find(id=re.compile('.*_Label10')).string
    building = row.find(id=re.compile('.*_Label3')).string
    street = row.find(id=re.compile('.*_Label4')).string
    incident = row.find(id=re.compile('.*_Label5')).string
    stolen = row.find(id=re.compile('.*_Label6')).string
    damage = row.find(id=re.compile('.*_Label7')).string
    clearance = row.find(id=re.compile('.*_Label8')).string
    narrative = row.find(id=re.compile('.*_Label9')).string
    print reported, building, incident, narrative
    

for i in incidents:
    if i[2]:
        lt, ltcreated = LocationType.objects.get_or_create(location_type="Building", location_type_slug="building")
        incloc, incloccreated = Location.objects.get_or_create(location_type=lt, location=i[2], location_slug=slugify(i[2]))
    elif i[3]:
        lt, ltcreated = LocationType.objects.get_or_create(location_type="Street", location_type_slug="street")
        incloc, incloccreated = Location.objects.get_or_create(location_type=lt, location=i[3], location_slug=slugify(i[3]))
    else:
        lt, ltcreated = LocationType.objects.get_or_create(location_type="Unknown", location_type_slug="unknown")
        incloc, incloccreated = Location.objects.get_or_create(location_type=lt, location="Unspecified", location_slug="unspecified")
    #idate = time.strptime(i[1], "%a, %d %b %Y %H:%M:%S CST")
    idate = time.strptime(i[1], "%m/%d/%Y %H:%M")
    incdate = datetime.datetime(idate.tm_year, idate.tm_mon, idate.tm_mday, idate.tm_hour, idate.tm_min, idate.tm_sec)
    inctype, inctypecreated = IncidentType.objects.get_or_create(incident_type=i[4], incident_type_slug=slugify(i[4]))
    clr, clrcreated = Clearance.objects.get_or_create(clearance_type=i[7], clearance_type_slug=slugify(i[7]))
    inc, inccreated = Incident.objects.get_or_create(incident_id=i[0], incident_date=incdate, incident_location=incloc, incident_type=inctype, stolen_amount=i[5], damaged_amount=i[6], clearance=clr, narrative=i[8])
    print inc