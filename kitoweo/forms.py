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
