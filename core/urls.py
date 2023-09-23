from django.urls import path
from controle.views.alunoView import AlunoView
from controle.views.alunoDetalheView import AlunoDetalheView
from controle.views.tarefaView import TarefaView
#from controle.views.tarefaAluno import TarefaAluno
from controle.views.tarefaDetalheView import TarefaDetalheView
from controle.views.disciplinaView import DisciplinaView
from controle.views.disciplinaDetalheView import DisciplinaDetalheView
from controle.views.tarefaAluno import TarefaAlunoView

# Caminhos(URLs) para encaminhar as APIViews
urlpatterns = [
    path('alunos/', AlunoView.as_view()),
    path('alunos/<int:id>/', AlunoDetalheView.as_view()),
    path('disciplinas/', DisciplinaView.as_view()),
    path('disciplinas/<int:id>/', DisciplinaDetalheView.as_view()),
    path('tarefas/', TarefaView.as_view()),
    path('tarefas/<int:id>/', TarefaDetalheView.as_view()),
    path('alunos/<int:id>/tarefas/', TarefaAlunoView.as_view())
]