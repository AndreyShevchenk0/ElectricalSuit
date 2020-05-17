from django.shortcuts import render


def index(request):
    return render(request, 'ElectrHead/base.html')

def xer(request):
    return render(request, 'ElectrHead/myJob.html')
