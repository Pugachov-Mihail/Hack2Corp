from django import forms
from .models import Person, Office

class CreateUser(forms.ModelForm):
    username = forms.CharField(label="Логин", max_length=30)
    password = forms.CharField(label='Пароль', max_length=30)
    password2 = forms.CharField(label="Повтор пароля", max_length=30)
    first_name = forms.CharField(label="Имя", max_length=30)
    last_name = forms.CharField(label="Фамилия", max_length=30)
    office = forms.ModelChoiceField(queryset=Office.objects.all(), label='Подразделение', widget=forms.widgets.Select(attrs={'size':5}))

    class Meta:
        model = Person
        fields = (
            'username', 'password', 'password2',
            'first_name', 'last_name', 'office'
                  )