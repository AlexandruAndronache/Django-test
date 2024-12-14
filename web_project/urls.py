from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from hello import views
from hello.models import LogMessage



urlpatterns = [
    path("", include("hello.urls")),
    path('admin/', admin.site.urls),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),

]







# add at the end
urlpatterns += staticfiles_urlpatterns()