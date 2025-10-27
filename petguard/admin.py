from django.contrib import admin
from .models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'especie', 'raca', 'idade', 'status')
    list_filter = ('status', 'especie')
    search_fields = ('especie', 'raca')
