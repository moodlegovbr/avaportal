import json
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Campus, Solicitacao


# Create your views here.
def index(request):
    campus = Campus.objects.all()
    return render(request, 'avaportal/index.html', {'campus': campus})


def raise_error(request, error):
    solicitacao = Solicitacao()
    solicitacao.requisicao_header = request.META
    solicitacao.requisicao_invalida = request.body.decode('utf-8')
    solicitacao.resposta = error
    solicitacao.status = Solicitacao.Status.FALHA
    solicitacao.save()
    response = JsonResponse(error)
    response.status_code=error["code"]
    return response

@csrf_exempt
def sync_up(request):
    if request.method != 'POST':
        return HttpResponse("Mandou via GET pq?")

    try:
        pkg = json.loads(request.body)
        filter = {"suap_id": pkg["campus"]["id"], "sigla": pkg["campus"]["sigla"]}
    except Exception as e:
        return raise_error(request, {"error": f"O JSON está inválido. {e}", "code": 406})
    
    campus = Campus.objects.filter(**filter).first()
    if campus is None:
        return raise_error(request, {"error": f"Não existe um campus com o id '{filter['suap_id']}' E a sigla '{filter['sigla']}'.", "code": 404})

    if not campus.active:
        return raise_error(request, {"error": f"O campus '{filter['sigla']}' existe, mas está inativo.", "code": 412})

    solicitacao = Solicitacao()
    solicitacao.requisicao_header = request.META

    return JsonResponse(campus.active, safe=False)

