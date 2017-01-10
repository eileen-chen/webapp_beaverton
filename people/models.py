import uuid
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class People(models.Model):

    # People field
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    birthday = models.DateField()
    age = models.CharField(max_length=10, null=True, blank=True)
    identity_number = models.CharField(max_length=30, db_index=True)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=50, null=True, blank=True)
    average_monthly_income = models.CharField(max_length=30, null=True, blank=True)
    

    weight = models.FloatField(null=True, blank=True)
    blood_type = models.CharField(max_length=1)

    #past_history = models.CharField(max_length=100, null=True, blank=True)
    hospital_records = models.CharField(max_length=100, null=True, blank=True)
    complaint = models.CharField(max_length=100, null=True, blank=True)
    food_allergy_history = models.CharField(max_length=100, null=True, blank=True)
    medicine_allergy_history = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = models.Manager()

    REQUIRED_FIELDS = ['name', 'gender', 'birthday',
                        'identity_number', 'phone']

    def __str__(self):
        return '%s %s %s' % (self.name, self.identity_number, self.phone)

class Contact(models.Model):

    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    people = models.ForeignKey(People, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.name, self.phone)

class PastHistory(models.Model):
    name = models.CharField(max_length=30)
    people = models.ManyToManyField(People)

    objects = models.Manager()
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        ordering = ('name',)


# class PastHistoryPeople(models.Model):
#     people = models.ForeignKey(People)
#     pasthistory = models.ForeignKey(PastHistory)

#     class Meta:
#         db_table = 'people_pasthistory_people'

#     def __str__(self):
#         return self