
from django.urls import path
from client import client_views


urlpatterns=[
        path('Home/', client_views.home),
        path('client_login/',client_views.customer_login),

        path('client_forgot_password/',client_views.forgotpassword),

        path('client_sendmail/', client_views.sendotp),
        path('client_resetpassword/',client_views.setpassword),
        path('client_registration/', client_views.client_register),
        path('pricing/<int:id>',client_views.client_package),
        path('pricing2/<int:id>/<int:id2>',client_views.client_package2),

        path('client_vehicle_category/<int:id>/<int:id2>', client_views.client_vehicle_category),

        path('client_transportcompany/<int:id>', client_views.transportcompany_client),
        path('client_transportcompany2/<int:id>/',client_views.transportcompany_client2),

        path('client_transportcompanydetail/<int:id>', client_views.transportcompanydetail_client),
        path('client_transportcompanydetail2/<int:id>/<int:id2>/',client_views.transportcompanydetail_client2),

        path('client_service/<int:id>/<int:id2>',client_views.service_client),

        path('client_booking/<int:id2>/<int:id3>/<int:id>', client_views.booking),
        path('client_package_booking/<int:id2>/<int:id3>',client_views.booking),

        path('client_addbooking/<int:id2>/<int:id3>/<int:id>',client_views.add_booking),
        path('client_package_addbooking/<int:id2>/<int:id3>',client_views.add_booking),

        path('client_feedback/', client_views.ins_feedback),
        #path('client_bookingdetails/', client_views.bookdetails),
        path('client_bookingdetails/',client_views.bookdetails),
        path('client_edit_profile/', client_views.client_profile_edit),
        path('client_update_profile/', client_views.client_profile_update),
        path('contact/',client_views.contact),
        path('client_logout/',client_views.clientlogout),

        path('accept_booking/<int:id>',client_views.acceptbooking),
        path('reject_booking/<int:id>',client_views.rejectbooking),

        path('payment/<int:id>',client_views.payment),
        path('cancel/',client_views.cancel),
        path('success/<int:id>', client_views.success ),
        path('cash/<int:id>',client_views.cash),


        path('client_header_menu2/', client_views.load_menu2),
        path('client_header_menu1/',client_views.load_menu1),

        path('insproduct/<int:id>', client_views.insproduct),
        path('productview/<int:id>', client_views.viewproduct),
        path('clientdeleteproduct/<int:id>', client_views.client_productdelete),

        path('client_header_menu/',client_views.load_menu),

        path('search/',client_views.autosuggest,name='search1'),

        path('viewproduct/',client_views.viewproduct),
]