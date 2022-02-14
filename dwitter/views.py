from multiprocessing import context
from django.shortcuts import render
from . models import Profile

# Create your views here.
def dashboard(request):
    context = {'page':'Dashboard'}
    return render(request, "base.html", context)

def profile_list(request):
    profiles = Profile.objects.exclude(user = request.user)
    context = {"profiles": profiles}
    return render(request, 'dwitter/profile_list.html', context)

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {"profile":profile}
    return render(request, "dwitter/profile.html", context)
