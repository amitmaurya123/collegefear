from django import forms
from basic_app.models import Exam,UserProfileInfo
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils.safestring import mark_safe
class ExamForm(forms.ModelForm):
    professor = forms.CharField(required=False,max_length=200,widget=forms.TextInput(attrs={'pattern':'[A-Za-z-_:\s]+', 'title':'Only alphanumeric characters - _ : and spaces are allowed'}))
    subject = forms.CharField(required=True,max_length=200)
    class Meta():
        model=Exam
        fields=('college','branch','semester','type','subject','professor','sessional','year','file')
        #widgets = {'name': forms.HiddenInput()}



class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=False)

    class Meta():
        model=User
        fields=('username','first_name','last_name','email','password')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email,is_active=True).exclude(username=username).exists():
            raise forms.ValidationError(((mark_safe('<div class="alert alert-danger alert-dismissibl fade in"><a href='' class="close" data-dismiss="alert" aria-label="close">&times;</a>An account already exists for this email address.</div>'))))
        return email

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('college','branch','semester')
