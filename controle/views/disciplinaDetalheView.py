from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importa os dados necessários  de serializer e model
from controle.models.disciplina import Disciplina
from controle.serializers.disciplinaSerializers import DisciplinaSerializer

# Cria a classe DiscplinaDetalheView para criar os metodos
class DisciplinaDetalheView(APIView):
    # Faz a busca de um objeto verificando se ele existe ou não
    def get_object(self, id):
        try:
            return Disciplina.objects.get(id=id)
        except Disciplina.DoesNotExist:
            raise Http404
    # Busca e serializa um objeto a ser atualizado
    def get(self, request, id, format=None):
        disciplina = self.get_object(id)
        serializer = DisciplinaSerializer(disciplina)
        return Response(serializer.data)
    # Faz a alteração em cima do objeto a selecionado
    def put(self, request, id, format=None):
        disciplina = self.get_object(id)
        serializer = DisciplinaSerializer(disciplina, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Realiza a exclusão de um objeto em especifico
    def delete(self, request, id, format=None):
        disciplina = self.get_object(id)
        disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)