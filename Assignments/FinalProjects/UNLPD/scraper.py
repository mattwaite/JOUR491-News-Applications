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
"""
import mechanize
import cookielib

url = "https://scsapps.unl.edu/policereports/default.aspx"

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

r = br.open(url)

forms = mechanize.ParseFile(r, url)

form = forms[0]

form["ctl00$ContentPlaceHolder1$ReportMonth"] = ["1"]
form["ctl00$ContentPlaceHolder1$ReportYear"] = ["2014"]

request2 = form.click()
response2 = mechanize.urlopen(request2)
"""
html = urllib2.urlopen("https://scsapps.unl.edu/policereports/default.aspx?__EVENTTARGET=ctl00%24ContentPlaceHolder1%24DateRange&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUKMTA3MDU4MjcyMQ9kFgJmD2QWAgIHD2QWAgIBD2QWCgIBDxBkZBYBZmQCAw88KwAKAQAPFgIeAlNEFgEGAIB7ntQg0QhkZAIFD2QWBAIBDxBkZBYBAgNkAgMPEGQPFglmAgECAgIDAgQCBQIGAgcCCBYJEAUEMjAwNgUEMjAwNmcQBQQyMDA3BQQyMDA3ZxAFBDIwMDgFBDIwMDhnEAUEMjAwOQUEMjAwOWcQBQQyMDEwBQQyMDEwZxAFBDIwMTEFBDIwMTFnEAUEMjAxMgUEMjAxMmcQBQQyMDEzBQQyMDEzZxAFBDIwMTQFBDIwMTRnFgECCGQCBw8PFgIeBFRleHQFCjA0LzA4LzIwMTRkZAIJDxYCHgtfIUl0ZW1Db3VudAICFgRmD2QWFAIBDw8WBB8BBQgxNDAwMTUwNB4LTmF2aWdhdGVVcmwFHlJlcG9ydFZpZXdlci5hc3B4P3JwdD0xNDAwMTUwNGRkAgMPDxYCHwEFEDA0LzA4LzIwMTQgMDE6NDZkZAIFDw8WAh8BBRFDbGVhcmVkIGJ5IEFycmVzdGRkAgcPDxYCHwEFPiA8c3BhbiBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDsiPkRhdGU6PC9zcGFuPiAwNC8wOC8yMDE0IDAxOjQ2ZGQCCQ8PFgIfAWVkZAILDw8WAh8BBRxOIDE0VEggU1QgJiBORVcgSEFNUFNISVJFIFNUZGQCDQ8PFgIfAQUNQUxDT0hPTCAtIERXSWRkAg8PDxYCHwEFBSQwLjAwZGQCEQ8PFgIfAQUFJDAuMDBkZAITDw8WAh8BBZ8BU3R1ZGVudCBjb250YWN0ZWQgb24gYSB0cmFmZmljIHN0b3AuICBDaXRlZC9EZXRveCBmb3IgRFVJICguMTA4KSwgTUlQQywgT3BlbiBDb250YWluZXIsIFBvc3MgTWFyaWp1YW5hIDwgMSBveiwgUG9zcyBEcnVnIFBhcmFwaGVybmFsaWEgYW5kIEZhaWwgdG8gU2lnbmFsIFR1cm4uZGQCAQ9kFhQCAQ8PFgQfAQUIMTQwMDE1MDgfAwUeUmVwb3J0Vmlld2VyLmFzcHg%2FcnB0PTE0MDAxNTA4ZGQCAw8PFgIfAQUQMDQvMDgvMjAxNCAxMTo0MmRkAgUPDxYCHwEFBkFjdGl2ZWRkAgcPDxYCHwEFfSA8c3BhbiBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDsiPkJldHdlZW46PC9zcGFuPiAwNC8wOC8yMDE0IDA5OjAwIDxzcGFuIHN0eWxlPSJmb250LXdlaWdodDpib2xkOyI%2BYW5kPC9zcGFuPiAwNC8wOC8yMDE0IDEwOjMwZGQCCQ8PFgIfAQUOTWFiZWwgTGVlIEhhbGxkZAILDw8WAh8BBRE4NDAgTm9ydGggMTR0aCBTdGRkAg0PDxYCHwEFF0xBUkNFTlkgLSBGUk9NIEJVSUxESU5HZGQCDw8PFgIfAQUGJDMwLjAwZGQCEQ8PFgIfAQUFJDAuMDBkZAITDw8WAh8BBTFQdXJzZSBhbmQgY29udGVudHMgc3RvbGVuIGZyb20gdGhlIGRhbmNlIHN0dWRpby4gZGRka8kjP6jlRvcJ7kkL%2FnA8gezYNDw%3D&__EVENTVALIDATION=%2FwEWMAKAhszzAQKS%2F7aJAgLL%2F7LRCwKn6v%2BACALp6JarCQL3gaOpBAKu0q3LDwKu0rnsBAKu0sWADAKu0tGlBQKu0v3%2BCgKu0omTAgKu0tX6BAKu0uGfDALL69OGCwLL6%2F9bAsvri%2FwJAsvrl5EBAsvro6oGAsvrz84PAsvr2%2BMEAsvr54QMAsvrs%2BwOAsvr34AGAtD8sagFAtD83cwKAtD86eEDAtD89boLAtD8gV8C0Pyt8AkC0Py5lQEC0PzFqQYC0PyRkQsC0Py9KgL9la7dDwL9lbr2BAL9lcaKDAL9ldKvBQL9lf7ACgL9lYrlAwL9lZa%2BCwL9laJTAv2VjroFAv2Vmt8KApqvjMYJApqvmJsBApqvpLwGApqvsNEPoDJ2SCXwd745Fi%2BYdEbW3NW%2FB8I%3D&ctl00%24ContentPlaceHolder1%24DateRange=month")
soup = BeautifulSoup(html)

print soup

#html = urllib2.urlopen("https://scsapps.unl.edu/policereports/default.aspx")

#soup = BeautifulSoup(response2)

"""
tables = soup.findAll('table')

reports_container = tables[3]

ids = reports_container.findAll('a', id=re.compile('.*_IncidentNumberLink'))
reported = reports_container.findAll('span', id=re.compile('.*_Label2'))
occurred = reports_container.findAll('span', id=re.compile('.*_Label10'))
buildings = reports_container.findAll('span', id=re.compile('.*_Label3'))
streets = reports_container.findAll('span', id=re.compile('.*_Label4'))
incidents = reports_container.findAll('span', id=re.compile('.*_Label5'))
stolens = reports_container.findAll('span', id=re.compile('.*_Label6'))
damages = reports_container.findAll('span', id=re.compile('.*_Label7'))
clearances = reports_container.findAll('span', id=re.compile('.*_Label8'))
narratives = reports_container.findAll('span', id=re.compile('.*_Label9'))

cids= []
creported = []
coccurred = []
cbuildings = []
cstreets = []
cincidents = []
cstolens = []
cdamages = []
cclearances = []
cnarratives = []

for row in ids:
    cids.append(row.b.font.string)

for row in reported:
    creported.append(row.renderContents())
    
for row in occurred:
    coccurred.append(row.contents[2])

for row in buildings:
    cbuildings.append(row.renderContents())

for row in streets:
    cstreets.append(row.renderContents())
    
for row in incidents:
    cincidents.append(row.renderContents())

for row in stolens:
    cstolens.append(row.renderContents())

for row in damages:
    cdamages.append(row.renderContents())
    
for row in clearances:
    cclearances.append(row.renderContents())

for row in narratives:
    cnarratives.append(row.renderContents())

mat = []

mat.append(cids)
mat.append(creported)
mat.append(coccurred)
mat.append(cbuildings)
mat.append(cstreets)
mat.append(cincidents)
mat.append(cstolens)
mat.append(cdamages)
mat.append(cclearances)
mat.append(cnarratives)

incidents = zip(*mat)

print incidents

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
    
"""