from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class main_page_view(View):
    this_is_main_page='this is main page.'
    template_name = "madarkharj/main_page.html"
    def get(self,request,username):
        return render(request, self.template_name,{"main_page_msg":self.this_is_main_page})