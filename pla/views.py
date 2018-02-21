import json, os
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from pla.models import Servei, Actiu, Seguiment
# Create your views here.

def index(request):

    sc_baixa = Servei.objects.filter(criticitat='Baixa')
    sc_mitjana = Servei.objects.filter(criticitat = 'Mitjana') #Criticitat mitjana#
    sc_alta =  Servei.objects.filter(criticitat = 'Alta') #Criticitat alta#
    return render(request,'index.html', {'sc_baixa' : sc_baixa, 'sc_mitjana' : sc_mitjana, 'sc_alta' : sc_alta})

def getSeguimentsServei(request, servei_id):
    seguiment = Servei.objects.get(pk=servei_id);
    print(seguiment);
    objson = serializers.serialize("json", seguiment.seguiment_set.all())
    return HttpResponse(objson)

def getSeguimentsActiu(request, actiu_id):
    return HttpResponse("Has selccionat el Servei = " % actiu_id)
    actiu = get_object_or_404(Question, actiu_id)
    return(actiu);

def test(request, servei_id):
    servei = Servei.objects.get(pk=servei_id);
    actius = servei.actiu_set.all();
    data = {}
    ope = [] #operatius
    ino =[] #inoperatius

    for actiu in actius:
        for ip in actiu.ip.all():
            response = os.system("ping -c 1"+ ip.address)
            if(response == 0):
                actiu.estat="Operatiu"
                actiu.save()
                ope.append(actiu.nomActiu)
            else:
                actiu.estat="Inoperatiu"
                actiu.save()
                ino.append(actiu.nomActiu)

        data['Operatius']=ope;
        data['Inoperatius']=ino;

    return HttpResponse(json.dumps(data))
