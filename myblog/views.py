from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class MyLoginView(LoginView):
    template_name = 'registration/login.html'  # Use your login template
    redirect_field_name = 'next'

    def get_success_url(self):
        url = super().get_success_url()
        print(f"Success URL from get_success_url: {url}")
        return url