from django.shortcuts import render

# Create your views here.
def metodo_index(request):	
    return render(request, 'produto/index.html')  