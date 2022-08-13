from operator import length_hint
from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    
    qyufurner = ['mal ', 'eblan ', 'ochxar ', 'anasun ', 'debil ', 'ebani qit ', 'idiot ', 'baran ']
    
    text = ''
    
    anun = request.GET.get('anun')
    
    if anun == 'tupagamer':
        text += 'Tupa Gamer@ '
    else:
        text += f'{anun}n '
    
    length = int(request.GET.get('length'))
    
    qyufur_list = []
    for x in range(length):
        qyufur = random.choice(qyufurner)
        if qyufur not in qyufur_list:
            text += qyufur
        else:
            qyufur = random.choice(qyufurner)
            if qyufur not in qyufur_list:
                text += qyufur
            
    text += ' e'
    return render(request, 'generator/password.html', {'text': text})