from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
# class CustomAccountManager(BaseUserManager):

#     def create_superuser(self,email,user_name,password,**other_fields):

#         other_fields.setdefault('is_staff',True)
#         other_fields.setdefault('is_superuser',True)
#         other_fields.setdefault('is_active',True)

#         if other_fields.get('is_staff') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_staff=True'
#             )
#         if other_fields.get('is_superuser') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_superuser=True'
#             )
#         return self.create_user(email,user_name,password,**other_fields)

#     def create_user(self,email,user_name,password,**other_fields):

#         if not email:
#             raise ValueError(_('You must provide an email adress'))
        
#         email = self.normalize_email(email)
#         user = self.model(email=email,user_name=user_name,**other_fields)
#         user.set_password(password)
#         user.save()
#         return user


# class NewUser(AbstractBaseUser,PermissionsMixin):

#     email = models.EmailField(_('email adress'),unique=True)
#     user_name = models.CharField(max_length=120,unique=True)
#     start_date = models.DateTimeField(default=timezone.now)
#     about = models.TextField(_('about'),max_length=700,blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)

#     objects = CustomAccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['user_name']

#     def __str__(self):
#         return self.user_name

options = (
        ('part-time','Part-time'),
        ('full-time','Full-time')
    )
class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name='profiles',null=True ,on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    location = models.CharField(max_length=300)
    experience = models.CharField(max_length=10)
    contract = models.CharField(max_length=20,choices=options,default='Full-time')
    bio = models.TextField(blank=False)
    date_joined = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to = 'media/',blank=True)

    def __str__(self):
        return self.full_name

# total profiles
    @classmethod
    def total_profiles(cls):
        return cls.objects.count()


class Comment(models.Model):
    profile = models.ForeignKey(Profile,related_name='profile_comment',on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # pub_date = models.DateField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.profile.full_name





