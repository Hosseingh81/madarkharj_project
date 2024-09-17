from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user=models.ForeignKey(User,  on_delete=models.CASCADE)
    debt_or_credit_amount=models.IntegerField(default=0)
    debt_status=models.BooleanField(default=False)
    joined_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __init__(self,*args,**kwargs):
        super(Member,self).__init__(*args, **kwargs)
        if self.debt_or_credit_amount <0:
            self.debt_status=True
    def debtor_or_creditor_status(self):
        if self.debt_or_credit_amount <0:
            return 'debtor'
        elif self.debt_or_credit_amount >0:
            return 'creditor'
        else:
            return '0'

class Share(models.Model):
    pass

class Group(models.Model):
    member=models.ManyToManyField(Member)

class Bill(models.Model):
    pass




