from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importa os dados necessários  de serializer e model
from controle.models.tarefa import Tarefa
from controle.serializers.tarefaSerializers import TarefaSerializer


# Cria a classe TarefaDetalheView
class TarefaDetalheView(APIView):
    """
    Retrieve, update or delete a category instance.
    """
    # Realiza o chamado do codigo e verifica se ele existe ou não
    def get_object(self, id):
        try:
            return Tarefa.objects.get(id=id)
        except Tarefa.DoesNotExist:
            raise Http404

    # Busca o objeto serializado para alterações
    def get(self, request, id, format=None):
        tarefa = self.get_object(id)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)

    # Faz alteração em cima do codigo chamado enviando as mudanças
    def put(self, request, id, format=None):
        tarefa = self.get_object(id)
        serializer = TarefaSerializer(tarefa,data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Deleta o codigo chamado através do GET
    def delete(self, request, id, format=None):
        tarefa = self.get_object(id)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)