
from random import randint

from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from djangoProject.settings import EMAIL_HOST_USER
from userextend.forms import UserExtendForm
from userextend.models import UserExtend


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = UserExtend
    form_class = UserExtendForm

    class UserCreateView(CreateView):
        template_name = 'userextend/create_user.html'
        model = UserExtend
        form_class = UserExtendForm


        # Varianta initiala

        # def form_valid(self, form):
            # if form.is_valid() and not form.errors:
            #    new_user = form.save(commit=False)
            #    new_user.first_name = new_user.first_name.title()
            #    new_user.last_name = new_user.last_name.title()
            #
            #    new_user.save()
            #
            #    subject = 'Created a new account!'
            #    message = f'Hello, {new_user.first_name} {new_user.last_name}. Your account is created.'
            #    from_email = EMAIL_HOST_USER
            #    to_email = [new_user.email]
            #
            #    send_mail(subject, message, from_email, to_email)


            # Trimite mail cu text in care setam noi numele usernameului si trebuie scos username din forms, fields si widgets

        # def form_valid(self, form):
            # if form.is_valid() and not form.errors:
            #     new_user = form.save(commit=False)
            #     new_user.first_name = new_user.first_name.title()  # cu litera mare la inceput
            #     new_user.last_name = new_user.last_name.title()
            #     new_user.username = f'{new_user.first_name.lower()}{new_user.last_name.lower()}_{randint(100000, 1000000)}'
            #     form.save()
            #
            #     subject = 'Created a new account!'
            #     message = f'Hello, {new_user.first_name} {new_user.last_name}. ' \
            #               f'Your account is created with user: {new_user.username}'
            #     from_email = EMAIL_HOST_USER
            #     email_to = [new_user.email]
            #
            #     send_mail(subject, message, from_email, email_to)

            #  Trimite mail cu template

        def form_valid(self, form):
            if form.is_valid() and not form.errors:
                new_user = form.save()

                details_user = {
                    'full_name': new_user,
                    'username': new_user.username
                }
                subject = 'Created a  new account!'
                message = get_template('userextend/mail_create_new_user.html').render(details_user)
                from_email = EMAIL_HOST_USER
                email_to = [new_user.email]

                email = EmailMessage(subject, message, from_email, email_to)
                email.content_subtype = 'html'  # main content is now text/html
                email.send()

            return redirect('homepage')
