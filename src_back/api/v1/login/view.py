from django.contrib.auth.views import LoginView


class OverrideLoginView(LoginView):
    template_name = 'login.html'
