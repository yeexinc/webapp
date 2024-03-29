from django import forms
from django.forms import ModelForm

from .models import User, Post

#VERY IMPORTANT
#http://stackoverflow.com/questions/2010747/empty-request-files-with-django-upload-forms
"""
class PostForm_2(forms.Form):
    postid = forms.CharField(max_length=100)
    sitename = forms.CharField(max_length=50)
    siteusername = forms.CharField(max_length=50)
    email = forms.EmailField()
    url = forms.URLField()
    usage = forms.CharField(max_length=50)
    category = forms.CharField(max_length=50)
    description = forms.CharField(max_length=100)
    vis = forms.CharField(max_length=50)
    logo = forms.ImageField()
"""


"""
    PostForm
    - Form used for both inserting and editing posts.
    - Based on the Post object.
    (See also: models.py)
"""
class PostForm(ModelForm):
    postid = forms.CharField(max_length=100)
    class Meta:
        model = Post
        fields = ['sitename', 'siteusername', 'email', 'url', 'category', 'description', 'usage', 'vis', 'logo']
        exclude = ['category']
        labels = {
            'sitename': 'Site name',
            'siteusername': 'Username',
            'vis' : 'Visibility',
        }
        widgets = {
            'sitename': forms.TextInput(attrs={'list': 'sitenamelist', 'autocomplete': 'off'}),
            'vis': forms.RadioSelect(attrs={'class': 'radiobutton'}),
            'usage': forms.RadioSelect(attrs={'class': 'radiobutton'}),
        }

"""
class AccountForm_2(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'value': 'your username'}))
    password = forms.CharField(max_length=50)
    email = forms.EmailField()
    displayname = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)
    vis = forms.CharField(max_length=50)
    profileImg = forms.ImageField() #change to imagefield?
    bgImg = forms.CharField(max_length=200)   #change to imagefield?
    useBg = forms.CharField(max_length=50)
"""

"""
    AccountForm
    - Form used for the settings page to edit the user's account settings.
    - Based on the User object.
    (See also: models.py)
"""
class AccountForm(ModelForm):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(), label='Password (required)')
    new_password = forms.CharField(max_length=50, required=False, widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'displayname', 'description', 'vis', 'profileImg', 'bgImg', 'useBg']
        exclude = ['profileImg', 'bgImg', 'useBg']
        labels = {
            'vis' : 'Visibility',
            'profileImg' : 'Profile image',
            'bgImg' : 'Background image',
            'useBg' : 'Enable background',
        }
        widgets = {
            'vis': forms.RadioSelect(attrs={'class': 'radiobutton'}),
        }
