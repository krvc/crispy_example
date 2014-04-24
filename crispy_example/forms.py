from django import forms


class SimpleForm(forms.Form):
    user_name = forms.CharField(label='Username', required=True)
    password = forms.CharField(label='Password', required=True,
                               widget=forms.PasswordInput)
