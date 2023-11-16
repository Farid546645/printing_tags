from django.shortcuts import render

# Create your views here.
def data_render(request):

    DATA='THIS IS MY  ASSUMPTION THE  DATA WILL  BE COME FROM  DATABASE TO BACKEND'
    d={'DATA':DATA}
    return render(request,'data_render.html',d)