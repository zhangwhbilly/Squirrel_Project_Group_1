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
            return redirect("/sightings/")
        else:
            form = SightingsForm()
            context = {
                'form': form,
            }
    return render(request, 'sightings/add.html', context)

