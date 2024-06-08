from django.shortcuts import render

def index(request):
    return render(request,'course/index.html')
# Create your views here.

def course_details(request):
    course=['Python','Django','PostgreSql','Mysql','Git&Github']
    #course=""
    return render(request,'course/course_detail.html',{'data':course})

def course_duration(request):
    dur={'python':'4 month','Django':'3 month','postgresql':'1 month','Git':'15 days'}
<<<<<<< HEAD
    return render(request,'course/course_detail.html',{'data':'dur'})
=======
    return render(request,'course/course_detail.html',{'data_dur':'dur'})
>>>>>>> 84bbc9675d6897ec580f242cd2bd944e12283228
