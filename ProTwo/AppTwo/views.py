from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import Sign_Up_Form

# Create your views here.

def index(request):
    return render(request, "AppTwo/index.html")

def help(request):
    my_dict = {'insert_me':"Help Page"}
    return render(request, "AppTwo/help.html",context=my_dict)

def users(request):
    users_list = User.objects.order_by('last_name')
    users_dict = {'users_list':users_list}
    return render(request, "AppTwo/users.html",context=users_dict)

def signup_view(request):

    form = Sign_Up_Form()

    if request.method=="POST":
        form = Sign_Up_Form(request.POST)
        if form.is_valid():
            new_user = form.save(commit=True)
            return index(request) # Go to homepage when form is valid
        else:
            "Form is invalid!!!"
    return render(request,'AppTwo/signup.html',{'form':form}) # If form is invalid reload it
