from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SnippetForm
from .models import Snippet
import urllib.request, json

def index(request):
    if request.method == 'POST':

        form = SnippetForm(request.POST)

        if form.is_valid():
            ip = form.cleaned_data['ip']
            model = Snippet
            ips = list(model.objects.values_list('ip', flat=True))
            
            if not ip in ips:
                form.save()
            return HttpResponseRedirect('/historico')

    else:
        form = SnippetForm()

    return render(request, 'index.html', {'form': form})


def retorna_resultado(request):
    model = Snippet
    ips = list(model.objects.values_list('ip', flat=True))
    datas = []

    for i in ips:
        datas.append(json.loads(urllib.request.urlopen(f'http://ip-api.com/json/{str(i)}').read().decode()))

    return render(request, 'results.html', {'datas': datas})