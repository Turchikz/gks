from typing import Any
from django.contrib import admin
from .models import *
from import_export import resources



@admin.register(DescriptionType)
class DescriptionTypeAdmin(admin.ModelAdmin):
    list_display = ('date', 'link', 'number', 'producer',)
    list_display_links = ('number',)  # гиперссылки
    search_fields = ('number',)  # поиск
    list_filter = ('number',)  # фильтрация

@admin.register(Etalon)
class EtalonAdmin(admin.ModelAdmin):
    list_display = ('code', 'name_short',)
    list_display_links = ('code',)  # гиперссылки
    search_fields = ('code',)  # поиск
    list_filter = ('code',)  # фильтрация

    def name_short(self, obj: Etalon) -> str:
        if len(obj.name) < 70:
            return obj.name
        return obj.name[:70] + '...'

@admin.register(Modification)
class ModificationAdmin(admin.ModelAdmin):
    list_display = ('modif',)
    list_display_links = ('modif',)  # гиперссылки
    search_fields = ('modif',)  # поиск
    list_filter = ('modif',)  # фильтрация

@admin.register(Methodika)
class MethodikaAdmin(admin.ModelAdmin):
    list_display = ('method',)
    list_display_links = ('method',)  # гиперссылки
    search_fields = ('method',)  # поиск
    list_filter = ('method',)  # фильтрация

@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)  # гиперссылки
    search_fields = ('name',)  # поиск
    list_filter = ('name',)  # фильтрация

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner',)
    list_display_links = ('owner',)  # гиперссылки
    search_fields = ('owner',)  # поиск
    list_filter = ('owner',)  # фильтрация

@admin.register(Pover)
class PoverAdmin(admin.ModelAdmin):
    list_display = ('povername',)
    list_display_links = ('povername',)  # гиперссылки
    search_fields = ('povername',)  # поиск
    list_filter = ('povername',)  # фильтрация

@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ('place',)
    list_display_links = ('place',)  # гиперссылки
    search_fields = ('place',)  # поиск
    list_filter = ('place',)  # фильтрация

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username',)
    list_display_links = ('username',)  # гиперссылки
    search_fields = ('username',)  # поиск
    list_filter = ('username',)  # фильтрация

class EtalonInline(admin.StackedInline):
    model = Register.etalons.through

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):

    # inlines = [
    #     EtalonInline,
    # ]
    list_display = ('id_numb', 'date', 'number', 'descr', )
    list_display_links = ('number', 'id_numb', 'descr')  # гиперссылки
    search_fields = ('date', 'id_numb', 'descr',)  # поиск
    list_filter = ('date', 'descr',)  # фильтрация
    ordering = ('id_numb',)
    date_hierarchy = 'date'
    filter_horizontal = ['etalons']

    def get_queryset(self, request):
        return Register.objects.select_related('descr').prefetch_related('etalons')
