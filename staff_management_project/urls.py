"""staff_management_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainapp import views as main_views
from  staffapp import views as staff_views
from managerapp import views as manager_views
from adminapp import views as admin_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main_views.index,name='home'),
    path('about',main_views.about,name='about'),
    path('contact',main_views.contact,name='contact'),
    # staff routings
    path('staff-login',staff_views.staff_login,name='staff-login'),
    path('staff-reg',staff_views.staff_details,name='staff-reg'),
    path('staff-profile',staff_views.staff_profile,name='staff-profile'),
    # manager routings
    path('manager-login',manager_views.manager_login,name='manager-login'),
    path('manager-reg',manager_views.manager_reg,name='manager-reg'),
    path('manager-profile',manager_views.manager_profile,name='manager-profile'),
    path('manager-view-staff',manager_views.man_view_staff,name='manager-view-staff'),
    path('manager-staff-edit/<int:id>/',manager_views.man_edit_staff,name='manager-staff-edit'),
    path('manager-staff-del/<int:id>/',manager_views.del_staff,name='manager-staff-del'),
    # admin routings
    path('admin-login',admin_views.admin_login,name='admin-login'),
    path('admin-index',admin_views.admin_index,name='admin-index'),
    path('accept-manager/<int:id>/',admin_views.accept_manager,name='accept-manager'),
    path('reject-manager/<int:id>/',admin_views.reject_manager,name='reject-manager'),
    path('view-managers',admin_views.view_managers,name='view-managers'),
    path('view-staff',admin_views.view_staff,name='view-staff'),
    path('edit-manager/<int:id>/',admin_views.edit_manager,name='edit-manager'),
    path('edit-staff/<int:id>/',admin_views.edit_staff,name='edit-staff'),
    path('del-manager/<int:id>/',admin_views.del_manager,name='del-manager'),



]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)