import uuid
from django.db import models
from django.utils import timezone
#from stdimage.models import StdImageField

def get_image_path(_instance, imagename):
    ext = imagename.split('-')[-1]
    imagename = f'{uuid.uuid4()}.{ext}'
    return imagename

# Create your models here.


class matricula(models.Model):
    PLANO_CHOICES = (
        ("1", "Musculação"),
        ("2", "Cross"),
        ("3", "Musculação + Cross")

    )
    SEXO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("O", "Outros"),
        ("NI", "Não Informado")

    )
    nome = models.CharField(max_length=40, blank=False, verbose_name="Nome do Cliente")  #unique = True - O valor é único e não pode ser repetido
    cpf = models.CharField(max_length=14, null=True, blank=True, unique=True, verbose_name="CPF")
    email = models.EmailField(max_length=40, blank=False, unique=True, verbose_name="Email")
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=3, null=True, blank=False, verbose_name="Sexo")
    telefone = models.CharField(max_length=15, blank=False, null=True, verbose_name="Telefone")
    endereco = models.CharField(max_length=240, blank=False, null=False, verbose_name="Endereço")
    data_da_matricula = models.DateField(auto_now_add=True, verbose_name="Data da Matricula")
    data_de_vencimento = models.DateField(blank=False, null=False, verbose_name='Vencimento')
    foto_aluno= models.ImageField(blank=True, null=True, verbose_name="Foto do Aluno", upload_to='alunos')
    plano = models.CharField(max_length=2, null=False, blank=False, choices=PLANO_CHOICES, verbose_name="Plano")
    valor = models.CharField(max_length=6, null=False, blank=False, verbose_name="Subtotal")
    desconto = models.CharField(max_length=5, null=False, blank=True, verbose_name="Desconto")
    valor_total = models.CharField(max_length=6, null=False, blank=False, verbose_name="Valor da Mensalidade", editable=False)
    num_matricula = models.AutoField(primary_key=True, blank=False, null=False, unique=True, verbose_name="Número da Matricula")
    observacoes = models.TextField(max_length=512, blank=True, null=True, verbose_name="Obeservações")

    #class Meta:
        #verbose_name = 'Matricula'
        #verbose_name_plural = 'Matriculas'

    def __str__(self):
        return f' {self.nome}'

    def save(self, *args, **kwargs):
        self.valor_total = self.valor - self.desconto
        return super(matricula, self).save(*args, **kwargs)

#############################Avaliação#########################################

class avaliacao(models.Model):
    nome = models.ForeignKey('matricula', on_delete=models.DO_NOTHING, default=1, verbose_name="Aluno")
    idade = models.DecimalField(max_digits=2, decimal_places=0, null=False, blank=False, verbose_name="Idade")
    altura = models.DecimalField(max_digits=3, decimal_places=2, null=False, blank=False, verbose_name="altura")
    imc = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False, verbose_name="IMC")
    cintura = models.DecimalField(max_digits=3, decimal_places=0, null=False, blank=False, verbose_name="Circunferência Cintura (cm)")
    quadril = models.DecimalField(max_digits=3, decimal_places=0, null=False, blank=False, verbose_name="Circunferência Quadril (cm)")
    rcq = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False, verbose_name="RCQ")
    d3 = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False, verbose_name="Subescapular")
    d1 = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False, verbose_name="Tricipital")
    d4 = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False, verbose_name="Peitoral")
    d5 = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False, verbose_name="Axilar Média")
    d6 = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False, verbose_name="Supra-Ilíaca")
    d7 = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False, verbose_name="Cutânea Abdominal")
    d8 = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False, verbose_name="Femural Médio")
    gordura = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False, verbose_name="% de Gordura")

    def __str__(self):
        return f' {self.nome}'




class ficha_de_saude(models.Model):
    VERDADEIRO_CHOICES = (
        ("S", "Sim"),
        ("N", "Não"),
        ("NI", "Não Informado")
    )
    nome = models.ForeignKey('matricula', on_delete=models.DO_NOTHING, default=1, verbose_name="Aluno")
    #matricula =
    diabetes = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Diabetes")
    hipertensao = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Hipertensão")
    artrite = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Artrite")
    artrose = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Artrose")
    reumatismo = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Reumatismo")
    doencas_cardiacas = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Doenças Cardiacas")
    avc = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Já Sofreu AVC")
    fuma = models.CharField(max_length=2, choices=VERDADEIRO_CHOICES, blank=False, null=True, verbose_name="Tabagismo")
    BEBIDA_CHOICES = (
        ("S", "Sempre que Posso"),
        ("O", "Ocasionalmente"),
        ("R", "Raramente"),
        ("N", "Não Bebo")
    )
    bebe = models.CharField(max_length=1, choices=BEBIDA_CHOICES, blank=False, null=True, verbose_name="Bebe")
    #personal = models.ForeignKey('personal', on_delete=models.DO_NOTHING, default=1, verbose_name='Personal Responsável')

    def __str__(self):
        return f'{self.nome}'


class medicamento(models.Model):
    TRUE_CHOICES = (
        ("S", "Sim"),
        ("N", "Não")
    )
    nome = models.ForeignKey('matricula', on_delete=models.DO_NOTHING, default=1, verbose_name='Aluno')
    insulina=models.CharField(max_length=2, choices=TRUE_CHOICES, null=False, blank=False, verbose_name="Insulina")
    antidepressivos=models.CharField(max_length=2, choices=TRUE_CHOICES, null=False, blank=False, verbose_name="Antidepressivos")
    antihistaminicos=models.CharField(max_length=2, choices=TRUE_CHOICES, null=False, blank=False, verbose_name="Anti-Histaminicos (Alergia)")
    betabloqueadores=models.CharField(max_length=2, choices=TRUE_CHOICES, null=False, blank=False, verbose_name="Betabloqueadores (Hipertensão)")
    analgesicos=models.CharField(max_length=2, choices=TRUE_CHOICES, null=False, blank=False, verbose_name="Analgésicos")
    ansiolitico=models.CharField(max_length=2, choices=TRUE_CHOICES, null=False, blank=False, verbose_name="Ansiolítico (Ansiedade)")
    suplementos_vit=models.CharField(max_length=2, choices=TRUE_CHOICES, null=False, blank=False, verbose_name="Suplementos Vitamínicos")
    observacoes = models.TextField(max_length=140, null=True, blank=True, verbose_name="Observações")
    #personal = models.ForeignKey('personal', on_delete=models.DO_NOTHING, default=1, verbose_name='Personal Responsável')

    def __str__(self):
        return f'{self.nome}'

####Exercícios

class cadastrar_exercicio(models.Model):
    exercicio = models.CharField(max_length=32, null=False, blank=False,verbose_name='Exercicio')


    def __str__(self):
        return f'{self.exercicio}'



###Treino


class treinoA(models.Model):
    nome = models.ForeignKey('matricula', on_delete=models.DO_NOTHING, default=None, verbose_name="Aluno")
    aexc_1 = models.CharField(max_length=32, blank=False, null=False, verbose_name='A1')
    rep1 = models.CharField(max_length=6, blank=False, null=False, verbose_name='RP')
    aexc_2 = models.CharField(max_length=32, blank=False, null=False, verbose_name='A2')
    rep2 = models.CharField(max_length=6, blank=False, null=False, verbose_name='RP')
    aexc_3 = models.CharField(max_length=32, blank=False, null=False, verbose_name='A3')
    rep3 = models.CharField(max_length=6, blank=False, null=False, verbose_name='RP')
    aexc_4 = models.CharField(max_length=32, blank=False, null=False, verbose_name='A4')
    rep4 = models.CharField(max_length=6, blank=False, null=False, verbose_name='RP')
    aexc_5 = models.CharField(max_length=32, blank=False, null=False, verbose_name='A5')
    rep5 = models.CharField(max_length=6, blank=False, null=False, verbose_name='RP')
    aexc_6 = models.CharField(max_length=32, blank=False, null=False, verbose_name='A6')
    rep6 = models.CharField(max_length=6, blank=False, null=False, verbose_name='RP')
    aexc_7 = models.CharField(max_length=32, blank=False, null=False, verbose_name='A7')
    rep7 = models.CharField(max_length=6, blank=False, null=False, verbose_name='RP')
    aexc_8 = models.CharField(max_length=32, blank=False, null=False, verbose_name='A8')
    rep8 = models.CharField(max_length=6, blank=False, null=False, verbose_name='RP')
    aexc_9 = models.CharField(max_length=32, blank=False, null=False, verbose_name='A9')
    rep9 = models.CharField(max_length=6, blank=False, null=False, verbose_name='RP')
    aexc_10 = models.CharField(max_length=32, blank=True, null=False, verbose_name='A10')
    rep10 = models.CharField(max_length=6, blank=True, null=False, verbose_name='RP')
    aexc_11 = models.CharField(max_length=32, blank=True, null=False, verbose_name='A11')
    rep11 = models.CharField(max_length=6, blank=True, null=False, verbose_name='RP')
    aexc_12 = models.CharField(max_length=32, blank=True, null=False, verbose_name='A12')
    rep12 = models.CharField(max_length=6, blank=True, null=False, verbose_name='RP')

    def __str__(self):
        return f'{self.nome}'


###Frequencia
class frequencia(models.Model):
    nome = models.ForeignKey('matricula', on_delete=models.CASCADE, default=None, null=True, related_name='aluno', verbose_name='Aluno')
    entrada = models.TimeField(auto_now_add=False, null=False, blank=False, verbose_name='Entrada')
    saida = models.TimeField(auto_now_add=False, null=True, blank=True, verbose_name='Saída')
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome}'





