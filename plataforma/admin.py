from django.contrib import admin
from .models import DiasVisitas, Horario, Imovel, Cidade, Image, Visitas



@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('rua', 'valor', 'quartos', 'tamanho', 'cidade', 'tipo',)
    list_editable = ('cidade', 'tipo',)
    list_filter = ('cidade', 'tipo',)
    
admin.site.register(DiasVisitas)
admin.site.register(Horario)
admin.site.register(Image)
admin.site.register(Cidade)
admin.site.register(Visitas)
