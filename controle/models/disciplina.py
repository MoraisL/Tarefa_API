from django.db import models

# Criação da classe pra inserção de seus atributos
class Disciplina(models.Model):
    nome = models.CharField(max_length=30, null=False)# Descreve o modelo do atributo nome da disciplina
    descricao = models.TextField()# Descreve o modelo do atributo descrição da disciplina

    def _str_(self) -> str:# Retorna a disciplina criada
        return super().__str__()