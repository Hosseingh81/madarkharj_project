from madarkharj.models import Member,Group,Bill,Share

class queries:
    """
    this class do required queries for the madarkharj app.
    """
    def __init__(self,members=None,groups=None,bills=None,shares=None,user=None):
        self.members=members
        self.groups=groups
        self.bills=bills
        self.shares=shares
        self.user=user

    def group_guery(self):   #this func returns a query sets of groups.
        return Group.objects.filter(member=self.members)