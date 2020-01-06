from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Team
from allauth.account.forms import SignupForm, LoginForm

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=30, label='Username')
    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)
        
        user.username = self.cleaned_data['username']
        user.save()
        return user

class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        self.fields['login'].label = 'Email or Username'

class TeamCreationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']

class TeamJoiningForm(forms.Form):
    teamId = forms.CharField(label="Team ID", max_length=9, min_length=9)