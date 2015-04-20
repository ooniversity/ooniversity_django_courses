from django.shortcuts import render, redirect, get_object_or_404

#create universal function (look week 5)

def detail_view(request, student_id, obj_class):
    obj_name = obj_class.__name__.lower()
    obj = get_object_or_404(obj_class, pk=student_id)
    return render(request, 'student_info.html', {obj_name: obj})
