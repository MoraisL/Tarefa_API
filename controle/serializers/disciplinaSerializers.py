from rest_framework import serializers
from controle.models.disciplina import Disciplina

#Cria um campo selecionando os arquivos a serem serializados
class DisciplinaSerializer(serializers.ModelSerializer):
    #Ferramenta de metaclasse que permite personalizar o comportamento de uma classe antes mesmo de ela ser criada
    class Meta:
        #Campos a serem uilizados no serializer
        model = Disciplina
        fields = ['nome', 'descricao']