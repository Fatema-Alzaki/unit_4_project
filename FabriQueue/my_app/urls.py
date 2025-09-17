from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),

    # PrintJobs
    path("printjobs/", views.PrintJobList.as_view(), name="printjob-list"),
    path("printjobs/create/", views.PrintJobCreate.as_view(), name="printjob-create"),
    path("printjobs/<int:pk>/", views.PrintJobDetail.as_view(), name="printjob-detail"),
    path("printjobs/<int:pk>/update/", views.PrintJobUpdate.as_view(), name="printjob-update"),
    path("printjobs/<int:pk>/delete/", views.PrintJobDelete.as_view(), name="printjob-confirm-delete"),
    path("printjobs/<int:pk>/history/", views.PrintJobHistoryList.as_view(), name="printjob-history"),
    
    
    # Materials
    path('materials/', views.MaterialList.as_view(), name='material-list'),
    path('materials/create/', views.MaterialCreate.as_view(), name='material-create'),
    path('materials/<int:pk>/', views.MaterialDetail.as_view(), name='material-detail'),
    path('materials/<int:pk>/update/', views.MaterialUpdate.as_view(), name='material-update'),
    path('materials/<int:pk>/delete/', views.MaterialDelete.as_view(), name='material-delete'),

    # Printers
    path('printers/', views.PrinterList.as_view(), name='printer-list'),
    path('printers/create/', views.PrinterCreate.as_view(), name='printer-create'),
    path('printers/<int:pk>/', views.PrinterDetail.as_view(), name='printer-detail'),
    path('printers/<int:pk>/update/', views.PrinterUpdate.as_view(), name='printer-update'),
    path("printers/<int:pk>/delete/", views.PrinterDelete.as_view(), name="printer-confirm-delete"),
    path("printers/<int:pk>/history/", views.PrinterHistoryList.as_view(), name="printer-history"),
    
    # History
    path("history/", views.PrintJobHistoryList.as_view(), name="history-list"),
    path("history/<int:pk>/", views.PrintHistoryDetail.as_view(), name="history-detail"),

    # About page
    path('about/', views.about, name='about'),
 
    # Dashboard
    path("dashboard/costs/", views.cost_dashboard, name="cost-dashboard"),

]
