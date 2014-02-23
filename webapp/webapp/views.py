from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.edit import FormView

from models import License
from forms import *

class HomeView(FormView):
    template_name = "index.html"
    form_class = UserLicenseForm

    #def get_success_url(self):
    #    self.

    def form_valid(self, form):
        form.save()
        return super(HomeView, self).form_valid(form)