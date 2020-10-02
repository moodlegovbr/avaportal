from django.utils.translation import gettext as _
from django.db.models import Model, ForeignKey, CASCADE, TextChoices
from django.db.models import CharField, URLField, ImageField, DateTimeField, TextField
from django.db.models import JSONField

class Campus(Model):
    suap_id = CharField('ID no SUAP', max_length=255, unique=True)
    sigla = CharField('Sigla', max_length=255, unique=True)
    descricao = CharField('Descrição', max_length=255)
    url = URLField('URL', max_length=255)
    thumbnail = ImageField('Sigla', max_length=255)

    class Meta:
        verbose_name = "Campus"
        verbose_name_plural = "Campi"
        ordering = ['sigla']

    def __str__(self):
        return f'{self.sigla} - {self.descricao}'


class Solicitacao(Model):
    class Status(TextChoices):
        SUCESSO = 'Sucesso', _('Sucesso')
        FALHA = 'Falha', _('Falha')
    timestamp = DateTimeField('Quando ocorreu', auto_now_add=False)
    requisicao = JSONField('Requisição', null=True, blank=True)
    requisicao_header = JSONField('Cabeçalho da requisição', null=True, blank=True)
    requisicao_invalida = TextField('Requisição inválida', null=True, blank=True)
    resposta = JSONField('Resposta', null=True, blank=True)
    resposta_header = JSONField('Cabeçalho da resposta', null=True, blank=True)
    resposta_invalida = TextField('Resposta inválida', null=True, blank=True)
    campus = ForeignKey(Campus, on_delete=CASCADE, verbose_name="Campus", null=True, blank=True)
    status = CharField(_("Kind"), max_length=255, choices=Status.choices, null=True, blank=True)

    class Meta:
        verbose_name = "Solicitação"
        verbose_name_plural = "Solicitações"
        ordering = ['id']
