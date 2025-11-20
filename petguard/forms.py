from django import forms

class PasswordRecoveryForm(forms.Form):
    username = forms.CharField(label="Usuário")
    cpf = forms.CharField(label="CPF", widget=forms.TextInput(attrs={"id": "cpf"}))
