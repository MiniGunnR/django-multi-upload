from django.conf.urls import url

from index import views

urlpatterns = [
        url(r'^form/$', views.Form),
        url(r'^upload/$', views.Upload),
        ]
