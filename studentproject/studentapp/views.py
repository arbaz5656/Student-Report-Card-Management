from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
# Create your views here.

def Home(request):
    Queryset=Student.objects.all().order_by('student_name')

    # search bar logic
    if request.GET.get('Search'):
        Queryset=Queryset.filter(student_name__icontains = request.GET.get('Search'))

    # pagination logic
    paginator_var = Paginator(Queryset, 5)
    page_no_var=request.GET.get('page')
    page_obj=paginator_var.get_page(page_no_var)
    total_pages=page_obj.paginator.num_pages

    return render(request,'Home.html',{"Queryset" : page_obj,"last_page":total_pages,})


#show marks details
from django.db.models import Sum

def ShowMarks(request,student_id):
    # query
    queryset=SubjectMarks.objects.filter(student__student_id__student_id =student_id)

    # search bar logic
    if request.GET.get('search'):
        queryset=queryset.filter(subject__subject_name__icontains = request.GET.get('search'))

    # total s
    # um
    totalmarks=queryset.aggregate(totalmarks = Sum('marks'))

    # Total rank
    current_rank=-1
    ranks=Student.objects.annotate(marks = Sum('Studentmarks__marks')).order_by('-marks','-student_age')
    i=1
    for r in ranks:
        if student_id==r.student_id.student_id:
            current_rank=i
            break
        i=i+1
    return render(request,"ShowMarks.html",{"queryset":queryset,"totalmarks":totalmarks,"current_rank":current_rank})