from django.db import models
from django.utils import timezone

# Criação da classe pra inserção de seus atributos
class Aluno(models.Model):
    nome = models.CharField(max_length=100)# Descreve o modelo do atributo nome do aluno
    email = models.EmailField(unique=True, null=False)## Descreve o modelo do atributo email do aluno

def __srt__(self) -> str:#Retronando o usuario criado
        return "User [%i - %s]" % (self.id, self.user_name)