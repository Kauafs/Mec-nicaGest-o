from django.shortcuts import render

# Create your views here.
def page_compras(request):
    return render(request, 'tpcompras/compras.html')