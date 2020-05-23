from django import forms

class Video_form(forms.Form):
    number = forms.IntegerField(label='Number')
