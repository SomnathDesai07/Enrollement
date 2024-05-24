from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User_model
from django.contrib.auth.hashers import make_password

# Create your views here.
def add_show_view(r):
    stud = User_model.objects.all()
    if r.method == 'POST':
        fm = StudentRegistration(r.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            hashed_pw = make_password(pw)
            obj = User_model(name=nm, email=em, password=hashed_pw)
            obj.save()
            fm = StudentRegistration()  # Clear the form after saving
        stud = User_model.objects.all()  # Assign stud in the POST branch
    else:
        fm = StudentRegistration()
    return render(r, 'enroll_app/enrollCreateShow.html', {'form': fm, 'stu': stud})
# This function will Update/Edit
def update_data_view(r,id):
    if r.method=="POST":
        pi=User_model.objects.get(pk=id)
        fm=StudentRegistration(r.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        pi = User_model.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(r,'enroll_app/updatestudent.html',{'form':fm})
def delete_data_view(r,id):
    if r.method=="POST":
        pi=User_model.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


