from django import forms

from .models import SgFlag

class SgFlagForm(forms.ModelForm):
    class Meta:
        model = SgFlag
        fields = ("qqnumber","email","flag",)
