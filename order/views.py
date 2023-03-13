from django.shortcuts import render, redirect
from order.forms import UserInfoForm, MemberForm
from order.models import UserInfo, Member

# Create your views here.
def index(request):
    status = request.session.get('is_login')
    uname = request.session.get('uname')
    return render(request, 'index.html', locals())


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


def register(request):
    member = Member.objects.all()
    form = MemberForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():

            # 錯誤放置位置 如果遇重複申請帳號 則會讓session先記錄
            # request.session['is_login'] = True
            # request.session['email'] = form.cleaned_data['email']
            # request.session['pwd'] = form.cleaned_data['pwd']
            # request.session['uname'] = form.cleaned_data['uname']
            
            try:
                form.save()

                # 正確放置位置 資料庫確認儲存完後 才會讓session紀錄
                # request.session['is_login'] = True
                # request.session['email'] = Member.email
                # request.session['pwd'] = Member.pwd
                # request.session['uname'] = Member.uname
                request.session['is_login'] = True
                request.session['email'] = form.cleaned_data['email']
                request.session['pwd'] = form.cleaned_data['pwd']
                request.session['uname'] = form.cleaned_data['uname']                     
                    
                return redirect('/member')
            except:
                pass
    else:
        form = MemberForm()
    
    context = {
        'member': member,
        'form': form,
    }

    return render(request, 'register.html', context)


def member(request):
    status = request.session.get('is_login')
    email = request.session.get('email')
    pwd = request.session.get('pwd')
    uname = request.session.get('uname')
    if not status:
        return redirect('/')
    return render(request, 'member.html', locals())

def logout(request):
    request.session.flush()
    return redirect('/')
