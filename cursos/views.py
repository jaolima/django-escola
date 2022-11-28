from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """
    API de Cursos
    """
    def get(self, request):
        cursos = Curso.objects.all()
        serializerCurso = CursoSerializer(cursos, many=True)
        return Response(serializerCurso.data)


class AvaliacaoAPIView(APIView):
    """
    API de Avaliações
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializerAvaliacao = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializerAvaliacao.data)
