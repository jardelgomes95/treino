from django.urls import path
from .views import matriculaUpdateView, index, matriculaDetailView, matriculaCreateView,  matriculaListView, indexadmin
from .views import matriculaDeleteView, matriculaPDFDetailView, treino, frequenciaCreateview, frequenciaListView, frequenciaUpdatesaida, frequenciaDeleteView

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('matricula', matriculaCreateView.as_view(), name="matricula"),
    path('alunos', matriculaListView.as_view(), name="listar_matricula"),
    path('matricula/atualizar/<int:pk>', matriculaUpdateView.as_view(), name="atualizar_matricula"),
    path('matricula/detalhar/<int:pk>', matriculaDetailView.as_view(), name="detalhar_matricula"),
    #path('sistema', indexadmin.as_view(), name='sistem'),
    path('matricula/deletar/<int:pk>', matriculaDeleteView.as_view(), name="deletar_matricula"),
    path('matricula/pdf/<int:pk>', matriculaPDFDetailView.as_view(), name="pdf_matricula"),


    path('frequencia', frequenciaCreateview.as_view(), name="frequencia"),
    path('lista/frequencia', frequenciaListView.as_view(), name="listar_frequencia"),
    path('frequencia/atualizar/<int:pk>', frequenciaUpdatesaida.as_view(), name="saida"),
    path('frequencia/deletar/<int:pk>', frequenciaDeleteView.as_view(), name="deletar_frequencia"),


    path('treino', treino.as_view(), name="treino"),

]
