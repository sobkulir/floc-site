from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.ShowListView.as_view(), name='show_list'),
]