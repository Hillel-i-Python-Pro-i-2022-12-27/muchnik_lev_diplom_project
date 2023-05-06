from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше Имя*', max_length=100)
    phone = forms.CharField(label='Ваш Номер*', max_length=20)
    email = forms.EmailField(label='Ваша Почта', required=False)
