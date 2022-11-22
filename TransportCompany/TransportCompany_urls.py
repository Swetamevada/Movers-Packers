from django.urls import path
from TransportCompany import TransportCompany_views
urlpatterns = [
    path('transportcompany_index/',TransportCompany_views.transportcopmany_index),
    path('trans_registration/',TransportCompany_views.transport_register),
    path('trans_login/',TransportCompany_views.transportCompany_login),
    path('trans_logout/',TransportCompany_views.trancom_logout),
    path('trans_forgot_password/', TransportCompany_views.trancom_forgotpassword),
    path('renew_package/<int:id>', TransportCompany_views.renew),
    path('renew_updtae/<int:id>', TransportCompany_views.renew_update),

    path('trans_sendmail/', TransportCompany_views.tran_send_OTP),
    path('trans_resetpassword/', TransportCompany_views.tran_setpassword),

    path('trans_pricing/',TransportCompany_views.tc_package),

    path('tc_state/',TransportCompany_views.trans_state),
    path('tc_city/',TransportCompany_views.trans_city),
    path('tc_area/',TransportCompany_views.trans_area),
    path('tc_company/',TransportCompany_views.trans_company),
    path('tc_customer/',TransportCompany_views.trans_customer),
    path('tc_transportcompany/',TransportCompany_views.trans_transportcompany),
    path('tc_service_category/',TransportCompany_views.trans_service_category),
    path('tc_vehicle_category/',TransportCompany_views.trans_vehicle_category),
    path('tc_package/',TransportCompany_views.trans_package),
    path('tc_packagedetails/',TransportCompany_views.trans_package_detail),

    path('trans_product/',TransportCompany_views.trans_product),
    path('trans_ins_product/',TransportCompany_views.trans_ins_product),
    path('trans_delete_product/<int:id>',TransportCompany_views.trans_del_product),
    path('trans_edit_product/<int:id>',TransportCompany_views.trans_product_edit),
    path('trans_update_product/<int:id>',TransportCompany_views.trans_product_update),

    path('trans_booking_detail/',TransportCompany_views.trans_booking_detail),

    path('tc_transport_service_category/', TransportCompany_views.transport_service_category),
    path('delete_trans_service_category/<int:id>',TransportCompany_views.del_trans_service_category),
    path('ins_trans_servicecategory/', TransportCompany_views.ins_tran_servcat),
    path('edit_trans_service_category/<int:id>',TransportCompany_views.edit_trans_service_category),
    path('update_trans_service_category/<int:id>', TransportCompany_views.upd_trans_service_category),

    path('tc_transport_vehicle_category/', TransportCompany_views.transport_vehicle_category),
    path('delete_trans_vehicle_category/<int:id>', TransportCompany_views.del_trans_vehicle_category),
    path('ins_trans_vehicle_category/', TransportCompany_views.ins_trans_vehicat),
    path('edit_trans_vehicle_category/<int:id>', TransportCompany_views.edit_trans_vehicle_category),
    path('update_trans_vehicle_category/<int:id>', TransportCompany_views.upd_trans_vehicle_category),

    path('trans_driver/',TransportCompany_views.trans_driver),
    path('trans_delete_driver/<int:id>',TransportCompany_views.del_trans_driver),
    path('trans_insert_driver/',TransportCompany_views.trans_insert_driver),
    path('trans_edit_driver/<int:id>',TransportCompany_views.edit_trans_driver),
    path('trans_update_driver/<int:id>',TransportCompany_views.upd_trans_driver),

    path('tras_feedback/',TransportCompany_views.trans_feedback),
    path('tras_booking/',TransportCompany_views.trans_booking),
    path('trans_editquotation/<int:id>', TransportCompany_views.trans_quotation),
    path('trans_updatequation/<int:id>', TransportCompany_views.trans_upd_quatation),
    path('trans_updatetdriver/<int:id>', TransportCompany_views.trans_editdriver),
    path('trans_upddriver/<int:id>', TransportCompany_views.trans_upd_driver),
    path('trans_accept_booking/<int:id>', TransportCompany_views.trans_acceptbooking),
    path('trans_reject_booking/<int:id>', TransportCompany_views.trans_rejectbooking),

    path('tras_gallery/',TransportCompany_views.trans_gallery),
    path('ins_trans_gallery/', TransportCompany_views.trans_insert_gallery),
    path('del_tran_gallery/<int:id>', TransportCompany_views.tran_del_gallery),
    path('edit_trans_gallery/<int:id>', TransportCompany_views.edit_trans_gallery),
    path('update_trans_gallery/<int:id>', TransportCompany_views.upd_trans_gallery),

    path('tras_package/',TransportCompany_views.transport_package),
    path('ins_trans_package/',TransportCompany_views.trans_ins_package),
    path('del_trans_package/<int:id>',TransportCompany_views.trans_del_package),
    path('edit_trans_package/<int:id>',TransportCompany_views.trans_package_edit),
    path('update_trans_package/<int:id>',TransportCompany_views.trans_package_update),

    path('transcomp_profile/',TransportCompany_views.Transcomp_profile),
    path('transcomp_update_profile/',TransportCompany_views.Transcomp_update_profile),
    path('transcomp_edit_profilepic/',TransportCompany_views.Transcomp_edit_profilepic),
    path('trascomp_profilepic/',TransportCompany_views.Transcomp_profilepic),

    path('trans_report1/', TransportCompany_views.trans_report1),
    path('trans_report2/', TransportCompany_views.trans_report2),
    path('trans_report3/', TransportCompany_views.trans_report3),
    path('trans_report6/',TransportCompany_views.trans_report6),

    path('quotationreport/',TransportCompany_views.quotationreport),
    path('cancellationreport/',TransportCompany_views.cancellationreport),
    path('paymentreport/',TransportCompany_views.paymentreport),


]