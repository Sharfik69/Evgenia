from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main_page/index.html', locals())
def Button(request):
    return render(request, 'mainApp/test_button.html', {'values': ['This is test button', 'raz raz raz']})