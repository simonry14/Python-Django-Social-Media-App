from django.shortcuts import render, redirect
from . models import Profile, Dweet
from . forms import DweetForm

# Create your views here.
def dashboard(request):
    form = DweetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("dashboard")
    followed_dweets = Dweet.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by("-created_at")
    context = {'form': form,"dweets": followed_dweets }
    return render(request, "dwitter/dashboard.html", context)

def profile_list(request):
    profiles = Profile.objects.exclude(user = request.user)#exclude self profile
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
