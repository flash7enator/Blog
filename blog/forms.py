from django import forms
from django.contrib.auth.models import User

from .models import Post, Comment, Subscriber


class PostForm(forms.ModelForm):
    image= forms.ImageField(required=False)

    class Meta:
        model = Post
        exclude = ('user', 'published_date', 'slug')



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('post','user')


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'})
        }


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm')


    def clean(self):
        cleen_data = super().clean()
        password = cleen_data.get('password')
        password_confirm = cleen_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError("Passwords don't match")
        return cleen_data




