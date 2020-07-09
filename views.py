from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from.models import *
from django.contrib.auth import authenticate, logout


# Create your views here.
def index1(request):
    return render(request, 'index1.html')


def about(request):
    return render(request, 'about.html')


def login(request):
  return render(request, 'login.html')


def index1(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    doctor = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()

    d = 0;
    p = 0;
    a = 0;
    for i in doctor:
        d += 1
    for i in patient:
        p += 1
    for i in appointment:
        a += 1
        d1 = {'d': d, 'p': p, 'a': a}
    return render(request, 'admin_login.html',d1)


def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
    p = request.POST['pawd']
    user = authenticate(username=u, password=p)
    try:
     if user.is_staff:
      admin_login(request, user)
      error = "no"
     else:
        error = "yes"
    except:
        error = "yes"
        d = {'error': error}
        return render(request, 'adminlogin.html', d)

def view_doctor(request):
            if not request.user.is_staff:
                return redirect('adminlogin')
            doc = Doctor.objects.all()
            d = {'doc': doc}
            return render(request, 'view_doctor.html', d)

def add_doctor(request):
            error = ""
            if not request.user.is_staff:
                return redirect('adminlogin')
            if request.method == 'POST':
                n = request.POST['name']
                c = request.POST['contact']
                sp = request.POST['special']

                try:
                    Doctor.objects.create(name=n, mobile=c, special=sp)
                    error = "no"
                except:
                    error = "yes"
            d = {'error': error}
            return render(request, 'add_doctor.html')

def delete_doctor(request, pid):
            if not request.user.is_staff:
                return redirect("adminlogin")
            doctor = Doctor.objects.get(id=pid)
            doctor.delete()
            return redirect("view_doctor")

def view_patient(request):
            if not request.user.is_staff:
                return redirect('adminlogin')
            pat = Patient.objects.all()
            d = {'pat': pat}
            return render(request, 'view_patient.html')

def add_patient(request):
            error = ""
            if not request.user.is_staff:
                return redirect('adminlogin')
            if request.method == 'POST':
                n = request.POST['name']
                g = request.POST['gender']
                m = request.POST['mobile']
                a = request.POST['address']

                try:
                    Patient.objects.create(name=n, gender=g, mobile=m, addressl=a)
                    error = "no"
                except:
                    error = "yes"
                    d = {'error': error}
                return render(request, 'add_patient.html', d)

def delete_patient(request, pid):
            if not request.user.is_staff:
                return redirect("adminlogin")
            patient = Patient.objects.get(id=pid)
            patient.delete()
            return redirect("view_patient")

def view_appointment(request):
            if not request.user.is_staff:
                return redirect('adminlogin')
            appoint = Appointment.objects.all()
            d = {'appoint': appoint}
            return render(request, 'view_appointment.html')

def add_appointment(request):
            error = ""
            if not request.user.is_staff:
                return redirect('adminlogin')
            doctor1 = Doctor.objects.all()
            patient1 = Patient.objects.all()
            if request.method == 'POST':
                d = request.POST['doctor']
                p = request.POST['patient']
                d1 = request.POST['date']
                t1 = request.POST['time']
            doctor = Doctor.objects.filter(name=d).first()
            patient = Patient.objects.filter(name=p).first()

            try:
                Appointment.objects.create(doctor=doctor, patient=patient, date=d1, time=t1)
                error = "no"
            except:
                error = "yes"
            d = {'doctor': doctor1, 'patient': patient, 'error': error}
            return render(request, 'add_appointment.html')

def delete_appointment(request, pid):
            if not request.user.is_staff:
                return redirect("adminlogin")
            appointment = Appointment.objects.get(id=pid)
            appointment.delete()
            return redirect("view_appointment")

def Logout_admin(request):
            if not request.user.is_staff:
                return redirect('adminlogin')
            logout(request)
            return redirect('adminlogin')

def reg_done(request):
            name = request.POST.get('name')
            mail = request.POST.get('mail')
            phone = request.POST.get('phone')
            psw = request.POST.get('psw')
            rpsw = request.POST.get('rpsw')
            all = [name, mail, phone, psw, rpsw]
            messages.success(request, 'Profile details updated.')
            return render(request, 'reg_done.html', {'all': all})


#Create your views here.
