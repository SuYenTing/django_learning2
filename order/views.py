from django.shortcuts import render, redirect
from order.forms import UserInfoForm, MemberForm, MemberLoginForm, ProductForm
from order.models import UserInfo, Member, Product

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
                # 寫法1
                result = Member.objects.get(email=form.cleaned_data['email'])
                request.session['is_login'] = True
                request.session['email'] = result.email
                request.session['pwd'] = result.pwd
                request.session['uname'] = result.uname

                # # 寫法2
                # request.session['is_login'] = True
                # request.session['email'] = form.cleaned_data['email']
                # request.session['pwd'] = form.cleaned_data['pwd']
                # request.session['uname'] = form.cleaned_data['uname']                     
                    
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


def login(request):

    member = Member.objects.all()
    form = MemberLoginForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():

            email = form.cleaned_data['email']
            pwd = form.cleaned_data['pwd']
            result = Member.objects.filter(email=email, pwd=pwd).first()
            if not result:
                return redirect('/login')
            else:
                request.session['is_login'] = True
                request.session['email'] = result.email
                request.session['pwd'] = result.pwd
                request.session['uname'] = result.uname
                return redirect('/member')
    else:
        form = MemberLoginForm()
        context = {
            'form': form,
        }
        return render(request, 'login.html', context)
    

def update(request, email):

    status = request.session.get('is_login')
    if status:
        member = Member.objects.get(email=email)
        form = MemberForm(instance=member)
        if request.method == 'POST':
            form = MemberForm(request.POST, instance=member)
            if form.is_valid():
        
                try:
                    form.save()
                    request.session['is_login'] = True
                    request.session['email'] = form.cleaned_data['email']
                    request.session['pwd'] = form.cleaned_data['pwd']
                    request.session['uname'] = form.cleaned_data['uname']                       
                    return redirect('/updateok')
                except:
                    pass

        context = {
            'member': member,
            'form': form,
        }

        return render(request, 'update.html', context)
    
    else:
        return redirect('/')
    

def updateok(request):
    status=request.session.get('is_login')
    email=request.session.get('email')
    pwd=request.session.get('pwd')
    uname=request.session.get('uname')
    if not status:
        return redirect('/')
    return render(request,'updateok.html',locals())


def delete(request, email):

    status = request.session.get('is_login')
    if status:

        member = Member.objects.get(email=email)
        member.delete()
        logout(request)
        return render(request, 'index.html', {'delflag': True})
    
    else:
        return redirect('/')


def productshows(request):
    status = request.session.get('is_login')
    if status:
        uname = request.session.get('uname')
        product = Product.objects.all()
        return render(request, 'productshows.html', locals())
    else:
        return redirect('/')
    

def productedit(request, id):
    status = request.session.get('is_login')
    if not status:
        return redirect('/')
    
    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
    
            try:
                form.save()
                return redirect('/proudcteditok')
            except:
                pass    

    return render(request, 'productedit.html', locals())


def producteditok(request):
    status=request.session.get('is_login')
    if not status:
        return redirect('/')
    return render(request,'proudcteditok.html', locals())