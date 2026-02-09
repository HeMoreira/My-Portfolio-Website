from django.shortcuts import render
from django.utils.translation import get_language_from_request

def redirect_to_main_page(request):
    user_language = get_language_from_request(request)
    
    if user_language == 'pt-br':
        return render(request, "main/portuguese_main_page.html")
    # elif user_language == 'en':
    #     return render(request, "main/english_main_page.html")
    return render(request, "main/portuguese_main_page.html")

def display_portuguese_main_page(request):
    return render(request, "main/portuguese_main_page.html")

def display_english_main_page(request):
    return render(request, "main/english_main_page.html")