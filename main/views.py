from django.shortcuts import render

def display_portuguese_main_page(request):
    return render(request, "main/portuguese_main_page.html")

def display_english_main_page(request):
    return render(request, "main/english_main_page.html")