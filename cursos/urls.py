from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    CursoAPIView,
    AvaliacoesAPIView,
    CursosAPIView,
    AvaliacaoAPIView,
    CursoViewSet,
    AvaliacaoViewSet)


router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)


urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    # Pegar todas as avaliações de um determinado curso
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='cursos_avaliacoes'),
    # Pegar determinada avaliaçõe de determinado curso
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='cursos_avaliacao'),

    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
]

