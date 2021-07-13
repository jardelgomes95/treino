from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, TemplateView, FormView, DeleteView, View
from django.shortcuts import render
from .models import matricula, treinoA, frequencia, ficha_de_saude, medicamento, cadastrar_exercicio
from .forms import matriculaForm, frequencia_saida, frequencia_entrada
from easy_pdf.views import PDFTemplateResponseMixin
from django.http import HttpResponseRedirect



# Create your views here.
#def index(request):
    #return render(request, 'index.html')

class index(TemplateView):
    template_name = 'index.html'

class indexadmin(TemplateView):
    template_name = 'adminlte/pages/index.html'


class matriculaCreateView(CreateView):
    model = matricula
    form_class = matriculaForm
    template_name = 'cadastrar/matricula.html'


    def get_success_url(self):
        messages.success(self.request, 'Aluno cadastrada com suceso!')
        return reverse_lazy("listar_matricula")


class matriculaListView(ListView):
    model = matricula
    template_name = 'listar/matricula.html'
    paginate_by = 50
    ordering = '-pk'


class matriculaUpdateView(UpdateView):
    model = matricula
    template_name = 'atualizar/matricula.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Avaliação atualizada com sucesso!')
        return reverse_lazy('listar_matricula')

class matriculaDetailView(DetailView):
    model = matricula
    template_name = 'detalhar/matricula.html'

class matriculaPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = matricula
    template_name = 'detalhar/matriculapdf.html'





class matriculaDeleteView(DeleteView):
    model = matricula
    template_name = 'excluir/matricula.html'

    def get_success_url(self):
        messages.success(self.request, 'Aluno excluído com Sucesso!')




#################TREINO##########################

class treino(CreateView):
    model = treinoA
    template_name = 'cadastrar/treino.html'
    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Treino cadastrado Sucesso!')
        return reverse_lazy("listar_treino")


class treinoListView(ListView):
    model = treinoA
    template_name = 'listar/treino.html'
    paginate_by = 100
    ordering = '-pk'


class treinoUpdateView(UpdateView):
    model = treinoA
    template_name = 'atualizar/treino.html'
    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Treino atualizado Sucesso!')
        return reverse_lazy("listar_treino")


class treinoDeleteView(DeleteView):
    model = treinoA
    template_name = 'excluir/treino.html'

    def get_success_url(self):
        messages.success(self.request, 'Treino excluido Sucesso!')
        return reverse_lazy("listar_treino")



class treinoDetailView(DetailView):
    model = treinoA
    template_name = 'detalhar/treino.html'

class treinoPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = treinoA
    template_name = 'detalhar/treinopdf.html'



##########FREQUENCIA#################

class frequenciaCreateview(CreateView):
    model = frequencia
    form_class = frequencia_entrada
    template_name = 'cadastrar/frequencia.html'


    def get_success_url(self):
        messages.success(self.request, 'Entrada adicionada com Sucesso!')
        return reverse_lazy("listar_frequencia")

class frequenciaListView(ListView):
    model = frequencia
    template_name = 'listar/frequencia.html'
    paginate_by = 1000
    ordering = '-pk'

class frequenciaUpdatesaida(UpdateView):
    model = frequencia
    form_class = frequencia_saida
    template_name = 'atualizar/frequencia.html'

    def get_success_url(self):
        messages.success(self.request, 'Saída adicionada com Sucesso!')
        return reverse_lazy("listar_frequencia")

class frequenciaDeleteView(DeleteView):
    model = frequencia
    template_name = 'excluir/frequencia.html'

    def get_success_url(self):
        messages.success(self.request, 'Aluno excluído com Sucesso!')
        return reverse_lazy("listar_frequencia")


#######Exercicio###########



class exercicioCreateView(CreateView):
    model = cadastrar_exercicio
    template_name = 'cadastrar/exercicio.html'
    fields = '__all__'


    def get_success_url(self):
        messages.success(self.request, 'exercicio cadastrado com Sucesso!')
        return reverse_lazy("cadastrar_exercicio")

class exercicioListView(ListView):
    model = cadastrar_exercicio
    template_name = 'listar/exercicio.html'
    paginate_by = 100
    ordering = '-pk'

class exercicioDeleteView(DeleteView):
    model = cadastrar_exercicio
    template_name = 'excluir/exercicio.html'

    def get_success_url(self):
        messages.success(self.request, 'Aluno excluído com Sucesso!')
        return reverse_lazy("listar_exercicio")
