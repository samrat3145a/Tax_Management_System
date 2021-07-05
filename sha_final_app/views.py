from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import CandidateLoanMaster, CandidateTrainingMaster, CourseMaster, SourceMaster, call_mast, call_trans, \
    training_trans, loan_trans
from .forms import CandidateLoanMasterForm, CandidateLoanMasterUpdateForm, CandidateTrainingMasterForm, \
    CourseMasterForm, SourceMasterForm, call_mast_form, call_trans_form, \
    training_trans_form, CandidateTrainingMasterUpdateForm, CourseMasterEditForm, SourceMasterUpdateForm, \
    call_mast_form_update, loan_trans_form
from NewLoginSystem.models import loan_offer, SignupData
from datetime import datetime

from django.db import connection


# home template to navigate
def home(request):
    return render(request, "base.html")


########## **Training Candidate Master** ##########

def training_candidate_master(request):
    courseids = CourseMaster.objects.values('Course_ID', 'Course_Name')
    match = call_mast.objects.values('Candidate_ID', 'Candidate_name')
    if request.method == 'POST':
        if CandidateTrainingMaster.objects.filter(email=request.POST['email']).exists():
            messages.error(request, 'Entry with same E-mail Already exists!')
            return render(request, 'training_candidate/training_master.html', {'courseids': courseids, 'canids': match})

        form = CandidateTrainingMasterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record saved successfully...!')
            return render(request, 'training_candidate/training_master.html', {'courseids': courseids, 'canids': match})
        else:
            form = CandidateTrainingMasterForm()
            messages.error(request, 'Something Wrong')
            return render(request, 'training_candidate/training_master.html',
                          {'form': form, 'courseids': courseids, 'canids': match})
    return render(request, 'training_candidate/training_master.html', {'courseids': courseids, 'canids': match})


def delete_candidate_master(request, pk, template_name='training_candidate/training_master_confirm_delete.html'):
    contact = get_object_or_404(CandidateTrainingMaster, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('view_query_candidate_master')
    return render(request, template_name, {'object': contact})


def view_query_candidate_master(request):
    return render(request, 'training_candidate/training_master_view_query.html')


def view_query_show_candidate_master(request):
    if request.method == 'GET':
        qur = request.GET.get("key")
        if qur:
            match = CandidateTrainingMaster.objects.filter(canname__contains=qur)
            return render(request, "training_candidate/training_master_view_query.html", {'allCandidates': match})
        else:
            messages.warning(request, "Invalid Input!")
            return render(request, "training_candidate/training_master_view_query.html")
    return render(request, "training_candidate/training_master_view_query.html")


# update view for details
def update_candidate_master(request, pk):
    context = {}
    obj = get_object_or_404(CandidateTrainingMaster, pk=pk)
    form = CandidateTrainingMasterUpdateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('view_query_candidate_master')
        # add form dictionary to context
    context["form"] = form
    return render(request, "training_candidate/training_master_update.html", context)


########## **Training Candidate Master End** ##########


########## **Course Master** ##########

def course_master_new(request):
    if request.method == 'POST':
        if (CourseMaster.objects.filter(Course_Name=request.POST['Course_Name']).exists()):
            messages.error(request, 'The Course Already Exits')
            return render(request, 'course_master/course_master.html')

        form = CourseMasterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Course Added!')
            return render(request, 'course_master/course_master.html')
        else:
            form = CourseMasterForm()
            messages.error(request, 'Something Wrong')
            return render(request, 'course_master/course_master.html', {'form': form})
    return render(request, 'course_master/course_master.html')


def delete_course(request, pk, template_name='course_master/course_master_delete.html'):
    contact = get_object_or_404(CourseMaster, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('view_query_course')
    return render(request, template_name, {'object': contact})


def view_query_course(request):
    return render(request, 'course_master/course_master_view.html')


def view_query_show_course(request):
    if request.method == 'GET':
        qur = request.GET.get("key")
        if qur:
            match = CourseMaster.objects.filter(Course_Name__contains=qur)
            return render(request, "course_master/course_master_view.html", {'courses': match})
        else:
            messages.warning(request, "Invalid Input!")
            return render(request, "course_master/course_master_view.html")
    return render(request, "course_master/course_master_view.html")


# update view for details
def update_course(request, pk):
    context = {}
    obj = get_object_or_404(CourseMaster, pk=pk)
    form = CourseMasterEditForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('view_query_course')
    context["form"] = form
    return render(request, "course_master/course_update.html", context)


########## **Course Master End** ##########

########## **Source Master** ##########

def source_master_new(request):
    if request.method == 'POST':
        if (SourceMaster.objects.filter(Source_name=request.POST['Source_name']).exists()):
            messages.error(request, 'The Sourse Already Exits')
            return render(request, 'source_master/source_master.html')

        form = SourceMasterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New source Added!')
            return render(request, 'source_master/source_master.html')
        else:
            form = SourceMasterForm()
            messages.error(request, 'Something Wrong')
            return render(request, 'source_master/source_master.html', {'form': form})
    return render(request, 'source_master/source_master.html')


def view_query_source(request):
    return render(request, 'source_master/source_master_view.html')


def view_query_show_source(request):
    if request.method == 'GET':
        qur = request.GET.get("key")
        if qur:
            match = SourceMaster.objects.filter(Source_name__contains=qur)
            return render(request, "source_master/source_master_view.html", {'sources': match})
        else:
            messages.warning(request, "Invalid Input!")
            return render(request, "source_master/source_master_view.html")
    return render(request, "source_master/source_master_view.html")


def delete_source(request, pk, template_name='source_master/source_master_delete.html'):
    contact = get_object_or_404(SourceMaster, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('view_query_source')
    return render(request, template_name, {'object': contact})


# update view for details
def update_source(request, pk):
    context = {}
    obj = get_object_or_404(SourceMaster, pk=pk)
    form = SourceMasterUpdateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('view_query_source')
    context["form"] = form
    return render(request, "source_master/source_master_update.html", context)


########## *Source Master End** ##########

########## **Calling Master** ##########

def call_mast_save(request):
    match = SourceMaster.objects.values('Source_ID', 'Source_name')
    canid = call_mast.objects.all().count()+1
    if request.method == "POST":
        form = call_mast_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Records saved successfully! Your Generated Candidate ID is:")
            return render(request, "calling_master/calling_master_form.html", {'s_ids': match, 'canid': canid})
        else:
            messages.warning(request, "Invalid Form Input!!!")
            return render(request, "calling_master/calling_master_form.html", {'s_ids': match, 'canid': canid})
    return render(request, "calling_master/calling_master_form.html", {'s_ids': match, 'canid': canid})


def view_query_callmast(request):
    kbc = call_mast.objects.values('Candidate_name')
    return render(request, 'calling_master/calling_master_search.html', {'kbc': kbc})


def view_query_show_callmast(request):
    kbc = call_mast.objects.values('Candidate_name')
    if request.method == 'GET':
        qur = request.GET.get("abc")
        if qur:
            match = call_mast.objects.filter(Candidate_name__contains=qur)
            if match:
                return render(request, "calling_master/calling_master_search.html", {"mfind": match, 'kbc': kbc})
            else:
                messages.warning(request, "Invalid Input!")
                return render(request, "calling_master/calling_master_search.html", {'kbc': kbc})
    return render(request, "scalling_master/calling_master_search.html", {'kbc': kbc})


def call_mast_delete(request, pk, template="calling_master/call_master_delete.html"):
    contact = get_object_or_404(call_mast, pk=pk)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, "Successfully Deleted!")
        return redirect('view_query_callmast')
    return render(request, template, {'object': contact})


# update view for details
def update_calling_master(request, pk):
    context = {}
    obj = get_object_or_404(call_mast, pk=pk)
    form = call_mast_form_update(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('view_query_callmast')
        # add form dictionary to context
    context["form"] = form
    return render(request, "calling_master/calling_master_update.html", context)


########## **Calling Master End** ##########

########## Calling Transaction ##########
def call_trans_save(request):
    match = call_mast.objects.values('Candidate_ID', 'Candidate_name')
    if request.method == "POST":
        form = call_trans_form(request.POST)
        if form.is_valid():
            form.save()
            obj = call_trans.objects.latest('Transaction_id')
            tnid = getattr(obj, 'Transaction_id')
            messages.success(request, "Records saved successfully! Your Transaction ID is = ")
            return render(request, "calling_transaction/calling_transaction_form.html", {'canids': match, 'tnid': tnid})
        else:
            messages.warning(request, "Invalid Form Input!!!")
            return render(request, "calling_transaction/calling_transaction_form.html", {'canids': match})
    return render(request, "calling_transaction/calling_transaction_form.html", {'canids': match})


def view_query_calltrans(request):
    return render(request, 'calling_transaction/calling_transaction_search.html')


def view_query_show_calltrans(request):
    if request.method == 'GET':
        qur = request.GET.get("key")
        if qur:
            match = call_trans.objects.filter(Transaction_id__contains=qur)
            if match:
                return render(request, "calling_transaction/calling_transaction_search.html", {"find": match})
            else:
                messages.warning(request, "Invalid Search Request!!!")
                return render(request, "calling_transaction/calling_transaction_search.html")
    return render(request, "calling_transaction/calling_transaction_search.html")


def call_trans_delete(request, pk, template="calling_transaction/calling_transaction_delete.html"):
    contact = get_object_or_404(call_trans, pk=pk)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, "Successfully Deleted!")
        return redirect('view_query_calltrans')
    return render(request, template, {'object': contact})


########## Calling Transaction End ##########

########## Training Transaction ##########

def training_trans_save(request):
    courseids = CourseMaster.objects.values('Course_ID', 'Course_Name')
    qur = CandidateTrainingMaster.objects.values('canname')
    if request.method == "POST":
        form = training_trans_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Records saved successfully!")
            return render(request, "training_transacation/training_transaction_form.html",
                          {'courseids': courseids, 'cannames': qur})
        else:
            messages.warning(request, "Invalid Form Input!!!")
            return render(request, "training_transacation/training_transaction_form.html",
                          {'courseids': courseids, 'cannames': qur})
    return render(request, "training_transacation/training_transaction_form.html",
                  {'courseids': courseids, 'cannames': qur})


def view_query_trainingtrans(request):
    return render(request, 'training_transacation/training_transaction_search.html')


def view_query_show_trainingtrans(request):
    if request.method == 'GET':
        qur = request.GET.get("go")
        if qur:
            match = training_trans.objects.filter(Candidate_name__contains=qur)
            if match:
                return render(request, "training_transacation/training_transaction_search.html", {"aja": match})
            else:
                messages.warning(request, "Invalid Search Request!!!")
                return render(request, "training_transacation/training_transaction_search.html")
    return render(request, "training_transacation/training_transaction_search.html")


def training_trans_delete(request, pk, template="training_transacation/training_transaction_delete.html"):
    contact = get_object_or_404(training_trans, pk=pk)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, "Successfully Deleted!")
        return redirect('view_query_trainingtrans')
    return render(request, template, {'object': contact})


########## Training Transaction End ##########


########## **Loan Candidate Master** ##########

def loan_candidate_master(request):
    today = datetime.now().date()
    loan_offers = loan_offer.objects.filter(end_date__gte=today).values('offer_id', 'offer_name')
    authorised_by = SignupData.objects.values('id', 'email_id', 'employee_name')
    match = call_mast.objects.filter(Interested_area__exact="loan").values('Candidate_ID', 'Candidate_name',
                                                                           'Contact_number', 'Email_id')
    if request.method == 'POST':
        if CandidateLoanMaster.objects.filter(email=request.POST['email']).exists():
            messages.error(request, 'Entry with same E-mail Already exists!')
            return render(request, 'loan_candidate/loan_master.html',
                          {'loan_offers': loan_offers, 'authorised_by': authorised_by, 'canids': match})

        form = CandidateLoanMasterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record saved successfully...!')
            return render(request, 'loan_candidate/loan_master.html',
                          {'loan_offers': loan_offers, 'authorised_by': authorised_by, 'canids': match})
        else:
            print(form.errors)
            form = CandidateLoanMasterForm()
            messages.error(request, 'Something Wrong')
            return render(request, 'loan_candidate/loan_master.html',
                          {'form': form, 'loan_offers': loan_offers, 'authorised_by': authorised_by, 'canids': match})
    return render(request, 'loan_candidate/loan_master.html',
                  {'loan_offers': loan_offers, 'authorised_by': authorised_by, 'canids': match})


def loan_delete_candidate_master(request, pk, template_name='loan_candidate/loan_master_confirm_delete.html'):
    contact = get_object_or_404(CandidateLoanMaster, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('loan_view_query_candidate_master')
    return render(request, template_name, {'object': contact})


def loan_view_query_candidate_master(request):
    return render(request, 'loan_candidate/loan_master_view_query.html')


def loan_view_query_show_candidate_master(request):
    if request.method == 'GET':
        qur = request.GET.get("key")
        if qur:
            match = CandidateLoanMaster.objects.filter(canname__contains=qur)
            return render(request, "loan_candidate/loan_master_view_query.html", {'allloanCandidates': match})
        else:
            messages.warning(request, "Invalid Input!")
            return render(request, "loan_candidate/loan_master_view_query.html")
    return render(request, "loan_candidate/loan_master_view_query.html")


# update view for details
def loan_update_candidate_master(request, pk):
    context = {}
    obj = get_object_or_404(CandidateLoanMaster, pk=pk)
    form = CandidateLoanMasterUpdateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('loan_view_query_candidate_master')
        # add form dictionary to context
    context["form"] = form
    return render(request, "loan_candidate/loan_master_update.html", context)


########## **Loan Candidate Master End** ##########


########## loan Transaction ##########

def loan_trans_save(request):
    authorised_by = SignupData.objects.values('id', 'email_id', 'employee_name')
    qur = CandidateLoanMaster.objects.values('Loan_ID', 'canname', 'email', 'LoanAmount')
    if request.method == "POST":
        form = loan_trans_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Records saved successfully!")
            return render(request, "loan_transaction/loan_transaction_form.html",
                          {'authorised_by': authorised_by, 'cannames': qur})
        else:
            print(form.errors)
            messages.warning(request, "Invalid Form Input!!!")
            return render(request, "loan_transaction/loan_transaction_form.html",
                          {'authorised_by': authorised_by, 'cannames': qur})
    return render(request, "loan_transaction/loan_transaction_form.html",
                  {'authorised_by': authorised_by, 'cannames': qur})


def view_query_loantrans(request):
    return render(request, 'loan_transaction/loan_transaction_search.html')


def view_query_show_loantrans(request):
    if request.method == 'GET':
        qur = request.GET.get("go")
        if qur:
            match = loan_trans.objects.filter(Loan_Candidate_name__contains=qur)
            if match:
                return render(request, "loan_transaction/loan_transaction_search.html", {"aja": match})
            else:
                messages.warning(request, "Invalid Search Request!!!")
                return render(request, "loan_transaction/loan_transaction_search.html")
    return render(request, "loan_transaction/loan_transaction_search.html")


def loan_trans_delete(request, pk, template="loan_transaction/loan_transaction_delete.html"):
    contact = get_object_or_404(loan_trans, pk=pk)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, "Successfully Deleted!")
        return redirect('view_query_loantrans')
    return render(request, template, {'object': contact})


def update_loan_transaction(request, pk):
    context = {}
    obj = get_object_or_404(loan_trans, pk=pk)
    form = loan_trans_form(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('view_query_loantrans')
        # add form dictionary to context
    context["form"] = form
    return render(request, "loan_transaction/loan_transaction_update.html", context)