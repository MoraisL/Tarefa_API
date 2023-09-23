from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Importa os dados necessários  de serializer e model
from controle.models.aluno import Aluno
from controle.serializers.alunoSerializers import AlunoSerializers


#Criação da classe AlunoView para realização dos metodos
class AlunoView(APIView):
    # Realiza o chamado do item Aluno para que ele possa ser serializado
    def get(self, request, format=None):
        disciplina = Aluno.objects.all()
        serializer = AlunoSerializers(disciplina, many=True)
        return Response(serializer.data)
    # Realiza a criação de um aluno
    def post(self, request, format=None):
        serializer = AlunoSerializers(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)