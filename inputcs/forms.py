from django import forms
from . import models


class SheetForm(forms.ModelForm):
    class Meta:
        model = models.Sheet
        fields = [
            'location',
            'process',
            'defect',
            'period',
            'coorx',
            'coory',
            'photo',
            'side',
        ]
        widgets = {
            'coorx': forms.HiddenInput(),
            'coory': forms.HiddenInput(),
            'side': forms.HiddenInput(),
        }