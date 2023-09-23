from rest_framework import serializers
from controle.models.aluno import Aluno
from rest_framework.serializers import ModelSerializer

#Cria um campo selecionando os arquivos a serem serializados
class AlunoSerializers(serializers.ModelSerializer):
   #Ferramenta de metaclasse que permite personalizar o comportamento de uma classe antes mesmo de ela ser criada
   class Meta:
        model = Aluno
        #Campos a serem uilizados no serializer
        fields = ['nome', 'email']