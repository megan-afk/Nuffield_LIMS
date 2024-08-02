from django import forms
from .models import Sample, Extraction
from django.forms import ModelForm, TextInput



class Sample(forms.ModelForm):

    class Meta:
        model = Sample
        fields = ['sample_name', 'taxon_id', 'scientific_name', 'common_name', 'date_collected', 'Sample_Img']
        widgets = {
            'sample_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
            'taxon_id': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
            'scientific_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
            }),
            'common_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
            }),
            'date_collected': forms.DateTimeInput(attrs={
                'class':'form-control',
                'style': 'max-width: 400px;',
                'type': 'datetime-local',
            })
        }

class Extraction(forms.ModelForm):

    class Meta:
        model = Extraction
        fields = ['sample', 'extraction_name', 'extraction_date', 'extraction_method']
        widgets = {
            'sample': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
            }),
            'extraction_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                }),
            'extraction_date': forms.DateTimeInput(attrs={
                'class':'form-control',
                'style': 'max-width: 400px;',
                'type': 'datetime-local',
            }),
            'extraction_method': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
            })
        }