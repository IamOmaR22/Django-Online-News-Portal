from django.shortcuts import render, get_object_or_404, redirect
from .models import Trending
from news.models import News
from cat.models import Cat  # for showing categories in footer
from subcat.models import SubCat  ## for SubMenu in the menu bar
from django.contrib.auth import authenticate, login, logout  # for authentication
from django.core.files.storage import FileSystemStorage  # for upload image

# Create your views here.

###---#---### Trending Add Function For Back (Admin Panel - Backend) Start ####--#--####
def trending_add(request):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End

    if request.method == 'POST':

        txt = request.POST.get('txt')

        if txt == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error':error})

        b = Trending(txt=txt)
        b.save()

    #-# Trending List for Admin Panel Start #-#
    trendinglist = Trending.objects.all()
    #-# Trending List for Admin Panel Start #-#

    return render(request, 'back/trending.html', {'trendinglist':trendinglist})
###---#---### Trending Add Function For Back (Admin Panel - Backend) End ####--#--####