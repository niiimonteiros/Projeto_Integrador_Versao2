from django.contrib import admin
from django.urls import path
from todos.views import home
from .views import listar_dados_turma

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]

urlpatterns = [
    path('dados-turma/<int:subtipo>/', listardadosturmaporsubtipo, name='listar_dados_turma'),
]
