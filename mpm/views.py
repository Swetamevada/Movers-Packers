
import sys
from datetime import date , datetime

from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_date
from django.views.decorators.csrf import csrf_exempt

from moverspackers import settings
from mpm.models import State
from mpm.models import City
from mpm.models import Area
from mpm.models import Company
from mpm.models import Customer
from mpm.models import TransportCompany
from mpm.models import Driver
from mpm.models import TransportCompany_package
from mpm.models import Service_category
from mpm.models import Vehicle_category
from mpm.models import TransportCompany_Service_category
from mpm.models import TransportCompany_Vehicle_category
from mpm.models import Feedback
from mpm.models import Gallery
from mpm.models import Package
from mpm.models import Booking
from mpm.models import Product
from mpm.models import Booking_detail
from django.core.mail import send_mail
import random
from mpm.forms import *
from mpm.function import handle_upload_file

from django.db import connection
from django.http import JsonResponse
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.


# select data from database
def state(request):
    if request.session.has_key('username'):
        s=State.objects.all()
        return render(request, "state.html",{"st":s})
    else:
        return redirect('/login/')

def city(request):
    if request.session.has_key('username'):
        c=City.objects.all()
        return render(request, "city.html",{"ct":c})
    else:
        return redirect('/login/')

def area(request):
    if request.session.has_key('username'):
        a=Area.objects.all()
        return render(request, "area.html",{"ar":a})
    else:
        return redirect('/login/')

def company(request):
    if request.session.has_key('username'):
        c=Company.objects.all()
        return render(request, "company.html",{"cm":c})
    else:
        return redirect('/login/')

def customer(request):
    if request.session.has_key('username'):
        c=Customer.objects.all()
        return render(request, "customer.html",{"cs":c})
    else:
        return redirect('/login/')

def transportcompany(request):
    if request.session.has_key('username'):
        c=TransportCompany.objects.all()
        return render(request, "transportcompany.html",{"tc":c})
    else:
        return redirect('/login/')


def driver(request):
    if request.session.has_key('username'):
        c=Driver.objects.all()
        return render(request, "driver.html",{"dr":c})
    else:
        return redirect('/login/')

def transportcompany_package(request):
    if request.session.has_key('username'):
        c=TransportCompany_package.objects.all()
        return render(request, "transportcompanypackage.html",{"tcp":c})
    else:
        return redirect('/login/')


def transportcompany_package_detail(request):
    if request.session.has_key('username'):
        c=TransportCompany_package_detail.objects.all()
        return render(request, "transportcompanypackagedetail.html",{"tcpd":c})
    else:
        return redirect('/login/')


def service_category(request):
    if request.session.has_key('username'):
        c=Service_category.objects.all()
        return render(request, "service_category.html",{"src":c})
    else:
        return redirect('/login/')


def vehicle_category(request):
    if request.session.has_key('username'):
        c=Vehicle_category.objects.all()
        return render(request, "vehicle_category.html",{"vhc":c})
    else:
        return redirect('/login/')


def transportCompany_service_category(request):
    if request.session.has_key('username'):
        c=TransportCompany_Service_category.objects.all()
        return render(request, "transportCompany_service_category.html",{"tcsc":c})
    else:
        return redirect('/login/')


def transportCompany_vehicle_category(request):
    if request.session.has_key('username'):
        c=TransportCompany_Vehicle_category.objects.all()
        return render(request, "transportCompany_vehicle_category.html",{"tcvc":c})
    else:
        return redirect('/login/')


def feedback(request):
    if request.session.has_key('username'):
        c=Feedback.objects.all()
        return render(request, "feedback.html",{"fb":c})
    else:
        return redirect('/login/')


def gallery(request):
    if request.session.has_key('username'):
        c=Gallery.objects.all()
        return render(request, "gallery.html",{"gr":c})
    else:
        return redirect('/login/')


def package(request):
    if request.session.has_key('username'):
        c=Package.objects.all()
        return render(request, "package.html",{"pc":c})
    else:
        return redirect('/login/')


def booking(request):
    if request.session.has_key('username'):
        c=Booking.objects.all()
        return render(request, "booking.html",{"bk":c})
    else:
        return redirect('/login/')


def product(request):
    if request.session.has_key('username'):
        c=Product.objects.all()
        return render(request, "product.html",{"pd":c})
    else:
        return redirect('/login/')


def booking_detail(request):
    if request.session.has_key('username'):
        c=Booking_detail.objects.all()
        return render(request, "booking_detail.html",{"bkd":c})
    else:
        return redirect('/login/')




# delete data

def del_state(request,id):
    try:
        s=State.objects.get(state_id=id)
        s.delete()
        messages.error(request, "Record is deleted successfully...")
    except ProtectedError:
        messages.error(request, "You can't delete this record...")
    return redirect("/state")


def del_city(request,id):
    try:
        c=City.objects.get(city_id=id)
        c.delete()
        messages.error(request, "Record is deleted successfully...")
    except ProtectedError:
        messages.error(request, "You can't delete this record...")
    return redirect("/city")


def del_area(request,id):
    try:
        a=Area.objects.get(area_id=id)
        a.delete()
        messages.error(request, "Record is deleted successfully...")
    except ProtectedError:
        messages.error(request, "You can't delete this record...")

    return redirect("/area")


def del_TransportCompany_Package(request,id):
    try:
        t=TransportCompany_package.objects.get(TransportCompany_pk_id=id)
        t.delete()
        messages.error(request, "Record is deleted successfully...")
    except ProtectedError:
        messages.error(request, "You can't delete this record...")
    return redirect("/transportcompanypackage")


def del_TransportCompany_Package_detail(request,id):
    try:
        t=TransportCompany_package_detail.objects.get(TransportCompany_pk_detail_id=id)
        t.delete()
        messages.error(request, "Record is deleted successfully...")
    except ProtectedError:
        messages.error(request, "You can't delete this record...")
    return redirect("/transportcompanypackagedetail")


def del_service_category(request,id):
    try:
        s=Service_category.objects.get(service_category_id=id)
        s.delete()
        messages.error(request, "Record is deleted successfully...")
    except ProtectedError:
        messages.error(request, "You can't delete this record...")
    return redirect("/servicecategory")


def del_vehicle_category(request,id):
    try:
        v=Vehicle_category.objects.get(vehicle_category_id=id)
        v.delete()
        messages.error(request, "Record is deleted successfully...")
    except ProtectedError:
        messages.error(request, "You can't delete this record...")
    return redirect("/vehiclecategory")


def del_service_category_detail(request,id):
    try:
        t=TransportCompany_Service_category.objects.get( TransportCompany_Service_category_id=id)
        t.delete()
        messages.error(request, "Record is deleted successfully...")
    except ProtectedError:
        messages.error(request, "You can't delete this record...")
    return redirect("/transportcompanyservicecategory")


def del_vehicle_category_detail(request,id):
    try:
        t=TransportCompany_Vehicle_category.objects.get( TransportCompany_Vehicle_category_id=id)
        t.delete()
        messages.error(request, "Record is deleted successfully...")
    except ProtectedError:
        messages.error(request, "You can't delete this record...")
    return redirect("/transportcompanyvehiclecategory")


def del_feedback(request,id):
    try:
        f=Feedback.objects.get(feedback_id=id)
        f.delete()
        messages.error(request, "Record is deleted successfully...")
    except ProtectedError:
        messages.error(request, "You can't delete this record...")
    return redirect("/feedback")


def del_gallery(request,id):
    try:
        g=Gallery.objects.get(gallery_id=id)
        g.delete()
        messages.error(request, "Record is deleted successfully...")
    except ProtectedError:
        messages.error(request, "You can't delete this record...")
    return redirect("/gallery")


def del_package(request,id):
    try:
        p=Package.objects.get(package_id=id)
        p.delete()
        messages.error(request, "Record is deleted successfully...")
    except ProtectedError:
        messages.error(request, "You can't delete this record...")
    return redirect("/package")


def del_product(request,id):
    try:
        p=Product.objects.get(product_id=id)
        p.delete()
        messages.error(request, "Record is deleted successfully...")
    except ProtectedError:
        messages.error(request, "You can't delete this record...")
    return redirect("/product")


# login module
def admin_login(request):
    if request.method=="POST":
        u=request.POST["email"]
        p=request.POST["password"]
        val=Customer.objects.filter(email=u,password=p,is_admin=1).count()
        if val==1:
            data=Customer.objects.filter(email=u,password=p,is_admin=1)
            for items in data:
                request.session['username']=items.email
                request.session['id']=items.customer_id

            if request.POST.get("remember"):
                response = redirect("/index/")
                response.set_cookie('admin_email', request.POST["email"])
                response.set_cookie('admin_pass', request.POST["password"])
                return response

            return redirect('/index/')
        else:
            messages.error(request,"Invalid E-mail And Password")
            return render(request,"login.html")
    else:
        if request.COOKIES.get("admin_email"):
            return render(request, "login.html",
                          {'admin_cookie_email': request.COOKIES['admin_email'],
                           'admin_cookie_password': request.COOKIES['admin_pass']})  # cookie1 and cookie2 are keys
        else:
            return render(request, "login.html")
    return render(request,"login.html")


def forgot_password(request):
    return render(request,"forgot-password.html")


def send_otp(request):
    otp1=random.randint(10000,99999)
    e=request.POST['email']
    request.session['temail']=e
    obj=Customer.objects.filter(email=e,is_admin=1).count()

    if obj==1:
        val=Customer.objects.filter(email=e,is_admin=1).update(OTP=otp1,OTP_used=0)
        subject='OTP verification'
        message=str(otp1)
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[e,]
        send_mail(subject,message,email_from,recipient_list)
       # return redirect('/sendmail/')
        return render(request,'reset_password.html')


def set_password(request):
    totp=request.POST['otp']
    tpassword=request.POST['npass']
    cpassword=request.POST['cpass']

    if tpassword==cpassword:
        e=request.session['temail']
        val=Customer.objects.filter(email=e,OTP=totp,OTP_used=0).count()

        if val==1:
            val=Customer.objects.filter(email=e).update(OTP_used=1,password=tpassword)
            return redirect('/login')
        else:
            messages.error(request,"OTP does not match")
            return render(request,"reset_password.html")
    else:
        messages.error(request, "New password and Confirm password does not match")
        return render(request, "reset_password.html")

    return render(request,"reset_password.html")


def logout(request):
    try:
        del request.session['username']
        del request.session['temail']
    except:
        pass

    return redirect('/login')


# Insert record in database
def ins_area(request):
    c=City.objects.all()
    if request.method=="POST":
        form=areaform(request.POST)
        print("--------",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/area")
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form=areaform()

    return render(request,"insert_area.html",{"form":form,"city":c})

def ins_state(request):
    if request.method=="POST":
        form=stateform(request.POST)
        print("--------",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/state")
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form=stateform()

    return render(request,"insert_state.html",{"form":form})

def ins_city(request):
    s=State.objects.all()
    if request.method=="POST":
        form=cityform(request.POST)
        print("--------",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/city")
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form=cityform()

    return render(request,"insert_city.html",{"form":form,"state":s})

def ins_package(request):
    t=TransportCompany.objects.all()
    s=Service_category.objects.all()
    if request.method=="POST":
        form=packageform(request.POST)
        print("--------",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/package")
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form=packageform()

    return render(request,"insert_package.html",{"form":form,"c1":t,"s1":s})

def ins_product(request):
    if request.method=="POST":
        form=productform(request.POST)
        print("--------",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/product")
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form=productform()

    return render(request,"insert_product.html",{"form":form})


def ins_servcat(request):
    if request.method=="POST":
        form=servicecategoryform(request.POST,request.FILES)
        print("--------",form.errors)
        if form.is_valid():
            try:
                handle_upload_file(request.FILES['service_image'])
                form.save()
                return redirect("/servicecategory")
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form=servicecategoryform()

    return render(request,"insert_servicecategory.html",{"form":form})


def ins_vehicat(request):
    if request.method == "POST":
        form=vehiclecategoryform(request.POST , request.FILES)
        print("--------",form.errors)
        if form.is_valid():
            try:
                handle_upload_file(request.FILES['vehicle_image'])
                form.save()
                return redirect("/vehiclecategory")
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form=vehiclecategoryform()

    return render(request,"insert_vehiclecategory.html",{"form":form})

def ins_trancom_servcat(request):
    t=TransportCompany.objects.all()
    s=Service_category.objects.all()
    if request.method=="POST":
        form=transportcompany_servicecategoryform(request.POST)
        print("--------",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/transportcompanyservicecategory")
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form=transportcompany_servicecategoryform()

    return render(request,"insert_trancom_servcat.html",{"form":form,"t1":t,"s1":s})

def ins_trancom_vehicat(request):
    t=TransportCompany.objects.all()
    v=Vehicle_category.objects.all()
    if request.method=="POST":
        form=transportcompany_vehiclecategoryform(request.POST)
        print("--------",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/transportcompanyvehiclecategory")
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form=transportcompany_vehiclecategoryform()

    return render(request,"insert_trancom_vehicat.html",{"form":form,"t1":t,"v1":v})

def ins_trancom_package(request):
    c=Company.objects.all()
    if request.method=="POST":
        form=transportcompanypackageform(request.POST)
        print("--------",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/transportcompanypackage")
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form=transportcompanypackageform()

    return render(request,"insert_trancom_package.html",{"form":form,"c1":c})

def ins_trancom_package_detail(request):
    tc=TransportCompany.objects.all()
    tc_pk=TransportCompany_package.objects.all()
    if request.method=="POST":
        form=transportcompanypackageform(request.POST)
        print("--------",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/transportcompanypackagedetail")
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form= transportcompanypackageform()

    return render(request,"insert_trancom_package_detail.html",{"form":form,"t1":tc,"tp1":tc_pk})


def insert_gallery(request):
    t = TransportCompany.objects.all()
    if request.method=="POST":
        form=galleryform(request.POST,request.FILES)
        print("---------",form.errors)
        if form.is_valid():
            handle_upload_file(request.FILES['gallry_path'])
            form.save()
            return redirect('/gallery')
    else:
        form=galleryform()

    return render(request,"insert_gallery.html",{"form":form,"t1":t})



# Update data in database
def state_update(request,id):
    s = State.objects.get(state_id=id)
    form = stateform(request.POST, instance=s)
    print("_______", form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/state")
        except:
            print("_________", sys.exc_info())
    return render(request,"edit_state.html", {"state": s})


def state_edit(request,id):
    s = State.objects.get(state_id=id)
    return render(request, "edit_state.html", {"state": s})


def city_update(request,id):

    c = City.objects.get(city_id=id)
    form = cityform(request.POST, instance=c)
    print("_______", form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/city")
        except:
            print("_________", sys.exc_info())
    return render(request,"edit_city.html",{"city":c})


def city_edit(request,id):
    s = State.objects.all()
    c = City.objects.get(city_id=id)
    return render(request, "edit_city.html", {"city": c,"state":s})


def area_update(request,id):
    a = Area.objects.get(area_id=id)
    form = areaform(request.POST, instance=a)
    print("_______", form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/area")
        except:
            print("_________", sys.exc_info())
    return render(request,"edit_area.html",{"area":a})


def area_edit(request,id):
    c=City.objects.all()
    a = Area.objects.get(area_id=id)
    return render(request, "edit_area.html", {"area": a,"city": c})



def product_update(request,id):
    t = TransportCompany.objects.all()
    s = Service_category.objects.all()
    p=Product.objects.get(product_id=id)
    form = productform(request.POST, instance=p)
    print("_______", form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/product")
        except:
            print("_________", sys.exc_info())
    return render(request,"edit_product.html", {"product": p})


def product_edit(request,id):
    p=Product.objects.get(product_id=id)
    return render(request, "edit_product.html", {"product":p})


def service_category_update(request,id):
    s=Service_category.objects.get(service_category_id=id)
    form = servicecategoryform(request.POST,request.FILES, instance=s)
    print("_______", form.errors)
    if form.is_valid():
        try:
            handle_upload_file(request.FILES['service_image'])
            form.save()
            return redirect("/servicecategory")
        except:
            print("_________", sys.exc_info())
    else:
        form = servicecategoryform()
    return render(request,"edit_servicecategory.html", {"sc": s})


def service_category_edit(request,id):
    s=Service_category.objects.get(service_category_id=id)
    return render(request, "edit_servicecategory.html", {"sc":s})


def vehicle_category_update(request,id):
    v=Vehicle_category.objects.get(vehicle_category_id=id)
    form = vehiclecategoryform(request.POST,request.FILES, instance=v)
    print("_______", form.errors)
    if form.is_valid():
        try:
            handle_upload_file(request.FILES['vehicle_image'])
            form.save()
            return redirect("/vehiclecategory")
        except:
            print("_________", sys.exc_info())
    else:
        form = vehiclecategoryform()
    return render(request,"edit_vehiclecategory.html", {"vc": v})


def vehicle_category_edit(request,id):
    v=Vehicle_category.objects.get(vehicle_category_id=id)
    return render(request, "edit_vehiclecategory.html", {"vc":v})


def servicecategorydetail_update(request,id):
    t = TransportCompany.objects.all()
    sc = Service_category.objects.all()
    s=TransportCompany_Service_category.objects.get( TransportCompany_Service_category_id=id)
    form = transportcompany_servicecategoryform(request.POST, instance=s)
    print("_______", form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/transportcompanyservicecategory")
        except:
            print("_________", sys.exc_info())
    return render(request,"edit_trancom_servcat.html", {"ts": s,"t":t,"s":s})


def servicecategorydetail_edit(request,id):
    t = TransportCompany.objects.all()
    sc = Service_category.objects.all()
    s = TransportCompany_Service_category.objects.get(TransportCompany_Service_category_id=id)
    return render(request, "edit_trancom_servcat.html", {"ts": s,"t":t,"s":sc})


def package_update(request,id):
    p = Package.objects.get(package_id=id)
    form = packageform(request.POST, instance=p)
    print("_______", form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/package")
        except:
            print("_________", sys.exc_info())
    t = TransportCompany.objects.all()
    s = Service_category.objects.all()
    return render(request,"edit_package.html",{"package":p,"tc":t,"sc":s})


def package_edit(request,id):
    t = TransportCompany.objects.all()
    s = Service_category.objects.all()
    p = Package.objects.get(package_id=id)
    return render(request, "edit_package.html", {"p": p,"tc":t,"sc":s})


def vehiclecategorydetail_update(request,id):
    t = TransportCompany.objects.all()
    vc = Vehicle_category.objects.all()
    v=TransportCompany_Vehicle_category.objects.get( TransportCompany_Vehicle_category_id=id)
    form = transportcompany_vehiclecategoryform(request.POST, instance=v)
    print("_______", form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/transportcompanyvehiclecategory")
        except:
            print("_________", sys.exc_info())
    return render(request,"edit_trancom_vehicat.html", {"tv": v,"t1":t,"v1":vc})


def vehiclecategorydetail_edit(request,id):
    t = TransportCompany.objects.all()
    vc = Vehicle_category.objects.all()
    v=TransportCompany_Vehicle_category.objects.get( TransportCompany_Vehicle_category_id=id)
    return render(request,"edit_trancom_vehicat.html", {"tv": v,"t1":t,"v1":vc})


def transportcompanypackage_update(request,id):
    c=Company.objects.all()
    t=TransportCompany_package.objects.get( TransportCompany_pk_id=id)
    form = transportcompanypackageform(request.POST, instance=t)
    print("_______", form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/transportcompanypackage")
        except:
            print("_________", sys.exc_info())
    return render(request,"edit_trancom_package.html", {"c1": c,"t1":t})


def transportcompanypackage_edit(request,id):
    c=Company.objects.all()
    t=TransportCompany_package.objects.get( TransportCompany_pk_id=id)

    return render(request,"edit_trancom_package.html", {"c1": c,"t1":t})


def transportcompanypackagedetail_update(request,id):
    t1=TransportCompany_package.objects.all()
    t2=TransportCompany.objects.all()
    t=TransportCompany_package_detail.objects.get(TransportCompany_pk_detail_id=id)
    form = transportcompanypackagedetailform(request.POST, instance=t)
    print("_______", form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/transportcompanypackagedetail")
        except:
            print("_________", sys.exc_info())
    return render(request,"edit_trancom_package_detail.html", {"a": t,"t":t2,"tp":t1})


def transportcompanypackagedetail_edit(request,id):
    t1 = TransportCompany_package.objects.all()
    t2 = TransportCompany.objects.all()
    t=TransportCompany_package_detail.objects.get(TransportCompany_pk_detail_id=id)

    d1 = datetime.strftime(t.register_date,"%Y-%m-%d")

    d2 = datetime.strftime(t.package_end_date,"%Y-%m-%d")

    return render(request,"edit_trancom_package_detail.html", {"a": t,"t":t2,"tp":t1,"start":d1,"end":d2})


def gallery_edit(request,id):
    t = TransportCompany.objects.all()
    g = Gallery.objects.get(gallery_id=id)
    return render(request, "edit_gallery.html", {"g": g, "t1": t})


def gallery_update(request, id):
    g = Gallery.objects.get(gallery_id=id)

    form = galleryform(request.POST,request.FILES ,instance=g)
    print("----------", form.errors)
    if form.is_valid():
        try:
            handle_upload_file(request.FILES['gallry_path'])
            form.save()
            return redirect("/gallery")
        except:
            print("--------", sys.exc_info())
    else:
        form = galleryform()

    t = TransportCompany.objects.all()
    return render(request, "edit_gallery.html", {"g": g, "t1": t})


#edit profile
def profile_edit(request):
    id=request.session['id']
    print("---------------",id)
    c = Customer.objects.get(customer_id = id )
    a = Area.objects.all()
    cm = Company.objects.all()
    return render(request, "edit_profile.html", {"c": c , "area" : a , "cm" : cm })


def profile_update(request):
    if request.method == "POST":
        id = request.session['id']
        c = Customer.objects.get(customer_id = id)
        print("----------------",c)
        a = Area.objects.all()
        cm = Company.objects.all()
        form = customerform(request.POST,instance=c)
        print("------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect("/edit_profile")
            except:
                print("----------------", sys.exc_info())
        else:
            pass

    else:
        form = customerform()

    return render(request, "edit_profile.html", {"c": c , "area": a , "cm": cm })


# Home page
def dashboard(request):
    if request.session.has_key('username'):
        b=Booking.objects.all().count
        t=TransportCompany.objects.all().count
        c=Customer.objects.all().count
        b1=Booking.objects.filter(date=date.today())
        f=Feedback.objects.filter(date=date.today())
        return render(request,"index.html",{"user":c,"tc":t,"booking":b,"b1":b1,"f":f})
    else:
        return redirect('/login/')


class ViewHome(View):
    def get(self,request,*args,**kwargs):
        return render(request,"doctorChart.html")


class DashboardChart(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self,request,format=None):
        cursor=connection.cursor()
        cursor.execute('''SELECT (SELECT TransportCompany_name transportcompany where TransportCompany_id = b.TransportCompany_id_id) as name , count(*) as total FROM booking b JOIN transportcompany t WHERE b.TransportCompany_id_id = t.TransportCompany_id GROUP by b.TransportCompany_id_id''')
        qs=cursor.fetchall()
        print("+++++++++++=")
        labels=[]
        default_items=[]
        for item in qs:
            labels.append(item[0])
            default_items.append(item[1])

        data = {
            "labels":labels,
            "default":default_items,
        }
        return Response(data)


def quotation(request,id):
    b=Booking.objects.get(booking_id=id)
    return render(request,"insert_quotation.html",{"b":b})

def upd_quatation(request,id):
    b=Booking.objects.get(booking_id=id)

    form = bookingform(request.POST,instance=b)
    print("----------",form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/booking")
        except:
            print("--------",sys.exc_info())
    else:
        form=bookingform()

    return render(request, "insert_quotation.html", {"b": b})



def editdriver(request,id):
    b=Booking.objects.get(booking_id=id)
    d=Driver.objects.all()
    return render(request,"insert_driver.html",{"b":b,"d":d})

def upd_driver(request,id):
    b=Booking.objects.get(booking_id=id)
    d = Driver.objects.all()
    form = bookingform2(request.POST,instance=b)
    print("----------",form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/booking")
        except:
            print("--------",sys.exc_info())
    else:
        form=bookingform2()

    return render(request, "insert_driver.html", {"b": b,"d":d})


def admin_acceptbooking(request,id):
    b = Booking.objects.get(booking_id=id)
    b.booking_status2 = 1
    b.save()
    return redirect("/booking/")

def admin_rejectbooking(request,id):
    b = Booking.objects.get(booking_id=id)
    b.booking_status2 = 3
    b.save()
    return redirect("/booking/")



def report1(request):
    t1 = TransportCompany.objects.all()
    bk = Booking.objects.all()

    if request.method == "POST":
        key = request.POST["TransportCompany_name"]
        print("--- Transport --------", key)
        bk = Booking.objects.filter(TransportCompany_id_id=key)

    return render(request, "report1.html",{"bk": bk, "t1": t1})


def report2(request):
    que = Booking.objects.all()

    if request.method == "POST":

        start = request.POST["start"]
        end = request.POST["end"]

        start = parse_date(start)
        end = parse_date(end)
        print("----",start,"---------",end)

        que = Booking.objects.filter(date__range=[start,end])

    return render(request, "report2.html", {"que": que})



def report3(request):
    sql1="SELECT (select area_name from area WHERE area_id = c.area_id_id) as customer_id , count(*) as total FROM customer c JOIN area a where c.area_id_id = a.area_id group by c.area_id_id"
    data=Customer.objects.raw(sql1)
    return render(request,"report3.html",{"data":data})


def report4(request):

    t1 = TransportCompany.objects.all()
    dr = Driver.objects.all()

    if request.method == "POST":
        key = request.POST["TransportCompany_name"]
        print("--- Transport --------", key)
        dr=Driver.objects.filter(TransportCompany_id_id=key)

    return render(request, "report4.html",{"dr": dr, "t1": t1})


def report5(request):

    t1 = TransportCompany.objects.all()
    fb=Feedback.objects.all()

    if request.method == "POST":
        key = request.POST["TransportCompany_name"]
        print("--- Transport --------", key)
        fb=Feedback.objects.filter(TransportCompany_id_id=key)

    return render(request, "report5.html",{"fb": fb, "t1": t1})


def report6(request):

    a1=Area.objects.all()
    cs=Customer.objects.all()

    if request.method == "POST":
        key = request.POST["area_name"]
        print("--- Transport --------", key)
        cs=Customer.objects.filter(area_id_id=key)

    return render(request, "report6.html",{"cs": cs, "a1": a1})


def report7(request):

    a1=Area.objects.all()
    tc=TransportCompany.objects.all()

    if request.method == "POST":
        key = request.POST["area_name"]
        print("--- Transport --------", key)
        tc=TransportCompany.objects.filter(area_id_id=key)

    return render(request, "report7.html",{"tc": tc, "a1": a1})