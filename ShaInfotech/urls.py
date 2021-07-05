from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from sha_final_app import views

urlpatterns = [
    url('admin/', admin.site.urls),
    path('', include('NewLoginSystem.urls')),
    # training_candidate_master urls
    path('training-candidate-master/', views.training_candidate_master, name="training_candidate_master"),
    path('training-candidate-master/view_query', views.view_query_candidate_master, name="view_query_candidate_master"),
    path('training-candidate-master/delete/<int:pk>/', views.delete_candidate_master, name='delete_candidate_master'),
    path('training-candidate-master/result/', views.view_query_show_candidate_master),
    path('training-candidate-master/update/<int:pk>/', views.update_candidate_master, name='update_candidate_master'),

    # course master urls
    path('course-master/create', views.course_master_new, name="course_master_new"),
    path('course-master/delete/<int:pk>/', views.delete_course, name='delete_course'),
    path('course-master/view', views.view_query_course, name="view_query_course"),
    path('course-master/update/<int:pk>/', views.update_course, name="update_course"),
    path('course-master/result/', views.view_query_show_course),

    # sourse master urls
    path('source-master/create', views.source_master_new, name="source_master_new"),
    path('source-master/view', views.view_query_source, name="view_query_source"),
    path('source-master/result/', views.view_query_show_source),
    path('source-master/update/<int:pk>/', views.update_source, name="update_source"),
    path('source-master/delete/<int:pk>/', views.delete_source, name='delete_source'),

    # calling master urls
    path('calling_master_form/', views.call_mast_save, name="calling_master_form"),
    path('view_query_callmast/', views.view_query_callmast, name="view_query_callmast"),
    path('calling-master/result/', views.view_query_show_callmast),
    path('call_mast_update/<int:pk>/', views.update_calling_master, name="update_calling_master"),
    path('call_mast_delete/<int:pk>/', views.call_mast_delete, name="call_mast_delete"),

    # calling transaction urls
    path('calling_transaction_form/', views.call_trans_save, name="calling_transaction_form"),
    path('view_query_calltrans/', views.view_query_calltrans, name="view_query_calltrans"),
    path('calling-transaction/result/', views.view_query_show_calltrans),
    path('call_trans_delete/<int:pk>/', views.call_trans_delete, name="call_trans_delete"),

    # training transaction urls
    path('training_transaction_form/', views.training_trans_save, name="training_transaction_form"),
    path('view_query_trainingtrans/', views.view_query_trainingtrans, name="view_query_trainingtrans"),
    path('training-transaction/result/', views.view_query_show_trainingtrans),
    path('training_transaction_delete/<int:pk>/', views.training_trans_delete, name="training_trans_delete"),

    # loan master app urls
    path('loan-candidate-master', views.loan_candidate_master, name="loan_candidate_master"),
    path('loan-candidate-master/view_query', views.loan_view_query_candidate_master,
         name="loan_view_query_candidate_master"),
    path('loan-candidate-master/delete/<int:pk>/', views.loan_delete_candidate_master,
         name='loan_delete_candidate_master'),
    path('loan-candidate-master/result/', views.loan_view_query_show_candidate_master),
    path('loan-candidate-master/update/<int:pk>/', views.loan_update_candidate_master,
         name='loan_update_candidate_master'),

    # loan transaction urls
    path('loan_transaction_form/', views.loan_trans_save, name="loan_transaction_form"),
    path('view_query_loantrans/', views.view_query_loantrans, name="view_query_loantrans"),
    path('loan-transaction/result/', views.view_query_show_loantrans),
    path('loan_transaction_delete/<int:pk>/', views.loan_trans_delete, name="loan_trans_delete"),
    path('loan_transaction_form/update/<int:pk>/', views.update_loan_transaction, name='update_loan_transaction'),
]
