from django.db import models

# Create your models here.


class State(models.Model):
    state_id=models.AutoField(primary_key=True)
    state_name=models.CharField(max_length=30)

    class Meta:
        db_table="State"


class City(models.Model):
    city_id=models.AutoField(primary_key=True)
    city_name=models.CharField(max_length=30)
    state_id=models.ForeignKey(State,on_delete=models.PROTECT)

    class Meta:
        db_table="City"


class Area(models.Model):
    area_id=models.AutoField(primary_key=True)
    area_name=models.CharField(max_length=30)
    pincode=models.IntegerField()
    city_id=models.ForeignKey(City,on_delete=models.PROTECT)

    class Meta:
        db_table="Area"


class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    company_name=models.CharField(max_length=50)
    email=models.EmailField()
    addressline1=models.CharField(max_length=100)
    addressline2=models.CharField(max_length=75)
    landmark=models.CharField(max_length=30)
    contact=models.CharField(max_length=13)

    class Meta:
        db_table="Company"


class Customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    contact=models.CharField(max_length=13)
    addressline1=models.CharField(max_length=100)
    addressline2=models.CharField(max_length=75)
    landmark=models.CharField(max_length=30)
    gender=models.CharField(max_length=11)
    is_admin=models.IntegerField(default=0)
    OTP=models.CharField(max_length=10)
    OTP_used=models.IntegerField(default=0)
    area_id=models.ForeignKey(Area,on_delete=models.PROTECT)
    company_id=models.ForeignKey(Company,on_delete=models.PROTECT,default=1)

    class Meta:
        db_table="Customer"





class TransportCompany_package(models.Model):
    TransportCompany_pk_id=models.AutoField(primary_key=True)
    TransportCompany_pk_name=models.CharField(max_length=30)
    Amount=models.IntegerField()
    description=models.CharField(max_length=45)
    duration=models.CharField(max_length=45)
    company_id=models.ForeignKey(Company,on_delete=models.PROTECT,default=1)

    class Meta:
        db_table="TransportCompany_package"


class TransportCompany(models.Model):
    TransportCompany_id=models.AutoField(primary_key=True)
    TransportCompany_name=models.CharField(max_length=50)
    owner_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=15)
    contact=models.CharField(max_length=13)
    addressline1=models.CharField(max_length=100)
    addressline2 = models.CharField(max_length=75)
    landmark = models.CharField(max_length=30)
    licence_no=models.CharField(max_length=20)
    TransportCompany_image=models.FileField(max_length=100)
    area_id = models.ForeignKey(Area, on_delete=models.PROTECT)
    company_id = models.ForeignKey(Company, on_delete=models.PROTECT,default=1,null=False)
    TransportCompany_pk_id = models.ForeignKey(TransportCompany_package, on_delete=models.PROTECT)
    reg_start_date = models.DateField()
    reg_end_date = models.DateField()


    class Meta:
        db_table = "TransportCompany"


class Driver(models.Model):
    driver_id=models.AutoField(primary_key=True)
    driver_name=models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=15)
    contact = models.CharField(max_length=13)
    addressline1 = models.CharField(max_length=100)
    addressline2 = models.CharField(max_length=75)
    landmark = models.CharField(max_length=30)
    license_image=models.FileField()
    TransportCompany_id=models.ForeignKey(TransportCompany,on_delete=models.PROTECT)

    class Meta:
        db_table="Driver"


class Service_category(models.Model):
    service_category_id=models.AutoField(primary_key=True)
    service_category_name=models.CharField(max_length=30)
    service_image=models.FileField(max_length=100)
    description=models.CharField(max_length=500)

    class Meta:
        db_table="Service_category"


class Vehicle_category(models.Model):
    vehicle_category_id = models.AutoField(primary_key=True)
    vehicle_category_name = models.CharField(max_length=30)
    vehicle_image=models.FileField(max_length=100)
    description = models.CharField(max_length=500)

    class Meta:
        db_table = "Vehicle_category"


class TransportCompany_Service_category(models.Model):
    TransportCompany_Service_category_id=models.AutoField(primary_key=True)
    TransportCompany_id = models.ForeignKey(TransportCompany, on_delete=models.PROTECT)
    service_category_id=models.ForeignKey(Service_category,on_delete=models.PROTECT)

    class Meta:
        db_table="TransportCompany_Service_category"


class TransportCompany_Vehicle_category(models.Model):
    TransportCompany_Vehicle_category_id=models.AutoField(primary_key=True)
    rateperKM=models.FloatField()
    TransportCompany_id = models.ForeignKey(TransportCompany, on_delete=models.PROTECT)
    Vehicle_category_id = models.ForeignKey(Vehicle_category, on_delete=models.PROTECT)

    class Meta:
        db_table = "TransportCompany_Vehicle_category"


class Feedback(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    description=models.CharField(max_length=100)
    date=models.DateField()
    customer_id=models.ForeignKey(Customer,on_delete=models.PROTECT)
    TransportCompany_id = models.ForeignKey(TransportCompany, on_delete=models.PROTECT)

    class Meta:
        db_table="Feedback"


class Gallery(models.Model):
    gallery_id=models.AutoField(primary_key=True)
    gallry_path=models.FileField()
    TransportCompany_id= models.ForeignKey(TransportCompany, on_delete=models.PROTECT)

    class Meta:
        db_table="Gallery"


class Package(models.Model):
    package_id=models.AutoField(primary_key=True)
    package_name=models.CharField(max_length=30)
    amount=models.IntegerField()
    description=models.CharField(max_length=400)
    TransportCompany_id = models.ForeignKey(TransportCompany, on_delete=models.PROTECT)
    service_category_id=models.ForeignKey(Service_category,on_delete=models.PROTECT)

    class Meta:
        db_table="Package"


class Booking(models.Model):
    booking_id=models.AutoField(primary_key=True)
    date=models.DateField()
    Transport_date=models.DateField()
    booking_status=models.CharField(max_length=11)
    booking_status2=models.CharField(max_length=11)
    payment_status=models.CharField(max_length=11)
    from_location=models.CharField(max_length=30)
    to_location=models.CharField(max_length=30)
    quotation_amount=models.FloatField()
    TransportCompany_id = models.ForeignKey(TransportCompany, on_delete=models.PROTECT)
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT)
    vehicle_id=models.ForeignKey(Vehicle_category,on_delete=models.PROTECT,null=True)
    package_id=models.ForeignKey(Package,on_delete=models.PROTECT)
    driver_id=models.ForeignKey(Driver,on_delete=models.PROTECT,null=True)

    class Meta:
        db_table="Booking"


class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=45)

    class Meta:
        db_table="Product"


class Booking_detail(models.Model):
    booking_detail_id=models.AutoField(primary_key=True)
    qty=models.IntegerField()
    booking_id=models.ForeignKey(Booking,on_delete=models.PROTECT)
    product_id=models.ForeignKey(Product,on_delete=models.PROTECT)

    class Meta:
        db_table="Booking_detail"
