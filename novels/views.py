from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def info(request):
    return render(request,'novels/novels.html')

def detail(request,novel_id):
    return HttpResponse(str(novel_id) + '       เรื่องย่อ')
