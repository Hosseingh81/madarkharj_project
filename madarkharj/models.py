from django.db import models
from django.contrib.auth.models import User

class member(models.Model):
    user=models.ForeignKey(User,  on_delete=models.CASCADE)
    debt_or_credit_amount=models.IntegerField(default=0)
    group=models.ForeignKey(group,on_delete=models.CASCADE)
    bill=models.ForeignKey(bill, on_delete=models.CASCADE)
    debt_status=models.BooleanField(default=False)
    def debt_status_assigner(self):
        if self.debt_or_credit_amount <0:
            self.debt_status=True
    def debtor_or_creditor_status(self):
        if self.debt_or_credit_amount <0:
            return 'debtor'
        elif self.debt_or_credit_amount >0:
            return 'creditor'
        else:
            return '0'
class group(models.Model):
    pass
class bill(models.Model):
    pass

class dong(models.Model):
    pass

