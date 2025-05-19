from django.shortcuts import render,HttpResponse, redirect
from . import models
from . import forms
from django.contrib import messages

# This is for Models Form in django

def create_student(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES)#capturing the post request
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Student Profile Created successfully.')
            return redirect('home')
    else:
        form = forms.StudentForm()
    return render(request, 'student/create_student.html', {'form': form})

def home(request):
    students = models.Student.objects.all()
    return render(request, 'student/index.html', {'students' : students})

def update_student(request, id):
    student = models.Student.objects.get(id=id)
    form = forms.StudentForm(instance = student) #showing previous data on form
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES, instance=student)#capturing the post request
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Student Profile Updated successfully.')
            return redirect('home')


    # form = forms.StudentForm()
    return render(request, 'student/create_student.html', {'form': form, 'edit': True})

def delete_student(request, id):
    student = models.Student.objects.get(id=id)
    student.delete()
    messages.add_message(request, messages.SUCCESS, 'Student Profile Deleted successfully.')
    return redirect('home')




# This is for HTML form...........................
# def home(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         password = request.POST.get('password')
#         checkbox = request.POST.get('checkbox')
#         photo = request.FILES.get('photo')


#         if checkbox == 'on':
#             checkbox = True
#         else:
#             checkbox = False

#         student = models.Student(name = name, email = email, phone = phone, password = password, checkbox = checkbox, photo = photo)

#         student.save()

#         return HttpResponse("Account created sucessfully. ")

#     return render(request, "student/index.html")
