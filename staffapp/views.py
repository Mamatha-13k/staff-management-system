from django.shortcuts import render,redirect
from staffapp.models import *
from django.contrib import messages

# Create your views here.
def staff_login(request):
           if request.method == "POST":
               gmail = request.POST.get("email")
               password = request.POST.get("password")
               try:
                 check = StaffDetailsModel.objects.get(email=gmail,password=password ) 
                 request.session["staff_id"]= check.staff_id
                 messages.success(request,"Valid Login")
                 return redirect ("staff-profile")
                 print('valid')
               except:
                    messages.error(request,"Valid Login") 
                    print('inavalid')     

           return render(request,'staff/staff-login.html')

def staff_details(request):
    if request.method == 'POST' and  request.FILES['photo']:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        department = request.POST.get('department')
        photo = request.FILES['photo']
        password = request.POST.get('password')
        StaffDetailsModel.objects.create(name=name,phone=phone,email=email,department=department,photo=photo,password=password)

    return render(request,'staff/staff-reg.html') 

def staff_profile(request):
    staff_id = request.session["staff_id"]
    profile = StaffDetailsModel.objects.filter(staff_id=staff_id)
    return render(request,'staff/staff-profile.html',{'profile': profile})       
