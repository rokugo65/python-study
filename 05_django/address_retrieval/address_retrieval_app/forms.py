from django import forms
 
class ZipCodeForm(forms.Form):
    zipCode = forms.CharField(max_length=150000)