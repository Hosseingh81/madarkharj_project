from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from madarkharj.models import Member,Group
from freezegun import freeze_time
import datetime
from django.utils import timezone

class Main_User_Page_Test(TestCase):
    def setUp(self):
        self.user1=User.objects.create(username='user1',password='user1')
        self.member1=Member.objects.create(user=self.user1)
        self.group1=Group()
        self.group1.save()
        self.group1.member.add(self.member1)
        self.group1.save()
    def access_the_main_page_url(self):
        url=reverse("madarkharj:mainpage",args=(self.user1.username,))
        return self.client.get(url)
    def test_the__main_user_page_returns_the_200_status_code(self): #this func tests that the user main page returns the 200 status code.
        self.client.force_login(user=self.user1)
        response=self.access_the_main_page_url()
        self.assertEqual(response.status_code,200)
    def test_main_user_page_uses_the_correct_template(self): #this func tests that the main user page uses the correct template.
        self.client.force_login(user=self.user1)
        response=self.access_the_main_page_url()
        self.assertTemplateUsed(response,template_name='madarkharj/main_page.html')
    def test_main_user_page_view_CBV_passes_the_groups_data_to_the_template(self): #this func tests wheter the context that passed from the CBV to the Main_Page_User had correct data(correct groups filterd by the logged in member) or not. 
        self.client.force_login(user=self.user1)
        response=self.access_the_main_page_url()
        groups_based_on_member=Group.objects.filter(member=self.member1)
        self.assertQuerySetEqual(response.context['groups'],groups_based_on_member)




    #     def test_not_logged_in_user_can_not_visit_main_user_page(self): #this func tests that the not logged in user can't visit the main user page by comparing it's template with the main user page template.
    #         response=self.access_the_main_page_url()
    #         self.assertTemplateNotUsed(response,template_name='madarkharj/main_page.html')
    #     def test_not_logged_in_user_redirects_it_it_tries_to_visit_main_user_page(self): # this func test that the not logged in user redirects when it tries to visit main page user by checking the status code.
    #         response=self.access_the_main_page_url()
    #         self.assertEqual(response.status_code,301)
    #         self.assertEqual(response.status_code,302)
    #     def test_not_logged_in_user_redirects_to_the_login_page_it_it_tries_to_visit_main_page_user(self): #this func tests that the web app redirects not loggedin user to the login page.
    #         response=self.access_the_main_page_url()
    #         self.assertRedirects(response,'accounts/login/')









        



























        