from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LocationForm

def location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            # zpracuj data
            return HttpResponseRedirect('/thanks/')
    else:
        form = LocationForm()
    return render(request, 'location.html', {'form': form})

