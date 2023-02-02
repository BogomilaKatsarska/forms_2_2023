from django.urls import path

from forms_2_2023.web.views import index

urlpatterns = (
    path('', index, name='index'),
)