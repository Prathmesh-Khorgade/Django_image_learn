from django.shortcuts import render
from  .models import ImageModel


def display(request):
    fm=ImageModel.objects.all()
    return render(request,'display.html',{'form':fm})
