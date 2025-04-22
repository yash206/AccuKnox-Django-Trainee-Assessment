from django.urls import path
from .views import trigger_log

urlpatterns = [
    path('log-thread/', trigger_log, name='log_thread'),
]
