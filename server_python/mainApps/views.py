from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Instructions, Office, Person
from .form import CreateUser

# Create your views here.

class PersonOfficeView(ListView):
    template_name = 'mainapps/index.html'
    model = Person
    context_object_name = 'office'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PersonView(DetailView):
    template_name = 'mainapps/person.html'
    context_object_name = 'person'
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['office'] = Person.objects.all()
        #context['']
        return context


class RegistratoinPerson(CreateView):
    template_name = 'mainapps/registration.html'
    form_class = CreateUser
    success_url = "/accoutns/login/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context