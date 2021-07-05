from django.db import models

Designation_choices = (('manager', 'Manager'), ('employee', 'Employee'))


# Create your models here.
class SignupData(models.Model):
    employee_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100, unique=True)
    contact_no = models.BigIntegerField()
    user_name = models.CharField(max_length=100)
    last_qualification = models.CharField(max_length=100)
    salary = models.BigIntegerField()
    id_proof_no = models.BigIntegerField()
    id_proof_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    designation = models.CharField(max_length=20, choices=Designation_choices, default='Manager')
    profile_pic = models.FileField(upload_to="projectimg/", default=True)
    country = models.CharField(max_length=100)
    pincode = models.BigIntegerField()
    date_of_birth = models.DateField(max_length=100)
    date_of_registration = models.DateField(auto_now=True)
    time_of_registration = models.TimeField(auto_now=True)
    status = models.CharField(max_length=100)

    class Meta:
        db_table = "Signup Data"

    def __str__(self):
        return self.email_id


class loan_offer(models.Model):
    offer_id = models.AutoField(primary_key=True)
    offer_name = models.CharField(max_length=50)
    discount = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    remarks = models.TextField(max_length=300)
    employee_id = models.IntegerField()
    date_of_entry = models.DateField()

    def _str_(self):
        return self.offer_id
