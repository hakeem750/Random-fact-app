from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import  get_user_model
import randfacts
 
 





class ContactForm(forms.Form):

    name = forms.CharField(max_length=120)
    email = forms.EmailField()

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        subject = "Random Fact"

        msg = f'Hi {name},\n\n'
        msg += f'Did you know that?\n'
        msg += f"{randfacts.get_fact()}\n\n"
        msg += "Enjoy,\n"
        msg += "Yusuf AbdulHakeem A."
        return subject, msg

    def send(self):

        subject, msg = self.get_info()
        cl_data = super().clean()
        email = cl_data.get('email')

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )