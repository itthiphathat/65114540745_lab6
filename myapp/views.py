from django.shortcuts import render

def home(request):
    return render(request, 'homepage1.html')  # แสดงหน้า homepage1.html

def next_page(request):
    return render(request, 'homepage2.html')  # แสดงหน้า homepage2.html

