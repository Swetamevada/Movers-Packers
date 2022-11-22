from mpm.models import *
from django import forms
from parsley.decorators import parsleyfy


@parsleyfy
class areaform(forms.ModelForm):
    class Meta:
        model=Area
        fields=["area_name","pincode","city_id"]

@parsleyfy
class stateform(forms.ModelForm):
    class Meta:
        model=State
        fields=["state_id","state_name"]


@parsleyfy
class cityform(forms.ModelForm):
    class Meta:
        model=City
        fields=["city_name","state_id"]


@parsleyfy
class packageform(forms.ModelForm):
    class Meta:
        model=Package
        fields=["package_name","amount","description","TransportCompany_id","service_category_id"]


@parsleyfy
class productform(forms.ModelForm):
    class Meta:
        model=Product
        fields=["product_name"]


@parsleyfy
class servicecategoryform(forms.ModelForm):
    class Meta:
        model=Service_category
        fields=["service_category_name","service_image","description"]


@parsleyfy
class vehiclecategoryform(forms.ModelForm):
    class Meta:
        model=Vehicle_category
        fields=["vehicle_category_name","vehicle_image","description"]


@parsleyfy
class transportcompany_servicecategoryform(forms.ModelForm):
    class Meta:
        model=TransportCompany_Service_category
        fields=["TransportCompany_id","service_category_id"]


@parsleyfy
class transportcompany_vehiclecategoryform(forms.ModelForm):
    class Meta:
        model=TransportCompany_Vehicle_category
        fields=["rateperKM","TransportCompany_id","Vehicle_category_id"]


@parsleyfy
class transportcompanypackageform(forms.ModelForm):
    class Meta:
        model=TransportCompany_package
        fields=["TransportCompany_pk_name","Amount","description","duration"]


@parsleyfy
class galleryform(forms.ModelForm):
    gallry_path=forms.FileField()
    class Meta:
        model=Gallery
        fields=["gallry_path","TransportCompany_id"]


@parsleyfy
class customerform(forms.ModelForm):
    class Meta:
        model=Customer
        fields=["customer_name","email","password","contact","addressline1","addressline2","landmark","gender","area_id"]


@parsleyfy
class bookingform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["quotation_amount"]


@parsleyfy
class bookingform2(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["driver_id"]


@parsleyfy
class transportcompanyform(forms.ModelForm):
    TransportCompany_image = forms.FileField()
    class Meta:
        model = TransportCompany
        fields = ["TransportCompany_name","owner_name","email","password","contact","addressline1","addressline2","landmark","licence_no","area_id","TransportCompany_image"]

@parsleyfy
class TransportCompanyform1(forms.ModelForm):
    class Meta:
        model = TransportCompany
        fields = ["TransportCompany_name", "owner_name", "email", "password", "contact", "addressline1",
                      "addressline2", "landmark", "licence_no", "area_id"]

@parsleyfy
class TransportCompanyform(forms.ModelForm):
    TransportCompany_image = forms.FileField()

    class Meta:
        model = TransportCompany
        fields = ["TransportCompany_image"]


@parsleyfy
class driverform(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["driver_name", "email", "password", "contact", "addressline1",
                  "addressline2", "landmark", "license_image", "TransportCompany_id"]


@parsleyfy
class Driverform(forms.ModelForm):
    class Meta:
        model=Driver
        fields=["driver_name","email","password","contact","addressline1","addressline2","landmark"]

@parsleyfy
class Driverform1(forms.ModelForm):
     license_image= forms.FileField()
     class Meta:
        model=Driver
        fields=["license_image"]



