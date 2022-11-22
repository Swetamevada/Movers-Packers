import sys
import calendar
from datetime import date
from random import random

from django.core.mail import send_mail
from django.db.models import ProtectedError
from django.shortcuts import render

# Create your views here.
from django.utils.dateparse import parse_date

from moverspackers import settings
from mpm.forms import *
from mpm.function import handle_upload_file
from mpm.models import *
from django.shortcuts import render,redirect
from django.contrib import messages


def transportcopmany_index(request):
    b = Booking.objects.all().count
    t = TransportCompany.objects.all().count
    c = Customer.objects.all().count
    b1 = Booking.objects.filter(date=date.today())
    f = Feedback.objects.filter(date=date.today())
    return render(request,"TransportCompany_index.html",{"user": c, "tc": t, "booking": b, "b1": b1, "f": f})


def transport_register(request):
    a=Area.objects.all()
    c=Company.objects.all()
    tp=TransportCompany_package.objects.all()

    sd = date.today()

    if request.method=="POST":
        tn = request.POST["TransportCompany_name"]
        ow = request.POST["owner_name"]
        e = request.POST["email"]
        p = request.POST["password"]
        c = request.POST["contact"]
        a1=request.POST["addressline1"]
        a2 = request.POST["addressline2"]
        l = request.POST["landmark"]
        ln = request.POST["licence_no"]
        a = request.POST["area_id"]

        tp = request.POST["TransportCompany_pk_id"]

        data = TransportCompany_package.objects.get(TransportCompany_pk_id=tp)

        months = int(data.duration)

        months_count = sd.month + months

        year = sd.year + int(months_count / 12)

        month = (months_count % 12)
        if month == 0:
            month = 12

        day = sd.day
        last_day_of_month = calendar.monthrange(year, month)[1]

        if day > last_day_of_month:
            day = last_day_of_month

        new_date = date(year, month, day)

        print("-------- new date -----------",new_date)

        form=transportcompanyform(request.POST,request.FILES)
        print("--------",form.errors)

        if form.is_valid():
            try:
                handle_upload_file(request.FILES['TransportCompany_image'])
                f = TransportCompany(reg_start_date=sd,TransportCompany_name=tn,owner_name=ow,email=e,password=p,contact=c,addressline1=a1,addressline2=a2,landmark=l,licence_no=ln,area_id_id=a,TransportCompany_pk_id_id=tp,reg_end_date=new_date)
                f.save()
                return redirect('/Tc/transportcompany_index')
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form=transportcompanyform()

    return render(request,"TransportCompany_registration.html",{"form":form ,"a":a ,"c":c,"tp":tp })


def renew(request,id):
    t1=TransportCompany.objects.all()
    #tid=request.session['transport_id']
    tid = int(id)
    t = TransportCompany.objects.get(TransportCompany_id = tid)
    print("---------------", t)
    a = Area.objects.all()
    p=TransportCompany_package.objects.all()
    return render(request, "renew_TransportCompany_registration.html", {"t":t ,"area": a,"t1":t1,"p":p})


def renew_update(request,id):
    if request.method == "POST":
        #tid = request.session['transport_id']
        tid = int(id)
        t = TransportCompany.objects.get(TransportCompany_id = tid)
        print("----------------",t)
        sd = date.today()
        a = Area.objects.all()
        tp = request.POST["TransportCompany_pk_id"]
        p = TransportCompany_package.objects.all()


        data = TransportCompany_package.objects.get(TransportCompany_pk_id=tp)

        months = int(data.duration)

        months_count = sd.month + months

        year = sd.year + int(months_count / 12)

        month = (months_count % 12)
        if month == 0:
            month = 12

        day = sd.day
        last_day_of_month = calendar.monthrange(year, month)[1]

        if day > last_day_of_month:
            day = last_day_of_month

        new_date = date(year, month, day)

        print("-------- new date -----------", new_date)
        t.reg_end_date = new_date
        t.save()
        return redirect("/Tc/trans_login/")


def transportCompany_login(request):
    a=Area.objects.all()
    if request.method == "POST":
        u = request.POST["email"]
        p = request.POST["password"]

        val = TransportCompany.objects.filter(email=u, password=p).count()
        d = date.today()
        #b = TransportCompany.objects.get(email=u, password=p)

        if val == 1:
            data = TransportCompany.objects.get(email=u, password=p)

            if d >= data.reg_end_date:
                messages.error( request,"package expire")
                return render(request,"TransportCompany_login.html",{"flag":1,"t1":data})
            else:
                data = TransportCompany.objects.filter(email=u, password=p)
                for items in data:
                    request.session['uname'] = items.email
                    request.session['transport_id'] = items.TransportCompany_id

                    if request.POST.get("remember"):
                        response = redirect("/Tc/transportcompany_index/")
                        response.set_cookie('tracom_email', request.POST["email"])
                        response.set_cookie('tracom_pass', request.POST["password"])
                        return response

                return redirect('/Tc/transportcompany_index/')
        else:
            messages.error(request, "Invalid E-mail id or password")
            return render(request, "TransportCompany_login.html")

    else:
        if request.COOKIES.get("tracom_email"):
            return render(request, "TransportCompany_login.html",
                          {'tracom_cookie_email': request.COOKIES['tracom_email'],
                           'tracom_cookie_password': request.COOKIES['tracom_pass']})
        else:
            return render(request, "TransportCompany_login.html")

    return render(request, "TransportCompany_login.html",{"a":a })


def trancom_logout(request):
    try:
        del request.session['uname']
        del request.session['transport_id']
    except:
        pass

    return redirect('/Tc/trans_login')


def trancom_forgotpassword(request):
    return render(request,"tran_forgotpassword.html")


def tran_send_OTP(request):
    otp1=random.randint(10000,99999)
    e=request.POST['email']
    request.session['temail']=e
    obj=TransportCompany.objects.filter(email=e).count()

    if obj==1:
        val = TransportCompany.objects.filter(email=e).update(OTP=otp1,OTP_used=0)
        subject = 'OTP verification'
        message = str(otp1)
        email_from= settings.EMAIL_HOST_USER
        recipient_list=[e,]
        send_mail(subject,message,email_from,recipient_list)
        return render(request,'trans_resetpassword.html')

    else:
        messages.error(request, " Invalid E-mail ")
        return render(request, "tran_forgotpassword.html")

    return render(request, "trans_resetpassword.html")


def tran_setpassword(request):
    totp=request.POST.get('otp')
    tpassword=request.POST.get('npass')
    cpassword=request.POST.get('cpass')

    if tpassword == cpassword:
        e = request.session['temail']
        val = TransportCompany.objects.filter(email=e  ,OTP = totp , OTP_used = 0).count()

        if val == 1:
            val=TransportCompany.objects.filter(email=e  ).update(OTP_used = 1 , password = tpassword)
            return redirect('/Tc/trans_login/')

        else:
            messages.error(request,'otp does not match')
            return render(request,"trans_resetpassword.html")

    else:
        messages.error(request,"New Password & Confirm Password does not match")
        return render(request,"trans_resetpassword.html")

    return render(request,"trans_resetpassword.html")


def tc_package(request):
    tp = TransportCompany_package.objects.all()
    return render(request,"trans_pricing.html",{"tp":tp})


def trans_state(request):
    if request.session.has_key('uname'):
         s=State.objects.all()
         return render(request, "trans_state.html",{"st":s})
    else:
        return redirect('/Tc/trans_login/')


def trans_city(request):
    if request.session.has_key('uname'):
        c=City.objects.all()
        return render(request, "trans_city.html",{"ct":c})
    else:
        return redirect('/Tc/trans_login/')


def trans_area(request):
    if request.session.has_key('uname'):
        a=Area.objects.all()
        return render(request, "trans_area.html",{"ar":a})
    else:
        return redirect('/Tc/trans_login/')


def trans_company(request):
    if request.session.has_key('uname'):
        c=Company.objects.all()
        return render(request, "trans_company.html",{"cm":c})
    else:
        return redirect('/Tc/trans_login/')


def trans_customer(request):
    if request.session.has_key('uname'):
        c=Customer.objects.all()
        return render(request, "trans_customer.html",{"cs":c})
    else:
        return redirect('/Tc/trans_login/')


def trans_transportcompany(request):
    if request.session.has_key('uname'):
        id1 = request.session['transport_id']
        c=TransportCompany.objects.filter(TransportCompany_id=id1)
        return render(request, "trans_transportcompany.html",{"tc":c})
    else:
        return redirect('/Tc/trans_login/')


def trans_service_category(request):
    if request.session.has_key('uname'):
        c=Service_category.objects.all()
        return render(request, "trans_service_category.html",{"src":c})
    else:
        return redirect('/Tc/trans_login/')


def trans_vehicle_category(request):
    if request.session.has_key('uname'):
        c=Vehicle_category.objects.all()
        return render(request, "trans_vehicle_category.html",{"vhc":c})
    else:
        return redirect('/Tc/trans_login/')


def trans_package(request):
    if request.session.has_key('uname'):
        c=TransportCompany_package.objects.all()
        return render(request, "trans_transportcompanypackage.html",{"tcp":c})
    else:
        return redirect('/Tc/trans_login/')


def trans_package_detail(request):
    if request.session.has_key('uname'):
        id1 = request.session['transport_id']
        c=TransportCompany_package_detail.objects.filter(TransportCompany_id=id1)

        return render(request, "trans_transportcompanypackagedetail.html",{"tcpd":c})
    else:
        return redirect('/Tc/trans_login/')


def transport_service_category(request):
    if request.session.has_key('uname'):
        id1 = request.session['transport_id']
        c=TransportCompany_Service_category.objects.filter(TransportCompany_id=id1)
        return render(request, "tran_transportCompany_service_category.html",{"tcsc":c})
    else:
        return redirect('/Tc/trans_login/')


def del_trans_service_category(request,id):
    try:
        a=TransportCompany_Service_category.objects.get(TransportCompany_Service_category_id=id)
        a.delete()
        messages.error(request, "Record is deleted successfully...")
    except ProtectedError:
        messages.error(request, "You can't delete this record...")
    return redirect("/Tc/tc_transport_service_category")


def ins_tran_servcat(request):
    if request.method=="POST":
        form=transportcompany_servicecategoryform(request.POST)
        print("--------",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/Tc/tc_transport_service_category")
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form=transportcompany_servicecategoryform()

    c = TransportCompany.objects.all()
    s = Service_category.objects.all()

    return render(request,"insert_trans_servcat.html",{"form":form,"t1":c,"s1":s})


def edit_trans_service_category(request,id):
    t=TransportCompany.objects.all()
    s=Service_category.objects.all()
    ts=TransportCompany_Service_category.objects.get(TransportCompany_Service_category_id=id)
    return render(request,"update_trans_service_category.html",{"ts":ts,"t":t,"s":s})


def upd_trans_service_category(request,id):
    ts = TransportCompany_Service_category.objects.get(TransportCompany_Service_category_id=id)
    form=transportcompany_servicecategoryform(request.POST,instance=ts)
    print("----------",form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/Tc/tc_transport_service_category")
        except:
            print("--------",sys.exc_info())
    else:
        form=transportcompany_servicecategoryform()

    t = TransportCompany.objects.all()
    s=Service_category.objects.all()
    return render(request, "update_trans_service_category.html", {"ts": ts, "s": s, "t": t})


def transport_vehicle_category(request):
    if request.session.has_key('uname'):
        id1 = request.session['transport_id']
        c = TransportCompany_Vehicle_category.objects.filter(TransportCompany_id=id1)
        return render(request, "trans_transportCompany_vehicle_category.html",{"tcvc":c})
    else:
        return redirect('/Tc/trans_login/')


def del_trans_vehicle_category(request,id):
    try:
        a=TransportCompany_Vehicle_category.objects.get(TransportCompany_Vehicle_category_id=id)
        a.delete()
        messages.error(request, "Record is deleted successfully...")
    except ProtectedError:
        messages.error(request, "You can't delete this record...")
    return redirect("/Tc/tc_transport_vehicle_category")


def ins_trans_vehicat(request):
    if request.method=="POST":
        form=transportcompany_vehiclecategoryform(request.POST)
        print("--------",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/Tc/tc_transport_vehicle_category")
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form=transportcompany_vehiclecategoryform()

    c = TransportCompany.objects.all()
    v = Vehicle_category.objects.all()

    return render(request,"insert_trans_vehicat.html",{"form":form,"t1":c,"v1":v})


def edit_trans_vehicle_category(request,id):
    t=TransportCompany.objects.all()
    v=Vehicle_category.objects.all()
    tv=TransportCompany_Vehicle_category.objects.get(TransportCompany_Vehicle_category_id=id)
    return render(request,"update_trans_vehicle_category.html",{"tv":tv,"t":t,"v":v})


def upd_trans_vehicle_category(request,id):
    tv = TransportCompany_Vehicle_category.objects.get(TransportCompany_Vehicle_category_id=id)

    form=transportcompany_vehiclecategoryform(request.POST,instance=tv)
    print("----------",form.errors)
    if form.is_valid():
        try:

            form.save()
            return redirect("/Tc/tc_transport_vehicle_category")
        except:
            print("--------",sys.exc_info())
    else:
        form=transportcompany_vehiclecategoryform()

    t = TransportCompany.objects.all()
    v=Vehicle_category.objects.all()
    return render(request,"update_trans_vehicle_category.html",{"tv":tv,"t":t,"v":v})


def trans_feedback(request):
    if request.session.has_key('uname'):
        id1 = request.session['transport_id']
        c = Feedback.objects.filter(TransportCompany_id=id1)
        return render(request, "trans_feedback.html",{"fb":c})
    else:
        return redirect('/Tc/trans_login/')


def trans_booking(request):
    if request.session.has_key('uname'):
        id1 = request.session['transport_id']
        c = Booking.objects.filter(TransportCompany_id=id1)

        return render(request, "trans_booking.html",{"bk":c})
    else:
        return redirect('/Tc/trans_login/')


def trans_gallery(request):
    if request.session.has_key('uname'):
        id1 = request.session['transport_id']
        c = Gallery.objects.filter(TransportCompany_id=id1)
        return render(request, "trans_gallery.html",{"gr":c})
    else:
        return redirect('/Tc/trans_login/')


def tran_del_gallery(request,id):
    try:
        a=Gallery.objects.get(gallery_id=id)
        a.delete()
        messages.error(request, "Record is deleted successfully...")
    except ProtectedError:
        messages.error(request, "You can't delete this record...")
    return redirect("/Tc/tras_gallery")


def trans_insert_gallery(request):

    if request.method == "POST":
        form = galleryform(request.POST,request.FILES)
        print("++++++++++++++++++",form.errors)
        if form.is_valid():
            handle_upload_file(request.FILES['gallry_path'])
            form.save()
            return redirect('/Tc/tras_gallery')
    else:
       form = galleryform()

    c = TransportCompany.objects.all()
    return render(request,'trans_insert_gallery.html',{"form":form,"t1":c})



def edit_trans_gallery(request,id):
    t = TransportCompany.objects.all()
    g = Gallery.objects.get(gallery_id=id)
    return render(request,"trans_update_gallery.html",{"g":g,"t":t})


def upd_trans_gallery(request,id):
    g = Gallery.objects.get(gallery_id=id)

    form=galleryform(request.POST,request.FILES,instance=g)
    print("----------",form.errors)
    if form.is_valid():
        try:
            handle_upload_file(request.FILES['gallry_path'])
            form.save()
            return redirect("/Tc/tras_gallery")
        except:
            print("--------",sys.exc_info())
    else:
        form=galleryform()

    t = TransportCompany.objects.all()
    return render(request,"trans_update_gallery.html",{"g":g,"t":t})





def transport_package(request):
    if request.session.has_key('uname'):
        id1 = request.session['transport_id']
        c = Package.objects.filter(TransportCompany_id=id1)

        return render(request, "trans_package.html",{"pc":c})
    else:
        return redirect('/Tc/trans_login/')



def trans_del_package(request,id):
    try:
        p=Package.objects.get(package_id=id)
        p.delete()
        messages.error(request, "Record is deleted successfully...")
    except ProtectedError:
        messages.error(request, "You can't delete this record...")
    return redirect("/Tc/tras_package/")


def trans_ins_package(request):
    t=TransportCompany.objects.all()
    s=Service_category.objects.all()
    if request.method=="POST":
        form=packageform(request.POST)
        print("--------",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/Tc/tras_package/")
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form=packageform()

    return render(request,"trans_insert_package.html",{"form":form,"c1":t,"s1":s})


def trans_package_update(request,id):
    p = Package.objects.get(package_id=id)
    form = packageform(request.POST, instance=p)
    print("_______", form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/Tc/tras_package/")
        except:
            print("_________", sys.exc_info())
    t = TransportCompany.objects.all()
    s = Service_category.objects.all()
    return render(request,"trans_edit_package.html",{"package":p,"tc":t,"sc":s})


def trans_package_edit(request,id):
    t = TransportCompany.objects.all()
    s = Service_category.objects.all()
    p = Package.objects.get(package_id=id)
    return render(request, "trans_edit_package.html", {"p": p,"tc":t,"sc":s})


def trans_product(request):
    c=Product.objects.all()
    return render(request, "trans_product.html",{"pd":c})


def trans_product_update(request,id):
    t = TransportCompany.objects.all()
    s = Service_category.objects.all()
    p=Product.objects.get(product_id=id)
    form = productform(request.POST, instance=p)
    print("_______", form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/Tc/trans_product")
        except:
            print("_________", sys.exc_info())
    return render(request,"trans_edit_product.html", {"product": p})


def trans_product_edit(request,id):
    p=Product.objects.get(product_id=id)
    return render(request, "trans_edit_product.html", {"product":p})


def trans_ins_product(request):
    if request.method=="POST":
        form=productform(request.POST)
        print("--------",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/Tc/trans_product")
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form=productform()

    return render(request,"trans_insert_product.html",{"form":form})


def trans_del_product(request,id):
    try:
        p=Product.objects.get(product_id=id)
        p.delete()
        messages.error(request, "Record is deleted successfully...")
    except ProtectedError:
        messages.error(request, "You can't delete this record...")
    return redirect("/Tc/trans_product")


def trans_booking_detail(request):
    c=Booking_detail.objects.all()
    return render(request, "trans_booking_detail.html",{"bkd":c})



def Transcomp_profile(request):
    id=request.session['transport_id']
    print("---------------",id)
    t = TransportCompany.objects.get(TransportCompany_id = id )
    t1 = TransportCompany.objects.filter(TransportCompany_id = id )
    a = Area.objects.all()
    cm = Company.objects.all()
    return render(request, "transcomp_edit_profile.html", {"t": t , "area" : a , "t1" : t1 , "cm" : cm })


def Transcomp_update_profile(request):
    if request.method == "POST":
        id = request.session['transport_id']
        print("--------id",id)
        t2 =TransportCompany.objects.get(TransportCompany_id = id)
        a1 = Area.objects.all()
        form =TransportCompanyform1(request.POST,instance= t2)
        print("------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect("/Tc/transcomp_profile/")
            except:
                print("----------------", sys.exc_info())
        else:
            pass

    else:
        form = TransportCompanyform1()

    t1 = TransportCompany.objects.filter(TransportCompany_id=id)
    return render(request , "transcomp_edit_profile.html" , {"t2" : t2 , "area" : a1 , "t1":t1 })


def Transcomp_edit_profilepic(request):
    id = request.session['transport_id']
    print("--------id", id)
    t2 = TransportCompany.objects.get(TransportCompany_id=id)
    return render(request, "transcomp_profilepic.html", {"t2": t2 })


def Transcomp_profilepic(request):
    if request.method == "POST":
        id = request.session['transport_id']
        print("--------id", id)
        t2 = TransportCompany.objects.get(TransportCompany_id=id)
        form = TransportCompanyform(request.POST,request.FILES,instance=t2)
        print("------------", form.errors)

        if form.is_valid():
            try:
                handle_upload_file(request.FILES['TransportCompany_image'])
                form.save()
                return redirect("/Tc/transcomp_profile/")
            except:
                print("----------------", sys.exc_info())
        else:
            pass

    else:
        form = TransportCompanyform()

    t1 = TransportCompany.objects.filter(TransportCompany_id=id)
    return render(request, "transcomp_profilepic.html", {"t2": t2,  "t1": t1})



def trans_acceptbooking(request,id):
    b = Booking.objects.get(booking_id=id)
    b.booking_status2 = 1
    b.save()
    return redirect("/Tc/tras_booking/")

def trans_rejectbooking(request,id):
    b = Booking.objects.get(booking_id=id)
    b.booking_status2 = 3
    b.save()
    return redirect("/Tc/tras_booking/")


def trans_driver(request):
    id1 = request.session['transport_id']
    d=Driver.objects.filter(TransportCompany_id=id1)
    return render(request,"trans_driver.html",{"dr":d})

def del_trans_driver(request,id):
    try:
        a=Driver.objects.get(driver_id=id)
        a.delete()
        messages.error(request, "Record is deleted successfully...")
    except ProtectedError:
        messages.error(request, "You can't delete this record...")
    return redirect("/Tc/trans_driver/")


def trans_insert_driver(request):
    if request.method == "POST":
        form = driverform(request.POST,request.FILES)
        print("++++++++++++++++++",form.errors)
        if form.is_valid():
            handle_upload_file(request.FILES['license_image'])
            form.save()
            return redirect('/Tc/trans_driver/')
    else:
       form = driverform()

    c = TransportCompany.objects.all()
    return render(request,'trans_insert_driver2.html',{"form":form,"t1":c})




def edit_trans_driver(request,id):
    t = TransportCompany.objects.all()
    g = Driver.objects.get(driver_id=id)
    return render(request,"trans_update_driver2.html",{"g":g,"t":t})


def upd_trans_driver(request,id):
    g = Driver.objects.get(driver_id=id)
    form=driverform(request.POST,request.FILES,instance=g)
    print("----------",form.errors)
    if form.is_valid():
        try:
            handle_upload_file(request.FILES['license_image'])
            form.save()
            return redirect("/Tc/trans_driver/")
        except:
            print("--------",sys.exc_info())
    else:
        form=driverform()
    t = TransportCompany.objects.all()
    return render(request,"trans_update_driver2.html",{"g":g,"t":t})


def trans_quotation(request,id):
    b=Booking.objects.get(booking_id=id)
    return render(request,"trans_insert_quotation.html",{"b":b})


def trans_upd_quatation(request,id):
    b=Booking.objects.get(booking_id=id)

    form = bookingform(request.POST,instance=b)
    print("----------",form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/Tc/tras_booking/")
        except:
            print("--------",sys.exc_info())
    else:
        form=bookingform()

    return render(request, "trans_insert_quotation.html", {"b": b})


def trans_editdriver(request,id):
    b=Booking.objects.get(booking_id=id)
    d=Driver.objects.all()
    return render(request,"trans_insert_driver.html",{"b":b,"d":d})

def trans_upd_driver(request,id):
    b=Booking.objects.get(booking_id=id)
    d = Driver.objects.all()
    form = bookingform2(request.POST,instance=b)
    print("----------",form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/Tc/tras_booking/")
        except:
            print("--------",sys.exc_info())
    else:
        form=bookingform2()

    return render(request, "trans_insert_driver.html", {"b": b,"d":d})



def trans_report1(request):
    t1 = TransportCompany.objects.all()
    bk = Booking.objects.all()

    if request.method == "POST":
        key = request.POST["TransportCompany_name"]
        print("--- Transport --------", key)
        bk = Booking.objects.filter(TransportCompany_id_id=key)

    return render(request, "trans_report1.html",{"bk": bk, "t1": t1})


def trans_report2(request):
    que = Booking.objects.all()

    if request.method == "POST":

        start = request.POST["start"]
        end = request.POST["end"]

        start = parse_date(start)
        end = parse_date(end)
        print("----",start,"---------",end)

        que = Booking.objects.filter(date__range=[start,end])

    return render(request, "trans_report2.html", {"que": que})



def trans_report3(request):
    sql1="SELECT (select area_name from area WHERE area_id = c.area_id_id) as customer_id , count(*) as total FROM customer c JOIN area a where c.area_id_id = a.area_id group by c.area_id_id"
    data=Customer.objects.raw(sql1)
    return render(request,"trans_report3.html",{"data":data})


def trans_report6(request):

    a1=Area.objects.all()
    cs=Customer.objects.all()

    if request.method == "POST":
        key = request.POST["area_name"]
        print("--- Transport --------", key)
        cs=Customer.objects.filter(area_id_id=key)

    return render(request, "trans_report6.html",{"cs": cs, "a1": a1})

def quotationreport(request):
    tid = request.session['transport_id']
    b = Booking.objects.filter(TransportCompany_id = tid )

    if request.method == "POST":
        key = request.POST["booking_status"]
        print("--- Area --------", key)
        b = Booking.objects.filter(booking_status = key ,TransportCompany_id = tid )

    return render(request, "quotationreport.html",{"b": b  })



def cancellationreport(request):
    tid = request.session['transport_id']
    b = Booking.objects.filter(TransportCompany_id=tid)

    if request.method == "POST":
        key = request.POST["booking_status2"]
        print("--- Area --------", key)
        b = Booking.objects.filter(booking_status2 = key , TransportCompany_id = tid)

    return render(request, "cancellationreport.html",{"b": b  })


def paymentreport(request):
    tid = request.session['transport_id']
    b = Booking.objects.filter(TransportCompany_id=tid)

    if request.method == "POST":
        key = request.POST["payment_status"]
        print("--- Area --------", key)
        b = Booking.objects.filter(payment_status = key , TransportCompany_id = tid)

    return render(request, "paymentreport.html",{"b": b  })

