from django.contrib import admin
from django.urls import path, include

from . import views


app_name = 'mbTest'


urlpatterns = [
    path('', views.mb_test_view, name='test'),
    path('ajax/test-submit/', views.mb_test_view_ajax, name='test_ajax'),
    path('result/<int:pk>/', views.display_result_view, name='result'),
    path('bas-EB-COSMOS-ke-liye/', views.display_results_for_eb_view, name='results_for_eb')
]