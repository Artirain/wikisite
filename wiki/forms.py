from tkinter import Widget
from django import forms
from .models import Category
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User




class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
    attrs = {
        'class' : 'form-control',
        'autocomplete' : 'off',
        'placeholder': 'Имя пользователя'
        }))

    password = forms.CharField(widget=forms.PasswordInput(
    attrs = {
        'class' : 'form-control',
        'placeholder': 'Пароль'
        }))


class UserRegisterForm():
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
    attrs = {
        'class' : 'form-control',
        'autocomplete' : 'off'
        }))

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
    attrs = {
        'class' : 'form-control'
        }))

    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(
    attrs = {
        'class' : 'form-control'
        }))

    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(
    attrs = {
        'class' : 'form-control'
        }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
     

class WikiForm(forms.Form):
    title = forms.CharField(max_length=150,widget=forms.TextInput(
        attrs={
            'class' : 'form-input',
            'type' : 'text',
            'placeholder' : 'Название',
            }))
    content = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'class' : 'form-input',
            'type' : 'text',
            'placeholder' : 'Текст',
            'rows' : 7,
            })) #required - делает поле необязательным
    is_published = forms.BooleanField(label = 'Опубликовано', initial=True, widget = forms.CheckboxInput(
        attrs={
            'id': 'add-form-file',
            })) #по умолчанию заполнит поле

    category = forms.ModelChoiceField(empty_label= 'Выберите категорию', 
    queryset=Category.objects.all(), widget=forms.Select(
    attrs={
        'class' : 'add-form-select',
        'rows' : 7,
        }))

