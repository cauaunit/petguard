from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from petguard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/animais/', views.index, name='listar_animais'),
    path('add-animal/', views.add_animal, name='add_animal'),
    path("add_animal/<int:id>/", views.add_animal, name="editar_animal"),
    path('racas/<int:especie_id>/', views.racas_por_especie, name='racas_por_especie'),
    path('', include('petguard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
