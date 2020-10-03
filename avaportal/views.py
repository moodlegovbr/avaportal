from django.shortcuts import render
from .models import Campus


# Create your views here.
def index(request):
    campus = Campus.objects.all()
    return render(request, 'avaportal/index.html', {'campus': campus})