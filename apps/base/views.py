from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.views.generic import TemplateView


def index(request: WSGIRequest):
    return render(
        request=request,
        template_name="index.html",
    )


class AboutUsView(TemplateView):
    template_name = "basic/basic.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "about_us"

        return context


class ContactsView(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "contacts"


class CertifView(TemplateView):
    template_name = "certificates.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "certificates"


class WorkView(TemplateView):
    template_name = "work.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work"
