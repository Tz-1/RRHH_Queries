from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseRedirect


from .models import *
from .forms import *

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"Welcome: {username}.")
                next_url = request.GET.get('next', '/')
                return HttpResponseRedirect(next_url)
    else:
        form = AuthenticationForm()

    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_view(request):
    logout(request)
    messages.info(request, "Bye.")
    return HttpResponseRedirect('/')


@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        choice_businessid = request.POST.get('select_businessid')
        choice_jobtitle = request.POST.get('select_jobtitle')
        choice_gender = request.POST.get('select_gender')

        datos_persona = []
        if choice_businessid != '':
            datos_persona = Person.objects.filter(businessentityid = choice_businessid).values('firstname', 'lastname', 'businessentityid', 'employee__jobtitle', 'employee__gender')

        if choice_jobtitle  != '' and choice_businessid == '':
            datos_persona = Person.objects.filter(employee__jobtitle = choice_jobtitle).values('firstname', 'lastname', 'businessentityid', 'employee__jobtitle', 'employee__gender')

        if choice_gender  != '' and choice_jobtitle == '' and choice_businessid == '':
            datos_persona = Person.objects.filter(employee__gender = choice_gender).values('firstname', 'lastname', 'businessentityid', 'employee__jobtitle', 'employee__gender')
    
        if choice_businessid != '' and choice_jobtitle != '':
            datos_persona = Person.objects.filter(businessentityid = choice_businessid, employee__jobtitle = choice_jobtitle).values('firstname', 'lastname', 'businessentityid', 'employee__jobtitle', 'employee__gender')

        if choice_businessid != '' and choice_gender != '':
            datos_persona = Person.objects.filter(businessentityid = choice_businessid, employee__gender = choice_gender).values('firstname', 'lastname', 'businessentityid', 'employee__jobtitle', 'employee__gender')

        if choice_gender != '' and choice_jobtitle != '': 
            datos_persona = Person.objects.filter(employee__gender = choice_gender, employee__jobtitle = choice_jobtitle).values('firstname', 'lastname', 'businessentityid', 'employee__jobtitle', 'employee__gender')

        if choice_gender  != '' and choice_jobtitle != '' and choice_gender != '':
            datos_persona = Person.objects.filter(employee__jobtitle = choice_jobtitle, employee__gender = choice_gender, businessentityid = choice_businessid).values('firstname', 'lastname', 'businessentityid', 'employee__jobtitle', 'employee__gender')

        if (choice_businessid != '' or choice_jobtitle != '' or choice_gender != '') and not datos_persona:
            messages.error(request, "The choices don't match with any data in our Database.")

        context = { 'person': datos_persona, 'form': ChoiceForm() }

    else:
        form = ChoiceForm()

        datos_persona = (Person.objects.filter(businessentityid=1).values('firstname', 'lastname', 'businessentityid', 'employee__jobtitle', 'employee__gender') | 
                         Person.objects.filter(businessentityid=2).values('firstname', 'lastname', 'businessentityid', 'employee__jobtitle', 'employee__gender') |
                         Person.objects.filter(businessentityid=3).values('firstname', 'lastname', 'businessentityid', 'employee__jobtitle', 'employee__gender'))
                        
        context = { 'person': datos_persona, 'form': form}

    return render(request, 'form.html', context)


