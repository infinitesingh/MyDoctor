from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

import logging

logger = logging.getLogger('django')

def signin_signup_view(request):
    return render(request, 'users/signin_signup.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            logger.info(f"form is %s",user)
            login(request, user)
            return redirect('home')  # Redirect to homepage or clinic dashboard based on role
        else:
            logger.info("invalid form")
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signin_signup.html', {'signup_form': form})


from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'users/signin_signup.html'  # Your custom login template

    def form_valid(self, form):
        # Call the parent class's form_valid method to log the user in
        response = super().form_valid(form)
        
        # Perform additional tasks after login
        user = form.get_user()
        logger.info(f"User {user.username} logged in successfully.")

        # Optionally, you can redirect to a specific URL after login
        # return redirect('your_desired_url')

        # If you want to return the default response, just return it
        return response

    def get_success_url(self):
        # You can specify where to redirect the user after a successful login
        return super().get_success_url()  # Default behavior, or specify your URL


