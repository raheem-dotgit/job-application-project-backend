from django.core.mail import EmailMessage
from django.shortcuts import render
from .forms import JobApplicationForm
from .models import Form
from django.contrib import messages

def index(request):

    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']

            Form.objects.create(first_name=first_name, last_name=last_name, email=email, date=date,
                                occupation=occupation)

            message_body = f'A new Job Application is Submiited for {first_name} {last_name}'
            email_message = EmailMessage('Form Submittion Confirmation', message_body, to=[email])
            email_message.send()
            messages.success(request, 'Form Submitted Successfully!')
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')