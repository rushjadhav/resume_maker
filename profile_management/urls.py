from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from profile_management import views

urlpatterns = [
        url(r'^signin/$',
            views.SignInView.as_view(),
            name="signin"),

        url(r'^signup/$',
            views.SignUpView.as_view(),
            name="signup"),

        url(r'^signout/$',
            views.SignOutView.as_view(),
            name="signout"),

        url(r'^profile_pic/$',
            login_required(views.ProfilePicView.as_view()),
            name="profile_pic"),

        url(r'^my_profile/$',
            login_required(views.MyProfileView.as_view()),
            name="my_profile"),
]
