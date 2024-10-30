from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login


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
                return redirect('itstaffdashboard')  # Redirect to the IT staff dashboard
            else:
                # Redirect to a default page for other roles
                return redirect('login')  # Change this to your default dashboard view

        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login/login.html')



# IT Staff IT Staff IT Staff IT Staff IT Staff IT Staff IT Staff IT Staff IT Staff START




# IT DASHBOARD START

def itstaffdashboard(request):
    # Render the IT staff dashboard without any role checks
    return render(request, 'itstaff/itstaff_dashboard.html')

# IT DASHBOARD END


# IT ADD USER START

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
            return redirect('itstaff_dashboard')  # Redirect to the IT staff dashboard or another appropriate page
        except Exception as e:
            messages.error(request, f'Error adding user: {str(e)}')

    return render(request, 'itstaff/itstaff_adduser.html')

# IT ADD USER END






# IT Staff IT Staff IT Staff IT Staff IT Staff IT Staff IT Staff IT Staff IT Staff END  




