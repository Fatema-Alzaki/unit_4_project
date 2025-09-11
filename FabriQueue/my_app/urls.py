from django.urls import path
from . import views  # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),

    # Print Jobs
    path('printjobs/', views.printjob_index, name='printjob-index'),
    path('printjobs/create/', views.PrintJobCreate.as_view(), name='printjob-create'),
    path('printjobs/<int:printjob_id>/', views.printjob_detail, name='printjob-detail'),
    path('printjobs/<int:pk>/update/', views.PrintJobUpdate.as_view(), name='printjob-update'),
    path('printjobs/<int:pk>/delete/', views.PrintJobDelete.as_view(), name='printjob-delete'),

    # Materials
    path('materials/', views.MaterialList.as_view(), name='material-index'),
    path('materials/create/', views.MaterialCreate.as_view(), name='material-create'),
    path('materials/<int:pk>/', views.MaterialDetail.as_view(), name='material-detail'),
    path('materials/<int:pk>/update/', views.MaterialUpdate.as_view(), name='material-update'),
    path('materials/<int:pk>/delete/', views.MaterialDelete.as_view(), name='material-delete'),

    # Printers
    path('printers/', views.PrinterList.as_view(), name='printer-index'),
    path('printers/create/', views.PrinterCreate.as_view(), name='printer-create'),
    path('printers/<int:pk>/', views.PrinterDetail.as_view(), name='printer-detail'),
    path('printers/<int:pk>/update/', views.PrinterUpdate.as_view(), name='printer-update'),
    path('printers/<int:pk>/delete/', views.PrinterDelete.as_view(), name='printer-delete'),

    # About page
    path('about/', views.about, name='about'),
]
