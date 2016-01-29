from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.files import File

from profile_management.forms import SignInForm, SignUpForm, ProfileForm
from profile_management.models import UserProfile

class SignInView(View):

    def get(self, request):
        form = SignInForm()
        return render(request, 'signin.html', {'form': form})

    def post(self, request):

        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard:index'))
            else:
                messages.error(request, 'Provided username or password is incorrect.')
        return render(request, 'signin.html', {'form': form})

class SignUpView(View):

    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):

        form = SignUpForm(request.POST)
        if form.is_valid():
            user = UserProfile()
            user.username = form.cleaned_data.get('username')
            user.first_name = form.cleaned_data.get('first_name')
            user.middle_name = form.cleaned_data.get('middle_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.date_of_birth = form.cleaned_data.get('date_of_birth')
            user.password = form.cleaned_data.get('password')
            try:
                user.full_clean()
                user.set_password(form.cleaned_data.get('password'))
                user.save()
                messages.success(request, 'You are signed up successfully.')
                return HttpResponseRedirect(reverse('accounts:signin'))
            except ValidationError as errors:
                for error in errors.error_dict.values():
                    form.add_error(None, error)
        return render(request, 'signup.html', {'form': form})

class MyProfileView(View):

    def get(self, request):
        form = ProfileForm(instance=request.user)
        return render(request, 'profile.html', {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Profile Updated successfully.')
            return HttpResponseRedirect(reverse('accounts:my_profile'))
        else:
            return render(request, 'profile.html', {'form': form})

class SignOutView(View):

    def get(self, request):
        logout(request)
        messages.success(request, 'You are signed out successfully.')
        return HttpResponseRedirect(reverse('accounts:signin'))

class ProfilePicView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ProfilePicView, self).dispatch(*args, **kwargs)

    def get(self, request):

        if request.user.profile_pic:
            pass
        else:
            return HttpResponse("Profile picture is not available.")

    def post(self, request):
        profile_pic = request.FILES.get('file')
        request.user.profile_pic.save('profile.png', File(profile_pic))
        return HttpResponseRedirect(reverse('dashboard:index'))

