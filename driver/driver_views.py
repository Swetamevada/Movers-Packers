import random
import sys
from datetime import date

from django.contrib import messages
from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.core.mail import send_mail
from django.utils.dateparse import parse_date

from moverspackers import settings
from mpm.forms import *
from mpm.function import handle_upload_file
from mpm.models import *

# Create your views here.

def driver_index(request):
    c=Customer.objects.all().count
    t=TransportCompany.objects.all().count
    b=Booking.objects.all().count
    id = request.session['dr_id']
    b2 = Booking.objects.filter(driver_id=id,date=date.today())
    return render(request,"driver_index.html",{"c":c,"t":t,"b1":b,"b2":b2})


def driver_login(request):
    a=Area.objects.all()
    if request.method == "POST":
        u = request.POST["email"]
        p = request.POST["password"]

        val = Driver.objects.filter(email=u, password=p).count()

        if val == 1:
            data = Driver.objects.filter(email=u, password=p )
            for items in data:
                request.session['dusername'] = items.email
                request.session['dr_id'] = items.driver_id
            return redirect('/driver/driver_index/')
        else:
            messages.error(request, "* Invalid E-mail id or password")
            return render(request, "driver_login.html")

    else:
        return render(request, "driver_login.html",{"a":a })


def driver_forgot_password(request):
    return render(request,"driver_forgot_password.html")


def driver_sendotp(request):
    otp1=random.randint(1000,9999)
    e=request.POST['email']

    print("---------------",e)
    request.session['dremail']=e
    obj=Driver.objects.filter(email=e).count()

    if obj == 1:
        val = Driver.objects.filter(email=e).update(otp=otp1 , otp_used=0)
        subject = 'OTP Verification'
        message = str(otp1)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]
        send_mail(subject, message, email_from, recipient_list)
        return render(request, 'driver_resetpassword.html')

    else:
        messages.error(request, " Invalid E-mail ")
        return render(request, "driver_forgot_password.html")

    return render(request, 'driver_resetpassword.html')


def driver_resetpassword(request):
    totp=request.POST.get('otp')
    tpassword=request.POST.get('npass')
    cpassword=request.POST.get('cpass')

    if tpassword == cpassword:
        e = request.session['dremail']
        val = Driver.objects.filter(email=e , otp = totp , otp_used = 0).count()

        if val == 1:
            val=Driver.objects.filter(email=e ).update(otp_used = 1 , password = tpassword)
            return redirect('/driver/driver_login/')

        else:
            messages.error(request,'otp does not match')
            return render(request,"driver_resetpassword.html")

    else:
        messages.error(request,"New Password & Confirm Password does not match")
        return render(request,"driver_resetpassword.html")

    return render(request,"driver_resetpassword.html")


def driver_profile(request):
    id=request.session['dr_id']
    print("---------------",id)
    d = Driver.objects.get(driver_id = id )
    d1 = Driver.objects.filter(driver_id = id )
    return render(request, "driver_edit_profile.html", {"d": d , "d1" : d1 })



def driver_update_profile(request):
    if request.method == "POST":
        id = request.session['dr_id']
        print("--------id",id)
        d2 =Driver.objects.get(driver_id = id)
        form =Driverform(request.POST,instance= d2)
        print("------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect("/driver/driver_profile/")
            except:
                print("----------------", sys.exc_info())
        else:
            pass

    else:
        form = Driverform()

    d1 = Driver.objects.filter(driver_id=id)
    return render(request , "driver_edit_profile.html" , {"d2" : d2 , "d1":d1 })


def driver_edit_image(request):
    id = request.session['dr_id']
    print("--------id", id)
    d2 = Driver.objects.get(driver_id=id)
    return render(request, "driver_pic.html", {"d2": d2 })


def driver_pic(request):
    if request.method == "POST":
        id = request.session['dr_id']
        print("--------id", id)
        d2 = Driver.objects.get(driver_id=id)
        form = Driverform1(request.POST,request.FILES,instance=d2)
        print("------------", form.errors)

        if form.is_valid():
            try:
                handle_upload_file(request.FILES['license_image'])
                form.save()
                return redirect("/driver/driver_profile/")
            except:
                print("----------------", sys.exc_info())
        else:
            pass

    else:
        form = Driverform1()

    d1 = Driver.objects.filter(driver_id=id)
    return render(request, "driver_pic.html", {"d2": d2,  "d1": d1})


def driver_logout(request):
    try:
        del request.session['dusername']
        del request.session['dr_id']
    except:
        pass
    return redirect("/driver/driver_login/")


def driver_state(request):
    s=State.objects.all()
    return render(request, "driver_state.html",{"st":s})


def driver_city(request):
    c=City.objects.all()
    return render(request, "driver_city.html",{"ct":c  })


def driver_area(request):
    a=Area.objects.all()
    return render(request, "driver_area.html",{"ar":a})


def driver_company(request):
    c=Company.objects.all()
    return render(request, "driver_company.html",{"cm":c})


def driver_customer(request):
    c=Customer.objects.all()
    return render(request, "driver_customer.html",{"cs":c})


def driver_transportcompany(request):
    c=TransportCompany.objects.all()
    return render(request, "driver_transportcompany.html",{"tc":c})


def driver_service_category(request):
    c=Service_category.objects.all()
    return render(request, "driver_service_category.html",{"src":c})


def driver_vehicle_category(request):
    c=Vehicle_category.objects.all()
    return render(request, "driver_vehicle_category.html",{"vhc":c})


def driver_feedback(request):
    c=Feedback.objects.all()
    return render(request, "driver_feedback.html",{"fb":c})


def driver_booking(request):
    id = request.session['dr_id']
    c=Booking.objects.filter(driver_id = id)
    return render(request, "driver_booking.html",{"bk":c})


def driver_gallery(request):
    c=Gallery.objects.all()
    return render(request, "driver_gallery.html",{"gr":c})


def driver_report1(request):
    id = request.session['dr_id']
    que = Booking.objects.filter(driver_id = id)

    if request.method == "POST":

        start = request.POST["start"]
        #end = request.POST["end"]

        start = parse_date(start)
        #end = parse_date(end)
        print("----",start,"---------")

        que = Booking.objects.filter(Transport_date=start,driver_id = id)

    return render(request, "driver_report1.html", {"que": que})



