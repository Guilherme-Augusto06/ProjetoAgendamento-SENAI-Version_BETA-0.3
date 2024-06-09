from django import forms
from .models import Salas, Agendamentos
from django.utils import timezone
from django.contrib.auth.models import User

class formCadastroUsuario(forms.Form):
    first_name = forms.CharField(label="Nome", max_length=40)
    last_name = forms.CharField(label="Sobrenome", max_length=40)
    user = forms.CharField(label="Usuário", max_length=40)   
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

class FormLogin(forms.Form):
    user = forms.CharField(label="Usuario", max_length=40)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

class SalaForm(forms.ModelForm):
    class Meta:
        model = Salas
        fields = ['salas', 'descricao', 'equipamentos']

class FormAgendamentosSala(forms.ModelForm):
    class Meta:
        model = Agendamentos
        fields = ['sala', 'dia_da_semana', 'periodo', 'agendado_por']
    
    def clean(self):
        cleaned_data = super().clean()
        sala = cleaned_data.get('sala')
        dia_da_semana = cleaned_data.get('dia_da_semana')
        periodo = cleaned_data.get('periodo')

        if Agendamentos.objects.filter(sala=sala, dia_da_semana=dia_da_semana, periodo=periodo).exists():
            raise forms.ValidationError("Este período já está agendado para esta sala.")
        
        return cleaned_data

class AdicionarSalaForm(forms.ModelForm):
    class Meta:
        model = Salas
        fields = ['salas', 'descricao', 'equipamentos']
