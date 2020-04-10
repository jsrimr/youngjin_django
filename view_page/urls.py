"""test_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path

from view_page import views

app_name = 'view_page'

urlpatterns = [
    # path('list_logs/', views.listlogs, name='list_logs'),
    # path('list_logs/(?P<dpt>[-\w]+)', views.listlogs.as_view(), name='list_logs'),
    path('list_logs/', views.listlogs.as_view(), name='list_logs'),
    # path('<dpt>', views.listlogs.as_view(), name='list_logs'),
    # path('list_logs/', views.listlogs.as_view(), name='list_logs'),
    # path('list_logs/', views.listlogs.as_view(), name='list_logs'),
    path('export/csv/', views.export_sales_csv, name='export_sales_csv'),
]

