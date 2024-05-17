from django.shortcuts import render
from django.http import HttpResponse
from .models import app


# Create your views here.
 
def api(request,value):
    try:
        x = app.objects.get(id=value)
    except:
        return HttpResponse(f'{x} is not found')
    return HttpResponse(f"customer_name-{x.cus_name}/ location-{x.location}")
   
    

def demo(request):
    return HttpResponse('Customer Details')

#def shows(request):
#    value = models.app.objects.get(id)
#    return render(request,'a.html',a=value.cus_name,b=value.location)   
