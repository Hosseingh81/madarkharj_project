from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from madarkharj.models import member,groups,resid,dong



class Main_User_Page_Test(TestCase):
    def creating_user1(self):
        self.user1=User.objects.create(username='user1',password='user1')
        self.client.force_login(user=self.user1)
    def accessing_the_main_page_url(self):
        url=reverse('madarkharj:mainpage',args=(self.user1.id,))
        return self.client.get(url)
    def test_the__main_user_page_returns_the_200_status_code(self): #this func tests that the user main page returns the 200 status code.
        self.creating_user1()
        response=self.accessing_the_main_page_url()
        self.assertEqual(response.status_code,200)
    def test_main_user_page_uses_the_correct_template(self): #this func tests that the main user page uses the correct template.
        self.creating_user1()
        response=self.accessing_the_main_page_url()
        self.assertTemplateUsed(response,template_name='madarkharj/main_page.html')
    def test_not_logged_in_user_can_not_visit_main_user_page(self): #this func tests that the not logged in user can't visit the main user page by comparing it's template with the main user page template.
        response=self.accessing_the_main_page_url()
        self.assertTemplateNotUsed(response,template_name='madarkharj/main_page.html')
    def test_not_logged_in_user_redirects_it_it_tries_to_visit_main_user_page(self): # this func test that the not logged in user redirects when it tries to visit main page user by checking the status code.
        response=self.accessing_the_main_page_url()
        self.assertEqual(response.status_code,301)
        self.assertEqual(response.status_code,302)
    def test_not_logged_in_user_redirects_to_the_login_page_it_it_tries_to_visit_main_page_user(self): #this func tests that the web app redirects not loggedin user to the login page.
        response=self.accessing_the_main_page_url()
        self.assertRedirects(response,'accounts/login/')
class test_Member_Model(TestCase):
    def setUp(self):
        self.user1=User.objects.create(username='user1',password='user1')
        self.user2=User.objects.create(username='user2',password='user2')
        self.group1=groups.objects.create()
        self.resid1=groups.objects.create()
        member.objects.create(debt_or_credit_amount=100,user=self.user1,groups=self.group1,resid=self.resid1)
        member.objects.create(debt_or_credit_amount=-100',user=self.user2,groups=self.group1,resid=self.resid1)
    def test_the_status_of_debtor_or_creditor_of_the_member(self): #this func tests the status of debtor or creditor of a member based on the debt or credit amount.
        member1=member.objects.get(user=self.user1)
        member2=member.objects.get(user=self.user2)
        self.assertEqual(member1.the_debt_or_credit_status(),'creditor')
        self.assertEqual(member2.the_debt_or_credit_status(),'debtor')
    def test_the_amount_of_depts_or_credits(self):
        member1=member.objects.get(user=self.user1)
        member2=member.objects.get(user=self.user2)
        self.assertEqual(member1.the_debt_or_credit_status(),100)
        self.assertEqual(member2.the_debt_or_credit_status(),-100)

