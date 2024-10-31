from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout

def custom_csrf_failure(request, reason=""):
    return redirect('login')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Log the user in
            auth_login(request, user)

            # Check the user's role and redirect accordingly
            if user.role == 'it_staff':
                return redirect('itstaffdashboard')
            elif user.role == 'ceso_staff':
                return redirect('cesodashboard')
            elif user.role == 'employee':
                return redirect('employeedashboard')
        else:
            # Error message for incorrect username or password
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login/login.html')


def custom_logout(request):
    logout(request)
    return redirect('login')


# IT Staff START


# Define a test function for the user role check
def it_staff_required(user):
    return user.is_authenticated and user.role == 'it_staff'

def ceso_staff_required(user):
    return user.is_authenticated and user.role == 'ceso_staff'

def employee_required(user):
    return user.is_authenticated and user.role == 'employee'




# it dashboard start
@user_passes_test(it_staff_required, login_url='login')
def itstaffdashboard(request):
    # Pass user info to the template
    return render(request, 'itstaff/itstaff_dashboard.html', {
        'username': request.user.username,
        'role': request.user.get_role_display()  # Display role label from ROLE_CHOICES
    })
# it dashboard end


# it add start
@user_passes_test(it_staff_required, login_url='login')
def itstaffadduser(request):
    User = get_user_model()  # Get the custom user model

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        role = request.POST.get('role')
        password = request.POST.get('password')

        # Create and save the new user
        try:
            new_user = User.objects.create_user(username=username, email=email, password=password, role=role)
            new_user.save()
            messages.success(request, f'User {username} has been added successfully.')
            return redirect('itstaffadduser')
        except Exception as e:
            messages.error(request, f'Error adding user: {str(e)}')

    return render(request, 'itstaff/itstaff_adduser.html', {
        'username': request.user.username,
        'role': request.user.get_role_display()
    })

# it add user end



# IT Staff END  




# CESO STAFF START



# ceso staff dashboard start
@user_passes_test(ceso_staff_required, login_url='login')
def cesodashboard(request):
    # Pass user info to the template
    return render(request, 'ceso_staff/ceso_dashboard.html',)
# ceso staff dashboard end




# ceso staff create events start
@user_passes_test(ceso_staff_required, login_url='login')
def cesoaddevent(request):
    # Pass user info to the template
    return render(request, 'ceso_staff/ceso_addevents.html',)
# ceso staff create events end





# CESO STAFF END





# EMPLOYEE STAFF START


@user_passes_test(employee_required, login_url='login')
def employeedashboard(request):
    # Pass user info to the template
    return render(request, 'employee/employee_dashboard.html',{
        'username': request.user.username,
        'role': request.user.get_role_display()  # Display role label from ROLE_CHOICES
    })



# EMPLOYEE STAFF END
