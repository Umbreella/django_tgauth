from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


@method_decorator(login_required(login_url='/login'), name='get')
class MainView(TemplateView):
    template_name: str = 'main_.html'

    def get_context_data(self, **kwargs):
        context_data: dict = super().get_context_data(**kwargs)

        context_data['user_username'] = self.request.user.username
        context_data['user_full_name'] = self.request.user.get_full_name()

        return context_data
