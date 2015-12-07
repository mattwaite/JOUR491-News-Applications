from django.shortcuts import render

from exampleapp.models import State, County

def homepage(request):
    states = State.objects.order_by('state_name')
    growing = County.objects.order_by('-change')[:20]
    shrinking = County.objects.order_by('change')[:20]
    context = {"states": states, "growing": growing, "shrinking": shrinking}
    return render(request, 'index.html', context)
    
def statedetail(request, stateslug):
    state = State.objects.get(state_slug=stateslug)
    counties = County.objects.filter(state=state)
    context = {"state": state, "counties": counties}
    return render(request, 'statedetail.html', context)

def countydetail(request, stateslug, countyslug):
    state = State.objects.get(state_slug=stateslug)
    county = County.objects.get(state=state, county_slug=countyslug)
    context = {"state": state, "county": county}
    return render(request, 'countydetail.html', context)
