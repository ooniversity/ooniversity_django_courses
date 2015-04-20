return render(request, 'name.html'{'variab':variab})
{{ variab }}

context = {'var1': 'ololo'}
context['var2'] = 'alala'
return render(request, 'name.html', context)

instructors = Instructors.objects.all()
context['instructors']=instructors
return render(request, 'name.html', context)