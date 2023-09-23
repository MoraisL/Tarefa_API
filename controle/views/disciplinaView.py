from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importa os dados necessários  de serializer e model
from controle.models.disciplina import Disciplina
from controle.serializers.disciplinaSerializers import DisciplinaSerializer

# Realiza a criação da classe DisciplinaView para inserção dos metodos
class DisciplinaView(APIView):

    #Faz o chamado do objeto serializado para fazer a alteração
    def get(self, request, format=None):
        disciplina = Disciplina.objects.all()
        serializer = DisciplinaSerializer(disciplina, many=True)
        return Response(serializer.data)
    # Aplica as alterações em cima do objeto chamado
    def post(self, request, format=None):
        serializer = DisciplinaSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)