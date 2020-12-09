from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from .models import *

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=80)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email')
class PostForm(forms.ModelForm):
    picture = CloudinaryField('image')

    class Meta:
        model = Post
        fields = ('picture', 'quantity', 'description',) 

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'location', 'image', 'order')
  class Catalogue(models.Model):
        quantity= models.CharField(max_length=250)
        location = models.CharField(max_length=250)
        orders = models.IntegerField(default=0)
        image = CloudinaryField('Profile pic', null=True, blank=True)
        admin = models.ForeignKey(User, on_delete=models.CASCADE)

        def __str__(self):
            return f'{self.name} catalogue'

        def save_neighborhood(self):
            self.save()

        def delete_neighborhood(self):
            self.delete()

