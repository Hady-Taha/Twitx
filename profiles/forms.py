from django import forms
from .models import Profile


class ProfileSetting(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo','firstName','lastName','bio',)
        pass
    
    pass
