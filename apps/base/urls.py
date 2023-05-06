from django.urls import path
from . import views

app_name = "basic"

urlpatterns = [
    path("basiс/", views.AboutUsView.as_view(), name="basic"),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
    path("certificates/", views.CertifView.as_view(), name="certificates"),
    path("work/", views.WorkView.as_view(), name="work")

]
