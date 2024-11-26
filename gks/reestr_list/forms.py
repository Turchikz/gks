from .models import Register
from django.forms import ModelForm, TextInput, DateInput, Select, ModelChoiceField, CheckboxSelectMultiple
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import modelformset_factory


class Add_to_registerForm(ModelForm):

    class Meta:

        model = Register
        fields = '__all__'
        exclude=['id_numb', 'place', 'd_min', 'd_max', 'ed_izm', 
                 'pogr_val', 'impl_name', 'status', 'publish', 'author',
                 'place', 
                ]


Add_to_registerFormSet = modelformset_factory(
    Register, extra=1, form=Add_to_registerForm, 
)

