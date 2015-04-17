from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404

from students.models import Student, StudentForm
from courses.models import Course


def students_list(request):
    course_id = request.GET.get('course_id')

    if course_id is None:
        students = Student.objects.all()
    else:
        course = Course.objects.get(pk=int(course_id))
        students = course.student_set.all()

    return render(request, 'students_list.html', {
        'students': students,
    })


def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    courses = student.courses.all()

    return render(request, 'detail_info.html', {
        'student': student,
        'courses': courses,
    })


def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.cleaned_data['name'] = form.cleaned_data['name'].capitalize()
            form.cleaned_data['surname'] = form.cleaned_data['surname'].capitalize()
            student = form.save()
            messages.success(
                request, u"Student {} {} add success!".format(
                    student.name, student.surname))
            return redirect('students:students-list')
    else:
        form = StudentForm()

    return render(request, 'add.html', {
        'form': form,
    })


def student_edit(request, pk):
    student = Student.objects.get(id=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student.save()
            messages.success(
                request, u"{} {} update success!".format(
                    student.name, student.surname))
            return redirect('students:students-list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'edit.html', {
        'form': form,
    })


def student_delete(request, pk):
    # try:
    #     student = Student.objects.get(id=pk)
    # except Student.DoesNotExist:
    #     raise Http404("Student does not exist")
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        messages.success(
            request, u"Student: {} {} was deleted".format(
                student.name, student.surname))
        return redirect('students:students-list')

    return render(request, 'delete.html', {
        'student': student,
    })
