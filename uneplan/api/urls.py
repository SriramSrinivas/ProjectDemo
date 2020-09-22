from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import (
DepartmentView,
DepartmentUpdateView,
DepartmentListView,
DepartmentCreateView,
DepartmentDeleteView,
DepartmentDetailView
)
urlpatterns = [
    url('read/', DepartmentView.department_list_get),
    url('writenew/', DepartmentView.department_list_post),
path('<int:pk>/read/', DepartmentView.department_detail_get),
path('<int:pk>/update/', DepartmentView.department_detail_update),

    path('<int:pk>/edit/',
         DepartmentUpdateView.as_view(), name='department_edit'),
    path('<int:pk>/',
         DepartmentDetailView.as_view(), name='department_detail'),
    path('<int:pk>/delete/',
         DepartmentDeleteView.as_view(), name='department_delete'),
    path('', DepartmentListView.as_view(), name='department_list'),
    path('new/', DepartmentCreateView.as_view(), name='department_new'),


]