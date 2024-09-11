from django.db import models
from django.contrib.auth.models import User
class Group(models.Model):
    pass

class Bill(models.Model):
    pass

class Member(models.Model):
    user=models.ForeignKey(User,  on_delete=models.CASCADE)
    debt_or_credit_amount=models.IntegerField(default=0)
    group=models.ForeignKey(Group, on_delete=models.CASCADE)
    bill=models.ForeignKey(Bill , on_delete=models.CASCADE)
    debt_status=models.BooleanField(default=False)
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




class Dong(models.Model):
    pass

