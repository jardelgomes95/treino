from django import forms
from django.core.mail.message import EmailMessage
from .models import matricula, avaliacao, treinoA, frequencia
from localflavor.br.forms import BRZipCodeField
from crispy_forms.bootstrap import InlineField
from django.core.exceptions import ValidationError


class matriculaForm(forms.ModelForm):
    class Meta:
        model = matricula
        fields = '__all__'



class avaliacaoForm(forms.ModelForm):
    class Meta:
        model = avaliacao
        fields = '__all__'


class frequencia_entrada(forms.ModelForm):
    class Meta:
        model = frequencia
        fields = ['nome', 'entrada']

class frequencia_saida(forms.ModelForm):
    class Meta:
        model = frequencia
        fields = ['nome', 'saida']




