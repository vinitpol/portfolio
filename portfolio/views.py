from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def certification(request):
    return render(request,'certification.html')

def project(request):
    return render(request,'project.html')

def resume(request):
    return render(request,'resume.html')

# def contact(request):
#     return render(request,'contact.html')

# views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        # Extract form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Sending the email
        send_mail(
            subject=f"Contact Form Submission from {name}",
            message=f"Message: {message}\n\nPhone: {phone}\nEmail: {email}",
            from_email=email,
            recipient_list=['vinitpol2000@gmail.com'],
        )

        # Add a success message
        messages.success(request, 'Your message has been sent successfully! We will get back to you shortly.')

        # Redirect to the same page to clear the form and show the toast
        return redirect('contact')  # Replace 'contact' with the name of your URL pattern for the contact page

    return render(request, 'contact.html')
