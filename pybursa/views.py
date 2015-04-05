from django.shortcuts import render_to_response

def dummy_render(request, template='index.html'):
	return render_to_response(template)




