from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from resume_management import views

urlpatterns = [
        url(r'^templates/$',
            login_required(views.ListTemplatesView.as_view()),
            name="list_templates"),

        url(r'^new_resume/$',
            login_required(views.CreateResumeView.as_view()),
            name="create_resume"),

        url(r'^update_resume/(?P<name>.+)$',
            login_required(views.UpdateResumeView.as_view()),
            name="update_resume"),

        url(r'^publish_resume/(?P<id>\d+)$',
            login_required(views.PublishResumeView.as_view()),
            name="publish_resume"),

        url(r'^template_preview/(?P<id>\d+)$',
            login_required(views.PreviewTemplateView.as_view()),
            name="preview_template"),

        url(r'^live_preview/(?P<template_id>\d+)/(?P<resume_id>\d+)$',
            login_required(views.LivePreviewView.as_view()),
            name="live_preview"),

        url(r'^pdf/(?P<id>\d+)$',
            login_required(views.ResumePDFView.as_view()),
            name="prepare_pdf"),

]
