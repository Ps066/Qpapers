from django.shortcuts import render, redirect
from userauth.forms import UserRegistrationForm
from userauth.models import User

from django.contrib import messages
from django.contrib.auth import login , authenticate , logout
# Create your views here.



def register_view(request):
     if request.user.is_authenticated:
        messages.warning(request, f"You are already logged in!")
        return redirect("fdash:index")

     if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            # Create a new instance of your custom user model
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                # password1= form.cleaned_data['password1'],
                userrole='user',
            )

             # Set and save the password
            user.set_password(form.cleaned_data['password1'])
            user.save()

            # Log in the user
            login(request, user)

            # Get the username for success message
            username = form.cleaned_data['username']
            request.session['username'] = user.username
            request.session['email'] = user.email

            # Display success message
            messages.success(request, f"Hello {username}, Your Account was created Successfully")

            # Redirect the user to a different page
            return redirect("fdash:index")
            # Redirect or do something else
            # For example, you can redirect the user to a success page
     else:
         form = UserRegistrationForm()



    # form = UserRegistrationForm()
     context = {
        'form': form,
     }

     return render(request, './userauth/register.html',context)

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"You are already logged in!")
        return redirect("fdash:index")

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')

        try:
            user = user.objects.get(email=email)
        except:
            messages.warning(request, f"There is no user with {email}")
        

        user = authenticate(request, email=email ,  password=password)


        if user is not None:
            login(request,user)
            request.session['username'] = user.username
            request.session['email'] = user.email
            messages.success(request, f"You are logged in")
            return redirect("fdash:index")
        else:
            messages.warning(request, f"User does'nt exists")
    

    context = {
    }
    return render(request, 'userauth/login.html', context)


def logout_view(request):
    logout(request)
    messages.error(request, f"Your account is logged out")
    return redirect("home:index")