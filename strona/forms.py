from django import forms
from .models import Main, About_us, Blog, Post, Contact, ContactForm
from captcha.fields import CaptchaField

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['Title', 'Description', 'Photo', 'Left', 'Right']

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['Title', 'Description', 'Photo', 'Left', 'Right', 'Middle', 'Empty']


class AboutUsForm(forms.ModelForm):

    class Meta:
        model = About_us
        fields = ['Title', 'Description', 'Photo', 'Left', 'Right']



class DataForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['Factory', 'Phone', 'Email']

class ContactFormForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = ContactForm
        fields = ['Name', 'Email', 'Phone', 'Subject', 'Message']

        widgets = {
            'Name': forms.TextInput(attrs={'placeholder': 'Imię i nazwisko', 'class': 'contactus'}),
            'Subject': forms.TextInput(attrs={'placeholder': 'Temat', 'class': 'contactus'}),
            'Phone': forms.TextInput(attrs={'placeholder': 'Numer telefonu', 'class': 'contactus'}),
            'Email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'contactus'}),
            'Message': forms.Textarea(attrs={'placeholder': 'Wiadomość', 'class': 'textarea', 'rows': 5}),
        }


class MainForm(forms.ModelForm):
    class Meta:
        model = Main
        exclude = ['Title', 'Description']