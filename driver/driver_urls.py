from django.urls import path
from driver import driver_views

urlpatterns = [
    path('driver_index/',driver_views.driver_index),

    path('driver_login/', driver_views.driver_login),
    path('driver_forgot_password/', driver_views.driver_forgot_password),
    path('driver_send_otp/', driver_views.driver_sendotp),
    path('driver_resetpassword/', driver_views.driver_resetpassword),
    path('driver_profile/',driver_views.driver_profile),
    path('driver_update_profile/',driver_views.driver_update_profile),
    path('driver_edit_pic/',driver_views.driver_edit_image),
    path('driver_update_pic/',driver_views.driver_pic),
    path('driver_logout/',driver_views.driver_logout),
    path('driver_report1/',driver_views.driver_report1),

    path('driver_state/',driver_views.driver_state),
    path('driver_city/',driver_views.driver_city),
    path('driver_area/',driver_views.driver_area),
    path('driver_company/', driver_views.driver_company),
    path('driver_customer/', driver_views.driver_customer),
    path('driver_transportcompany/', driver_views.driver_transportcompany),
    path('driver_servicecate/', driver_views.driver_service_category),
    path('driver_vehiclecate/', driver_views.driver_vehicle_category),
    path('driver_feedback/',driver_views.driver_feedback),
    path('driver_booking/',driver_views.driver_booking),
    path('driver_gallery/',driver_views.driver_gallery)

]