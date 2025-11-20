from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_animal, name='add_animal'),
    path('add/<int:id>/', views.add_animal, name='edit_animal'),
    path('detalhes/<int:id>/', views.detalhes, name='detalhes'),
    path('excluir/<int:animal_id>/', views.excluir_animal, name='excluir_animal'),
    path('perfil/', views.perfil, name='perfil'),
    path('veterinario/<int:animal_id>/', views.veterinario_view, name='veterinario'),
    path('racas/<int:especie_id>/', views.racas_por_especie, name='racas_por_especie'),
    path('animal/<int:animal_id>/', views.veterinario_view, name='veterinario'),
    path('medicacao/<int:pk>/deletar/', views.deletar_medicacao, name='deletar_medicacao'),
    path('editar_medicacao/<int:medicacao_id>/', views.editar_medicacao, name='editar_medicacao'),
    path('recover_passoword/', views.recover_password, name='recuperar_senha')
]
