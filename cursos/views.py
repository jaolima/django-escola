# APIVIEW recebe a requisição
from rest_framework.views import APIView
# serve para retornar a responsta da requisição
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """
    API de cursos da Geek
    """

    def get(self, request):
        cursos = Curso.object.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)


class AvaliacaoAPIView(APIView):
    """
    API de cursos da Geek
    """

    def get(self, request):
        avaliacoes = Avaliacao.object.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
