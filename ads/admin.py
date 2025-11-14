from django.contrib import admin
from .models import UserProfile, Ad

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_type', 'rating']
    list_filter = ['user_type']

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'ad_type', 'owner', 'category', 'budget', 'is_active']
    list_filter = ['ad_type', 'category', 'is_active']