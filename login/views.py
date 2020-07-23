from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            print("logged in")

            auth.login(request, user)
            return redirect('/')
        else:
            print("failure")
            return redirect('login')
    else:
        print("yommon failure")
        return render(request, 'login.html')


# Create your views here.
def register(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        user = User.objects.create(first_name=first_name, last_name=last_name, username=username, password=password1,
                                   email=email)
        user.save()
        return redirect('login')


    else:
        return render(request, 'register.html')

