from django.shortcuts import render

def index(request):
    return render(request,'course/index.html')
# Create your views here.

def course_details(request):
    course=['Python','Django','PostgreSql','Mysql','Git&Github']
    #course=""
    return render(request,'course/course_detail.html',{'data':course})
