from django.shortcuts import render , redirect, get_object_or_404
from managerapp.models import ManagerDetailsModel
from staffapp.models import *
from django.contrib import messages
import profile

# Create your views here.
def manager_login(request):
       if request.method == "POST":
               gmail = request.POST.get("email")
               password = request.POST.get("password")
               try:
                 check = ManagerDetailsModel.objects.get(email=gmail,password=password ) 
                 request.session["manager_id"]= check.manager_id
                 status = check.status
                 if status =='Accepted':
                         message=messages.success(request,'login success')
                        
                 elif status =='Rejected' : 
                         message=messages.error(request,'Your request is Rejected so you cannot login')  
                 elif status == 'pending':
                         message=messages.info(request,'Your request is Pending so cannot login') 
                 return redirect ("manager-profile")
               
               except:
                    messages.error(request,"Valid Login") 
                    print('inavalid')     

       return  render(request,'manager/manager-login.html')

def manager_reg(request):
     if request.method == 'POST' and  request.FILES['photo']:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        department = request.POST.get('department')
        photo = request.FILES['photo']
        password = request.POST.get('password')
        ManagerDetailsModel.objects.create(name=name,phone=phone,email=email,department=department,photo=photo,password=password)
     return render(request,'manager/manager-reg.html')    

def manager_profile(request):
    manager_id = request.session["manager_id"]
    profile = ManagerDetailsModel.objects.filter(manager_id=manager_id)
    return render(request, 'manager/manager-profile.html',{'profile':profile})

def man_view_staff(request):
    staff_id = request.session["staff_id"]
    data = StaffDetailsModel.objects.get(staff_id=staff_id)
    department=data.department
    manager_id = request.session["manager_id"]
    data2 = ManagerDetailsModel.objects.get(manager_id=manager_id)
    department2 = data2.department
    print(department2)
    view_employee = StaffDetailsModel.objects.filter(department=department2) 
    return render(request,'manager/view-staff.html',{'view_employee':view_employee})    
   


def man_edit_staff(request,id):
    edit_staff = StaffDetailsModel.objects.filter(staff_id=id)
    obj = get_object_or_404(StaffDetailsModel,staff_id=id)
    if request.method == 'POST' :
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
     
        
        obj.name=name
        obj.phone=phone
        obj.email=email
        obj.save()
        return redirect('manager-view-staff')
    
    return render(request,'manager/staff-edit.html',{'edit_staff':edit_staff})  
   
   
# delete function of staff
def del_staff(request,id):
    staff = StaffDetailsModel.objects.filter(staff_id=id)
    staff.delete()
    return redirect('manager-view-staff')   