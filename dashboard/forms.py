from django import forms
from events.models import *

class EmailForm(forms.Form):
    events = forms.ModelMultipleChoiceField(Event.objects.all(), widget=forms.CheckboxSelectMultiple(), label="Events")
    sender = forms.EmailField(max_length=100, required=False, label="Sender (optional)")
    subject = forms.CharField(max_length=100, label="Subject")
    message = forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":40}), label="Message/Body")
    attachments = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}) ,label="Attach Files", required=False)