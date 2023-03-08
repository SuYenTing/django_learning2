from django.shortcuts import render, redirect
from order.forms import UserInfoForm
from order.models import UserInfo

# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/signupok')
            except:
                pass
    else:
        form = UserInfoForm()
    return render(request, 'signup.html', {'form': form})

def signupok(request):
    userInfo = UserInfo.objects.all()
    return render(request, 'signupok.html', {'userInfo': userInfo})