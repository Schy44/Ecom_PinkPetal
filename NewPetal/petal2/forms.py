from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class signupForm(UserCreationForm):
    password2 = forms.CharField(label='confirm Password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  ]


class InvoiceForm(forms.Form):
    invoice_date = forms.DateField()
    due_date = forms.DateField()
    total_amount = forms.DecimalField()
