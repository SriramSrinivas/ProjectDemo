from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from . import models
from .models import (
Department
)

from .DepartmentSerializer import DepartmentSerializer
from django.http import Http404, JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


class ReadOnly(object):
    pass


class DepartmentView(APIView):


    permission_classes = (IsAuthenticated)
    @csrf_exempt
    def department_list_post(request):

        if request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = DepartmentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)

    permission_classes = (IsAuthenticated)
    @csrf_exempt
    def department_list_get(request):
        if request.method == 'GET':
            departments = Department.objects.all()
            serializer = DepartmentSerializer(departments, many=True)
            return JsonResponse(serializer.data, safe=False)
    permission_classes = (IsAuthenticated)
    @csrf_exempt
    def department_detail_get(request, pk):
        print('here')
        department=getDepartment(pk)

        if request.method == 'GET':
            serializer = DepartmentSerializer(department)
            return JsonResponse(serializer.data)
    permission_classes = (IsAuthenticated,permissions.IsAdminUser)
    @csrf_exempt

    def department_detail_update(request, pk):
        department = getDepartment(pk)

        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = DepartmentSerializer(department, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            department.delete()
            return HttpResponse(status=204)


def getDepartment(pk):
    try:
        department = Department.objects.get(pk=pk)
        return department
    except Department.DoesNotExist:
        return HttpResponse(status=404)


class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = 'department_list.html'

class DepartmentDetailView(LoginRequiredMixin ,DetailView):
    model = Department
    template_name = 'department_detail.html'
    login_url = 'login'

class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Department
    fields = ('abbreviation', 'name', 'description', 'active')
    template_name = 'department_edit.html'
    success_url = reverse_lazy('department_list')

class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Department
    template_name = 'department_delete.html'
    success_url = reverse_lazy('department_list')

class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    template_name = 'department_new.html'
    fields = ('abbreviation', 'name', 'description', 'active')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

