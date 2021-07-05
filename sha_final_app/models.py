from django.db import models
from NewLoginSystem.models import loan_offer, SignupData


# Create your models here.

class SourceMaster(models.Model):
    Source_ID = models.AutoField(primary_key=True)
    Source_name = models.CharField(max_length=100)
    Rate_per_candidate = models.BigIntegerField()
    Contact_no = models.BigIntegerField()
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Employee_id = models.CharField(max_length=100, blank=True, null=True)
    Date_of_Entry = models.DateTimeField("Created At", auto_now_add=True)


class CourseMaster(models.Model):
    Course_ID = models.AutoField(primary_key=True)
    Course_Name = models.CharField(max_length=100)
    Fees = models.BigIntegerField()


class call_mast(models.Model):
    Candidate_ID = models.AutoField(primary_key=True)
    Candidate_name = models.CharField(max_length=255)
    Contact_number = models.CharField(max_length=255)
    Email_id = models.CharField(max_length=255)
    Interested_area = models.CharField(max_length=255)
    Source_name = models.ForeignKey(SourceMaster, db_column='Source_ID', to_field='Source_ID', related_name='+',
                                    default=1, on_delete=models.SET_DEFAULT)
    Receiving_date = models.DateField()

    class Meta:
        db_table = "calling master"


class call_trans(models.Model):
    Transaction_id = models.AutoField(primary_key=True)
    Candidate_ID = models.ForeignKey(call_mast, db_column='Candidate_ID', to_field='Candidate_ID', related_name='+',
                                     default=1, on_delete=models.SET_DEFAULT)
    Feedback = models.CharField(max_length=100)
    Next_Call_Date = models.DateField()
    Next_Call_Time = models.TimeField()
    Cofirm = models.CharField(max_length=100)
    Call_Date = models.DateField()
    Call_Time = models.TimeField()

    class Meta:
        db_table = "calling transaction"


class CandidateTrainingMaster(models.Model):
    Training_ID = models.AutoField(primary_key=True)
    Candidate_ID = models.ForeignKey(call_mast, db_column='Candidate_ID', to_field='Candidate_ID', related_name='+',
                                     default=1, on_delete=models.SET_DEFAULT)
    canname = models.CharField(max_length=100)
    ContactNo = models.BigIntegerField()
    email = models.EmailField()
    qualification = models.CharField(max_length=250, )
    idProofName = models.CharField(max_length=250)
    idProofNo = models.CharField(max_length=250)
    dateOfBirth = models.DateField()
    Course_ID = models.ForeignKey(CourseMaster, db_column='Course_ID', to_field='Course_ID', related_name='+',
                                  default=1, on_delete=models.SET_DEFAULT)
    Placement = models.CharField(max_length=250)
    callId = models.IntegerField()
    Address = models.TextField()
    parentName = models.CharField(max_length=250)
    offerId = models.IntegerField()
    ParentCont = models.CharField(max_length=250)
    dateOfReg = models.DateField()
    Status = models.CharField(max_length=250)
    paymentDueDay = models.DateField()
    noOfInstallments = models.IntegerField()
    Date_of_entry = models.DateTimeField("Created At", auto_now_add=True)


class training_trans(models.Model):
    Payment_ID = models.AutoField(primary_key=True)
    Candidate_name = models.CharField(max_length=100)
    Date_of_transaction = models.DateField()
    Course_ID = models.ForeignKey(CourseMaster, db_column='Course_ID', to_field='Course_ID', related_name='+',
                                  default=1, on_delete=models.SET_DEFAULT)
    Course_amount = models.CharField(max_length=100)
    Payment_mode = models.CharField(max_length=100)
    Amount_deposited = models.CharField(max_length=100)
    Bank_transaction_id = models.CharField(max_length=20)
    Bank_account_number = models.CharField(max_length=20)
    Cheque_number = models.CharField(max_length=100)
    Warning_level = models.CharField(max_length=100)
    Payment_status = models.CharField(max_length=100)
    Reason_for_nonPayment = models.CharField(max_length=100)

    class Meta:
        db_table = "training transaction"


class CandidateLoanMaster(models.Model):
    Loan_ID = models.AutoField(primary_key=True)
    Candidate_ID = models.ForeignKey(call_mast, db_column='Candidate_ID', to_field='Candidate_ID', related_name='+',
                                     default=1, on_delete=models.SET_DEFAULT)
    canname = models.CharField(max_length=100)
    ContactNo = models.CharField(max_length=60)
    email = models.EmailField()
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=50)
    Occupation = models.CharField(max_length=250)
    idProofName = models.CharField(max_length=250)
    idProofNo = models.CharField(max_length=250)
    inputCity = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=100)
    country = models.CharField(max_length=200)
    photograph = models.ImageField(upload_to="projectimg/", default=True)
    medicalrecord = models.ImageField(upload_to="projectimg/", default=True)
    bankname = models.CharField(max_length=100)
    bankrecord = models.FileField(upload_to="projectimg/", default=True)
    accountholdername = models.CharField(max_length=150)
    accountno = models.CharField(max_length=250)
    ifsccode = models.CharField(max_length=50)
    purpose = models.TextField(max_length=2500)
    LoanAmount = models.CharField(max_length=40)
    RateofInt = models.SmallIntegerField()
    Offer_ID = models.ForeignKey(loan_offer, db_column='Offer_ID', to_field='offer_id', related_name='+',
                                 default=1, on_delete=models.SET_DEFAULT)
    Dateofsaction = models.DateField()
    Dateofdisbursment = models.DateField()
    Security = models.FileField(upload_to="projectimg/", default=True)
    NoofInstalment = models.BigIntegerField()
    EMIlimit = models.CharField(max_length=60)
    NoofFamilymembers = models.BigIntegerField()
    MonthlyFamilyEarnings = models.CharField(max_length=100)
    dateOfReg = models.DateField()
    Status = models.CharField(max_length=250)
    Authorised_by = models.ForeignKey(SignupData, db_column='Authorised_by', to_field='email_id', related_name='+',
                                      default=1, on_delete=models.SET_DEFAULT)

    Date_of_entry = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return str(self.Loan_ID)


class loan_trans(models.Model):
    loan_transaction_id = models.AutoField(primary_key=True)
    loan_candidate_details = models.ForeignKey(CandidateLoanMaster, db_column='loan_candidate_details',
                                               to_field='Loan_ID', related_name='+',
                                               default=1, on_delete=models.SET_DEFAULT)
    Loan_Candidate_name = models.CharField(max_length=100)
    Date_of_transaction = models.DateField()
    amount_deposit = models.CharField(max_length=50)
    principal_amount = models.CharField(max_length=50)
    Payment_mode = models.CharField(max_length=100)
    Bank_transaction_id = models.CharField(max_length=50)
    Bank_account_number = models.CharField(max_length=50)
    Cheque_number = models.CharField(max_length=100)
    UPI_Ewallet_id = models.CharField(max_length=100)
    Warning_level = models.CharField(max_length=100)
    Payment_status = models.CharField(max_length=50)
    Reason_for_nonPayment = models.CharField(max_length=250)
    Date_of_entry = models.DateTimeField("Created At", auto_now_add=True)
    Authorised_by = models.ForeignKey(SignupData, db_column='Authorised_by', to_field='email_id', related_name='+',
                                      default=1, on_delete=models.SET_DEFAULT)

    def _str_(self):
        return self.loan_transaction_id
