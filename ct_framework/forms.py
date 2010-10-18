
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _



class UsernameOrEmailAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label=_('Username or email'), max_length=46)
    
    def clean(self):
        data = self.cleaned_data.get('username', '')
        if data.find('@') > -1:
            bad_email = True
            try:
                user = User.objects.get(email=data)
                if user.check_password(self.cleaned_data.get('password', '')):
                    self.cleaned_data['username'] = user.username
                    bad_email = False
            except User.DoesNotExist:
                pass
            if bad_email:
                raise forms.ValidationError(
                    _("Please enter a correct username or email address, and  password."))
        return super(UsernameOrEmailAuthenticationForm, self).clean()
        
