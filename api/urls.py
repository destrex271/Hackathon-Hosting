from django.contrib import admin
from django.urls import path

from .views import GetUserHackathons, HackathonView, RegisterHackathon, SubmissionView

urlpatterns = [
    path('hackathons/create', HackathonView.as_view(), name="all_hackathon_ops"),
    path('hackathons/list', HackathonView.as_view(), name="get_all_hackathons"),
    path('hackathons/register', RegisterHackathon.as_view(), name="register_hackathon"),
    path('hackathons/submit', SubmissionView.as_view(), name="submission_view"),
    path('hackathons/view_submission', SubmissionView.as_view(), name="view_submission"),
    path('hackathons/my_hackathons', GetUserHackathons.as_view(),name="get_user_hackathons")
]
