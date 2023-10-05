from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "login.html"

    def get_success_url(self):
        # return reverse_lazy("feedbacks-list")
        return reverse_lazy("home")

    def form_invalid(self, form):
        messages.error(self.request, "Usuário ou senha inválidos")
        return self.render_to_response(self.get_context_data(form=form))
