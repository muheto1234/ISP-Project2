from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import cop

User=get_user_model()
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields={'username','first_name','last_name','email'}

class modifierForm(forms.ModelForm):
    class Meta:
        model=cop
        fields=['motif','date_aller','date_retour']