from multiprocessing import context
from django.shortcuts import render
from . models import Profile, Dweet
from . forms import DweetForm

# Create your views here.
def dashboard(request):
    form = DweetForm()
    context = {'form': form}
    return render(request, "dwitter/dashboard.html", context)

def profile_list(request):
    profiles = Profile.objects.exclude(user = request.user)
    context = {"profiles": profiles}
    return render(request, 'dwitter/profile_list.html', context)

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == 'POST':
        logged_in_user_profile = request.user.profile
        action = request.POST.get("follow")
        if action == "follow":
            logged_in_user_profile.follows.add(profile)
        elif action == "unfollow":
            logged_in_user_profile.follows.remove(profile)
        logged_in_user_profile.save()
        
    
    context = {"profile":profile}
    return render(request, "dwitter/profile.html", context)
