from django.contrib import admin
from django.urls import path
from .views import matriculaUpdateView, index, matriculaDetailView, matriculaCreateView,  matriculaListView
from .views import matriculaDeleteView, matriculaPDFDetailView, frequenciaCreateview, frequenciaListView, frequenciaUpdatesaida, frequenciaDeleteView
from .views import exercicioListView, exercicioCreateView, exercicioDeleteView
from .views import treinoDeleteView, treinoListView, treinoDetailView, treinoPDFDetailView,  treino, treinoUpdateView



urlpatterns = [
    path('', index.as_view(), name="index"),
    path('matricula', matriculaCreateView.as_view(), name="matricula"),
    path('alunos', matriculaListView.as_view(), name="listar_matricula"),
    path('matricula/atualizar/<int:pk>', matriculaUpdateView.as_view(), name="atualizar_matricula"),
    path('matricula/detalhar/<int:pk>', matriculaDetailView.as_view(), name="detalhar_matricula"),
    path('matricula/deletar/<int:pk>', matriculaDeleteView.as_view(), name="deletar_matricula"),
    path('matricula/pdf/<int:pk>', matriculaPDFDetailView.as_view(), name="pdf_matricula"),


    path('frequencia', frequenciaCreateview.as_view(), name="frequencia"),
    path('lista/frequencia', frequenciaListView.as_view(), name="listar_frequencia"),
    path('frequencia/atualizar/<int:pk>', frequenciaUpdatesaida.as_view(), name="saida"),
    path('frequencia/deletar/<int:pk>', frequenciaDeleteView.as_view(), name="deletar_frequencia"),


    path('exercicio', exercicioCreateView.as_view(), name="cadastrar_exercicio"),
    path('exercicios', exercicioListView.as_view(), name="listar_exercicio"),
    path('exercicio/<int:pk>', exercicioDeleteView.as_view(), name="deletar_exercicio"),


    path('treino', treino.as_view(), name="treino"),
    path('treinos', treinoListView.as_view(), name="listar_treino"),
    path('treino/atualizar/<int:pk>', treinoUpdateView.as_view(), name="atualizar_treino"),
    path('treino/detalhar/<int:pk>', treinoDetailView.as_view(), name="detalhar_treino"),
    path('treino/deletar/<int:pk>', treinoDeleteView.as_view(), name="deletar_treino"),
    path('treino/pdf/<int:pk>', treinoPDFDetailView.as_view(), name="pdf_treino"),
]
