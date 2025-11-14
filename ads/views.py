from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import Ad, UserProfile
from .forms import AdForm, SimpleRegisterForm

def home(request):
    return render(request, 'ads/home.html')

def buy_ads(request):
    ads = Ad.objects.filter(ad_type='sell', is_active=True)
    return render(request, 'ads/buy_ads.html', {'ads': ads})

def sell_ads(request):
    ads = Ad.objects.filter(ad_type='buy', is_active=True)
    return render(request, 'ads/sell_ads.html', {'ads': ads})

@login_required
def my_ads(request):
    user_profile = UserProfile.objects.get(user=request.user)
    my_ads = Ad.objects.filter(owner=user_profile)
    return render(request, 'ads/my_ads.html', {'my_ads': my_ads})

@login_required
def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.owner = UserProfile.objects.get(user=request.user)
            ad.save()
            messages.success(request, 'Объявление успешно создано!')
            return redirect('my_ads')
    else:
        form = AdForm()
    return render(request, 'ads/create_ad.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = SimpleRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('home')
    else:
        form = SimpleRegisterForm()
    return render(request, 'ads/register.html', {'form': form})

def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, is_active=True)
    return render(request, 'ads/ad_detail.html', {'ad': ad})