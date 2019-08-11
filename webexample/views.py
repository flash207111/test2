from django.shortcuts import render


def index(request):
    return render(request, 'webexample/wehomePage.html')

def index1(request):
    return render(request, 'webexample/wehomePage1.html')

def index2(request):
    return render(request, 'webexample/bootstrap_exam.html')

def index3(request):
    return render(request, 'webexample/boot_45.html')

def index4(request):
    return render(request, 'webexample/boot_40.html')