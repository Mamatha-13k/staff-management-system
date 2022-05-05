from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages

from managerapp.models import ManagerDetailsModel
from staffapp.models import StaffDetailsModel

# Create your views here.
def admin_login(request):
    if request.method ==  "POST":
            name = request.POST.get('username')
            password =request.POST.get('password')
            if name =='admin' and password =='admin':
                print('correct')
                messages.success(request,"login successful")     
                return redirect('admin-index')
            else:
                  print('invalid')
                  messages.error(request,"login successful")
    return render(request,'admin/adminn-login.html')

def admin_index(request):
    manager_count = ManagerDetailsModel.objects.count()
    staff_count = StaffDetailsModel.objects.count()
    return render(request,'admin/admin-index.html',{'manager_count':manager_count,'staff_count':staff_count})  



def view_managers(request):
    manager = ManagerDetailsModel.objects.all()
    return render(request,'admin/admin-view-managers.html',{'manager':manager}) 



def view_staff(request):
    staff = StaffDetailsModel.objects.all()
    return render(request,'admin/admin-view-staff.html',{'staff':staff}) 

def edit_manager(request,id):
    manager = ManagerDetailsModel.objects.filter(manager_id=id)
    obj = get_object_or_404(ManagerDetailsModel,manager_id=id)
    if request.method == 'POST' :
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
     
        
        obj.name=name
        obj.phone=phone
        obj.email=email
        obj.save()
        return redirect('view-managers')
    return render(request,'admin/manager-edit.html',{'manager':manager})


def del_manager(request,id):
     manager_del = ManagerDetailsModel.objects.filter(manager_id=id)
     manager_del.delete()
     return redirect('view-managers')


def edit_staff(request,id):
    staff = StaffDetailsModel.objects.filter(staff_id=id)
    obj = get_object_or_404(StaffDetailsModel,staff_id=id)
    if request.method == 'POST' :
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
     
        
        obj.name=name
        obj.phone=phone
        obj.email=email
        obj.save()
        return redirect('view-staff')
    return render(request,'admin/staff-edit-admin.html',{'staff':staff})

def accept_manager(request,id):
           accept=get_object_or_404(ManagerDetailsModel,manager_id=id)  
           accept.status='Accepted'
           accept.save(update_fields=['status'])
           accept.save()
           return redirect('view-managers')  
       
def reject_manager(request,id):
           reject=get_object_or_404(ManagerDetailsModel,manager_id=id) 
           reject.status='Rejected'
           reject.save(update_fields=['status'])
           reject.save()
           return redirect('view-managers')          
