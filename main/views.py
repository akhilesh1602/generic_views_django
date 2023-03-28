from django.shortcuts import render
from django.views import View
from django.shortcuts import HttpResponse
from django.views.generic import(
    DetailView, ListView, CreateView, UpdateView, DeleteView
)
from main import models




# Create your views here.
class Index(View):
    def get(self, request):
        return HttpResponse("GET request")
    def post(self,request):
        return HttpResponse('POST request')

class CollegeDetail(DetailView):
    model = models.College
    template_name = 'college_detail.html'


class CollegeList(ListView):
    model = models.College
    template_name = 'college_list.html'
    context_object_name = 'colleges'

class CollegeCreate(CreateView):
    model = models.College
    template_name = 'college_create.html'
    fields = '__all__'
    success_url = '/college'



class CreateStudent(CreateView):
    model = models.Student
    template_name = 'student_create.html'
    fields = '__all__'
    success_url = '/'

class CollegeUpdate(UpdateView):
    model = models.College
    template_name = 'college_create.html'
    fields = '__all__'
    success_url = '/college'

class StudentDelete(DeleteView):
    model = models.Student
    template_name = 'confirm.html'
    success_url = '/'




def get_absolute_url(*args, **kwargs):
    return '/'






# five generic views
# 1) Detail view
# 2) List view
# 3) Create view
# 4) Update view
# 5) Delete view
