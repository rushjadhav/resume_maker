from django.shortcuts import render
from django.views.generic import View

class Index(View):

    def get(self, request):
        resumes = request.user.resumes.all()
        return render(request, 'dashboard.html', {'resumes': resumes})
