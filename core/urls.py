from django.urls import path,include
from . import views
from core.views import FeedbackFormView, SuccessView

app_name = 'core'

urlpatterns = [
    path('', views.total, name="core"),
    path("feedback/", FeedbackFormView.as_view(), name="feedback"),
    path("success/", SuccessView.as_view(), name="success"),
]