from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Team
from allauth.account.forms import SignupForm as NormalSignupForm, LoginForm
import uuid
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.core.mail import send_mail

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
)

YEAR_CHOICES = (
    ('first_year', 'First Year'),
    ('second_year', 'Second Year'),
    ('third_year', 'Third Year'),
    ('fourth_year', 'Fourth Year'),
    ('fifth_year', 'Fifth Year')
)

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomSignupForm(NormalSignupForm):
    username = forms.CharField(max_length=30, label='Username')
    first_name = forms.CharField(max_length=50, label='First Name')
    last_name = forms.CharField(max_length=50, label='Last Name')
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender', initial='male')
    contact = forms.CharField(max_length=10, min_length=10, label='Contact')
    current_year = forms.ChoiceField(choices=YEAR_CHOICES, label='Current Year of Study', initial='first_year')
    college = forms.CharField(max_length=60, label='College Name')
    city = forms.CharField(max_length=40, label='City')
    join_referral = forms.CharField(max_length=8, min_length=8, required=False, label="Referral Code (optional)")
    ambassador = forms.BooleanField(label='Do you want to be a campus ambassador?', required=False, initial=False)
    
    field_order = ['username', 'email', 'first_name', 'last_name', 'contact', 'college', 'city', 'gender', 'current_year', 'password1', 'password2', 'join_referral', 'ambassador']
    
    def clean(self):
        cleaned_data = super(CustomSignupForm, self).clean()
        referral = cleaned_data['join_referral']
        if(cleaned_data['join_referral']):
            if(not CustomUser.objects.filter(invite_referral=referral).exists()):
                raise forms.ValidationError({'join_referral' : 'The referral code you have entered is incorrect.'})
        return cleaned_data
    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)
        
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.gender = self.cleaned_data['gender']
        user.contact = self.cleaned_data['contact']
        user.current_year = self.cleaned_data['current_year']
        user.college = self.cleaned_data['college']
        user.city = self.cleaned_data['city']
        user.ambassador = self.cleaned_data['ambassador']
        if(user.ambassador):
            user.invite_referral = 'CA' + str(uuid.uuid4().int)[:6]
        if(self.cleaned_data['join_referral']):
            user.referred_by = CustomUser.objects.get(invite_referral=self.cleaned_data['join_referral'])
        user.save()
        return user

class CustomSocialSignupForm(SocialSignupForm):

    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender', initial='male')
    contact = forms.CharField(max_length=10, min_length=10, label='Contact')
    current_year = forms.ChoiceField(choices=YEAR_CHOICES, label='Current Year of Study', initial='first_year')
    college = forms.CharField(max_length=60, label='College Name')
    city = forms.CharField(max_length=40, label='City')
    join_referral = forms.CharField(max_length=8, min_length=8, required=False, label="Referral Code (optional)")
    ambassador = forms.BooleanField(label='Do you want to be a campus ambassador?', required=False)

    field_order = ['email', 'username', 'contact', 'college', 'city', 'gender', 'current_year', 'join_referral', 'ambassador']

    def clean(self):
        cleaned_data = super(CustomSocialSignupForm, self).clean()
        referral = cleaned_data['join_referral']
        if(cleaned_data['join_referral']):
            if(not CustomUser.objects.filter(invite_referral=referral).exists()):
                raise forms.ValidationError({'join_referral' : 'The referral code you have entered is incorrect.'})
        return cleaned_data

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomSocialSignupForm, self).save(request)

        # Add your own processing here.
        user.gender = self.cleaned_data['gender']
        user.contact = self.cleaned_data['contact']
        user.current_year = self.cleaned_data['current_year']
        user.college = self.cleaned_data['college']
        user.city = self.cleaned_data['city']
        user.ambassador = self.cleaned_data['ambassador']
        if(user.ambassador):
            user.invite_referral = 'CA' + str(uuid.uuid4().int)[:6]
        if(self.cleaned_data['join_referral']):
            user.referred_by = CustomUser.objects.get(invite_referral=self.cleaned_data['join_referral'])
        user.save()

        
        # You must return the original result.
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

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'contact', 'college', 'city', 'gender', 'current_year']
  
class EditTeamForm(forms.ModelForm):

    # members = forms.ModelMultipleChoiceField(CustomUser.objects.all(), required=False)

    class Meta:
        model = Team
        fields = ['name', 'members']

    def __init__(self, team, *args, **kwargs):
        super(EditTeamForm, self).__init__(*args, **kwargs)
        self.fields['members'].queryset = team.members.all()