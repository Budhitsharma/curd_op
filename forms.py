from django.core import validators
from django import forms
from .models import Detailmodel
from django.core.exceptions import ValidationError


class Detailform(forms.ModelForm):
    class Meta:
        model = Detailmodel
        fields = ['name', 'email', 'contact', 'gender', 'birth_date', 'join_date', 'aadhar_no',
                 'pan_no', 'skype_id', 'linkedin_id', 'qualification', 'technology', 'perv_company',
                 'experience', 'acc_no', 'bank_name', 'acc_name', 'ifsc_code', 'role','image']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'contact': forms.NumberInput(attrs={'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control'}),
            'birth_date': forms.DateInput(attrs={'class':'form-control', 'type': 'date', 'format': '%Y-%m-%d'}),
            'join_date': forms.DateInput(attrs={'class':'form-control', 'type': 'date', 'format': '%Y-%m-%d'}),
            'aadhar_no': forms.NumberInput(attrs={'class':'form-control'}),
            'pan_no': forms.TextInput(attrs={'class':'form-control'}),
            'skype_id': forms.TextInput(attrs={'class':'form-control'}),
            'linkedin_id': forms.TextInput(attrs={'class':'form-control'}),
            'qualification': forms.TextInput(attrs={'class':'form-control'}),
            'technology': forms.TextInput(attrs={'class':'form-control'}),
            'perv_company': forms.TextInput(attrs={'class':'form-control'}),
            'experience': forms.NumberInput(attrs={'class':'form-control'}),
            'acc_no': forms.NumberInput(attrs={'class':'form-control'}),
            'bank_name': forms.TextInput(attrs={'class':'form-control'}),
            'acc_name': forms.TextInput(attrs={'class':'form-control'}),
            'ifsc_code': forms.TextInput(attrs={'class':'form-control'}),
            'role': forms.Textarea(attrs={'cols': 70, 'rows': 3}),
            # 'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}), 
            }

  

            