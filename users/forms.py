from django import forms

class ResetPasswordForm(forms.Form):
    username = forms.CharField(max_length= 100)
    password_atual = forms.CharField(max_length= 50)
    nova_password = forms.CharField(max_length= 50)
    confirmacao_password = forms.CharField(max_length= 50)