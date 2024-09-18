from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from .models import Member,Group
from . import queries

# Create your views here.
class main_user_page_view(ListView):
    this_is_main_page='this is main page.'
    template_name = "madarkharj/main_page.html"
    def get_queryset(self):
        user=self.request.user
        self.groups=queries.queries(members=Member.objects.get(user=user)).group_guery()
        return None
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["groups"] = self.groups
        return context

    