from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importa os dados necessários  de serializer e model
from controle.models.tarefa import Tarefa
from controle.serializers.tarefaSerializers import TarefaSerializer

# Cria a classe tarefa para implementar os metodos
class TarefaView(APIView):
    # Chama o metodo que chama o objeto serializado
    def get(self, request, format=None):
        disciplina = Tarefa.objects.all()
        serializer = TarefaSerializer(disciplina, many=True)
        return Response(serializer.data)

    # Cria um novo objeto de tarefa
    def post(self, request, format=None):
        serializer = TarefaSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)