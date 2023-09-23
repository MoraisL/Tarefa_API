from django.db import models
from controle.models.disciplina import Disciplina
from controle.models.aluno import Aluno

# Criação da classe pra inserção de seus atributos
class Tarefa(models.Model):
    titulo = models.CharField(max_length=30, null=False)# Descreve o modelo do atributo titulo da tarefa
    descricao = models.TextField()# Descreve o modelo do atributo descrição da tarefa
    dataEntrega = models.DateField(null=False)# Descreve o modelo do atributo de data de entrega da tarefa
    concluida = models.BooleanField(default=False)# Descreve o modelo do atributo se a tarefa esta concluida ou não
    aluno = models.ForeignKey(Aluno, related_name='tarefa', on_delete=models.CASCADE)# Descreve o modelo do atributo do aluno que está sendo buscado por tarefa
    disciplina = models.ManyToManyField(Disciplina, related_name='tarefa')# Descreve o modelo do atributo disciplina da tarefa

    # Retorna sua string
    def _str_(self) -> str: 
        return super().__str__()