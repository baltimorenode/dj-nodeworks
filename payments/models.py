# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Donation(models.Model):
    custid = models.TextField(primary_key=True)
    email = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'donations'

    def __str__(self):
        return '{}: {} (${} on {})'.format(
            self.custid, self.email, self.value, self.date
        )


class Subscription(models.Model):
    SUBSCRIPTION_PLANS = {
        # plan name: amount in cents
        'test': 100,
        'member': 5000,
        'family': 7500,
        'supporter': 1000,
        'student': 2500,
    }

    custid = models.TextField(primary_key=True)
    email = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    plan = models.TextField(blank=True, null=True)
    utoken = models.TextField(blank=True, null=True)

    @property
    def amount(self):
        return self.SUBSCRIPTION_PLANS[self.plan]

    class Meta:
        managed = False
        db_table = 'subscriptions'

    def __str__(self):
        return '{}: {} ({} initiated on {})'.format(
            self.custid, self.email, self.plan, self.date
        )
