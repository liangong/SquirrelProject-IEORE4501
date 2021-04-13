from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect, reverse
from sightings.models import SquirrelData
from django.views import View
from sightings.forms import AddSightingForm


# Create your views here.


def get_map(request):
    sightings = SquirrelData.objects.all()[:100]
    return render(request, 'map/index.html', context={'sightings': sightings})


def index(request):
    """
    •	A view that lists all squirrel sightings with links to view each sighting
    •	Located at: /sightings
    •	Methods Supported: GET
    •	Fields to show:
        	Unique Squirrel ID
        	Date
        	Link to unique squirrel sighting
    •	This view should also have a single link to the “add” sighting view
    """
    sightings = SquirrelData.objects.all()
    context = {'sightings': sightings, 'title': 'all sightings'}
    return render(request, 'squirrel/index.html', context)


class SightingDetail(View):
    """
    •	A view to update a particular sighting
        •	Located at: /sightings/<unique-squirrel-id>
        •	Methods Supported: GET & POST
        •	Fields to show:
            	Latitude
            	Longitude
            	Unique Squirrel ID
            	Shift
            	Date
            	Age
    """

    def get(self, request, s_id):
        sighting = get_object_or_404(SquirrelData, unique_squirrel_id=s_id)
        context = {'sighting': sighting, 'title': s_id,
                   'msg': 'You can edit the sighting detail below by changing the text and click save.'}
        return render(request, 'squirrel/detail.html', context)

    def post(self, request, s_id):
        sighting = get_object_or_404(SquirrelData, unique_squirrel_id=s_id)
        after_mod_id = request.POST.get('unique_squirrel_id')
        if after_mod_id != s_id and SquirrelData.objects.filter(unique_squirrel_id=after_mod_id):
            print('The %s to be modified already exists in the database!' % after_mod_id)
        else:
            sighting.unique_squirrel_id = request.POST.get('unique_squirrel_id')
            sighting.shift = request.POST.get('shift')
            sighting.date = request.POST.get('date')
            sighting.latitude = request.POST.get('latitude')
            sighting.longitude = request.POST.get('longitude')
            sighting.age = request.POST.get('age')
            sighting.save()
        return redirect(reverse('sightings:detail', kwargs={'s_id': s_id}))


class AddSighting(View):
    """
    •	A view to create a new sighting
        •	Located at: /sightings/add
        •	Methods Supported: GET & POST
        •	Fields supported:
            	Latitude
            	Longitude
            	Unique Squirrel ID
            	Shift
            	Date
            	Age
            	Primary Fur Color
            	Location
            	Specific Location
            	Running
            	Chasing
            	Climbing
            	Eating
            	Foraging
            	Other Activities
            	Kuks
            	Quaas
            	Moans
            	Tail flags
            	Tail twitches
            	Approaches
            	Indifferent
            	Runs from
    """

    def get(self, request):
        context = {'title': 'add sighting', 'msg': 'Add a new sighting.'}
        add_form = AddSightingForm(None, SquirrelData)
        context['add_form'] = add_form
        return render(request, 'squirrel/add.html', context)

    def post(self, request):
        add_form = AddSightingForm(request.POST, SquirrelData)
        if add_form.is_valid():
            add_form.save()
            add_unique_squirrel_id = request.POST.get('unique_squirrel_id')
            return redirect(reverse('sightings:detail', kwargs={'s_id': add_unique_squirrel_id}))
        else:
            return redirect(reverse('sightings:add'))


def stats(request):
    context = {'title': 'general stats', 'msg': 'general stats.'}
    sightings = SquirrelData.objects.all()
    total = sightings.count()
    context['pct_dict'] = {'shift_am_pct': sightings.filter(shift='AM').count() / total,
                           'shift_pm_pct': sightings.filter(shift='PM').count() / total,
                           'running_true_pct': sightings.filter(running=True).count() / total,
                           'running_false_pct': sightings.filter(running=False).count() / total,
                           'eating_true_pct': sightings.filter(eating=True).count() / total,
                           'eating_false_pct': sightings.filter(eating=False).count() / total,
                           'climbing_true_pct': sightings.filter(climbing=True).count() / total,
                           'climbing_false_pct': sightings.filter(climbing=False).count() / total,
                           'chasing_true_pct': sightings.filter(chasing=True).count() / total,
                           'chasing_false_pct': sightings.filter(chasing=False).count() / total}

    return render(request, 'squirrel/stats.html', context)
