from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
#pasa, en este caso, un html
#def home(request):
#    return render(request, 'index.html', {'foo':'bar'})

#pasa un json
def home(request):
    return JsonResponse({'foo':'bar'})