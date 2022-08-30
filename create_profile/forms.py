from django.forms import ModelForm
from django import forms

from .models import admit_card

class admitCardForm(ModelForm):

    class Meta:
        model = admit_card
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            
        }   
    def __init__(self, *args, **kwargs):
        super(admitCardForm, self).__init__(*args, **kwargs)
        self.fields['profile_image'].required = False
        self.fields['sign_image'].required = False
       