from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    o_services= Service.objects.all()
    return render(request, "Services/services.html",{"o_services":o_services})