from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main_page/index.html', locals())
def AddGroup(request):
    return render(request, 'main_page/AddGroup.html', locals())