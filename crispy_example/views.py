from django.views.generic import FormView

from crispy_example.forms import SimpleForm


class Index1View(FormView):
    # import ipdb; ipdb.set_trace()
    template_name = 'crispy_example/index.html'
    form_class = SimpleForm
