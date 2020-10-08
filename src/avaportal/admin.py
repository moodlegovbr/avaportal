# from import_export.admin import ImportExportModelAdmin
from django.contrib.admin import register, ModelAdmin, TabularInline
from .models import Campus, Solicitacao

@register(Campus)
class CampusAdmin(ModelAdmin):
    list_display = ['sigla', 'descricao', 'descricao']
    search_fields = ['sigla', 'descricao', 'suap_id', 'url']


@register(Solicitacao)
class SolicitacaoAdmin(ModelAdmin):
    list_display = ['campus', 'status', 'timestamp']
    search_fields = ['campus', 'requisicao', 'requisicao_invalida', 'requisicao_header', 'resposta', 'resposta_header', 'resposta_invalida']
    autocomplete_fields = ['campus']
    date_hierarchy = 'timestamp'
    list_filter = ['status', 'campus']
