from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET

@csrf_exempt
@require_GET
def hello(request):
    if 'name' in request.GET and 'message' in request.GET:
        name = request.GET['name']
        message = request.GET['message']
    
        response = {'name': name,
                    'message': message,
                    }
        return render(request, 'hello.html', response)
    
    elif 'name' in request.GET or 'message' in request.GET:
        return HttpResponse('<h1>Только одна переменная передана. Нужно две.</h1>')
    
    else:
        return HttpResponse('<h1>Привет, незнакомец...</h1>')

def ss(request):
    return render(request, 'ss.html')
