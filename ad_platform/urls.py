from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from ads import views as ads_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ads_views.home, name='home'),
    path('buy/', ads_views.buy_ads, name='buy_ads'),
    path('sell/', ads_views.sell_ads, name='sell_ads'),
    path('my-ads/', ads_views.my_ads, name='my_ads'),
    path('create-ad/', ads_views.create_ad, name='create_ad'),
    path('ad/<int:ad_id>/', ads_views.ad_detail, name='ad_detail'),
    path('register/', ads_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='ads/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)