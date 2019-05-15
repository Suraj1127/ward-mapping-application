from django.urls import path

from . import views

urlpatterns = [
    path('upload_<int:year>', views.accumulate, name='accumulate'),
    path('<int:year>-to-2018', views.index, name='index'),
    path('ajax/<int:year>', views.index_asJSON, name='my_ajax_url')
]
