from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Student
from .forms import StudentForm

# Create your views here.
def index(request):
    students = Student.objects.all()
    return render(request,'index.html',{'students':students})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    
    return render(request,'add_student.html',{'form':form})

def delete_stud(request,pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('index')
 
 
def update_stud(request,pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = StudentForm(instance=student)
    return render(request,'update.html',{'form':form})