import random
import sys
from datetime import date, datetime

from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from moverspackers import settings
from mpm.forms import *
from mpm.models import *
from django.core.mail import send_mail

from django.http import JsonResponse

def load_menu1(request):
    cid = request.session['id']
    c = Customer.objects.get(customer_id=cid)
    return render(request,"test1.html",{"c":c })

def home(request):
    s = Service_category.objects.all()
    c=Customer.objects.all().count
    t=TransportCompany.objects.all().count
    b=Booking.objects.all().count
    d=Driver.objects.all().count
    f=Feedback.objects.all()
    t1 = TransportCompany.objects.all()
    v = Vehicle_category.objects.all()
    return render(request,"home.html",{"c1":c,"t1":t,"b1":b,"d1":d,"f1":f,"s1":s,"t2":t1 ,"v" : v})



def customer_login(request):
    a=Area.objects.all()
    c=Customer.objects.all()
    if request.method == "POST":
        u = request.POST["email"]
        p = request.POST["password"]

        val = Customer.objects.filter(email=u, password=p , is_admin = 0).count()

        if val == 1:
            data = Customer.objects.filter(email=u, password=p , is_admin = 0)
            for items in data:
                request.session['username'] = items.email
                request.session['id'] = items.customer_id
                request.session['name'] = items.customer_name

                if request.POST.get("remember"):
                    response = redirect("/client/Home/")
                    response.set_cookie('client_email', request.POST["email"])
                    response.set_cookie('client_pass', request.POST["password"])
                    return response

            return redirect('/client/Home/')
        else:
            messages.error(request, "Invalid E-mail id or password")
            return render(request, "customer_login.html")

    else:
        if request.COOKIES.get("client_email"):
            return render(request, "customer_login.html",
                          {'client_cookie_email': request.COOKIES['client_email'],
                           'client_cookie_password': request.COOKIES['client_pass']})
        else:
            return render(request, "customer_login.html")

    return render(request, "customer_login.html",{"a":a,"c":c })


def forgotpassword(request):
    return render(request,"client_forgotpassword.html")


def sendotp(request):
    otp1=random.randint(1000,9999)
    e=request.POST['email']

    print("---------------",e)
    request.session['temail']=e
    obj=Customer.objects.filter(email=e , is_admin=0).count()

    if obj == 1:
        val = Customer.objects.filter(email=e , is_admin=0).update(OTP=otp1 , OTP_used=0)
        subject = 'OTP Verification'
        message = str(otp1)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]
        send_mail(subject, message, email_from, recipient_list)
        return render(request, 'client_resetpassword.html')

    else:
        messages.error(request, " Invalid E-mail ")
        return render(request, "client_forgot_password.html")

    return render(request, 'client_resetpassword.html')

def setpassword(request):
    totp=request.POST.get('otp')
    tpassword=request.POST.get('npass')
    cpassword=request.POST.get('cpass')

    if tpassword == cpassword:
        e = request.session['temail']
        val = Customer.objects.filter(email=e , is_admin=0 , OTP = totp , OTP_used = 0).count()

        if val == 1:
            val=Customer.objects.filter(email=e , is_admin = 0 ).update(OTP_used = 1 , password = tpassword)
            return redirect('/client/client_login/')

        else:
            messages.error(request,'otp does not match')
            return render(request,"client_resetpassword.html")

    else:
        messages.error(request,"New Password & Confirm Password does not match")
        return render(request,"client_resetpassword.html")

    return render(request,"client_resetpassword.html")


def client_register(request):
    a=Area.objects.all()
    c=Company.objects.all()
    if request.method=="POST":
        form=customerform(request.POST)
        print("--------",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/client/Home/')
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form=customerform()

    return render(request,"client_registration.html",{"form":form ,"a":a ,"c":c })






def client_package(request,id):
   #id=request.POST['TransportCompany_id']
   #p=Package.objects.filter(TransportCompany_id=id)
        #return render(request,"pricing.html",{"p":p})
   s=Package.objects.filter(service_category_id=id,TransportCompany_id_id=id)
   print("---",s)
   return render(request,"pricing.html",{"p1":s})

def client_package2(request,id,id2):
    i=int(id2)
    #id=request.POST['TransportCompany_id']
    #p=Package.objects.filter(TransportCompany_id=id)
    #return render(request,"pricing.html",{"p":p})
    s=Package.objects.filter(service_category_id=id,TransportCompany_id_id=id)
    return render(request,"pricing2.html",{"p1":s,"id":i})



def client_vehicle_category(request,id,id2):
    v = TransportCompany_Vehicle_category.objects.filter(TransportCompany_id=id2)
    p=int(id)
    t=int(id2)
    #i=request.POST['TransportCompany_id']
    return render(request,"vehiclecategory.html",{"v1":v,"p1":p,"t1":t})

def service_client(request,id,id2):
    i=int(id2)
    t=TransportCompany.objects.all()
    s=TransportCompany_Service_category.objects.filter(TransportCompany_id=id)
    sc=Service_category.objects.all()
    #i=s.TransportCompany_Service_category_id.service_category_id_id
    #s1=Service_category.objects.filter(service_category_id=i)
    return render(request,"client_service.html",{"t1":t,"s1":s,"id":i,"sc":sc})

def transportcompany_client(request,id):
    t=TransportCompany.objects.all()
    s=TransportCompany_Service_category.objects.filter(service_category_id=id)
    return render(request,"client_transportcompany.html",{"t1":t,"t2":s})

def transportcompany_client2(request,id):
    i=int(id)
    t=TransportCompany.objects.all()
    s=TransportCompany_Vehicle_category.objects.filter(Vehicle_category_id=id)
    return render(request,"client_transportcompany2.html",{"t1":t,"t2":s,"id":i})



def transportcompanydetail_client(request,id):
    f = Feedback.objects.filter(TransportCompany_id=id)
    t = TransportCompany.objects.all()
    s = TransportCompany.objects.filter(TransportCompany_id=id)
    g = Gallery.objects.filter(TransportCompany_id=id)
    print("++++++++++", s)
    return render(request, "transportcompany-details.html", {"t1": t, "t2": s, "f1": f, "g1": g})


def transportcompanydetail_client2(request,id,id2):
    i=int(id2)
    f=Feedback.objects.filter(TransportCompany_id=id)
    t=TransportCompany.objects.all()
    s=TransportCompany.objects.filter(TransportCompany_id=id)
    g=Gallery.objects.filter(TransportCompany_id=id)
    print("++++++++++",s)
    return render(request,"client_transportcompanydetail2.html",{"t1":t,"t2":s,"f1":f,"g1":g,"id":i})



def booking(request,id2,id3,id=None):
    if request.session.has_key('id'):
        a = Area.objects.all()
        if id==None:
            p = Package.objects.get(package_id=id2)
            t = TransportCompany.objects.get(TransportCompany_id=id3)
            return render(request, "client_packagebooking.html", {"a": a, "p": p, "t": t})
        else:
            v= Vehicle_category.objects.get(vehicle_category_id=id)
            p=Package.objects.get(package_id=id2)
            t=TransportCompany.objects.get(TransportCompany_id=id3)
            return render(request,"clientBooking.html",{"a":a,"v":v,"p":p,"t":t})
    else:
        return redirect('/client/client_login/')

def add_booking(request, id2, id3, id=None):
    if request.method=="POST":
        d=date.today()
        d1=request.POST['Transport_date']
        f=request.POST['from_location']
        t=request.POST['to_location']
        #tid=request.POST['TransportCompany_id']
        tid=int(id3)
        cid=request.session['id']
        #pid=request.POST['package_id']
        pid=int(id2)
        #vid=request.POST['vehicle_category_id']
        vid=id
        try:
            bid=Booking(date=d,Transport_date=d1,booking_status=0,booking_status2=0,payment_status=0,from_location=f,to_location=t,quotation_amount=0,TransportCompany_id_id=tid,customer_id_id=cid,package_id_id=pid,vehicle_id_id=vid)
            bid.save()
            b=Booking.objects.latest("booking_id")
            print("-- Booking id --",b.booking_id)
           # return render(request,"insproduct.html",{"b":bid.booking_id})
            return redirect("/client/insproduct/%s" %b.booking_id)
        except:
            print("-----------", sys.exc_info())
    return redirect('/client/Home')

def payment(request,id):
      b=Booking.objects.filter(booking_id=id)
      b1=Booking.objects.get(booking_id=id)
      d1=datetime.strftime(b1.date,"%Y-%m-%d")
      return render(request,"payment.html",{"b":b,"date":d1})


def cash(request,id):
    b = Booking.objects.get(booking_id=id)
    b.payment_status = 1
    b.save()
    print("-----------Payment success--------")
    return redirect('/client/client_bookingdetails/')

def success(request,id):
    b = Booking.objects.get(booking_id=id)
    b.payment_status = 2
    b.save()
    print("-----------Payment success--------")
    return redirect('/client/client_bookingdetails/')


def cancel(request):
    return render(request,'cancel.html')





def ins_feedback(request):
    if request.method=="POST":
        d=date.today()
        des=request.POST["description"]

        t_id=request.POST["TransportCompany_id"]
        c_id=request.session["id"]
        try:
            val = Feedback.objects.filter(customer_id_id=c_id).count()
            if val == 0:
                f = Feedback(date=d, description=des, TransportCompany_id_id=t_id, customer_id_id=c_id)
                f.save()
                return redirect("/client/client_transportcompanydetail/%s"  %t_id)
            else:
                f=Feedback.objects.get(customer_id_id=c_id)
                f.description=des
                f.save()
                return redirect("/client/client_transportcompanydetail/%s" % t_id)
        except:
            pass
            print("-----------", sys.exc_info())
    return redirect("/client/Home/")


def client_profile_edit(request):
    c1=Customer.objects.all()
    cid=request.session['id']
    print("---------------",cid)
    c = Customer.objects.get(customer_id = cid )
    a = Area.objects.all()
    return render(request, "client_editprofile.html", {"c":c ,"area": a,"c1":c1})


def client_profile_update(request):
    if request.method == "POST":
        cid = request.session['id']
        c = Customer.objects.get(customer_id = cid)
        print("----------------",c)
        a = Area.objects.all()
        form = customerform(request.POST,instance=c)
        print("------------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/client/Home/")
            except:
                print("----------------", sys.exc_info())
        else:
            pass
    else:
        form = customerform()
    return render(request, "client_editprofile.html", {"c": c , "area": a})



def bookdetails(request):
    id1=request.session['id']
    b=Booking.objects.filter(customer_id=id1)
    return render(request,"client_bookingdetails.html",{"b1":b})

def contact(request):
    c=Company.objects.all()
    return render(request,"contact.html",{"c1":c})

def clientlogout(request):
    try:
        del request.session['username']
        del request.session['id']
    except:
        pass
    return redirect('/client/Home/')



def acceptbooking(request,id):
    b = Booking.objects.get(booking_id=id)
    b.booking_status = 1
    b.save()
    return redirect("/client/client_bookingdetails/")

def rejectbooking(request,id):
    b = Booking.objects.get(booking_id=id)
    b.booking_status = 2
    b.booking_status2 = 2
    b.save()
    return redirect("/client/client_bookingdetails/")

def load_menu(request):
	c=Service_category.objects.all()
	return render(request,"test.html",{"s1":c})


def autosuggest(request):
    if 'term' in request.GET:
        qs=Service_category.objects.filter(service_category_name__istarstwith=request.GET.get('term'))

        names=list()
        for x in qs:
            names.append(x.service_category_name)
        return JsonResponse(names,safe=False)

    return render(request,"header_footer.html")


def insproduct(request,id):
    p1=Product.objects.all()
    if request.method == "POST":
        pid= request.POST["product_id"]
        qty = request.POST["qty"]

        try:
            p =Booking_detail(qty=qty,booking_id_id=id , product_id_id=pid)
            p.save()
            return render(request,"insproduct.html",{"p1":p1,"b":id})
            #return redirect("/client/insproduct/%s"%b)
        except:
            pass
            print("-----------", sys.exc_info())
       # return redirect("/client/Home/")

    return render(request,"insproduct.html",{"p1":p1,"b":id})



def viewproduct(request,id):
    p=Booking_detail.objects.filter(booking_id=id)
    return render(request,"viewproduct.html",{"b1":p})


def client_productdelete(request,id):
    b=Booking_detail.objects.get(booking_detail_id=id)
    b.delete()

    return redirect("/client/productview/%s"%b.booking_id_id)

def load_menu(request):
	c=Service_category.objects.all()
	return render(request,"test.html",{"s1":c})


def load_menu2(request):
    v=Vehicle_category.objects.all()
    return render(request,"test.html",{"v1":v})

