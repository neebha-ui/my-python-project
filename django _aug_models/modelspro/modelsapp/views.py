from django.shortcuts import render, redirect
from .models import Student


def student_form(request):
    if request.method == "POST":
        name = request.POST['name']
        roll_number = request.POST['roll_number']
        student_class = request.POST['student_class']
        age = request.POST['age']
        parent_contact = request.POST['parent_contact']

        Student.objects.create(
            name=name,
            roll_number=roll_number,
            student_class=student_class,
            age=age,
            parent_contact=parent_contact
        )

        return redirect('/modelsapp/list/')

    return render(request, 'student_form.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def student_update(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.roll_number = request.POST['roll_number']
        student.student_class = request.POST['student_class']
        student.age = request.POST['age']
        student.parent_contact = request.POST['parent_contact']

        student.save()

        return redirect('/modelsapp/list/')

    return render(request, 'student_update.html', {'student': student})


def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()

    return redirect('/modelsapp/list/')




