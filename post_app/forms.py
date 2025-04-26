from django import forms
from .models import Post,Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class Login(AuthenticationForm):
    pass



class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username','password1','password2','email'
        ]

class CreatePost(forms.ModelForm):
    class Meta:
        model= Post
        fields = [
            'post'
        ]
        widgets = {
            'post': forms.Textarea(attrs={
                'placeholder': "What's on your mind?",
                'rows': 4,
                'class': 'post-textarea',
            })
        }

class UpdateUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email']

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class UpdateProfile(forms.ModelForm):
    class Meta:
        model= Profile
        fields = [
            'location', 'contact','profile_pic','user'
        ]
        def __init__(self, *args, **kwargs):
            super(UpdateProfile, self).__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs.update({'class': 'form-control'})