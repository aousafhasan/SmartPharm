from django.urls import path
# from .import HODViews
# from .import pharmacistViews,DoctorViews,views,patient_view,clerkViews
from django.contrib.auth import views as auth_views
from .import views


urlpatterns=[
    # path('',HODViews.adminDashboard,name='admin_dashboard'),
    # path('admin_user/patient_form/',HODViews.createPatient,name='patient_form'),
    # path('admin_user/all_patients/',HODViews.allPatients,name='all_patients'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    # path('get_user_details/', views.get_user_details, name="get_user_details"),
]