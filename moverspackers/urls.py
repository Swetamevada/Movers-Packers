"""moverspackers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mpm import views
from django.conf.urls import url
from mpm.views import ViewHome , DashboardChart


urlpatterns = [
    path('admin/', admin.site.urls),
    path('state/', views.state),
    path('city/',views.city),
    path('area/',views.area),
    path('company/',views.company),
    path('customer/',views.customer),
    path('transportcompany/',views.transportcompany),
    path('driver/',views.driver),
    path('transportcompanypackage/',views.transportcompany_package),
    path('transportcompanypackagedetail/',views.transportcompany_package_detail),
    path('servicecategory/',views.service_category),
    path('vehiclecategory/',views.vehicle_category),
    path('transportcompanyservicecategory/',views.transportCompany_service_category),
    path('transportcompanyvehiclecategory/',views.transportCompany_vehicle_category),
    path('feedback/',views.feedback),
    path('gallery/',views.gallery),
    path('package/',views.package),
    path('booking/',views.booking),
    path('product/',views.product),
    path('bookingdetail/',views.booking_detail),

    path('login/',views.admin_login),
    path('forgotpassword/',views.forgot_password),
    path('sendmail/',views.send_otp),
    path('reset/',views.set_password),
    path('logout/',views.logout),
    path('report1/',views.report1),
    path('report2/',views.report2),
    path('report3/',views.report3),
    path('report4/',views.report4),
    path('report5/',views.report5),
    path('report6/',views.report6),
    path('report7/',views.report7),

    path('delete_state/<int:id>',views.del_state),
    path('delete_city/<int:id>',views.del_city),
    path('delete_area/<int:id>',views.del_area),
    path('delete_transportcompanypackage/<int:id>',views.del_TransportCompany_Package),
    path('delete_transportcompanypackagedetail/<int:id>',views.del_TransportCompany_Package_detail),
    path('delete_service_category/<int:id>',views.del_service_category),
    path('delete_vehicle_category/<int:id>',views.del_vehicle_category),
    path('delete_service_category_detail/<int:id>',views.del_service_category_detail),
    path('delete_vehicle_category_detail/<int:id>',views.del_vehicle_category_detail),
    path('delete_feedback/<int:id>',views.del_feedback),
    path('delete_gallery/<int:id>',views.del_gallery),
    path('delete_package/<int:id>',views.del_package),
    path('delete_product/<int:id>',views.del_product),


    path('ins_state/',views.ins_state),
    path('ins_area/',views.ins_area),
    path('ins_city/',views.ins_city),
    path('ins_package/',views.ins_package),
    path('ins_product/',views.ins_product),
    path('ins_servicecategory/',views.ins_servcat),
    path('ins_vehiclecategory/',views.ins_vehicat),
    path('ins_transportcompanyservicecategory/',views.ins_trancom_servcat),
    path('ins_transportcompanyvehiclecategory/',views.ins_trancom_vehicat),
    path('ins_transportcompanypackage/',views.ins_trancom_package),
    path('ins_transportcompanypackagedetail/',views.ins_trancom_package_detail),
    path('ins_gallery/',views.insert_gallery),


    path('edit_state/<int:id>',views.state_edit),
    path('update_state/<int:id>',views.state_update),
    path('edit_city/<int:id>',views.city_edit),
    path('update_city/<int:id>',views.city_update),
    path('edit_area/<int:id>',views.area_edit),
    path('update_area/<int:id>',views.area_update),
    path('edit_package/<int:id>', views.package_edit),
    path('update_package/<int:id>', views.package_update),
    path('edit_product/<int:id>', views.product_edit),
    path('update_product/<int:id>', views.product_update),
    path('edit_servicecategory/<int:id>', views.service_category_edit),
    path('update_servicecategory/<int:id>', views.service_category_update),
    path('edit_vehiclecategory/<int:id>', views.vehicle_category_edit),
    path('update_vehiclecategory/<int:id>', views.vehicle_category_update),
    path('edit_servicecategorydetail/<int:id>', views.servicecategorydetail_edit),
    path('update_servicecategorydetail/<int:id>', views.servicecategorydetail_update),
    path('edit_vehiclecategorydetail/<int:id>',views.vehiclecategorydetail_edit),
    path('update_transportcompanyvehiclecategory/<int:id>',views.vehiclecategorydetail_update),
    path('edit_transportcompanypackage/<int:id>', views.transportcompanypackage_edit),
    path('update_transportcompanypackage/<int:id>', views.transportcompanypackage_update),
    path('edit_transportcompanypackagedetail/<int:id>', views.transportcompanypackagedetail_edit),
    path('update_transportcompanypackagedetail/<int:id>', views.transportcompanypackagedetail_update),
    path('edit_gallery/<int:id>', views.gallery_edit),
    path('update_gallery/<int:id>', views.gallery_update),
    path('edit_profile/',views.profile_edit),
    path('update_profile/',views.profile_update),

    path('updatetdriver/<int:id>', views.editdriver),
    path('upddriver/<int:id>', views.upd_driver),

    path('editquotation/<int:id>', views.quotation),
    path('updatequation/<int:id>', views.upd_quatation),

    path('admin_accept_booking/<int:id>', views.admin_acceptbooking),
    path('admin_reject_booking/<int:id>', views.admin_rejectbooking),

    path('index/',views.dashboard),
    url(r'home', ViewHome.as_view(), name='home'),
    url(r'^api/chart/data/$', DashboardChart.as_view(),name="api-data"),




    path('client/',include('client.urls')),
    path('Tc/', include('TransportCompany.TransportCompany_urls')),
    path('driver/', include('driver.driver_urls')),


]
