from django.contrib import admin

from django.contrib import admin
from .forms import matriculaForm

from .models import matricula, avaliacao, medicamento, ficha_de_saude, cadastrar_exercicio, treinoA

class matriculaadmin(admin.ModelAdmin):
    form = matriculaForm

admin.site.register(matricula, matriculaadmin)
admin.site.register(medicamento)
admin.site.register(ficha_de_saude)
admin.site.register(cadastrar_exercicio)
admin.site.register(treinoA)
admin.site.register(avaliacao)
#admin.site.register()