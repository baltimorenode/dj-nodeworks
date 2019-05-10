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

class Person(models.Model):
    name = models.CharField(255)
    date_given_key = models.DateField()
    donation = models.ManyToManyField(Donation)
    subscription = models.ManyToManyField(Subscription)

    FEMINIE = 'F'
    MASCULINE = 'M'
    NEUTRAL = 'N'
    GENDER_PRONOUNS_CHOICES = (
        (FEMINIE, 'She, Her, Hers'),
        (MASCULINE, 'He, Him, His'),
        (NEUTRAL, 'Yo, Yo, Yo\'s'),
    )
    gender_pronouns = models.CharField(
        max_length=1,
        choices=GENDER_PRONOUNS_CHOICES,
        default=NEUTRAL,
    )
    
    key_holder = models.BooleanField(
        default=False
    )
    
    official_email = models.TextField(blank=True, null=True)
    bill_email = models.TextField(blank = True, null= True)
    mailing_list_email = models.TextField(blank = True, null= True)

    phone_numbers = models.TextField(blank=True, null=True)






