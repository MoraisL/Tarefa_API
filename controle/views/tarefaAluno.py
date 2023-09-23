from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importa os dados necessários  de serializer e model
from controle.serializers.tarefaSerializers import TarefaSerializer
from controle.models.tarefa import Tarefa

# Cria a classe view para Tarefa junto aos dados do Aluno
class TarefaAlunoView(APIView):
    # Realiza o chamado da tarefa filtrando por id do Aluno, ambos serializados
    def get(self, request, id, format=None):
        tarefa = Tarefa.objects.filter(aluno_id=id)
        serializer = TarefaSerializer(tarefa, many=True)
        return Response(serializer.data)
