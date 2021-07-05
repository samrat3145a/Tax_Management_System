from django import forms
from .models import CandidateLoanMaster, loan_trans, CandidateTrainingMaster, CourseMaster, SourceMaster, call_mast, \
    call_trans, training_trans


# from NewLoginSystem.models import loan_offer
# CandidateLoanMasterForm
class CandidateLoanMasterForm(forms.ModelForm):
    class Meta:
        model = CandidateLoanMaster
        fields = "__all__"


class CandidateLoanMasterUpdateForm(forms.ModelForm):
    Status = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CandidateLoanMaster
        fields = "__all__"


# loan transaction
class loan_trans_form(forms.ModelForm):
    class Meta:
        model = loan_trans
        fields = "__all__"


# CourseMasterForm
class CourseMasterForm(forms.ModelForm):
    class Meta:
        model = CourseMaster
        fields = "__all__"


class CourseMasterEditForm(forms.ModelForm):
    Fees = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}))

    class Meta:
        model = CourseMaster
        fields = ["Fees"]


# CandidateTrainingMasterForm
class CandidateTrainingMasterForm(forms.ModelForm):
    class Meta:
        model = CandidateTrainingMaster
        fields = "__all__"


class CandidateTrainingMasterUpdateForm(forms.ModelForm):
    Placement = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Status = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CandidateTrainingMaster
        fields = ["Placement", "Status"]


# SourceMasterForm
class SourceMasterForm(forms.ModelForm):
    class Meta:
        model = SourceMaster
        fields = "__all__"


class SourceMasterUpdateForm(forms.ModelForm):
    Rate_per_candidate = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}))
    Contact_no = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}))
    City = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    State = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = SourceMaster
        fields = ["Rate_per_candidate", "Contact_no", "City", "State"]


class call_mast_form(forms.ModelForm):
    class Meta:
        model = call_mast
        fields = "__all__"


class call_mast_form_update(forms.ModelForm):
    Contact_number = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}))
    Email_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = call_mast
        fields = ["Contact_number", "Email_id"]


class call_trans_form(forms.ModelForm):
    class Meta:
        model = call_trans
        fields = "__all__"


class training_trans_form(forms.ModelForm):
    class Meta:
        model = training_trans
        fields = "__all__"
