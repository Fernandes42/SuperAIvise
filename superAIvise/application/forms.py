from django import forms

class Video_form(forms.Form):
    number = forms.CharField(label='Phone Number',max_length=100, help_text="Please enter your phone number you want to be sent messages with")
    time = forms.IntegerField(label='Time in minutes', required=False,help_text="Please enter how long you want SuperAIvise to run for")
