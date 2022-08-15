from django.http.response import HttpResponse
from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .tasks import *

from core.forms import FeedbackForm



def total(request):
    res = add.delay(4, 5)
    return HttpResponse(res)


class FeedbackFormView(FormView):
    template_name = "core/feedback.html"
    form_class = FeedbackForm
    success_url = "/success/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "core/success.html"