from django.shortcuts import render, redirect
from .models import Student



def home(request):
    return render(request,'home.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST['username']

        # check if username already exists
        if Student.objects.filter(username=username).exists():
            return render(request, 'register.html', {'message': 'Username already exists'})

        Student.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            gender=request.POST['gender'],
            course=request.POST['course'],
            username=username,
            password=request.POST['password']
        )

        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            student = Student.objects.get(username=username, password=password)

            # store session
            request.session['student_id'] = student.id
            request.session['student_name'] = student.first_name

            return redirect('student_home')

        except Student.DoesNotExist:
            return render(request, 'login.html', {'message': 'Invalid Username or Password'})

    return render(request, 'login.html')


def student_home(request):
    if 'student_id' not in request.session:
        return redirect('login')

    student = Student.objects.get(id=request.session['student_id'])
    return render(request, 'student_home.html', {'student': student})


def edit_student(request):
    if 'student_id' not in request.session:
        return redirect('login')

    student = Student.objects.get(id=request.session['student_id'])

    if request.method == "POST":
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.email = request.POST['email']
        student.phone = request.POST['phone']
        student.gender = request.POST['gender']
        student.course = request.POST['course']
        student.save()

        return redirect('student_home')

    return render(request, 'edit_student.html', {'student': student})


def delete_student(request):
    if 'student_id' not in request.session:
        return redirect('login')

    student = Student.objects.get(id=request.session['student_id'])
    student.delete()

    request.session.flush()
    return redirect('register')


def logout(request):
    request.session.flush()
    return redirect('login')