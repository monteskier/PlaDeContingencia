from django.shortcuts import render
from pla.models import Servei, Actiu, Seguiment
# Create your views here.

def index(request):

    sc_baixa = Servei.objects.filter(criticitat='Baixa')
    sc_mitjana = Servei.objects.filter(criticitat = 'Mitjana') #Criticitat mitjana#
    sc_alta =  Servei.objects.filter(criticitat = 'Alta') #Criticitat alta#
    return render(request,'index.html', {'sc_baixa' : sc_baixa, 'sc_mitjana' : sc_mitjana, 'sc_alta' : sc_alta})

def desplegar(request, servei_id):
    return HttpResponse("Has selccionat el Servei = " % servei_id)
