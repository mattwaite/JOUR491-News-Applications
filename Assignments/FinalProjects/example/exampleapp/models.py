from django.db import models

class State(models.Model):
    state_name = models.CharField(max_length=255)
    state_slug = models.SlugField()
    def __unicode__(self):
        return self.state_name
    def get_absolute_url(self):
        return "/population/%s/" % self.state_slug
        
class County(models.Model):
    state = models.ForeignKey(State)
    county_name = models.CharField(max_length=255)
    county_slug = models.SlugField()
    pop2013 = models.IntegerField()
    pop2012 = models.IntegerField()
    pop2011 = models.IntegerField()
    pop2010 = models.IntegerField()
    change = models.FloatField()
    def __unicode__(self):
        return "%s, %s" % (self.county_name, self.state)
    def get_absolute_url(self):
        return "/population/%s/%s/" % (self.state.state_slug, self.county_slug)