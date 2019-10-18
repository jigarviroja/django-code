from django.shortcuts import render
from django.urls import reverse_lazy
# from django.http import HttpResponse
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from . import models


# Create your views here.
# def index(request):
#     return render(request, 'index.html')


# class IndexView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'I am Inject in index page'
#         return context


class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):

    context_object_name = 'schools'
    model = models.School
    # ListView take the models name and return with _list  ex.  school_list


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    # DetailView return model name with lower case  ex.school
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('collage_name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('collage_name', 'principal')
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
