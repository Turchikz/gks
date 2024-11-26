from .models import Register
from django.forms import ModelForm, TextInput, DateInput, Select, ModelChoiceField, CheckboxSelectMultiple
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import modelformset_factory


class Add_to_registerForm(ModelForm):

    class Meta:

        model = Register
        fields = ['kind', 'descr',     'date', 
                  'id_numb',
                  'number',  
                  ]


Add_to_registerFormSet = modelformset_factory(
    Register, extra=2, fields=['kind', 'descr', 'date', 'id_numb',
                  'number', 
                  ], form=Add_to_registerForm, 
)

