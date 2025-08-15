

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        s1 = int(request.POST['subject1'])
        s2 = int(request.POST['subject2'])
        s3 = int(request.POST['subject3'])
        Student.objects.create(name=name, subject1=s1, subject2=s2, subject3=s3)
        return redirect('report')
    return render(request, 'main/home.html')

def report(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()
    return render(request, 'main/report.html', {'students': students})

def edit_student(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == "POST":
        student.name = request.POST['name']
        student.subject1 = int(request.POST['subject1'])
        student.subject2 = int(request.POST['subject2'])
        student.subject3 = int(request.POST['subject3'])
        student.save()
        return redirect('report')
    return render(request, 'main/edit.html', {'student': student})

def delete_student(request, id):
    student = get_object_or_404(Student, pk=id)
    student.delete()
    return redirect('report')
