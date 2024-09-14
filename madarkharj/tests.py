from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from madarkharj.models import Member,Group,Bill,Dong
from freezegun import freeze_time
import datetime
from django.utils import timezone

# class Main_User_Page_Test(TestCase):
#     def creating_user1(self):
#         self.user1=User.objects.create(username='user1',password='user1')
#         self.client.force_login(user=self.user1)
#     def accessing_the_main_page_url(self):
#         url=reverse('madarkharj:mainpage',args=(self.user1.id,))
#         return self.client.get(url)
#     def test_the__main_user_page_returns_the_200_status_code(self): #this func tests that the user main page returns the 200 status code.
#         self.creating_user1()
#         response=self.accessing_the_main_page_url()
#         self.assertEqual(response.status_code,200)
#     def test_main_user_page_uses_the_correct_template(self): #this func tests that the main user page uses the correct template.
#         self.creating_user1()
#         response=self.accessing_the_main_page_url()
#         self.assertTemplateUsed(response,template_name='madarkharj/main_page.html')
#     def test_not_logged_in_user_can_not_visit_main_user_page(self): #this func tests that the not logged in user can't visit the main user page by comparing it's template with the main user page template.
#         response=self.accessing_the_main_page_url()
#         self.assertTemplateNotUsed(response,template_name='madarkharj/main_page.html')
#     def test_not_logged_in_user_redirects_it_it_tries_to_visit_main_user_page(self): # this func test that the not logged in user redirects when it tries to visit main page user by checking the status code.
#         response=self.accessing_the_main_page_url()
#         self.assertEqual(response.status_code,301)
#         self.assertEqual(response.status_code,302)
#     def test_not_logged_in_user_redirects_to_the_login_page_it_it_tries_to_visit_main_page_user(self): #this func tests that the web app redirects not loggedin user to the login page.
#         response=self.accessing_the_main_page_url()
#         self.assertRedirects(response,'accounts/login/')
class test_Member_Model(TestCase):
    def setUp(self):
        self.user1=User.objects.create(username='user1',password='user1')
        self.user2=User.objects.create(username='user2',password='user2')
        self.user3=User.objects.create(username='user3',password='user3')
        Member.objects.create(debt_or_credit_amount=100,user=self.user1)
        Member.objects.create(debt_or_credit_amount=-100,user=self.user2)
        Member.objects.create(debt_or_credit_amount=0,user=self.user3)
    def test_debt_status_feild_based_on_debt_or_credit_amount(self): #this func tests that debt status has the correct status based on the debt_or_credit_amount feild.
        member1=Member.objects.get(user=self.user1)
        member2=Member.objects.get(user=self.user2)
        member3=Member.objects.get(user=self.user3)
        self.assertFalse(member1.debt_status)
        self.assertTrue(member2.debt_status)
        self.assertFalse(member3.debt_status)
    def test_the_status_of_debtor_or_creditor_of_the_member(self): #this func tests the status of debtor or creditor of a member based on the debt or credit amount.
        member1=Member.objects.get(user=self.user1)
        member2=Member.objects.get(user=self.user2)
        member3=Member.objects.get(user=self.user3)
        self.assertEqual(member1.debtor_or_creditor_status(),'creditor')
        self.assertEqual(member2.debtor_or_creditor_status(),'debtor')
        self.assertEqual(member3.debtor_or_creditor_status(),'0')
    def test_the_amount_of_depts_or_credits(self): #this func test that the debt or credit amount is correctly saved.
        member1=Member.objects.get(user=self.user1)
        member2=Member.objects.get(user=self.user2)
        member3=Member.objects.get(user=self.user3)
        self.assertEqual(member1.debt_or_credit_amount,100)
        self.assertEqual(member2.debt_or_credit_amount,-100)
        self.assertEqual(member3.debt_or_credit_amount,0)
    def test_the_updated_at_feild_saves_the_correct_date(self): # this func tests that updated_at and joined_at fields saves the date of updating and joining the member correctly.
        initial_datetime = datetime.datetime(year=1971, month=1, day=1,hour=1, minute=1, second=1)
        other_datetime = datetime.datetime(year=1973, month=1, day=1,hour=1, minute=3, second=2)
        with freeze_time(initial_datetime) as frozen_datetime:
            member=Member.objects.create(user=self.user1,debt_or_credit_amount=0)
            self.assertEqual(member.joined_at,timezone.now())
            frozen_datetime.move_to(other_datetime)
            member.debt_or_credit_amount=100
            member.save()
            self.assertEqual(member.updated_at,timezone.now())
class Test_Group_Model(TestCase):
    def setUp(self):
        self.user1=User.objects.create(username='user1',password='user1')
        self.member1=Member.objects.create(debt_or_credit_amount=100,user=self.user1)
        self.group=Group.objects.create()
        self.member1.save()
        self.group.member.add(self.member1)
        print(x for x in Group.objects.all())
        
    def test_Group_Model_feilds_is_not_none(self): #this func tests that Group model feilds are saving the data correctly and not none.
        self.group1=Group.objects.get(id=1)
        print(self.group.member)
        self.assertIsNotNone(self.group1.member,msg='member of group1 is none.')
    # def test_Group_Model_feilds_types_saved_correctly(self): #this func tests that the type Group Model feilds saved correctly in the database.
    #     self.group1=Group.objects.filter(member=self.member1)
    #     self.assertFieldOutput(self.group1.member,{self.member1:self.member1},{'testinput':['invalid']})