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
    
import urllib2, string, datetime, time, re
#from django.template.defaultfilters import slugify, urlize

#from unlcrime.incidents.models import Clearance, IncidentType, Incident
#from unlcrime.locations.models import Location, LocationType

#html = urllib2.urlopen("https://scsapps.unl.edu/policereports/default.aspx?__EVENTARGUMENT=&__EVENTTARGET=ctl00$ContentPlaceHolder1$ViewByMonth&__EVENTVALIDATION=%2FwEWQAK9pJXNBgLI17yHDwLm6MqECgKt0r3sBAKt0smADAKt0tWlBQKt0uH%2BCgKt0o2TAgKt0tn6BAKt0uWfDALK69eGCwLK6%2BNbAsrrj%2FwJAsrrm5EBAsrrp6oGAsrrs88PAsrr3%2BMEAsrr64QMAsrrt%2BwOAsrrw4AGAtf8tagFAtf8wcwKAtf87eEDAtf8%2BboLAtf8hV8C1%2FyR8AkC1%2Fy9lQEC1%2FzJqQYC1%2FyVkQsC1%2FyhKgL8lZLdDwL8lb72BAL8lcqKDAL8ldavBQL8leLACgL8lY7lAwL8lZq%2BCwL8laZTAvyV8roFAvyVnt8KApmv8MYJApmvnJsBApmvqLwGApmvtNEPApmvwPUEArHVh7wOArDVh7wOArPVh7wOArLVh7wOArXVh7wOArTVh7wOArfVh7wOAqbVh7wOAqnVh7wOArHVx78OArHVy78OArHVz78OApX%2FnPYBApX%2FiJsJApX%2FpPIPApX%2FkJcHAv7Gog4C%2Fsae0wsC0crAlwLSsbzm9Zsa37e78yoQB5Ja00U1kQ%3D%3D&__VIEWSTATE=%2FwEPDwUKMTg4MTU1ODc4MA9kFgJmD2QWAgIHD2QWAgIBD2QWBgIFDxBkDxYGZgIBAgICAwIEAgUWBhAFBDIwMDYFBDIwMDZnEAUEMjAwNwUEMjAwN2cQBQQyMDA4BQQyMDA4ZxAFBDIwMDkFBDIwMDlnEAUEMjAxMAUEMjAxMGcQBQQyMDExBQQyMDExZ2RkAgkPDxYCHgRUZXh0BQowNC8xOC8yMDExZGQCCw8WAh4LXyFJdGVtQ291bnQCBBYIZg9kFhICAQ8PFgIfAAUIMTEwMDE1MjVkZAIDDw8WAh8ABR1Nb24sIDE4IEFwciAyMDExIDA5OjA2OjAyIENTVGRkAgUPDxYCHwAFGkNvbGxlZ2Ugb2YgQnVzaW5lc3MgQWRtaW4uZGQCBw8PFgIfAGVkZAIJDw8WAh8ABRdWQU5EQUxJU00gLSBCWSBHUkFGRklUSWRkAgsPDxYCHwAFBSQwLjAwZGQCDQ8PFgIfAAUGJDE1LjAwZGQCDw8PFgIfAAUISW5hY3RpdmVkZAIRDw8WAh8ABURQaGFsbGljIHBlbmNpbCBkcmF3aW5nIG9uIGEgbWV0YWwgZG9vciBpbiB0aGUgbWVuJ3MgcmVzdHJvb20gYXQgQ0JBLmRkAgEPZBYSAgEPDxYCHwAFCDExMDAxNTA0ZGQCAw8PFgIfAAUdU2F0LCAxNiBBcHIgMjAxMSAxNTo1OToyMiBDU1RkZAIFDw8WAh8ABRBNZW1vcmlhbCBTdGFkaXVtZGQCBw8PFgIfAGVkZAIJDw8WAh8ABRNESVNUVVJCQU5DRSAtIE9USEVSZGQCCw8PFgIfAAUFJDAuMDBkZAINDw8WAh8ABQUkMC4wMGRkAg8PDxYCHwAFFENsZWFyZWQgYnkgRXhjZXB0aW9uZGQCEQ8PFgIfAAU9RGlzdHVyYmFuY2Ugb2NjdXJyaW5nIGF0IHRoZSBzdGFkaXVtIGFmdGVyIHRoZSBzcHJpbmcgZ2FtZS4gIGRkAgIPZBYSAgEPDxYCHwAFCDExMDAxNTI5ZGQCAw8PFgIfAAUdTW9uLCAxOCBBcHIgMjAxMSAxMzo1MDowNSBDU1RkZAIFDw8WAh8ABQ1OZWJyYXNrYSBIYWxsZGQCBw8PFgIfAGVkZAIJDw8WAh8ABRZBU1NBVUxUIC0gTk9OIERPTUVTVElDZGQCCw8PFgIfAAUFJDAuMDBkZAINDw8WAh8ABQUkMC4wMGRkAg8PDxYCHwAFFENsZWFyZWQgYnkgRXhjZXB0aW9uZGQCEQ8PFgIfAAViRGlzYWdyZWVtZW50IGJldHdlZW4gdHdvIFVOTCBzdHVkZW50IG92ZXIgYSBzZWF0IGluc2lkZSBvZiBhIGNsYXNzcm9vbS4gTm8gY3JpbWluYWwgY2hhcmdlcyBmaWxlZC5kZAIDD2QWEgIBDw8WAh8ABQgxMTAwMTUzMmRkAgMPDxYCHwAFHU1vbiwgMTggQXByIDIwMTEgMTg6NTU6NDYgQ1NUZGQCBQ8PFgIfAAUKUG91bmQgSGFsbGRkAgcPDxYCHwBlZGQCCQ8PFgIfAAURVEVMRVBIT05FIC0gT1RIRVJkZAILDw8WAh8ABQUkMC4wMGRkAg0PDxYCHwAFBSQwLjAwZGQCDw8PFgIfAAUISW5hY3RpdmVkZAIRDw8WAh8ABV9TdHVkZW50IHJlY2VpdmluZyB1bndhbnRlZCBwaG9uZSBjYWxsIGZyb20gdW5rbm93biBwZXJzb24uIE51bWJlciB3YXMgYmxvY2tlZCBvbiBwZXJzb25zIHBob25lLmRkZDKlvkJIrPwVuw8hK2XHSKvKEWtT&ctl00%24ContentPlaceHolder1%24ReportMonth=6&ctl00%24ContentPlaceHolder1%24ReportYear=2011")

#This only works for today
html = urllib2.urlopen("https://scsapps.unl.edu/policereports/default.aspx")

soup = BeautifulSoup(html)

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

"""
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
