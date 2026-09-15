from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Marks


def add_student(request):
    if request.method == "POST":
        roll = request.POST['roll']
        name = request.POST['name']
        age = request.POST['age']
        course = request.POST['course']

        Student.objects.create(
            roll=roll,
            name=name,
            age=age,
            course=course
        )

    return render(request, 'add_student.html')


def add_marks(request):
    if request.method == "POST":
        roll = request.POST['roll']

        try:
            student = Student.objects.get(roll=roll)

            telugu = request.POST['telugu']
            english = request.POST['english']
            maths = request.POST['maths']
            science = request.POST['science']

            Marks.objects.create(
                student=student,
                telugu=telugu,
                english=english,
                maths=maths,
                science=science
            )

        except Student.DoesNotExist:
            pass

    return render(request, 'add_marks.html')


def view_student(request):
    student = None
    marks = None

    if request.method == "POST":
        roll = request.POST['roll']

        try:
            student = Student.objects.get(roll=roll)
            marks = Marks.objects.get(student=student)

        except:
            student = None
            marks = None

    return render(
        request,
        'view_student.html',
        {
            'student': student,
            'marks': marks
        }
    )


def edit_student(request, roll):
    student = get_object_or_404(Student, roll=roll)

    try:
        marks = Marks.objects.get(student=student)
    except Marks.DoesNotExist:
        marks = None

    if request.method == "POST":
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.course = request.POST['course']
        student.save()

        if marks:
            marks.telugu = request.POST['telugu']
            marks.english = request.POST['english']
            marks.maths = request.POST['maths']
            marks.science = request.POST['science']
            marks.save()

        return redirect('view_student')

    return render(
        request,
        'edit_student.html',
        {
            'student': student,
            'marks': marks
        }
    )

def delete_student(request, roll):

    student = get_object_or_404(Student, roll=roll)

    if request.method == "POST":
        student.delete()
        return redirect('view_student')

    return render(
        request,
        'delete_detail.html',
        {'student': student}
    )
