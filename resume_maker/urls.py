"""resume_maker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from resume_management import views as rm_views

urlpatterns = patterns('',

                       url(r'^resume/(?P<access_url>.+)$',
                           rm_views.DisplayResume.as_view(),
                           name="display_resume"),

                       url(r'^',
                       include('website.urls', namespace="website")),

                       url(r'^accounts/',
                       include('profile_management.urls', namespace="accounts")),

                       url(r'^dashboard/',
                       include('dashboard.urls', namespace="dashboard")),

                       url(r'^rm/',
                       include('resume_management.urls', namespace="resume")),

                       url(r'^admin/',
                       include(admin.site.urls)),

                       url(r'^jsreverse/$',
                           'django_js_reverse.views.urls_js',
                           name='js_reverse'),
)

if settings.DEBUG:
    urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
