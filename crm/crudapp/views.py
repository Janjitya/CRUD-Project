from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from .models import Records
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

# ---home
def home(request):
    return render(request, 'crudapp/index.html')

# --- register
def register(request):

    form = CreateUserForm()

    if(request.method == 'POST'):

        form = CreateUserForm(request.POST)

        if(form.is_valid()):

            form.save()

            messages.success(request, "User created successfully!")

            return redirect('login')

    context = {'form':form}

    return render(request,"crudapp/register.html", context=context)

# login
def user_login(request):

    form = LoginForm()

    if(request.method == 'POST'):

        form = LoginForm(request, data=request.POST)

        if(form.is_valid()):

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if(user is not None):

                auth.login(request, user)

                messages.success(request, "Login successfull")

                return redirect('dashboard')

    context = {'form':form}

    return render(request, "crudapp/login.html", context=context)

# logout
def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logout successfull")

    return redirect('login')

#dashboard
@login_required(login_url='login')
def dashboard(request):

    my_records = Records.objects.all()

    context = {'records':my_records}

    return render(request, 'crudapp/dashboard.html', context=context)

@login_required(login_url='login')
def create_record(request):
    
    form = CreateRecordForm()

    if(request.method == 'POST'):

        form = CreateRecordForm(data= request.POST)

        if(form.is_valid()):

            form.save()

            messages.success(request, "Record added successfully!")

            return redirect('dashboard')
        
    context = {'form': form}

    return render(request, 'crudapp/create.html', context=context)

# update record
@login_required(login_url='login')
def update_record(request, pk):
    
    record = Records.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if(request.method == 'POST'):

        form = UpdateRecordForm(data=request.POST, instance=record)

        if(form.is_valid()):

            form.save()

            messages.success(request, "Record updated successfully!")

            return redirect('dashboard')
        
    context = {'form':form}

    return render(request, 'crudapp/update.html', context=context)

# view record
@login_required(login_url='login')
def view_record(request,pk):

    all_record = Records.objects.get(id=pk)

    context = {'record':all_record}

    return render(request,'crudapp/view-record.html', context=context)

# delete record
@login_required(login_url='login')
def delete_record(request, pk):

    record = Records.objects.get(id=pk)

    record.delete()

    messages.success(request, "Record deleted successfully!")

    return redirect('dashboard')




