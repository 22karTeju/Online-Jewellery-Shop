from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from Japp.models import product,Cart,Order
from django.db.models import Q
import random
import razorpay
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        userid=request.user.id
        #print("id of logged in user:",userid)
        #print("Result:",request.user.is_authenticated)
        context={}
        p=product.objects.filter(is_active=True)
        context['products']=p
        print(p)
        return render(request,"index.html",context)
    else:
        return render(request,"login.html")

def aboutus(request):
    return render(request,"about.html")

def pdetails(request,pid):
    context={}
    p=product.objects.filter(id=pid)
    context['products']=p
    return render(request,"pdetails.html",context)


def viewcart(request):
    c=Cart.objects.filter(uid=request.user.id)
    print(c)
    #print(c[0].pid)
    #print(c[0].uid)
    #print(c[0].pid.name)
    context={}
    context['data']=c
    s=0
    for x in c:
        #print(x)
        #print(x.pid.price)
        s=s+x.pid.price*x.qty
    print(s)
    context['total']=s
    np=len(c)
    context['items']=np
    return render(request,"viewcart.html",context)


def register(request):
    if request.method=="POST":
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        #print(uname)
        context={}
        if uname=="" or upass=="" or ucpass=="":
            context['errmsg']="Feilds cannot be empty"
            return render(request,"register.html",context)
        elif upass!=ucpass:
            context['errmsg']="Password didn't match"
            return render(request,"register.html",context)
        else:
            try:
                u=User.objects.create(password=upass,username=uname,email=uname)
                u.set_password(upass)
                u.save()     
                context['success']="User registered sucessfully"
                return render(request,"register.html",context)
                #return HttpResponse("Data fetched")
            except Exception:
                 context['success']="Username already existes!! Try again."
                 return render(request,"register.html",context)
    else:
       return render(request,"register.html")

def ulogin(request):
    if request.method=="POST":
        uname=request.POST['uname']
        upass=request.POST['upass']
        context={}
        if uname=="" or upass=="":
            context['errmsg']="Feilds cannot be empty"
            return render(request,"login.html",context)
            
        else:
            u=authenticate(username=uname,password=upass)
           
            if u is not None:
                print("inif")
                login(request,u)
                print("login")
                return redirect ('/home')
            else:
                context['errmsg']="Invalid Username/password" 
                print("innerelse")  
                return render(request,"login.html",context)
    else:
        print("outerelse")
        return render(request,"login.html")

def ulogout(request):
    logout(request)
    #return redirect('/home')
    return render(request,"index.html")


def catfilter(request,cv):
    q1=Q(is_active=True)
    q2=Q(Cat=cv)
    p=product.objects.filter(q1 & q2)
    context={}
    context['products']=p
    return render(request,"index.html",context)

def Pfilter(request,pv):
    q1=Q(is_active=True)
    q2=Q(Product_Name=pv)
    p=product.objects.filter(q1 & q2)
    context={}
    context['products']=p
    return render(request,"index.html",context)



def range(request):
    min=request.GET['min']
    max=request.GET['max']
    q1=Q(price__gte=min)
    q2=Q(price__lte=max)
    q3=Q(is_active=True)
    p=product.objects.filter(q1 & q2 & q3)
    context={}
    context['products']=p
    return render(request,"index.html",context)

def addtocart(request,pid):
    if request.user.is_authenticated:
        userid=request.user.id
        u=User.objects.filter(id=userid)
        print(u)
        p=product.objects.filter(id=pid)
        print(p)
        q1=Q(uid=u[0])
        q2=Q(pid=p[0])
        c=Cart.objects.filter(q1 & q2)
        print(c)
        context={}
        n=len(c)
        if n==1:
            context['errmsg']="Product already exists in a cart"
            context['products']=p
            return render(request,'pdetails.html',context)
        else:
            c=Cart.objects.create(uid=u[0],pid=p[0])
            c.save()
            context['success']="Product added to cart!!"
            context['products']=p
            return render(request,"pdetails.html",context)  
    else:
        return redirect("/login")


def remove(request,cid):
    c=Cart.objects.filter(id=cid)
    c.delete()
    return redirect('/viewcart')

def oremove(request,cid):
    c=Order.objects.filter(id=cid)
    c.delete()
    return redirect('/placeorder')

def updateqty(request,qv,cid):
    c=Cart.objects.filter(id=cid)
    print(c[0])
    print(c[0].qty)
    if qv=='1':
        t=c[0].qty+1
        c.update(qty=t)
    else:
       t=c[0].qty-1
       c.update(qty=t)
    return redirect('/viewcart')



def placeorder(request):
    userid=request.user.id
    c=Cart.objects.filter(uid=userid)
    oid=random.randrange(1000,9999)
    print(oid)
    for x in c:
        o=Order.objects.create(order_id=oid,pid=x.pid,uid=x.uid,qty=x.qty)
        o.save()
        x.delete()
    orders=Order.objects.filter(uid=request.user.id)
    context={}
    context['data']=orders
    s=0
    for x in orders:
        #print(x)
        #print(x.pid.price)
        s=s+x.pid.price*x.qty
    context['total']=s
    np=len(orders)
    context['items']=np
    return render(request,"placeorder.html",context)
    


def makepayment(request):
    orders=Order.objects.filter(uid=request.user.id)
    s=0
    np=len(orders)
    for x in orders:
        #print(x)
        #print(x.pid.price)
        s=s+x.pid.price*x.qty
        oid=x.order_id 
        x.delete()
    client = razorpay.Client(auth=("rzp_test_pI78IUyevrXhIQ", "BJuKUOHRoVdj97SpkIL5aL6R"))
    data = { "amount":s*100, "currency": "INR", "receipt": "oid" }
    payment = client.order.create(data=data)
    context={}
    context['data']=payment
    return render(request,"pay.html",context)

def sendusermail(request):
    send_mail(
        "Your order placed successfully",
        "Order completed !! THANK YOU.",
        "ketn.pawar07@gmail.com",
        ["22karneha16@gmail.com"],
        fail_silently=False,     
    )
    context={}
    context['emailsend']="Email Sent Successfully"
    return render(request,'index.html',context)