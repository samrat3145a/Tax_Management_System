from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect, get_object_or_404

from NewLoginSystem.forms import SignupForm, UserUpdateForm
from .forms import offer_form
from .models import SignupData, loan_offer


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have successfully login!')
            return redirect('home')
        else:
            messages.success(request, ' Error Logging In / Please try again !')
            return redirect('login')
    else:
        return render(request, 'NewLoginSystem/login.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        employee_name = request.POST.get("first_name")
        email_id = request.POST.get("email")
        contact_no = request.POST.get("ContactNo")
        user_name = request.POST.get("username")
        last_qualification = request.POST.get("Last_qualification")
        salary = request.POST.get("Salary")
        id_proof_no = request.POST.get("Id_proof_no")
        id_proof_name = request.POST.get("Id_proof_name")
        address = request.POST.get("Address")
        state = request.POST.get("State")
        designation = request.POST.get("DESIGNATION")
        profile_pic = request.POST.get("pic")
        country = request.POST.get("Country")
        date_of_birth = request.POST.get("DOB")
        pincode = request.POST.get("Pincode")
        status = request.POST.get("Status")
        New_Data = SignupData(employee_name=employee_name, email_id=email_id, contact_no=contact_no,
                              user_name=user_name, last_qualification=last_qualification, salary=salary,
                              id_proof_name=id_proof_name, id_proof_no=id_proof_no, address=address,
                              state=state, designation=designation, profile_pic=profile_pic,
                              country=country, pincode=pincode, date_of_birth=date_of_birth,
                              status=status)
        New_Data.save()
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            messages.success(request, 'Please Enter Valid Details !')
            return redirect('signup')
    else:
        form = SignupForm()
    all_data_count = SignupData.objects.all().count()
    all_data_count = all_data_count + 1
    return render(request, 'NewLoginSystem/registration.html', {'form': form, 'count': all_data_count})


def home(request):
    all_data = SignupData.objects.all()
    return render(request, 'NewLoginSystem/home.html', {'data': all_data})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You have successfully logout!')
        return redirect('login')


##############################################################################
def offer_master_new(request):
    match = SignupData.objects.values('id', 'employee_name')
    count = loan_offer.objects.all().count() + 1
    if request.method == 'POST':
        if loan_offer.objects.filter(offer_name=request.POST['offer_name']).exists():
            messages.error(request, 'The offer Already Exits')
            return render(request, 'offer_master/offer_master.html', {'count': count, 'match_id': match})

        form = offer_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New offer Added!')
            return render(request, 'offer_master/offer_master.html', {'count': count, 'match_id': match})
        else:
            form = offer_form()
            messages.error(request, 'Something Wrong')
            return render(request, 'offer_master/offer_master.html', {'form': form})

    return render(request, 'offer_master/offer_master.html', {'match_id': match, 'count': count})


def delete_offer(request, pk, template_name='offer_master/offer_master_delete.html'):
    contact = get_object_or_404(loan_offer, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('view_query_offer')
    return render(request, template_name, {'object': contact})


def view_query_offer(request):
    all_offer = loan_offer.objects.all()
    return render(request, 'offer_master/offer_master_view.html', {'all_offer': all_offer})


def view_query_show_offer(request):
    all_offer = loan_offer.objects.all()
    if request.method == 'GET':
        qur = request.GET.get("key")
        if qur:
            match = loan_offer.objects.filter(offer_name__contains=qur)
            return render(request, "offer_master/offer_master_view.html", {'offers': match})
        else:
            messages.warning(request, "Invalid Input!")
            return render(request, "offer_master/offer_master_view.html")
    return render(request, "offer_master/offer_master_view.html", {'all_offer': all_offer})


# update view for details
def update_offer(request, pk):
    context = {}
    obj = get_object_or_404(loan_offer, pk=pk)
    form = offer_form(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('view_query_offer')
    context["form"] = form
    return render(request, "offer_master/offer_master_update.html", context)

##################################################################################
