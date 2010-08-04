# ct_framework.views

from django.contrib.auth.views import login as dj_login

from ct_framework.forms import UsernameOrEmailAuthenticationForm

def login(request):

    return dj_login(request, authentication_form=UsernameOrEmailAuthenticationForm)


