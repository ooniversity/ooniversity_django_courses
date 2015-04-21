from django.shortcuts import get_object_or_404, render

def detail_view(request, pk, obj_class):
    obj_name = obj_class.__name__.lower()
    obj = get_object_or_404(obj_class, pk=pk)
    return render(request, "%ss/edit.html", %obj_name, {obj_name: obj})