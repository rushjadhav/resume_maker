from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

class Index(View):

    def get(self, request):
        resumes = request.user.resumes.all()
        return render(request, 'dashboard.html', {'resumes': resumes})

class ToggleSideBar(View):

    def get(self, request):
        is_expanded = js_to_python_bool(request.GET.get('is_expanded', False))
        request.session['is_expanded'] = is_expanded
        return HttpResponse('Success')

def js_to_python_bool(flag):

    return True if flag == 'true' else False
