from rest_framework import serializers
from controle.models.tarefa import Tarefa
from controle.models.aluno import Aluno
from controle.models.disciplina import Disciplina

#Cria um campo selecionando os arquivos a serem serializados
class TarefaSerializer(serializers.ModelSerializer):
    aluno = serializers.PrimaryKeyRelatedField(queryset=Aluno.objects.all())
    disciplina = serializers.PrimaryKeyRelatedField(queryset=Disciplina.objects.all() ,many=True)
    #Ferramenta de metaclasse que permite personalizar o comportamento de uma classe antes mesmo de ela ser criada
    class Meta:
        #Campos a serem uilizados no serializer
        model = Tarefa
        fields = ['titulo', 'descricao', 'dataEntrega', 'concluida', 'aluno', 'disciplina']