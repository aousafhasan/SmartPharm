from django.urls import path
# from .import pharmacistViews,DoctorViews,views,patient_view,clerkViews
from django.contrib.auth import views as auth_views
from .import views, clerkViews, HODViews


urlpatterns=[
    path('',HODViews.adminDashboard,name='admin_dashboard'),
    path('admin_user/patient_form/',HODViews.createPatient,name='patient_form'),
    path('admin_user/all_patients/',HODViews.allPatients,name='all_patients'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    # path('get_user_details/', views.get_user_details, name="get_user_details"),

#HOD
path('admin_user/add_pharmacist/',HODViews.createPharmacist,name='add_pharmacist'),
    path('admin_user/manage_pharmacist/',HODViews.managePharmacist,name='manage_pharmacist'),
    path('admin_user/add_doctor/',HODViews.createDoctor,name='add_doctor'),
    path('admin_user/manage_doctor/',HODViews.manageDoctor,name='manage_doctor'),
    path('admin_user/add_pharmacyClerk/',HODViews.createPharmacyClerk,name='add_pharmacyClerk'),
    path('admin_user/admin_user/manage_pharmacyClerk/',HODViews.managePharmacyClerk,name='manage_pharmacyClerk'),
    path('admin_user/add_stock/',HODViews.addStock,name='add_stock'),
    path('admin_user/add_category/',HODViews.addCategory,name='add_category'),
    path('admin_user/manage_stock/',HODViews.manageStock,name='manage_stock'),
    path('admin_user/prescribe_drug/',HODViews.addPrescription,name='prescribe'),
    path('admin_user/edit_patient/<patient_id>/',HODViews.editPatient,name='edit_patient'),
    # path('add_patient_save/',HODViews.editPatientSave,name='edit_patient_save'),

    path('admin_user/delete_patient/<str:pk>/',HODViews.confirmDelete,name='delete_patient'),
    path('admin_user/patient_personalRecords/<pk>/',HODViews.patient_personalRecords,name='patient_record'),
    path('admin_user/delete_prescription/<str:pk>/',HODViews.deletePrescription,name='delete_prescription'),
    # path('admin_user/doctor_profile/',DoctorViews.doctorProfile,name='doctor_profile'),
    path('admin_user/hod_profile/',HODViews.hodProfile,name='hod_profile'),
    path('admin_user/delete_doctor/<str:pk>/',HODViews.deleteDoctor,name='delete_doctor'),
    path('admin_user/delete_pharmacist/<str:pk>/',HODViews.deletePharmacist,name='delete_pharmacist'),
    path('admin_user/delete_receptionist/<str:pk>/',HODViews.deletePharmacyClerk,name='delete_clerk'),
    path('admin_user/hod_profile/editAdmin_profile/',HODViews.editAdmin,name='edit-admin'),
    path('admin_user/delete_drug/<str:pk>/',HODViews.deleteDrug,name='delete_drug'),


    path('admin_user/edit_pharmacist/<staff_id>/', HODViews.editPharmacist, name="edit_pharmacist"),
    path('admin_user/edit_doctor/<doctor_id>/', HODViews.editDoctor, name="edit_doctor"),
    path('admin_user/edit_receptionist/<clerk_id>/', HODViews.editPharmacyClerk, name="edit_clerk"),
    path('admin_user/edit_drug/<pk>/', HODViews.editStock, name="edit_drug"),
    path('admin_user/receive_drug/<pk>/', HODViews.receiveDrug, name="receive_drug"),
    path('admin_user/reorder_level/<str:pk>/', HODViews.reorder_level, name="reorder_level"),
    path('admin_user/drug_details/<str:pk>/', HODViews.drugDetails, name="drug_detail"),

#Receptionist
    path('receptionist_profile/',clerkViews.receptionistProfile,name='clerk_profile'),
    path('receptionist_home/',clerkViews.clerkHome,name='clerk_home'),
    path('receptionist/patient_form/',clerkViews.createPatient,name='patient_form2'),
    path('receptionist/all_patients/',clerkViews.allPatients,name='all_patients2'),
    path('receptionist/edit_patient/<patient_id>/',clerkViews.editPatient,name='edit_patient_clerk'),
    path('receptionist/patient_personalRecords/<str:pk>/',clerkViews.patient_personalRecords,name='patient_record_clerk'),
    path('receptionist/delete_patient/<str:pk>/',clerkViews.confirmDelete,name='delete_patient_clerk'),
    # path('receptionist/dispense_drug/<str:pk>/',pharmacistViews.dispenseDrug,name='dispense_drug'),

]