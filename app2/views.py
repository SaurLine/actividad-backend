from django.shortcuts import render

# Create your views here.

def vista1(request):
    lista_elemento = [
        {"id": 1, "nombre": "elemento 1"},
        {"id": 2, "nombre": "elemento 2"}
    ]

    return render(request, "app2/v1.html")