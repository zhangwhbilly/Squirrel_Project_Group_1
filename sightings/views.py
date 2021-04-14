from django.shortcuts import render, get_object_or_404, redirect
from map.models import Squirrel



def sightings():
    Squirrels = Squirrel.objects.all()
    context = {
        'Squirrels': Squirrels,
    }
    return render(request, 'sightings/', context)


def update_sighting(request):
    squirrel_detail = get_object_or_404(Squirrel, unique_squirrel_id)
    if request.method == 'POST':
        form = SightingsForm(request.POST, instance = squirrel_detail)
        if form.is_valid():
            form.save()
            return redirect(f'sightings/{unique_squirrel_id}')
        else:
            form = SightingsForm(instance = squirrel_detail)
    context = {
        'form': form,
    }
    return render(request, 'sightings/update.html', context)


def create_sighting(request):
    if request.method = 'POST':
        form = SightingsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sightings/")
        else:
            form = SightingsForm()
    context = {
        'form': form,
    }
    return render(request, 'sightings/add.html', context)


def stats(request):
    total = Squirrel.objects.all().count()
    gray_count = Squirrel.objects.filter(primary_fur_color = 'Gray').count()
    PM_count = Squirrel.objects.filter(shift = 'PM').count()
    AM_count = Squirrel.objects.filter(shift = 'AM').count()
    avg_lat = Squirrel.objects.aggregate(Avg('latitude'))
    avg_long = Squirrel.objects.aggregate(Avg('longitude'))
    above_count = Squirrel.objects.filter(location = 'Above Ground').count()
    context = {
        'total': total,
        'gray_count': gray_count,
        'PM_count': PM_count,
        'AM_count': AM_count,
        'avg_lat': avg_lat,
        'avg_long': avg_long,
        'above_count': above_count,
    }
    return render(request, 'sightings/stats.html', context)

