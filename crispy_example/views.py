from django.views.generic import FormView

from crispy_example.forms import SimpleForm


class Index1View(FormView):
    template_name = 'crispy_example/index.html'
    form_class = SimpleForm
