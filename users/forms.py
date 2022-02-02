from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.forms.models import ModelForm
from .models import Profile, Message



class userRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    def __init__(self, *args, **kwargs):
        super(userRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class AccountForm(ModelForm):

    class Meta:
        model = Profile     
        exclude = ['user']

    
    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['intro'].widget.attrs['class'] = 'form-control'
        self.fields['biography'].widget.attrs['class'] = 'form-control'
        self.fields['skills'].widget.attrs['class'] = 'form-control'
        self.fields['other_skill'].widget.attrs['class'] = 'form-control'
        self.fields['location'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['instagram_link'].widget.attrs['class'] = 'form-control'
        self.fields['facebook_link'].widget.attrs['class'] = 'form-control'
        self.fields['linkedin_link'].widget.attrs['class'] = 'form-control'
        self.fields['youtube_link'].widget.attrs['class'] = 'form-control'
        self.fields['website_link'].widget.attrs['class'] = 'form-control'



class CreateAccountForm(ModelForm):

    class Meta:
        model = Profile     
        fields = ['user']
        

    def __init__(self, *args, **kwargs):
        super(CreateAccountForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'



class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = [  'senderName', 'email', 'subject', 'body']
        labels = {
            'senderName':'Name'
        }

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        self.fields['senderName'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['body'].widget.attrs['class'] = 'form-control'


