from django.conf import settings
from django.contrib.auth.views import LoginView

from src_back.models import LoginToken


class OverrideLoginView(LoginView):
    template_name: str = 'login.html'
    redirect_authenticated_user: bool = True
    next_page = '/'

    def get(self, request, *args, **kwargs):
        login_token: LoginToken = LoginToken.objects.create()

        context = self.get_context_data(**kwargs)
        context['login_token'] = login_token.token
        context['tg_bot_name'] = settings.TG_BOT_NAME

        return self.render_to_response(context)
