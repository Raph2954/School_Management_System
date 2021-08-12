from django.contrib.auth.models import User
from secondary.models import Teacher, Student, Subjects, Class
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from secondary.models import Student


def teacher_view(request):
    obj = Teacher.objects.all()
    return render(request, "teacherdetails.html", {'teachers': obj})



def student_view(request):
    obj = Student.objects.all()
    return render(request, "secondary/studentlist.html", {'students': obj})

@login_required
def studentdetailview(request):
    obj = Student.objects.all()
    return render(request, "secondary/studentdetail.html", {'students': obj})


#def DisplayResult(request):
    #obj = ResultForm.object.all()
    #return render(request, "secondary/check_result.html", {'ResultForm': obj})



@login_required
def SettingsView(request):
    return render(request, 'settings.html')

@login_required
def Indetail(request):
    obj = get_object_or_404(Student)
    return render(request, 'secondary/indetail.html', {'section':'Student',
                                                       'obj':obj})

@login_required
def classdetail(request):
    obj = Class.objects.all
    return render(request, 'secondary/classes.html',{'classes':obj})
