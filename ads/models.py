from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    USER_TYPES = (
        ('advertiser', 'Рекламодатель'),
        ('publisher', 'Веб-мастер'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='advertiser')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    rating = models.FloatField(default=5.0)

    def __str__(self):
        return f"{self.user.username} ({self.user_type})"

class Ad(models.Model):
    AD_TYPES = (
        ('buy', 'Купить рекламу'),
        ('sell', 'Продать рекламу'),
    )
    
    CATEGORY_CHOICES = (
        ('tech', 'Технологии'),
        ('sports', 'Спорт'),
        ('entertainment', 'Развлечения'),
        ('news', 'Новости'),
        ('education', 'Образование'),
        ('business', 'Бизнес'),
        ('other', 'Другое'),
    )
    
    ad_type = models.CharField(max_length=10, choices=AD_TYPES)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    budget = models.DecimalField(max_digits=10, decimal_places=2, help_text="Бюджет или цена")
    contact_info = models.CharField(max_length=200, help_text="Контактная информация")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_ad_type_display()}: {self.title}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()