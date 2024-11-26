from django.urls import path
from .views import JobListView, ApplicationView

urlpatterns = [
    path('list/', JobListView.as_view(), name='job-list'),
    path('apply/', ApplicationView.as_view(), name='apply'),
]
